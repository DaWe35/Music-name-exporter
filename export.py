path = 'C:\webserver\www\music_names\dir.txt'
with open(path, 'r', errors='ignore') as current:
    lines = current.readlines()
    if not lines:
        print('FILE IS EMPTY')
    else:
        for line in lines:
            line = line.strip()
            print(line)
            if (line.endswith(('.mp3', '.avi'))):
                print(line)