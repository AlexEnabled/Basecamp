binary = input('Enter Binary number: ')
x = len(binary)
y = 1
i = 0
sum = 0
while x > i:
    digit = int(binary[-1-i]) * y
    sum += digit
    y *= 2
    i+=1
print(sum)
