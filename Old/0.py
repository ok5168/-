import re
p=re.compile('(one|two|three)')
print p.sub('num', 'one word two words three words apple', 2)

