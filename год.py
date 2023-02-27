god=int(input('введите год\n'))
if god%4==0 or god%400==0 and god%100!=0:
    print('год вискосный')
else:
    print('год не високосный')