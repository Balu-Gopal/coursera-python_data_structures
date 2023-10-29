fname = input('Enter the Filename : ')
try:
    fhand = open (fname)
except:
    print('File cannot be opened: ',fname)
    quit()
s = 0
s= float(s)
count = 0
for line in fhand :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    pos = line.find(':')
    l = line[pos+1:]
    strp = l.strip()
    fstrp = float(strp)
    s = s + fstrp
    count = count +1
a = s / count
print("Average spam confidence:",a)