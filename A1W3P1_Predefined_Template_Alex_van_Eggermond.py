program = True
while program == True:
    ans = input("write more letter?").upper()
    if ans == "YES":
        program = True
        type = input("job offer or rejection? ").upper()
        if type == "JOB OFFER":
            fname = input("First name? ").title()
            while len(fname) < 2 or len(fname) > 10 or fname.isalpha() != True:
                print("input error")
                fname = input("First name?").title()
            lname = input("last name? ").title()
            while len(lname) < 2 or len(lname) > 10 or lname.isalpha() != True:
                print("input error")
                lname = input("last name?").title()
            title = input("title?")
            while len(title) < 10 or title.isnumeric() != False:
                print("input error")
                title = input("title?")
            sal = input("salary")
            salary = sal.replace(".","")
            salary = salary.replace(",", ".")
            while float(salary) < 20000.00 or float(salary) > 80000.00:
                print("input error")
                sal = input("salary")
                salary = sal.replace(".", "")
                salary = salary.replace(",", ".")
            sdate = input("starting date")
            split_sdate = sdate.split("-")
            while len(split_sdate[0]) != 4 or len(split_sdate[1]) != 2 or len(split_sdate[2]) != 2 or int(split_sdate[1]) > 12 or int(split_sdate[2]) > 31 or int(split_sdate[0]) < 2021 or int(split_sdate[1]) < 0 or int(split_sdate[2]) < 0:
                print("input error")
                sdate = input("starting date")
                split_sdate = sdate.split("-")
            print("Here is the final letter to send:")
            print(f"Dear {fname} {lname},\n"
                  f"After careful evaluation of your application for the position of {title},\n"
                  f"we are glad to offer you the job. Your salary will be {sal} euro annually.\n"
                  f"Your start date will be on {sdate}. Please do not hesitate to contact us with any questions.\n"
                  f"Sincerely,\n"
                  f"HR Department of XYZ ")
        elif type == "REJECTION":
            fname = input("First name? ").title()
            while len(fname) < 2 or len(fname) > 10 or fname.isalpha() != True:
                print("input error")
                fname = input("First name?").title()
            lname = input("last name? ").title()
            while len(lname) < 2 or len(lname) > 10 or lname.isalpha() != True:
                print("input error")
                lname = input("last name?").title()
            title = input("title?")
            while len(title) < 10 or title.isnumeric() != False:
                print("input error")
                title = input("title?")
            feed = input("Feedback? (Yes or No)").upper()
            if feed == "YES":
                back= input("Enter your Feedback (One Statement): ")
                print("Here is the final letter to send:")
                print(f"Dear {fname} {lname},\n"
                      f"After careful evaluation of your application for the position of {title},\n"
                      f"at this moment we have decided to proceed with another candidate.\n"
                      f"Here we would like to provide you our feedback about the interview.\n"
                      f"{back}\n"
                      f"We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.\n"
                      f"Sincerely,\n"
                      f"HR Department of XYZ ")
            if feed == "NO":
                print("Here is the final letter to send:")
                print(f"Dear {fname} {lname},\n"
                      f"After careful evaluation of your application for the position of {title},\n"
                      f"at this moment we have decided to proceed with another candidate.\n"
                      f"We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.\n"
                      f"Sincerely,\n"
                      f"HR Department of XYZ ")
    elif ans == "NO":
        program = False
        print("Closing")
    else:
        print("input error")

