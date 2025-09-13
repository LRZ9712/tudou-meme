from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

# 图片素材存放在 "images" 文件夹下
# 请确保该文件夹内有对应 "拉屎" 主题的 0.png, 1.png 文件（根据JSON中有2个位置信息）
img_dir = Path(__file__).parent / "images"

def la_shi(images: list[BuildImage], texts, args):
    """
    生成"拉屎"GIF表情包。
    头像位于模板图片的下层。
    """
    # 1. 处理用户头像：转换为圆形透明PNG
    # JSON中 "round": true 表示需要圆形头像
    avatar = images[0].convert("RGBA").circle()

    frames: list[IMG] = []
    # 2. 各帧中头像的位置和大小参数 (x, y, width, height)
    # 源自您提供的JSON数据
    locs = [
        (48, 29, 140, 117),  # 第一帧
        (49, 29, 141, 110)   # 第二帧
    ]

    # 3. 遍历每一帧，合成图片
    for i in range(len(locs)):
        # 加载对应的模板图片作为前景
        try:
            foreground = BuildImage.open(img_dir / f"{i}.png")
        except FileNotFoundError:
            raise FileNotFoundError(f"错误：模板图片 'images/{i}.png' 未找到。")

        # 获取当前帧的位置和尺寸信息
        pos = locs[i]
        avatar_pos = (pos[0], pos[1])
        avatar_size = (pos[2], pos[3])

        # 调整头像尺寸
        resized_avatar = avatar.resize(avatar_size)
        
        # 创建与前景图相同大小的透明背景
        frame = BuildImage.new("RGBA", foreground.size)
        
        # 先粘贴头像（下层）
        frame.paste(resized_avatar, avatar_pos, alpha=True)
        
        # 再粘贴前景模板（上层）
        frame.paste(foreground, (0, 0), alpha=True)

        frames.append(frame.image)

    # 4. 将所有帧保存为GIF，设置帧间隔为0.08秒（可按需调整）
    return save_gif(frames, 0.08)

# 5. 注册这个新的表情包
add_meme(
    "lash",                    # 表情包的唯一ID (英文或拼音)
    la_shi,                    # 处理函数
    min_images=1,              # 最少需要1张图片（头像）
    max_images=1,              # 最多也只接受1张图片
    keywords=["拉屎"],         # 触发关键词
    date_created=datetime(2025, 9, 9), # 创建日期
    date_modified=datetime(2025, 9, 9) # 修改日期
)