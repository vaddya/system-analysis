import numpy as np
from numpy.linalg import norm
from sympy import *


def conjugate_gradients(y, f, symbols, x_init, max_step):
    M = len(symbols)
    derivs = [y.diff(sym) for sym in symbols]
    H = np.array(hessian(y, symbols))

    X = [np.array(x_init, dtype=np.float32)]
    step = 0
    while step < max_step:
        x_curr = {symbols[j]: X[-1][j] for j in range(M)}

        grad = np.array([derivs[i].subs(x_curr) for i in range(M)], dtype=np.float32)
        K = grad
        if step > 0:
            x_prev = {symbols[j]: X[-2][j] for j in range(M)}
            grad_prev = np.array([derivs[i].subs(x_prev) for i in range(M)], dtype=np.float32)
            K += norm(grad) ** 2 / norm(grad_prev) ** 2 * grad_prev

        t = -grad.dot(grad[np.newaxis].T) / grad.dot(H).dot(grad)

        x_temp = np.array(X[-1] + t * K, dtype=np.float32)

        if np.allclose(X[-1], x_temp) or np.allclose(f(X[-1]), f(x_temp)):
            break

        X.append(x_temp)
        step += 1
    return X
