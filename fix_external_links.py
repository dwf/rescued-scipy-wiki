import fileinput

import re

for line in fileinput.input():
    link_pattern = r'\[`(http:\/\/[^\s]+)`\_ ([\w\s]+)\]'
    match = re.search(link_pattern, line)
    line_accum = []
    while match:
        line_accum.append(line[:match.start()])
        new_link = "`%s <%s>`_" % tuple([s.strip('_') for s in match.groups()])[::-1]
        line_accum.append(new_link)
        line = line[match.end():]
        match = re.search(link_pattern, line)
    line_accum.append(line)
    print ''.join(line_accum).rstrip()

