import numpy as np
from sympy import *


def newton(y, f, symbols, x_init, max_step):
    M = len(symbols)
    derivs = [y.diff(sym) for sym in symbols]
    Hinv = np.array(hessian(y, symbols).inv())

    X = [np.array(x_init, dtype=np.float32)]
    step = 0
    while step < max_step:
        x_curr = {symbols[j]: X[-1][j] for j in range(M)}

        grad = np.array([derivs[i].subs(x_curr) for i in range(M)])
        grad = grad.astype(np.float32)

        x_temp = np.array(X[-1] - Hinv.dot(grad))
        x_temp = x_temp.astype(np.float32)

        if np.allclose(X[-1], x_temp) or np.allclose(f(X[-1]), f(x_temp)):
            break

        X.append(x_temp)
        step += 1

    return X
