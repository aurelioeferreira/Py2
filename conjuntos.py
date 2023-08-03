list = [1,2,3,2,1,4,5,10,8,5]
conj = set(list)
print(list)
print(conj)
text = ""
for i in conj:
    text.join(str(i))
print(text)