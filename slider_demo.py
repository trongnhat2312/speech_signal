import matplotlib.pylab as plt
from matplotlib.mlab import find
from numpy import argmax, diff

from utils import *


class SnaptoCursor(object):
    """
    Like Cursor but the crosshair snaps to the nearest x,y point
    For simplicity, I'm assuming x is sorted
    """

    def __init__(self, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, signal, sr, window_len=0.02):
        self.ax1 = ax1
        self.ax2 = ax2
        self.ax3 = ax3
        self.ax4 = ax4
        self.ax5 = ax5
        self.ax6 = ax6
        self.ax7 = ax7
        self.ax8 = ax8
        self.ly1 = ax1.axvline(color='k')  # the vert line
        self.ly2 = ax1.axvline(color='k')  # the vert line
        self.ax2ly3 = ax2.axvline(color='k')  # the vert line
        self.x = 0
        self.y = 0
        self.signal = signal
        self.sr = sr
        # text location in axes coords
        self.window_len = window_len
        self.window_N_len = window_len * sr

    def mouse_click(self, event):
        if not event.inaxes:
            return
        x, y = event.xdata, event.ydata

        self.ly1.set_xdata(x)
        self.ly2.set_xdata(x + self.window_len)

        # self.txt.set_text('x=%4.9f, y=%4.9f' % (x, y))
        self.x = x
        self.y = y
        # print(x, y, self.sr)
        # print(len(self.y_or[int(x*self.sr):int((x+self.window_len)*self.sr)]), len(self.y_or))
        # print(self.y_or[int(x*self.sr):int((x+self.window_len)*self.sr)] )
        y_windows = self.signal[int(x * self.sr):int(x * self.sr + self.window_N_len)]

        ###############draw ax2##########################
        self.ax2.clear()
        self.ax2.set_title('Window signal')
        self.ax2.set_xlabel('N')
        self.ax2.set_ylabel('amplitude')
        self.ax2.plot(range(len(y_windows)), y_windows)

        ###############draw ax4##########################
        self.ax4.clear()
        self.ax4.set_title('Self correlation')
        self.ax4.set_xlabel('k')
        R_1 = compute_self_correlation(y_windows, 300)

        self.ax4.plot(range(len(R_1)), R_1)

        ###############draw ax6##########################
        self.ax6.clear()
        self.ax6.set_title('AMDF')
        self.ax6.set_xlabel('k')
        R_2 = compute_AMDF(y_windows, 300)

        self.ax6.plot(range(len(R_2)), R_2)

        ###############draw ax7##########################
        self.ax7.clear()
        w, h = compute_formant(y_windows)

        self.ax7.set_title('Frequency respond')
        self.ax7.set_xlabel('Frequency [rad/sample]')
        self.ax7.set_ylabel('Magnitude [dB]')
        self.ax7.plot(w * self.sr / (2 * np.pi), 20 * np.log10(abs(h)))

        plt.draw()

    def draw_tu_tuong_quan(self, y_or, sr, window_len):
        duration = len(y_or) / sr
        # print("duration:", duration)
        x = window_len
        time_ptr = []
        f0_list = []
        while x < duration - window_len * 1.01:
            # print("x: ", x)
            y_windows = y_or[int((x - window_len / 2) * sr):int((x + window_len / 2) * sr)]
            _, R = compute_self_correlation(y_windows, 300)
            # Find the first low point
            d = diff(R)
            start = find(d > 0)[0]

            # Find the next peak after the low point (other than 0 lag).  This bit is
            # not reliable for long signals, due to the desired peak occurring between
            # samples, and other peaks appearing higher.
            # Should use a weighting function to de-emphasize the peaks at longer lags.
            # Also could zero-pad before doing circular autocorrelation.
            peak = argmax(R[start:]) + start
            time_ptr.append(x)
            f0_list.append(peak)
            x += window_len / 2
        self.ax3.plot(time_ptr, f0_list)
        pass

    def amdf(self):

        pass

# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2*2*np.pi*t)
# fig, ax = plt.subplots()
#
# cursor = SnaptoCursor(ax, t, s)
# plt.connect('motion_notify_event', cursor.mouse_move)
#
# ax.plot(t, s, 'o')
# plt.axis([0, 1, -1, 1])
# plt.show()
