import os
from shutil import copyfile

# 遍历项目文件夹
# 将项目文件夹下的java源代码复制到另外一个目录

def getJavaSourceCode(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            print(os.path.join(root, f))
            # 如果以.java结尾，我们就复制到另外一个文件夹下
            if f.endswith('.java'):
                copyfile(os.path.join(root, f),'../data/our_data/spring-source-code/'+f)

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))


def main():
    getJavaSourceCode(r"F:\Program Files\mypycode\DebugMethodName\data\our_data\spring-framework-master")


if __name__ == '__main__':
    main()