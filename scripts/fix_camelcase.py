import fileinput

import re

for line in fileinput.input():
    #link_pattern = r'`(http\:\/\/[^\s`]+)`_?'
    link_pattern = r'([A-Z][a-z]+[A-Z][a-zA-Z]*)_'
    match = re.search(link_pattern, line)
    line_accum = []
    while match:
        line_accum.append(line[:match.start()])
        new_link = "%s" % match.groups()
        line_accum.append(new_link)
        line = line[match.end():]
        match = re.search(link_pattern, line)
    line_accum.append(line)
    print ''.join(line_accum).rstrip()

