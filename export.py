# !/usr/bin/python

file = 'C:\webserver\www\music_names\Music list export.txt'
folder = 'C:\Users\Hp\Music'

import re
import os
file_array = []
open(file, 'w').close()
for root, dirs, files in os.walk(folder, topdown=True):
   for name in files:
       file_ = os.path.join(name)
       filename, file_extension = os.path.splitext(file_)
       if (file_extension == '.mp3') or (file_extension == '.wav'):
           filename = re.sub(r" ?\([^)]+\)", "", filename)
           filename = re.sub(r" ?\[[^)]+\]", "", filename)
           splitted = filename.split('-', 1)
           splitted[0] = splitted[0].strip()
           if len(splitted) >= 2:
               file_array.append(splitted[0] + '\t' + splitted[1].strip())
           else:
               file_array.append(splitted[0])
   '''for name in dirs:
      print(os.path.join(root, name))'''

file_array.sort()
#file_array = list(dict.fromkeys(file_array)) # Remove duplicates (comment out if needed)
string = ''
for item in file_array:
    string += item + '\n'
new_days = open(file,'w')
new_days.write(string)