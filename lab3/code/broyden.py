import numpy as np
from sympy import *


def broyden(y, f, symbols, x_init, max_step):
    M = len(symbols)
    derivs = [y.diff(sym) for sym in symbols]
    H = np.array(hessian(y, symbols))
    X = [np.array(x_init, dtype=np.float32)]
    G = []
    N = []
    Z = []
    step = 0
    while step < max_step:
        x_curr = {symbols[j]: X[-1][j] for j in range(M)}

        grad = np.array([derivs[i].subs(x_curr) for i in range(M)], dtype=np.float32)

        if step == 0:
            nu = -np.eye(M)
            N.append(nu)
        else:
            x_prev = {symbols[j]: X[-2][j] for j in range(M)}
            grad_prev = np.array([derivs[i].subs(x_prev) for i in range(M)], dtype=np.float32)

            delta_g = grad - grad_prev
            delta_X = X[-1] - X[-2]
            z = delta_X - N[-1].dot(delta_g)
            Z.append(z)

            zm = z[np.newaxis]  # 1x2
            delta_nu = zm.T.dot(zm) / zm.dot(delta_g[np.newaxis].T)
            nu = N[-1] + delta_nu
            N.append(nu)

        K = -nu.dot(grad[np.newaxis].T).flatten()

        t = -grad.dot(grad[np.newaxis].T) / grad.dot(H).dot(grad[np.newaxis].T)

        x_temp = np.array(X[-1] + t * K, dtype=np.float32)

        if np.allclose(X[-1], x_temp) or np.allclose(f(X[-1]), f(x_temp)):
            break

        X.append(x_temp)
        step += 1
    return X
