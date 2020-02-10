fp = open('file.txt', 'r')
fp.read(10)
'python sup'
currentpos=fp.tell
print currentpos
fp.close()
