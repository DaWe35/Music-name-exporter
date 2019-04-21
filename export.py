# !/usr/bin/python

file = 'C:\webserver\www\music_names\dir.txt'
folder = 'C:\Users\Hp\Music'

import os
string = ''
open(file, 'w').close()
for root, dirs, files in os.walk(folder, topdown=True):
   for name in files:
       file_ = os.path.join(name)
       filename, file_extension = os.path.splitext(file_)
       if (file_extension == '.mp3') or (file_extension == '.wav'):
            splitted = filename.split('-', 1)
            splitted[0] = splitted[0].strip()
            if len(splitted) >= 2:
                string += splitted[0] + '\t' + splitted[1] + '\n'
            else:
                string += splitted[0] + '\n'
   '''for name in dirs:
      print(os.path.join(root, name))'''


new_days = open(file,'w')
new_days.write(string)