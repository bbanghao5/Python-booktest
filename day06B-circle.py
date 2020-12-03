import turtle as t

n=60		# 원을 50개
r=80		# 반지름
t.shape("turtle")
t.color("green")
t.bgcolor("black")
t.speed(0)	# fastest

for x in range(n):
	t.circle(r)
	t.left(360/n)
t.done()

