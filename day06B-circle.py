import turtle as t

n=5		# 오각형
t.shape("turtle")
t.color("purple")
t.begin_fill()
for x in range(n):
	t.forward(50)
	t.left(360/n)
t.end_fill()

