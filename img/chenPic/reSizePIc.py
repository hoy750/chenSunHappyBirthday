from PIL import Image
import os

# 设置目标文件夹路径
folder_path = r'D:\code\好玩的小事\微信\生日祝福\HappyBirthday-chenSun\HappyBirthday-main\img\chenPic'

# 设置目标图片大小
target_size = (640, 480)

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # 拼接完整的文件路径
        file_path = os.path.join(folder_path, filename)
        
        # 打开图片
        with Image.open(file_path) as img:
            # 调整图片大小
            img = img.resize(target_size, Image.ANTIALIAS)
            
            # 保存图片，覆盖原文件
            img.save(file_path)

print("所有图片已调整大小并保存。")