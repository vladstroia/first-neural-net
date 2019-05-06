import numpy as np
def calc(x):
    product = sum(x[k] * w[k] for k in range(len(x)))
    return product + b

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

def check(x, y):
    result = calc(x) 
    if sign(result) == y:
        return True
    return False

def checkAll():
    for i in range(3):
        if check(x[i], y[i]) == False:
            return False
    return True


 
with open("x.txt", 'r') as f:
    x = f.read()
    x = x.split()
    x = map(int, x)
    x = np.reshape(x, (3,2))
with open("y.txt", 'r') as f:
    y = f.read()
    y = y.split()
    y = map(int, y)

w = [0, 0]
b = 0
i = 0
while checkAll() == False:
    for i in range(3):
        if check(x[i], y[i]) == False:
            for k in range(2):
                w[k] = w[k] + x[i][k]*y[i]
                b = b + y[i]
print(w[0], w[1], b)
         


