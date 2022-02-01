import time


while True:
    inputdate = input('Введите дату в формате DD/MM/YYYY\n')
    try:
        realdate = time.strptime(inputdate, '%d/%m/%Y')
        print("Верная дата!")
    except:
        print("Не верная дата!")
