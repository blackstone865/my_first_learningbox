import os
import shutil

# 1. 定义你要整理的文件夹路径（换成你电脑里一个比较乱的文件夹，比如下载目录）
# 注意：路径前面的 r 表示“原始字符串”，防止 Windows 里的斜杠报错
target_folder = r"E:\Backup\桌面\test_folder" 

# 2. 定义分类规则（字典：文件后缀名 -> 存放的文件夹名）
rules = {
    ".jpg": "图片",
    ".png": "图片",
    ".txt": "文档",
    ".pdf": "文档",
    ".mp4": "视频"
}

def sort_files(folder_path):
    # 检查文件夹是否存在
    if not os.path.exists(folder_path):
        print(f"错误：找不到文件夹 {folder_path}")
        return

    # 遍历文件夹里的所有文件
    for filename in os.listdir(folder_path):
        # 获取文件的完整路径
        file_path = os.path.join(folder_path, filename)
        
        # 如果是文件夹，就跳过，不处理
        if os.path.isdir(file_path):
            continue
            
        # 提取文件的后缀名，并转换为小写（比如 .JPG 变成 .jpg）
        ext = os.path.splitext(filename)[1].lower()
        
        # 如果后缀名在我们的规则里
        if ext in rules:
            folder_name = rules[ext]
            # 拼接出目标文件夹的路径
            destination_folder = os.path.join(folder_path, folder_name)
            
            # 如果目标文件夹不存在，就创建它
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                
            # 移动文件
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"已移动: {filename} -> {folder_name}/")

# 运行函数
print("开始整理文件...")
sort_files(target_folder)
print("整理完成！")