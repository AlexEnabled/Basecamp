word = input().replace(" ","")
y = word[::-1]
if word == y:
    print("It's a palindrome!")
else:
    print("It's not a palindrome")
