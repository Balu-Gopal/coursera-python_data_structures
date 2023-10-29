name = input("Enter file:")
handle = open(name)
d = dict()
for line in handle :
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0]!='From' :
        continue
    for word in words:
        if ':' not in word :
            continue
        t = word[:2]
        d[t] = d.get(t,0) + 1
lst = list()
lst = sorted(d.items())
for k,v in lst :
    print(k,v)
