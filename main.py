from macronutrientcalc import (bmrcalc, ask_body_parameters, check_body_parameters,
                               calories_calc, macros_calc)

if __name__ == '__main__':

    print('Hi! This program will help you to calculate the calories and macronutrient that your body needs.')
    print('First, we´ll estimate your basal metabolism (the amount of energy required to do body basic functions)')
    print('Please, enter the following information:')

    body_parameters = ask_body_parameters()

    check = check_body_parameters(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])
    if check:
        bmr = bmrcalc(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])[0]
        print(f'Your basal metabolism is {bmr} kcal daily. Now we have to multiply it by your activity factor')

    print('Your activity factor depends on the amount of exercise you do weekly.')
    print('If you do not do any exercise your activity factor is 1.2')
    print('If you do non intense exercise your activity factor is 1.375 (Walk 1/3 times weekly)')
    print('If you do medium intense exercise your activity factor is 1.55 (Gym or swimming 3/5 times weekly)')
    print('If you do very intense exercise your activity factor is 1.75')

    kcal = calories_calc(bmr)
    print(f'The amount of kcalories you need daily to maintenance is {round(kcal, 2)}')

    print("If your goal is not maintenance, then have to write if you want to enter in deficit or exceeded calories")
    goal = input("Enter deficit or exceeded: ")
    protein, fat, carbs = macros_calc(body_parameters[1], round(kcal, 2), body_parameters[2], goal)
    print(f'The amount of protein you need is {round(protein, 2)} kcal')
    print(f'The amount of fat you need is {round(fat, 2)} kcal')
    print(f'The amount of carbs you need is {round(carbs, 2)} kcal')
