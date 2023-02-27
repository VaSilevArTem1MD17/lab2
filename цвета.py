colors=('красный','синий','желтый')
a=input('введите цвет\n')
b=input('введите цвет\n')
if a in colors and b in colors:
    if a != b:
        if a in ('красный','синий') and b in ('красный','синий'):
            print ('фиолетовый')
        if a in ('синий','желтый') and b in ('синий','желтый'):
            print('зеленый')
        if a in ('красный', 'желтый') and b in ('красный', 'желтый'):
            print('оранжевый')
    else:
        print(a)
else:
    print('цвет введен неверно')