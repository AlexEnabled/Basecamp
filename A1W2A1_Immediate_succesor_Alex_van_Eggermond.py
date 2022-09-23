monthday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
split_date = input().split("-")
if len(split_date[0]) == 4 and len(split_date[1]) == 2 and len(split_date[2]) == 2:
    int(split_date[2]) +=1
    if int(split_date[2]) > monthday[int(split_date[1])]:
        split_date[2] = 1
        int(split_date[1]) +=1
        if int(split_date[1]) > 12:
            split_date[1] = 1
            int(split_date[0]) += 1
    print("Next date: ",int(split_date[0]),"-","%02d" % (int(split_date[1]),),"-","%02d" % (int(split_date[2])))
else:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")

