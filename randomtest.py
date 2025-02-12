import random

result = random.randint(1, 10)
print(result)

while True:

    guess = int(input("请输入一个1-10之间的整数："))
    if guess < result:
        print("猜小了，再试试！")
    elif guess > result:
        print("猜大了，再试试！")
else:
    print("恭喜你，猜对了！")  # 猜中后退出循环


i = 0
while i < 10:
    i += 1
    if i == 5:
        continue  # 跳过本次循环
    if i == 8:
        break  # 结束循环
    print(i)
