
import math
import numpy as np 
def grad(x):
    return x-1

def cost(x):
    return 1/2 * (x-1)**2 - 2

def GD(eta, x0):
    xt = x0
    while math.fabs(grad(xt)) > eta:
        xt = xt - grad(xt)
    return xt
print("Solution x1 = " , GD(0.0001, -10))