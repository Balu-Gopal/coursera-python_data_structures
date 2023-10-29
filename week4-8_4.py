fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened')
lst = list()
for line in fh:
    line1 = line.strip()
    line2 = line1.split()
    for word in line2:
        if word not in lst:
            lst.append(word)
    
lst.sort()
print(lst)
