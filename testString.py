stringList=[]
with open('rawString.txt','r') as f:
    for line in f.readlines():
        # print(line.strip())
        my_set=sorted(line.strip())
        str=''.join(my_set)
        stringList.append(str)
    print(stringList)

with open('RawDataStored.txt','w') as f:
    for line in stringList:
        f.write(line+'\n')