import fileinput

import re

for line in fileinput.input():
    #link_pattern = r'`(http\:\/\/[^\s`]+)`_?'
    link_pattern = r'\[ (http[^\s\]]+) \]'
    match = re.search(link_pattern, line)
    line_accum = []
    matched =  False
    while match:
        matched = True
        line_accum.append(line[:match.start()])
        new_link = "%s" % tuple([s.strip('_') for s in match.groups()])[::-1]
        #print match.groups()
        line_accum.append(new_link)
        line = line[match.end():]
        match = re.search(link_pattern, line)
    line_accum.append(line)
    #if matched:
    print ''.join(line_accum).rstrip()

