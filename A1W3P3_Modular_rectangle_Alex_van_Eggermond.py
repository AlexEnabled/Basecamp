height = int(input())
width = int(input())
num = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

a= 0
y= 0
while y < height:
    i = a + width
    print(*num[a: i])
    a = i
    y += 1





