
import sys

tags = set(['javascript', 'java', 'python', 'ruby', 'php', 'c++', 'c#', 'go', 'scala', 'swift'])

fh_output = open(sys.argv[2], 'w')
fh_input = open(sys.argv[1], 'r')
cnt = 0
for line in fh_input:
	cnt += 1
	line = line.split('\t')
	if len(line) != 2:
		continue
	text, label = line
	label = label.split()
	label = set(label) & tags
	if len(label) != 1:
		continue
	label = label.pop()
	text = text.replace(':', '')
	text = text.replace('|', '')
	fh_output.write(label + ' | ' + text + '\n')

fh_output.close()