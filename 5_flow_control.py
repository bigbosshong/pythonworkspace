from random import *

customer = 0
for i in range(1, 51):
    time = randrange(1, 51)
    if 5 < time <15:
        print('[0]{0}번째 손님 (소요시간 : {1})'.format(i, time))
        customer += 1
    else:
        print('[ ]{0}번째 손님 (소요시간 : {1})'.format(i, time))
    
print('총 탑승 승객 : {0} '.format(customer))
