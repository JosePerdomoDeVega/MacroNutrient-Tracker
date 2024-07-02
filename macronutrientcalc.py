from _datetime import datetime


def bmrcalc():
    birthday = datetime.strptime(input("Enter your birthday (in format MM/DD/YYYY): "), "%m/%d/%Y")
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    sex = input("Enter an M if you are male o F if you are female: ")
    weight = int(input("Enter your weight (in kilograms): "))
    height = int(input("Enter your height (in centimeters): "))

    bmr = 10*weight + 6.25*height - 5*age
    if sex == 'M':
        bmr += 5
    else:
        bmr -= 161
    return bmr, sex