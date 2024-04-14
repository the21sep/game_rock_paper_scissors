import random
round = 0
score_player = 0
score_bot = 0
while round < 3:
    print('Выберите один из вариантов: ')
    print('1 - камень')
    print('2 - ножницы')
    print('3 - бумага')
    bot = random.randint(1, 3)
    player = input('Ваш ход: ')
    if player == '1' or player == '2' or player == '3':
        player = int(player)
    else:
        print('Совсем глупый? Нужно ввести 1, 2 или 3')
        continue
    if bot == 1: # камень
        if player == 1:
            print('Ничья')
        elif player == 2:
            score_bot += 1
            print('Камень бьёт ножницы. Очко боту.')
        else:
            score_player += 1
            print('Бумага заворачивает камень. Очко игроку.')
    elif bot == 2: # ножницы
        if player == 1:
            score_player += 1
            print('Камень бьёт ножницы. Очко игроку.')
        elif player == 2:
            print('Ничья')
        else:
            score_bot += 1
            print('Ножницы режут бумагу. Очко боту.')
    else: # бумага
        if player == 1:
            score_bot += 1
            print('Бумага заворачивает камень. Очко боту.')
        elif player == 2:
            score_player += 1
            print('Ножницы режут бумагу. Очко игроку.')
        else:
            print('Ничья')
    round += 1

print(f'Очки игрока = {score_player}')
print(f'Очки бота = {score_bot}')
if score_player > score_bot:
    print('Победил игрок!')
elif score_bot == score_player:
    print('Ничья!')
else:
    print('Победил бот :(')


