fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

lines = open(fname)
count = 0
emails = list()
names = dict()
for line in lines:
	if line.startswith('From') and not line.startswith('From:'):
		items = line.split()
		item = items[1] 
		emails.append(item)

for email in emails:
	if email not in names.keys():
		names[email] = 1
	else: 
		names[email] += 1
#find largest in values

max = max(names.values())
keys = list(names.keys())

for key in keys: 
	if names[key] is max:
		print key, max