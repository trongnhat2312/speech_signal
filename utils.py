import numpy as np
from scikits.talkbox.linpred.levinson_lpc import lpc
from scipy import signal


def compute_self_correlation(y, K):
    y = np.array(y)
    N = len(y)
    R = [np.sum(np.multiply(y[0:N - k], y[k:N])) for k in range(K + 1)]

    return R


def compute_AMDF(y, K):
    y = np.array(y)
    N = len(y)
    R = [np.sum(np.abs(y[0:N - k] - y[k:N])) for k in range(K + 1)]

    return R


def compute_formant(y):
    em_y = signal.lfilter([1.0], [1.0, -0.98], y)

    a, e, k = lpc(em_y, 14, axis=-1)

    # while len(a) < 512:
    #     a.add(0.)
    w, h = signal.freqz([1.0], a)
    return w, h
