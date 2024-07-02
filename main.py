from macronutrientcalc import bmrcalc

if __name__ == '__main__':
    print('Hi! This program will help you to calculate the calories and macronutrient that your body needs.')
    print('First, we´ll estimate your basal metabolism (the amount of energy required to do body basic functions)')
    print('Please, enter the following information:')
    print(f'Your basal metabolism is {bmrcalc()[0]} kcal daily. Now we have to multiply it by your activity factor')
