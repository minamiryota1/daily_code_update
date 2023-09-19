import os
import paramiko
import subprocess
from tqdm import tqdm

# 配置SSH连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.137.170', username='caros', password='Csec@keyL7256')

ssh.exec_command("echo hello >> /opt/data/nlt/test")
# 定义本地目录和远程目录

# local_directory = input("请输入需要传输的本地目录")
# remote_directory = input("请输入需要接收的远程目录")


# # def check_remote_space(target_path):
# #     # 执行命令行命令，获取目标路径的可用空间（以字节为单位）
# #     result = subprocess.run(['df', target_path], stdout=subprocess.PIPE)
# #     output = result.stdout.decode('utf-8')
# #     lines = output.split('\n')
# #     # 提取可用空间的行，并返回可用空间大小（以字节为单位）
# #     available_space_line = lines[1]
# #     available_space = int(available_space_line.split()[1])
# #     return available_space

# # # 检查目标设备的可用空间
# # available_space = check_remote_space(remote_directory)

# # if available_space < 3737418240:  # 10G in bytes
# #     print("目标设备空间不足，请确保至少有4G的可用空间。")
# # else:
# #     print("目标设备空间充足，可以进行文件拷贝。")

# # local_file = 'local_file.txt'
# # local_size = os.path.getsize(local_file)

# # 遍历本地目录并传输文件和目录
# for root, dirs, files in os.walk(local_directory):
#     for file in files:
#         # 构建本地文件路径
#         print(file)
#         local_file_path = os.path.join(root, file)
        
#         # 构建远程文件路径
#         remote_file_path = os.path.join(remote_directory, os.path.relpath(local_file_path, local_directory))
        
#         # 创建远程目录（如果不存在）
#         remote_dir = os.path.dirname(remote_file_path)
#         print(remote_file_path)
#         print(remote_dir)
#         sftp = ssh.open_sftp()
#         sftp.mkdir(remote_dir)#第一级目录不用创建
        
#         # 传输文件并显示进度条
#         #sftp.put(local_file_path, remote_file_path)
#         with open(local_file_path, 'rb') as f:
#             file_data = f.read()
#             chunk_size = 1024 * 1024 * 50  # 设置每个数据块的字节数，例如1MB
#             total_chunks = len(file_data) // chunk_size + 1
#             for i in tqdm(range(total_chunks)):
#                 sftp.sendfile(f.fileno(), i * chunk_size, i * chunk_size + chunk_size - 1, file_data[i * chunk_size: (i + 1) * chunk_size])
#         print(f"Transferred: {local_file_path} -> {remote_file_path}")

# 关闭SSH连接
ssh.close()