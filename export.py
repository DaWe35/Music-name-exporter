# !/usr/bin/python
import re
import os
import time
from datetime import datetime


file = 'C:\webserver\www\Music-name-exporter\Music list export.txt'
folder = 'C:\Users\Hp\Music'
exclude = ['C:\Users\Hp\Music\Samples']
collectAfter = '2019-04-29'

collectAfter = datetime.strptime(collectAfter, '%Y-%m-%d')
file_array = []
open(file, 'w').close()
for root, dirs, files in os.walk(folder, topdown=True):
    for name in files:
        notExc = True
        for exc in exclude:
            if root.startswith(exc):
                notExc = False
        if notExc:
            file_ = os.path.join(root, name)
            try:
                last_modified = datetime.utcfromtimestamp(os.path.getmtime(file_))
                if last_modified > collectAfter:
                    filename, file_extension = os.path.splitext(name)
                    print(filename)
                    if (file_extension == '.mp3') or (file_extension == '.wav'):
                        filename = re.sub(r" ?\([^)]+\)", "", filename)
                        filename = re.sub(r" ?\[[^)]+\]", "", filename)
                        splitted = filename.split('-', 1)
                        splitted[0] = splitted[0].strip()
                        if len(splitted) >= 2:
                            file_array.append(splitted[0] + '\t' + splitted[1].strip())
                        else:
                            file_array.append(splitted[0])
            except Exception as e:
                print(e)
    '''for name in dirs:
        print(os.path.join(root, name))'''

file_array.sort()
#file_array = list(dict.fromkeys(file_array)) # Remove duplicates (comment out if needed)
string = ''
for item in file_array:
    string += item + '\n'
new_days = open(file,'w')
new_days.write(string)