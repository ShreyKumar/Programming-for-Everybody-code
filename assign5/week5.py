largest = None
smallest = None
while True:
    #prompt user
    num = raw_input("Enter a number: ");
    #validation 
    if num != "done":
        try:
            int_num = int(num)
        except:
            int_num = -1
    else:
        break
        
    if int_num == -1:
        print "Invalid input"
        continue
    
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
        
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
print "Maximum is ", largest
print "Minimum is ", smallest
    