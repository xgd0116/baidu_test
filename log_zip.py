#!/usr/bin python
"""压缩日志"""
import os
import datetime
import re
import tarfile


# 获取文件路径集合
def getFile(logsPath):
    logsFile = []
    fileList = os.listdir(logsPath)
    for fileName in fileList:
        path = os.path.join(logsPath, fileName)
        # 过滤子文件的文件被压缩
        if os.path.isdir(path):
            continue
        logsFile.append(path)
    return logsFile


# 检查文件,备份文件
def checkFile(logsFiles):
    newDate = datetime.datetime.now().strftime('%Y-%m-%d')  # 当前时间
    tar_file = []
    for f in logsFiles:
        # 过滤压缩文件检查
        if f.endswith(".tar.gz"):
            continue
        # 使用正则获取日志文件名的时间
        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", f)
        if bool(mat):
            delta = datetime.datetime.strptime(newDate, '%Y-%m-%d') - datetime.datetime.strptime(mat.group(), '%Y-%m-%d')
            # 当前时间 - 文件时间 ：大于0
            if delta.days > 0:
                # 已经压缩完成的日志文件,删除原日志文件,保留压缩文件
                if f.endswith(".tar.gz") and f.endswith("%s.tar.gz" % mat.group()):
                    continue
                tar_file.append(f)

    for tar_f in tar_file:
        # 截取日志文件名
        file_name = tar_f.split("logs/")[1]
        # 截取日志的序号
        file_num = file_name.split(".log")[1]
        # 根据序号创建不同名称的压缩包
        if file_num == "":
            tar_name = f"{file_name[0:10]}.tar.gz"
        else:
            tar_name = f"{file_name[0:10]}-{file_num[1]}.tar.gz"
        tar = tarfile.open(f"./logs/{tar_name}", 'w:gz')
        tar.add(tar_f)
        tar.close()
        os.remove(tar_f)

def run():
    project_path = os.path.abspath(os.path.dirname(__file__))
    logsPath = f"{project_path}/logs"
    logsFiles = getFile(logsPath)
    checkFile(logsFiles)

if __name__ == "__main__":
    run()