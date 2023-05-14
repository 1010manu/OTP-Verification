from random import *
otp=randint(10000,100000)
print(otp)
user=int(input())
if otp==user:
    print('access granted')
else:
    print('access denied!')
