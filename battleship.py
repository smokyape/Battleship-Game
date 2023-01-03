def get_shot(guesses):

    ok = "n"
    while ok == "n":
        shot = input("Введите своё предположение ")
        shot = int(shot)
        if shot < 0 or shot > 99:
            print("Неверное значение, повторите снова ")
        elif shot in guesses:
            print("Неверное значение, уже использовано ")
        else:
            ok = "y"
            break
    return shot

def show_board(hit,miss,comp):
    print("       Морской Бой!")
    print("    |1||2||3||4||5||6|")

    place = 0
    for x in range(6):
        row = ""
        for y in range(6):
            ig = " O "
            if place in miss:
                ig = " x "
            elif place in hit:
                ig = " o "
            elif place in comp:
                ig = " 0 "

            row = row + ig
            place = place + 1
        print(x," ",row)

def check_shot(shot, ship1,ship2,hit,miss,comp):

    if shot in ship1:
        hit.append(shot)
        ship1.remove(shot)
        if len(ship1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    elif shot in ship2:
        hit.append(shot)
        ship2.remove(shot)
        if len(ship2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    else:
        miss.append(shot)

    return ship1,ship2,hit,miss,comp



ship1 = [12,13,14]
ship2 = [5,15,25]
hit = []
miss = []
comp = []

for i in range(10):
    guesses = hit + miss + comp
    shot = get_shot(guesses)
    ship1,ship2,hit,miss,comp = check_shot(shot,ship1,ship2,hit,miss,comp)
    show_board(hit,miss,comp)

    if len(ship1) < 1 and len(ship2) < 1:
        print("Ты победил! ")
        break
print("Игра закончена! ")

