from datetime import datetime
from pathlib import Path
from PIL.Image import Image as IMG
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import save_gif

# 假设您的图片素材都存放在 "images" 文件夹下
# ================= 新增表情说明 =================
# 请确保该文件夹内有 "正在找你" 主题的背景图片, 文件名为 "zheng_zai_zhao_ni_bg.png"
# ===============================================
img_dir = Path(__file__).parent / "images"


def zheng_zai_zhao_ni(images: list[BuildImage], texts, args):
    """
    生成“正在找你”GIF表情包。
    """
    # 1. 加载背景图片
    try:
        bg = BuildImage.open(img_dir / "0.png")
    except FileNotFoundError:
        raise FileNotFoundError("错误：模板图片 'images/zheng_zai_zhao_ni_bg.png' 未找到。")

    # 2. 处理用户头像：转换为圆形透明PNG
    # JSON中 "round": true 表示需要圆形头像
    avatar = images[0].convert("RGBA").circle()
    # 3. 从JSON获取头像的位置和大小参数
    # "pos": [[158, 39, 165, 165]]
    x, y, w, h = 158, 39, 165, 165
    avatar_pos = (x, y)
    avatar_size = (w, h)

    # 预先调整好头像尺寸
    resized_avatar = avatar.resize(avatar_size)

    frames: list[IMG] = []
    # 4. 创建旋转动画
    # 我们生成36帧，每帧旋转10度，以实现360度平滑旋转
    num_frames = 36
    angle_step = 10
    
    for i in range(num_frames):
        # 创建当前帧的背景副本，避免在原图上重复绘制
        frame = bg.copy()
        
        # 计算当前旋转角度
        current_angle = -(i * angle_step)
        
        # 旋转头像。BuildImage的rotate方法默认以中心为原点旋转
        # 且不改变图片尺寸 (expand=False)，完美符合需求
        rotated_avatar = resized_avatar.rotate(current_angle)
        
        # 将旋转后的头像粘贴到背景副本上
        # paste方法的第三个参数 alpha=True 用于处理透明背景
        frame.paste(rotated_avatar, avatar_pos, alpha=True)
        
        frames.append(frame.image)

    # 5. 将所有帧保存为GIF，设置合适的帧间隔以控制旋转速度
    # 0.05秒 * 36帧 = 1.8秒旋转一圈
    return save_gif(frames, 0.05)


# 6. 注册这个新的表情包
add_meme(
    "zheng_zai_zhao_ni",          # 表情包的唯一ID (建议使用拼音或英文)
    zheng_zai_zhao_ni,            # 处理函数
    min_images=1,                 # 最少需要1张图片（头像）
    max_images=1,                 # 最多也只接受1张图片
    keywords=["正在找你"],          # 触发关键词
    date_created=datetime(2025, 9, 10), # 创建日期
    date_modified=datetime(2025, 9, 10) # 修改日期
)