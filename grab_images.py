import fileinput
import re
import os
from subprocess import Popen

f = fileinput.input()
for line in f:
    #link_pattern = r'`(http\:\/\/[^\s`]+)`_?'
    link_pattern = r'inline\:([^\s]+)jpg'
    match = re.search(link_pattern, line)
    line_accum = []
    matched =  False
    while match:
        dir = f.filename()[1:-4] # Strip off leading . and trailing .rst
        try:
            os.makedirs('./images/' + dir)
        except:
            pass
        imgfile = match.group(1)
        localfile = './images/%s/%s' % (dir, imgfile)
        url = "http://scipy.org/%s?action=AttachFile&do=get&target=%s" % (dir, imgfile)
        p = Popen("wget -o %s %s" % (localfile, url), shell=True)
        print "!!!!!!!!! Saved %s" % localfile
        sts = os.waitpid(p.pid, 0)
        line = line[match.end():]
        match = re.search(link_pattern, line)

