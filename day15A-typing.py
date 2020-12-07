import random
import time

w = ["cat", "dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n = 1
print("[타자 게임] 준비되면 엔터!")
input()
start = time.time()

q = random.choice(w)
while n <= 5:
    print("문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과")
        n = n + 1
        q = random.choice(w)
    else:
        print("오타! 다시 시도!")

end = time.time()
diff = end - start
diff = format(diff, ".2f")
print("타자 시간: ", diff, "초")
