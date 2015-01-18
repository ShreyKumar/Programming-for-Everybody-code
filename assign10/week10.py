name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
lines = open(name)
alltimes = dict()
for line in lines:
	if line.startswith('From') and not line.startswith('From:'):
		words = line.split()
		#take times and make a dict 
		times = words[5]
		for chars in times:
			hour = times[:2]
		alltimes[hour] = alltimes.get(hour, 0) + 1
#add dict to tuple list
list = list()
for time, freq in alltimes.items():
	list.append( (time, freq) )
list.sort()

for time, freq in list:
	print time, freq