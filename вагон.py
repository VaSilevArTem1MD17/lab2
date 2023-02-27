mesto=int(input('введите номер вагона\n'))
if mesto in range(36,55):
    print('ваше место боковое\n')
    quit()
if mesto%2==0:
    print('ваше место сверху\n')
else:
    print('ваше место снизу\n')