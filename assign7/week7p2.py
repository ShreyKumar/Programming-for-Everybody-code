# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ");
fh = open(fname);
total = 0;
values = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        #retrive value and add
        values += float(line[19:])
        total += 1;
    else: 
        continue
#exit from loop 
average = values/total;
print "Average spam confidence:",average;