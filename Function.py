
str = input("please enter a string ")
print("entered string is :" + str)
count = {}
for c in str:
    if c in count.keys():
        count[c] += 1
    else:
        count[c]=1
print(count)

