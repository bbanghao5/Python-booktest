import random

def make_question():
    a = random.randint(1, 40)
    b = random.randint(1, 20)
    op = random.randint(1, 3)

    q = str(a)
    if op == 1:
        q = q + "+"
    elif op == 2:
        q = q + "-"
    elif op == 3:
        q = q + "*"

    q = q + str(b)
    return q

ans_correct = 0
ans_wrong = 0

for x in range (5):
    q = make_question()
    print(q)
    ans_str = input("=")
    ans_val = int(ans_str)

    if ans_val == eval(q):
        print("정답")
        ans_correct = ans_correct + 1
    else:
        print("오답!")
        ans_wrong = ans_wrong + 1

print("정답:", ans_correct, ", 오답:", ans_wrong)
if ans_wrong == 0:
    print("당신은 천재입니다!")

random.choice()
