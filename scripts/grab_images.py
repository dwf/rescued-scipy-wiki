import fileinput
import re
import os
from subprocess import Popen

f = fileinput.input()
for line in f:
    #link_pattern = r'`(http\:\/\/[^\s`]+)`_?'
    link_pattern = r'(?:attachment|inline)\:([^\s]+(?:jpe?g|png))'
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
        url = "http://scipy.org/%s?action=AttachFile\\&do=get\\&target=%s" % (dir, imgfile)
        p = Popen("wget -O %s %s" % (localfile, url), shell=True)
        sts = os.waitpid(p.pid, 0)
        if sts[1] != 0:
            print "\n\nNOT A CLEAN EXIT!\n"
            #print "\nSaved: %s" % localfile
            #print "\n"
            raw_input()
        line = line[match.end():]
        match = re.search(link_pattern, line)

