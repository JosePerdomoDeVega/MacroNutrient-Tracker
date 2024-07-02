from macronutrientcalc import bmrcalc, ask_body_parameters, check_body_parameters

if __name__ == '__main__':
    print('Hi! This program will help you to calculate the calories and macronutrient that your body needs.')
    print('First, we´ll estimate your basal metabolism (the amount of energy required to do body basic functions)')
    print('Please, enter the following information:')

    body_parameters = ask_body_parameters()

    check = check_body_parameters(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])
    if check:
        bmr = bmrcalc(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])[0]
        print(f'Your basal metabolism is {bmr} kcal daily. Now we have to multiply it by your activity factor')
