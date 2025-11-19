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
            [-4, 186, 105, 105],
            [-10, 188, 107, 107]
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
            [59, 266, 74, 74],
            None,
            None,
            None,
            None,
            [65, 272, 76, 76],
            [65, 272, 74, 74]
        ],
        [  # 头像3
            [198, 276, 63, 63],
            [162, 260, 61, 61],
            [160, 248, 65, 65],
            [164, 247, 65, 65],
            [161, 250, 65, 65],
            None,
            [165, 259, 65, 65],
            [171, 271, 65, 65],
            [173, 275, 65, 65],
            None,
            [175, 276, 65, 65],
            [163, 271, 65, 65],
            [166, 269, 65, 65],
            [148, 273, 65, 65],
            [142, 266, 65, 65],
            [146, 286, 65, 65],
            [147, 281, 63, 63],
            [156, 309, 67, 67],
            [155, 310, 65, 65]
        ],
        [  # 头像4
            [229, 305, 68, 68],
            [214, 311, 66, 66],
            [207, 291, 68, 68],
            [214, 292, 68, 68],
            [207, 302, 68, 68],
            [213, 299, 72, 72],
            [212, 289, 72, 72],
            [211, 285, 72, 72],
            [225, 289, 72, 72],
            None,
            [233, 298, 72, 72],
            [234, 291, 72, 72],
            [218, 285, 72, 72],
            [207, 293, 72, 72],
            [208, 292, 72, 72],
            [206, 301, 72, 72],
            [208, 298, 70, 70],
            [217, 305, 70, 70],
            [217, 314, 68, 68]
        ],
        [  # 头像5
            [287, 312, 65, 65],
            [270, 296, 65, 65],
            [270, 306, 65, 65],
            [277, 312, 65, 65],
            [273, 316, 65, 65],
            [277, 312, 63, 63],
            [271, 302, 65, 65],
            [272, 304, 65, 65],
            [282, 305, 65, 65],
            None,
            [285, 308, 65, 65],
            [286, 313, 65, 65],
            [276, 317, 65, 65],
            [271, 308, 65, 65],
            [277, 302, 65, 65],
            [272, 305, 63, 63],
            [279, 295, 69, 69],
            [289, 320, 69, 69],
            [287, 320, 67, 67]
        ],
        [  # 头像6
            [344, 307, 52, 52],
            [336, 298, 63, 64],
            [336, 301, 63, 64],
            [333, 304, 63, 64],
            [333, 304, 63, 63],
            [335, 303, 63, 63],
            [334, 290, 65, 65],
            [335, 289, 65, 65],
            [337, 279, 64, 64],
            None,
            [338, 279, 64, 64],
            [340, 277, 64, 64],
            None,
            [337, 275, 64, 64],
            [338, 274, 64, 64],
            None,
            [342, 277, 62, 62],
            [343, 278, 62, 62],
            [345, 280, 62, 62]
        ],
        [  # 头像7
            [371, 268, 55, 55],
            [368, 260, 57, 57],
            [370, 259, 57, 57],
            [369, 259, 57, 57],
            [369, 256, 57, 57],
            [371, 256, 57, 57],
            [372, 257, 57, 57],
            [373, 256, 57, 57],
            [380, 249, 57, 57],
            None,
            [376, 251, 57, 57],
            [378, 249, 57, 57],
            None,
            [380, 235, 57, 57],
            [378, 236, 57, 57],
            None,
            [379, 239, 55, 55],
            [383, 232, 55, 55],
            [383, 236, 55, 55]
        ],
        [  # 头像8
            [380, 216, 56, 56],
            [373, 225, 56, 56],
            [379, 212, 56, 56],
            [381, 202, 56, 56],
            [375, 203, 56, 56],
            [375, 203, 56, 56],
            [380, 200, 56, 56],
            [380, 200, 56, 56],
            [378, 203, 56, 56],
            None,
            [380, 200, 54, 54],
            [359, 177, 58, 58],
            [358, 186, 58, 58],
            [361, 184, 58, 58],
            [348, 159, 56, 56],
            [342, 160, 56, 56],
            [315, 151, 56, 56],
            [294, 133, 56, 56],
            [290, 127, 56, 56]
        ]
    ]
    
    # 旋转角度
    avatar_angles = [-2, 2, 19, 8, 355, 358, 1, 3]
    
    # 计算总帧数
    total_frames = max(len(positions) for positions in avatar_positions)
    
    # 预处理头像 - 所有头像都变成圆形
    processed_avatars = []
    for i in range(min(len(images), 8)):  # 最多8个头像
        avatar = images[i].convert("RGBA")
        
        # 计算该头像的最大尺寸
        if i < len(avatar_positions):
            valid_positions = [pos for pos in avatar_positions[i] if pos is not None]
            if valid_positions:
                max_size = max(max(pos[2], pos[3]) for pos in valid_positions)
                # 调整大小并变成圆形
                avatar = avatar.resize((max_size, max_size), keep_ratio=True).circle()
                # 应用旋转角度
                if i < len(avatar_angles):
                    avatar = avatar.rotate(avatar_angles[i])
        
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
                # 根据位置数据估计基础帧尺寸
                frame = BuildImage.new("RGBA", (500, 400), (255, 255, 255, 0))
        
        # 为每个头像处理当前帧的位置
        for avatar_idx in range(min(len(processed_avatars), 8)):
            if avatar_idx >= len(avatar_positions):
                continue
                
            positions = avatar_positions[avatar_idx]
            
            # 获取当前帧的位置数据
            pos_data = None
            # 从当前帧向前查找最近的有效位置
            for check_idx in range(frame_idx, -1, -1):
                if check_idx < len(positions) and positions[check_idx] is not None:
                    pos_data = positions[check_idx]
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
    date_created=datetime(2025, 11, 19),
    date_modified=datetime(2025, 11, 19),
)
