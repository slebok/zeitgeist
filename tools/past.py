#!/c/Users/vadim/AppData/Local/Programs/Python/Python35/python

import sys

f = open('past.txt', 'r', encoding='utf-8')
lines = f.readlines()
kws = []
goodlines = []
if lines[0].strip().lower().startswith('keywords: '):
	print('Found keywords!')
	line = lines[0].strip()[9:].strip()
	if line.endswith('.'):
		line = line[:-1]
	kws = line.split(', ')
	lines = lines[1:]
if not lines:
	pass
elif lines[0].strip().startswith('1. '):
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
elif lines[0].strip().startswith('[') and lines[0].find(']') > 0:
	goodlines = []
	for line in lines:
		line = line.strip()
		if line.startswith('['):
			goodlines.append(line)
		else:
			goodlines[-1] += ' ' + line
else:
	f.close()
	print('FAIL!')
	sys.exit(1)
f.close()

f = open('past.txt', 'w', encoding='utf-8')

if goodlines:
	last = goodlines[-1]
	f.write('\t"past": [\n')
	for line in goodlines:
		comma = '' if line == last else ','
		f.write('\t\t"{0}"{1}\n'.format(line, comma))
	f.write('\t],\n')

if kws:
	f.write('\t"present": [\n')
	last = kws[-1]
	for line in kws:
		comma = '' if line == last else ','
		f.write('\t\t"keyword:{0}"{1}\n'.format(line, comma))
	f.write('\t],\n')

f.close()
