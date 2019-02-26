import subprocess
import re
import sys

filename = sys.argv[1]
cmd = "ffprobe -show_frames {}".format(filename)
command = cmd.split()
p = subprocess.Popen(command, stdout=subprocess.PIPE)
fd = open('frame_size.txt', 'w+')
for line in p.stdout:
    str_line = str(line)
    m = re.search('pkt_size=\d+', str_line)
    if m:
        print(m.group().split('=')[1])
        fd.write(m.group().split('=')[1]+'\n')
fd.close()
p.wait()
print(p.returncode)


