fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

lines = open(fname)
count = 0
for line in lines:
	if line.startswith('From') and not line.startswith('From:'):
		items = line.split()
		count += 1
		print items[1]
print 'There were', count,'lines in the file with From as the first word'