# if you want to use it to copy some file from one directory to the other directory,
# you can you this file
# first, you should have a list file that list test/train sets. eg:trainval.txt
# write by GX.
import os
import shutil


# the path is you original file directory
# the newpath is the new directory
class CopyXml():
    def __init__(self):
        # 你的xml格式的annotation的路径
        self.path = '/home/lsc/datasets/butterfly/Annotations'
        # 你训练集/测试集xml格式annotation存放的路径
        self.newpath = '/home/lsc/datasets/butterfly/Annotations_train'

    def startcopy(self):
        filelist = os.listdir(self.path)  # file list in this directory
        # print(len(filelist))
        test_list = loadFileList()
        # print(len(test_list))
        for f in filelist:
            filedir = os.path.join(self.path, f)
            (shotname, extension) = os.path.splitext(f)
            if str(shotname) in test_list:
                # print('success')
                shutil.copyfile(str(filedir), os.path.join(self.newpath, f))


# load the list of train/test file list
def loadFileList():
    filelist = []
    f = open("/home/lsc/datasets/butterfly/ImageSets/train.txt", "r")
    lines = f.readlines()
    for line in lines:
        # 去掉文件中每行的结尾字符
        line = line.strip('\r\n')  # to remove the '\n' for test.txt, '\r\n' for tainval.txt
        line = str(line)
        filelist.append(line)
    f.close()
    # print(filelist)
    return filelist


if __name__ == '__main__':
    demo = CopyXml()
    demo.startcopy()