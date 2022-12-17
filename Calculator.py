from random import randint
from time import sleep
from os import system
from os import path


def MainApp():
    check_win = path.exists("C:\Windows\SysWOW64")
    if check_win == True:
        clear_screen = 'cls'

    if check_win == False:
        clear_screen = 'clear'

    spectrum = [1,2,2,4,5,6]
    system(clear_screen)

    print("Temperature Calculator v1.1") ; print(" ") ; print("1 = Fahrenheit To Celsius") ; print("2 = Celsius to Fahrenheit") ; print(" ") ; print("3 = Celsius To Kelvin") ; print("4 = Fahrenheit To Kelvin") ; print(" ") ; print("5 = Kelvin To Fahrenheit") ; print("6 = Kelvin To Celsius") ; print(" ")
    choice_i = int(input("Choice: "))
    if choice_i == 1:  
        user_i = int(input("Farenheight To Celcius: "))
        print(" ")
        sub0 = user_i - 32
        times = sub0 * 5/9
        rounding = round(times)
        print(f'{user_i}°F is {rounding}°C')
        print(" ") ; input("Press 'Any' Key To Convert More.")
        MainApp()

    if choice_i == 2:
        user_i = int(input("Celsius to Fahrenheit: ")) ; print(" ")
        times = user_i * 9/5
        sub0 = times + 32
        rounding = round(sub0)
        print(f'{user_i}°C is {rounding}°F')
        print(" ") ; input("Press 'Any' Key To Convert More.")
        MainApp()
    
    if choice_i == 3:
        user_i = int(input("Celsius To Kelvin: ")) ; print(" ")
        sub0 = user_i + 273
        rounding = round(sub0)
        print(f'{user_i}°C is {rounding}°K')
        print(" ") ; input("Press 'Any' Key To Convert More.")
        MainApp()
    
    if choice_i == 4:
        user_i = int(input("Fahrenheit To Kelvin: "))
        print(" ")
        sub0 = user_i - 32
        times = sub0 * 5/9
        rounding = round(times)
        kelvin = rounding + 273
        print(f'{user_i}°F is {kelvin}°K')
        print(" ") ; input("Press 'Any' Key To Convert More.")
        MainApp()

    if choice_i == 5:
        user_i = int(input("Kelvin To Fahrenheit: "))
        print(" ")
        sub0 = user_i * 9/5
        times = sub0 - 459.67
        rounding = round(times)
        print(f'{user_i}°K is {rounding}°F')
        print(" ") ; input("Press 'Any' Key To Convert More.")
        MainApp()
    
    if choice_i == 6:
        user_i = int(input("Kelvin To Celsius: "))
        print(" ")
        sub0 = user_i - 273
        rounding = round(sub0)
        print(f'{user_i}°K is {rounding}°C')
        print(" ") ; input("Press 'Any' Key To Convert More.")
        MainApp()


    if choice_i not in spectrum:
        print("Invalid Input Recieved...")
        sleep(1)
        MainApp()
MainApp()
# This simple python application can convert to and from Kelvin, Celsius, & Fahrenheit. It uses no external modules other than the base ones "os", "random", and "time". Oh, and it rounds to the nearest whole number.
