thisList = ['one','one','one','two','two','three','three','three','three']
compiledList = set(thisList)
numberedList = [''] * len(compiledList)
count = 0
for i in compiledList:
    numberedList[count] = [i,thisList.count(i)]
    count += 1
matching = [s for s in numberedList if 'one' in s]
print(matching[0][1])