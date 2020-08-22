from random import *
users = range(1, 20)
users = list(users)
shuffle(users)
winners = sample(users, 4)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))

for waiting in [0, 1, 2, 3, 4]: #range(0, 10)
    print("대기번호 : {0}".format(waiting))

from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money


balance = 0
balance = deposit(balance, 1000)
print(balance)

def std_weight(height, gender):
    if gender == "여자":
        return height*height*21
    else:
        return height*height*22
height = 164
gender = "여자"
weight = round(std_weight(height / 100, gender))
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))