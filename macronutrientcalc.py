from _datetime import datetime


def ask_body_parameters():
    today = datetime.today()

    try:
        birthday = datetime.strptime(input("Enter your birthday (in format MM/DD/YYYY): "), "%m/%d/%Y")
    except ValueError:
        print("Invalid date")

    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    sex = input("Enter an M if you are male o F if you are female: ")
    weight = int(input("Enter your weight (in kilograms): "))
    height = int(input("Enter your height (in centimeters): "))
    return age, sex, weight, height


def check_body_parameters(age, sex, weight, height):
    age_confirm = age in range(1, 120)
    sex_confirm = sex == 'M' or sex == 'F'
    weight_confirm = weight in range(1, 600)
    height_confirm = height in range(50, 300)

    if age_confirm and sex_confirm and weight_confirm and height_confirm:
        return True
    else:
        if not age_confirm:
            print("--> Invalid age. Please enter your birthday again.")
        if not sex_confirm:
            print("--> Invalid sex. Please enter your sex again.")
        if not weight_confirm:
            print("--> Invalid weight. Please enter your weight again.")
        if not height_confirm:
            print("--> Invalid height. Please enter your height again.")
        return False


def bmrcalc(age, sex, weight, height):
    bmr = 10 * weight + 6.25 * height - 5 * age
    if sex == 'M':
        bmr += 5
    else:
        bmr -= 161
    return bmr, sex


def calories_calc(bmr):
    activity_factor = float(input("Enter your activity factor: "))
    return bmr * activity_factor


def calories_goal(total_calories, goal):
    if goal == 'exceeded':
        total_calories = total_calories + 400
    if goal == 'deficit':
        total_calories = total_calories - 400
    return total_calories


def macros_calc(sex, calories, weight, goal):
    calories = calories_goal(calories, goal)
    protein = 1.6 * weight * 4
    if sex == 'M':
        fat = 0.25 * calories
        carbs = (1 - (protein / calories + 0.25)) * calories
    if sex == 'F':
        fat = 0.3 * calories
        carbs = (1 - (protein / calories + 0.3)) * calories
    return protein, fat, carbs
