#Просим пользователя ввести целое число для проверки на чётность или нечётность
number = int(input("Введите число для проверки на четность/нечетность: "))
#Если число делится на 2, то оно чётное
if number % 2 == 0: 
    print("Ваше число - четное")
#Если число не делится на 2, то оно нечётное
else:
    print("Ваше число - нечетное") 
