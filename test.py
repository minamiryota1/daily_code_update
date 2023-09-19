import os
local_directory = input("dadada")
for root, dirs, files in os.walk(local_directory):
    for file in files:
        # 构建本地文件路径
        print(file)
        print(root)
        print(dirs)
        local_file_path = os.path.join(root, file)
        print(local_file_path)
        input("下一个\n")
