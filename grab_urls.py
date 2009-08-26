import fileinput
import re

for line in fileinput.input():
    match = re.search(r'\[`(http:\/\/[^\s]+)`\_ (\w+)\]', line)
    if match:
        print match.groups()
        #print "url=%s, text=%s" % (match.group(1), match.group(2))
