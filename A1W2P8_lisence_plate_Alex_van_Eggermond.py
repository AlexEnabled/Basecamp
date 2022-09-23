license_plate = input("Enter license_plate: ").split("-")
if license_plate[0].isalpha() and license_plate[1].isnumeric() and license_plate[2].isalpha():
    print("VALID")
else:
    print("INVALID")
