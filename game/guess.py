from random import randint
from os import system, name
from time import sleep
        
print("               Угадай Слово ", '\n')
c = input("       Нажмите Enter для продолжения   ")
while c != '':
    c = input("       Нажмите Enter для продолжения   ")

words = ["замок", "вершина", "цветок", "сумма", "плата", "секунда", "образ", "толпа", 
"голова", "ухо", "участник", "зефир", "достижение", "год", "человек", "время", "дело",
"жизнь", "день", "рука", "работа", "слово", "место", "лицо", "круг", "друг", "вопрос",
"дом", "сторона", "мир", "случай", "сила", "конец", "вид", "система", "город", "земля",
"машина", "вода", "проблема", "час", "право", "решение", "дверь", "образ", "история",
"закон", "голос", "тысяча", "книга", "стол", "имя", "область", "статья", "число",
"возможность", "результат", "компания", "народ", "качество", "ветер", "процесс"]

alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

randword = words[randint(0, len(words)-1)]
unknown = ""
unknown += ('_' * len(randword))

fails_count = 0

while True:
    if name == 'nt':
        system("cls")
    else:
        system("clear")

    print(unknown.center(len(unknown)+20))
    print('\n')
    print("   Неправильно угадано: ", fails_count)

    if fails_count == 6:
        print("      Вы проиграли!")
        break

    if unknown == randword:
        print("      Вы выиграли!")
        break

    x = input('\n'+"   Введите букву: ")
    x = x.lower()
    if len(x) > 1:
        print("\n    Введите одну букву!")
        sleep(1)
        continue
    if x not in alph:
        print("\n      Введите букву!")
        sleep(1)
        continue

    if x in randword:
        for i in range(len(randword)):
            if randword[i] == x:
                unknown = unknown[:i] + x + unknown[i+1:]
    else:
        fails_count += 1
input()