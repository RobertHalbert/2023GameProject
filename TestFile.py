thisList = ['one','one','one','two','two','three','three','three','three']
compiledList = set(thisList)
numberedList = [''] * len(compiledList)
count = 0
for i in compiledList:
    numberedList[count] = [i,thisList.count(i)]
    count += 1
print(numberedList[0][1])