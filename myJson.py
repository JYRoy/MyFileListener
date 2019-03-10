#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: JYRoooy
import collections
import json
import hashlib
import os
import sys
import time
import importlib
import threading
importlib.reload(sys)

class myListener(threading.Thread):
    '''
    监听类
    '''
    def __init__(self, input_dir, filt_in, filt_ex):
        threading.Thread.__init__(self)
        self.input_dir = input_dir
        self.filt_in = filt_in
        self.filt_ex = filt_ex
        self.dict = {}
        self.file_list = []
        self.file_list = []
        self.pop_list = []

    def run(self):
        while (1):
            for cur_dir, dirs, files in os.walk(self.input_dir):
                if files != []:
                    self.file_list = []
                    for each_file_1 in files:
                        each_file = each_file_1
                        if self.filt_in:
                            flagone = 1
                            for i in range(len(self.filt_in)):
                                if self.filt_in[i] not in each_file:
                                    flagone = 0
                            for i in range(len(self.filt_in)):
                                if self.filt_in[i] in each_file:
                                    flagone = 1

                        if self.filt_ex:
                            flagtwo = 0
                            for i in range(len(self.filt_ex)):
                                if self.filt_ex[i] in each_file:
                                    flagtwo = 1

                        if flagtwo==1 and flagone==0:
                            continue

                        self.file_list.append(each_file)
                        full_path = os.path.join(cur_dir, each_file)
                        m = hashlib.md5()

                        myFile = open(full_path, 'rb')

                        for line in myFile.readlines():
                            m.update(line)
                        if each_file not in self.dict.keys():
                            self.dict[each_file] = m.hexdigest()
                            print('文件夹:' +cur_dir+ "中的文件名为：" + each_file + "的文件为新文件" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                  time.localtime(time.time())))
                        if each_file in self.dict.keys() and self.dict[each_file] != m.hexdigest():
                            print('文件夹:' +cur_dir+ "中的文件名为：" + each_file + "的文件被修改于" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                  time.localtime(time.time())))
                            self.dict[each_file] = m.hexdigest()
                        myFile.close()
                pop_list = []
                for i in self.dict.keys():
                    if i not in self.file_list:
                        print('文件夹:' +cur_dir+ '中的文件名为:' + i + "的文件已被删除!!!" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime(time.time())))
                        pop_list.append(i)
                for i in pop_list:
                    self.dict.pop(i)

            time.sleep(2)

if __name__ == '__main__':
    threads = []
    with open('E:/python/code/PythonProject/jsonConfig.txt','r+') as f:
        myjson = json.load(f)
        myList = myjson['dict']
        for i in range(len(myList)):
            json_list_include = []
            json_list_exclude = []
            mydir = myList[i]['path']
            for sublist in range(len(myList[i]['include'])):
                json_list_include.append(myList[i]['include'][sublist])
            for sublist in range(len(myList[i]['exclude'])):
                json_list_exclude.append(myList[i]['exclude'][sublist])
            thread1 = myListener(mydir, json_list_include, json_list_exclude)
            threads.append(thread1)

        for t in threads:
            t.start();


