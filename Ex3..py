Year = int(input('inter a Year: '))
Month=int(input('inter a Month: '))
Day  =int(input('inter a Day:   '))
if Year%400==0 or Year%4==0:
    l1=[31,29,31,30,31,30,31,31,30,31,30,31]      
    SumMonth=sum(l1[:Month-1])
    SumMonth+=Day
    print('Number of days pass: ')
    print(SumMonth)
else:
    l2=[31,28,31,30,31,30,31,31,30,31,30,31]
    SumMonth=sum(l2[:Month-1])
    SumMonth+=Day
    print('Number of days pass: ')
    print(SumMonth)
