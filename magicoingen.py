coins = int(input("Введите количество монет: ")) # Количество монет
year = coins / 2 * 365
year = int(year) # изменяем float в interger
total = year + coins # делаем финальное вычисление
print("Вы заработаете:", total, "монет в течении 1 года")
crow = int(input("Но Ворона, падла, будет у вас тырить: "))
crowweek = crow * 52
total = total - crowweek
if crowweek > 0 :
    print("Но долбанная ворона стащила все твои заработанные деньги и ты будешь должен:", total, "рублей.")
else crowweek < 0:
    print("В общем, ты получишь", total, "рублей")
else crowweek == 0:
    print("Ого, какой ты снайпер!")
fi
# Я тут не знаю пока, как использовать if
