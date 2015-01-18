fname = raw_input("Enter file name: ")
fh = open(fname)
list = list()
for line in fh:
	#break in lines
	line = line.split()
	for word in line:
		#break in words
		#check if word is in line
		if word not in list:
			list.append(word)
list = sorted(list)
print list
