# !/usr/bin/python

file = 'C:\webserver\www\music_names\dir.txt'
folder = 'C:\Users\Hp\Music'

import os
for root, dirs, files in os.walk(folder, topdown=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

'''
import os




from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(folder):
    print(filenames)
    break




with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1'''