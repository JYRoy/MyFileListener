#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: JYRoooy
import collections
import json
import toml
if __name__ == '__main__':

    myOrderDict = collections.OrderedDict
    myOrderDict = {'dict':[{'path':'E:/testing', 'include':['log_'], 'exclude': ['.swp', '.swx', 'tmp']},{'path':'E:/tmp', 'include':['.record'], 'exclude': ['.tmp']}]}
    myJson = json.dump(myOrderDict, open('E:/python/code/PythonProject/jsonConfig.txt','w+'))

    myToml = toml.dump(myOrderDict, open('E:/python/code/PythonProject/tomlConfig.txt','w+'))

