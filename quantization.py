from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def main():
    f_max = 200
    fs = 20000
    num_sample = 100
    muy = 255

    n = np.linspace(0, num_sample / fs, num_sample)
    signal = [np.sin(2 * np.pi * f_max * i) for i in n]

    y_abs = np.log(1 + muy * np.abs(signal)) / np.log(1 + muy)
    y_sign = np.sign(signal)
    plt.figure(1)
    plt.plot(n, y_abs)

    plt.show()


if __name__ == "__main__":
    main()
