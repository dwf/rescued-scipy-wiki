import fileinput

import re
f = fileinput.input()
for line in f:
    #link_pattern = r'`(http\:\/\/[^\s`]+)`_?'
    link_pattern = r'(?:attachment|inline)\:([^\s]+(?:jpe?g|png))'
    match = re.search(link_pattern, line)
    line_accum = []
    while match:
        dir = f.filename()[:-4].strip('./')
        line_accum.append(line[:match.start()])
        new_link = "\n.. image:: images/%s/%s\n" % (dir, match.group(1))
        line_accum.append(new_link)
        line = line[match.end():]
        match = re.search(link_pattern, line)
    line_accum.append(line)
    print ''.join(line_accum).rstrip()

