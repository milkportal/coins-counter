print('Добро пожаловать в программу для генерации VIP-плана занятий на день!')
text = 'Мы начнём путешествие с %s, после чего позавтракаем в %s. Далее сходим в %s и %s. После этого на %s уедем домой.'
location1 = input('В какой ТЦ вы планируете зайти?: ')
location2 = input('В какой еще ТЦ вы хотите зайти?: ')
location3 = input('Какой еще ТЦ вы хотите посетить сегодня?: ')
location_break = input('Где вы собираетесь покушать?: ')
wehicle_model = input('На каком авто собираетесь ехать домой?: ')
print(text % (location1, location_break, location2, location3, wehicle_model))
print('Надеюсь, я помог вам!')
print('Приятного вам отдыха!')

