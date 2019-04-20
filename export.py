import os

for root, subs, files in os.path('C:\Users\Hp\Pictures'):
    for file in files:
        print(os.path.join(root, file))
        # Modify directories in place to remove directories starting with '.'
    for dir in subs[:]:
        if dir.startswith('.'):
            subs.remove(dir)
'''
f = open("music_list.txt", "w")
f.write(matches)
f.close()

#open and read the file after the appending:
f = open("music_list.txt", "r")
print(f.read())'''