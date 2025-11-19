from datetime import datetime
from pathlib import Path

from meme_generator import add_meme
from meme_generator.utils import save_gif
from PIL.Image import Image as IMG
from pil_utils import BuildImage

img_dir = Path(__file__).parent / "images"


def lulu_feed_pig(images: list[BuildImage], texts, args):
    # 位置数据 - 总共8个头像
    avatar_positions = [
        [  # 头像1
            [62, 171, 101, 101],
            [56, 167, 101, 101],
            [59, 164, 101, 101],
            [59, 160, 101, 101],
            [90, 152, 101, 101],
            None,
            [104, 146, 101, 101],
            [94, 173, 101, 101],
            [99, 167, 101, 101],
            [93, 160, 101, 101],
            None,
            None,
            None,
            None,
            None,
            [79, 164, 105, 105],
            [45, 179, 105, 105],
            [-9, 192, 103, 103],
            [-13, 192, 105, 105]
        ],
        [  # 头像2
            [32, 295, 72, 72],
            [7, 293, 72, 72],
            None,
            None,
            [13, 286, 72, 72],
            None,
            None,
            None,
            None,
            [31, 272, 72, 72],
            [38, 264, 72, 72],
            [43, 265, 74, 74],
            [59, 266, 74, 74]
        ],
        [  # 头像3
            [196, 285, 61, 61],
            [162, 260, 61, 61],
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            [146, 266, 63, 63],
            None,
            None,
            None,
            [141, 285, 61, 61]
        ],
        [  # 头像4
            [224, 316, 66, 66],
            [214, 311, 66, 66],
            None,
            None,
            [206, 304, 66, 66]
        ],
        [  # 头像5
            [285, 315, 63, 63],
            None,
            None,
            None,
            None,
            [277, 312, 63, 63],
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            [272, 305, 63, 63],
            None,
            None,
            [285, 322, 65, 65]
        ],
        [  # 头像6
            [344, 310, 50, 50],
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            [344, 281, 60, 60]
        ],
        [  # 头像7
            [368, 273, 53, 53],
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            [380, 243, 53, 53],
            [382, 237, 53, 53]
        ],
        [  # 头像8
            [375, 226, 54, 54],
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            [380, 200, 54, 54],
            None,
            None,
            [353, 192, 56, 56],
            [349, 162, 54, 54],
            [342, 160, 56, 56],
            [323, 160, 54, 54],
            [297, 131, 54, 54]
        ]
    ]
    
    # 计算总帧数（取最长的位置列表长度）
    total_frames = max(len(positions) for positions in avatar_positions)
    
    # 预处理头像 - 所有头像都变成圆形
    processed_avatars = []
    for i in range(min(len(images), 8)):  # 最多8个头像
        avatar = images[i].convert("RGBA")
        # 第一个头像有旋转角度357度
        if i == 0:
            avatar = avatar.resize((105, 105), keep_ratio=True).circle().rotate(357)
        else:
            # 其他头像根据最大尺寸调整大小并变成圆形
            if i < len(avatar_positions):
                # 获取该头像所有非空位置中的最大宽度
                valid_positions = [pos for pos in avatar_positions[i] if pos is not None]
                if valid_positions:
                    max_size = max(pos[2] for pos in valid_positions)
                    avatar = avatar.resize((max_size, max_size), keep_ratio=True).circle()
        processed_avatars.append(avatar)
    
    frames: list[IMG] = []
    
    # 为每一帧构建图像
    for frame_idx in range(total_frames):
        # 加载背景帧
        frame_path = img_dir / f"{frame_idx}.png"
        if frame_path.exists():
            frame = BuildImage.open(frame_path)
        else:
            # 如果帧文件不存在，使用上一帧或创建空白帧
            if frames:
                frame = BuildImage.new("RGBA", frames[0].size)
            else:
                # 根据位置数据估计基础帧尺寸，假设为400x400
                frame = BuildImage.new("RGBA", (400, 400), (255, 255, 255, 0))
        
        # 为每个头像处理当前帧的位置
        for avatar_idx in range(min(len(processed_avatars), 8)):
            if avatar_idx >= len(avatar_positions):
                continue
                
            positions = avatar_positions[avatar_idx]
            
            # 如果当前帧超出位置列表长度，跳过
            if frame_idx >= len(positions):
                continue
                
            pos_data = positions[frame_idx]
            
            # 如果是null，查找上一帧的位置
            if pos_data is None:
                # 向前查找最近的非null位置
                for prev_idx in range(frame_idx - 1, -1, -1):
                    if prev_idx < len(positions) and positions[prev_idx] is not None:
                        pos_data = positions[prev_idx]
                        break
                # 如果找不到有效位置，跳过这个头像
                if pos_data is None:
                    continue
            
            x, y, w, h = pos_data
            
            # 调整头像大小（如果需要）
            current_avatar = processed_avatars[avatar_idx]
            if current_avatar.width != w or current_avatar.height != h:
                current_avatar = current_avatar.resize((w, h), keep_ratio=True).circle()
            
            # 将头像粘贴到帧上
            frame.paste(current_avatar, (x, y), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.05)


add_meme(
    "lulu_feed_pig",
    lulu_feed_pig,
    min_images=2,
    max_images=8,
    keywords=["鲁鲁喂猪", "鲁鲁养猪"],
    date_created=datetime(2023, 3, 7),
    date_modified=datetime(2023, 3, 7),
)