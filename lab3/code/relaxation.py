import numpy as np
from sympy import *


def relaxation(y, f, symbols, x_init, max_step):
    M = len(symbols)
    exprs = [y.diff(sym) * y.diff(sym, 2) ** (-1) for sym in symbols]

    X = [np.array(x_init, dtype=float)]
    step = 0
    while step < max_step:
        x_curr = {symbols[j]: X[-1][j] for j in range(M)}
        x = X[-1]
        for j in range(M):
            x = x.copy()
            x[j] -= exprs[j].subs(x_curr)
            X.append(x)

        if np.allclose(X[-2], X[-1]) or np.allclose(f(X[-2]), f(X[-1])):
            break

        step += 1
    return X
