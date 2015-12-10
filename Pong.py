import math
x = 3
while True:
    print(x)
    try:
        x = math.factorial(x)
    except:
        x = x*x
