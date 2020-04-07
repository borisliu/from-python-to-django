import os
import time

# 1. 在列表中指出需要备份的文件和目录。
# 在Mac OS X和Linux中的列子:
# source = ['/Users/swa/notes']
# 在Windows中的例子:
source = ['"C:\\My Documents"', 'C:\\Code']
# 注意我们在有空格的名字的字符串内必须使用双引号。
# 我们也可以使用原始字符串[r'C:\My Documents']。

# 2. 备份必须存储在一个主备份目录中。
# 在Mac OS X和Linux中的例子:
# target_dir = '/Users/swa/backup'
# 在Windows中的例子:
target_dir = 'D:\\Backup' 
# 记住把它改为你要使用的目录

# 3. 备份的文件压缩到一个压缩文件中。
# 4. 压缩文件的名称是当前的日期和时间。
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目录不存在就创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 5. 我们使用zip命令把文件压缩到一个压缩文件中
zip_command = "zip -qr {0} {1}".format(target, 
                                       ' '.join(source))

# 运行备份
print("Zip命令为:")
print(zip_command)
print("运行:")
if os.system(zip_command) == 0:
    print('成功备份到', target)
else:
    print('备份失败')
