import turtle as t

n=5		# 오각형
d=100	# 변의 길이
t.shape("turtle")
t.color("purple")
t.begin_fill()
for x in range(n):
	t.forward(d)
	t.left(360/n)
t.end_fill()
t.done()

