import turtle as t
def triangle(size):
    if size <= 20:
        for i in range(0,3):
            t.forward(size)
            t.left(120)
        return
    new_size = size / 2
    triangle(new_size)
    t.forward(new_size)
    triangle(new_size)
    t.backward(new_size)
    t.left(60)
    t.forward(new_size)
    t.right(60)
    triangle(new_size)
    t.left(60)
    t.backward(new_size)
    t.right(60)
t.speed(1)
triangle(100)
t.hideturtle()
t.done()