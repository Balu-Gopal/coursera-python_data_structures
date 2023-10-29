fname = input('Enter the Filename: ')
try:
    fhand = open(fname)
except:
    print('File entered cannot be opened: ',fname)
for line in fhand :
    fcap = line.upper()
    fcap = fcap.rstrip()
    print(fcap)
    