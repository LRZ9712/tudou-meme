def huijiadeyouhuo(images: list[BuildImage], texts, args):
    if len(images) < 2:
        raise ValueError("回家的诱惑模板需要至少2张图片")
    
    frames: list[IMG] = []
    
    # 准备两个头像
    avatar1 = images[0].convert("RGBA").resize((100, 100)).circle()
    avatar2 = images[1].convert("RGBA").resize((55, 55)).circle()
    
    # 创建3帧的轻微动画效果
    for i in range(3):
        frame = BuildImage.open(img_dir / "0.png")
        
        # 第一个头像位置 (143, 48, 90, 90)
        x1, y1, width1, height1 = 143, 48, 90, 90
        # 添加轻微的移动（可选）
        if i == 1:
            x1_offset = x1 + 1
            y1_offset = y1
        elif i == 2:
            x1_offset = x1 - 1
            y1_offset = y1
        else:
            x1_offset, y1_offset = x1, y1
            
        avatar1_resized = avatar1.resize((width1, height1))
        frame.paste(avatar1_resized, (x1_offset, y1_offset), alpha=True)
        
        # 第二个头像位置 (387, 219, 48, 48)
        x2, y2, width2, height2 = 387, 219, 48, 48
        # 添加轻微的移动（可选）
        if i == 1:
            x2_offset = x2
            y2_offset = y2 + 1
        elif i == 2:
            x2_offset = x2
            y2_offset = y2 - 1
        else:
            x2_offset, y2_offset = x2, y2
            
        avatar2_resized = avatar2.resize((width2, height2))
        frame.paste(avatar2_resized, (x2_offset, y2_offset), alpha=True)
        
        frames.append(frame.image)
    
    return save_gif(frames, 0.2)  # 每帧0.2秒

add_meme(
    "huijiadeyouhuo",
    huijiadeyouhuo,
    min_images=2,
    max_images=2,
    keywords=["回家的诱惑"],
    date_created=datetime(2026, 2, 2),
    date_modified=datetime(2026, 2, 2),
)