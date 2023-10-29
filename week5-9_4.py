name = input('Enter file name:')
fh = open(name)
counts = dict()
for line in fh :
    line1 = line.rstrip()
    word = line1.split()
    if len(word) < 3 or word[0] != 'From':
        continue
    w= word[1]
    counts[w] = counts.get(w,0) + 1
bigcount = None
bigword = None
for a,b in counts.items():
    if bigcount is None or b > bigcount :
        bigword = a
        bigcount = b
print(bigword, bigcount)