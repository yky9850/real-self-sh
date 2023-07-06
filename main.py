import random
#충돌 수정했어요
print("로또 번호 추첨하기!")

print("어차피 꽝일테니 사지마세요")

for i in range(5):
    lotto= random.sample(range(1,46),6)
    print(lotto)
