# coding: utf-8
# Document description
# 这个程序是用来将指定文件夹的内容进行复制，到目标文件夹
# 更新作用

from os.path import join, isfile, isdir, exists, basename, dirname
import os
import shutil

pwd = os.getcwd()
dir_name = dirname(pwd)
t_dir = 'D:/My_code'


# 查找目标文件夹中含有特定字符串的文件夹名称
def find_dir_with_rule(dir_name, rule):
    filtered_dir = []
    for dir in os.listdir(dir_name):
        if rule in dir:
            filtered_dir.append(dir)
    return filtered_dir


def transfer_dir(c_dir, v_dir):
    # 解析c_dir中的文件
    for root, dirs, files in os.walk(c_dir):
        # print(dirs, '----------\n', files, 'for_结束')

        # 处理目录下的文件
        for file in files:
            # 判断是否是一个文件以及目标文件夹中是否存在
            if isfile(join(c_dir, file)) and not exists(join(v_dir, file)):
                shutil.copy(join(c_dir, file), join(v_dir, file))
                print('已复制文件{}'.format(join(c_dir, file)))

        # 处理目录下的文件夹
        for c1_dir in dirs:
            v1_dir = join(v_dir, c1_dir)
            if isdir(join(c_dir, c1_dir)) and not exists(v1_dir):
                print('已创建文件夹{}'.format(v1_dir))
                os.mkdir(v1_dir)  # 创建目标子文件夹
            # 递归调用
            # 组成子文件调用的绝对路径
            transfer_dir(join(c_dir, c1_dir), join(v_dir, v1_dir))


def main():
    # 组成首目标文件夹名
    target_dir = join(t_dir, basename(dir_name))
    if not exists(target_dir):
        os.mkdir(target_dir)
    # 将每个目录的文件复制到My_code文件夹中，上传到github
    transfer_dir(dir_name, target_dir)


if __name__ == '__main__':
    main()
