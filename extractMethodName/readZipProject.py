import os
import zipfile

def zip2file(zip_file_name: str, extract_path: str, members=None, pwd=None):
    """ 压缩文件内容提取值指定的文件夹

    :param zip_file_name: 待解压的文件  .zip          r'D:\Desktop\tst.zip'
    :param extract_path:  提取文件保存的目录           r'D:\Desktop\tst\test\test'
    :param members:       指定提取的文件，默认全部
    :param pwd:           解压文件的密码
    :return:
    """
    with zipfile.ZipFile(zip_file_name) as zf:
        zf.extractall(extract_path, members=members, pwd=pwd)


if __name__ == '__main__':
    zip2file(r'F:\Program Files\mypycode\ DebugMethodName\data\our_data\spring-framework-master.zip','F:\Program Files\mypycode\ DebugMethodName\data\our_data\spring-framework-master')