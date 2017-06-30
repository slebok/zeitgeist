#!/c/Users/vadim/AppData/Local/Programs/Python/Python35/python

import sys

f = open('past.txt', 'r', encoding='utf-8')
lines = f.readlines()
if lines[0].strip().startswith('1. '):
	nex = 1
	goodlines = []
	for line in lines:
		line = line.strip()
		sf = '{0}. '.format(nex)
		if line.startswith(sf):
			goodlines.append(line)
			nex += 1
		else:
			goodlines[-1] += ' ' + line
elif lines[0].strip().startswith('[1] '):
	nex = 1
	goodlines = []
	for line in lines:
		line = line.strip()
		sf = '[{0}] '.format(nex)
		if line.startswith(sf):
			goodlines.append(line)
			nex += 1
		else:
			goodlines[-1] += ' ' + line
else:
	f.close()
	print('FAIL!')
	sys.exit(1)
f.close()

f = open('past.txt', 'w', encoding='utf-8')
last = goodlines[-1]
f.write('\t"past": [\n')
for line in goodlines:
	comma = '' if line == last else ','
	f.write('\t\t"{0}"{1}\n'.format(line, comma))
f.write('\t],\n')
f.close()
