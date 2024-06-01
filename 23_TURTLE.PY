import turtle as tr
pen = tr.Turtle()
def spiral(matrix):
    while matrix:
        for num in matrix.pop(0):
            print(num)
            pen.forward(50)
            pen.write(num,align='center')
        pen.right(90)
        if matrix:
            matrix = list(zip(*matrix))[::-1]
            print(matrix)
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]
spiral(a)
tr.done()