message = 'I am aviral'
count={}

for char in message:
    count.setdefault(char, 0)
    count[char] +=1

print(count)

