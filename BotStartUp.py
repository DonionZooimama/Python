from InstagramAccount import *

accountInfo = [["books_cars_business", "dRuc*bawr5du", 70, 70]]
accounts = []

for a in accountInfo:
    temp = account(a[0], a[1], a[2], a[3])
    accounts.append(temp)