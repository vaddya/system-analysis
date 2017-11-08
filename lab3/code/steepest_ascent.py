import numpy as np
from sympy import *


def steepest_ascent(y, f, symbols, x_init, max_step):
    M = len(symbols)
    derivs = [y.diff(sym) for sym in symbols]
    H = np.array(hessian(y, symbols))

    X = [np.array(x_init, dtype=np.float32)]
    step = 0
    while step < max_step:
        x_curr = {symbols[j]: X[-1][j] for j in range(M)}

        grad = np.array([derivs[i].subs(x_curr) for i in range(M)])
        grad = grad.astype(np.float32)

        t = -grad.dot(grad[np.newaxis].T) / grad.dot(H).dot(grad)
        x_temp = np.array(X[-1] + t * grad, dtype=np.float32)

        if np.allclose(X[-1], x_temp) or np.allclose(f(X[-1]), f(x_temp), rtol=1e-6):
            break

        X.append(x_temp)
        step += 1

    return X
