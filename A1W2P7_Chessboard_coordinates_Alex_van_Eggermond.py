pos = input("Input chesscoordinates: ")
if pos[0] in ["a","c","e","g"]:
    if int(pos[1]) % 2 == 0 and int(pos[1]) < 8:
        print("The square is WHITE")
    else:
        print("The square is BLACK")
elif pos[0] in ["b","d","f","h"]:
    if int(pos[1]) % 2 == 0 and int(pos[1]) < 8:
        print("The square is BLACK")
    else:
        print("The square is WHITE")
else:
    print("incorrect input!")


