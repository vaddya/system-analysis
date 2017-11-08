import numpy as np
from sympy import *


def relaxation(y, f, symbols, x_init, max_step):
    M = len(symbols)
    derivs = [y.diff(sym) for sym in symbols]
    H = np.array(hessian(y, symbols))

    X = [np.array(x_init, dtype=float)]
    step = 0
    while step < max_step:
        x = X[-1]
        for j in range(M):
            x = x.copy()
            x_curr = {symbols[j]: X[-1][j] for j in range(M)}
            grad = np.array([derivs[i].subs(x_curr) for i in range(M)])
            grad = grad.astype(np.float32)

            K = np.zeros(M)
            K[j] = derivs[j].subs(x_curr)
            t = -grad.T.dot(K[np.newaxis].T) / K.dot(H).dot(K)

            x[j] += t * K[j]
            X.append(x)

        if np.allclose(X[-2], X[-1]) or np.allclose(f(X[-2]), f(X[-1])):
            break

        step += 1

    return X
