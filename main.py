from __future__ import print_function, division
import librosa
import matplotlib.pyplot as plt
from librosa import display

from slider_demo import SnaptoCursor


def main():
    # signal, sr = librosa.load("khoosoothunhus.wav", duration=10)
    signal, sr = librosa.load("Xe.wav", sr=None)
    print(signal, sr)
    fig1 = plt.figure()
    fig1.suptitle('mouse hover over figure or axes to trigger events')
    ax1 = fig1.add_subplot(421)
    ax1.set_title('Signal')
    ax1.set_xlim(0, sr * len(signal))

    ax1.set_ylabel('amplitude')
    display.waveplot(signal, sr=sr)
    ax1.set_xlabel('Time (s)')

    ax2 = fig1.add_subplot(422)

    ax3 = fig1.add_subplot(423)
    ax3.set_title('FF from Self correlation ')
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Frequency (Hz)')

    ax4 = fig1.add_subplot(424)

    ax5 = fig1.add_subplot(425)
    ax5.set_title('FF from AMDF')
    ax5.set_xlabel('Time (s)')
    ax5.set_ylabel('Frequency (Hz)')

    ax6 = fig1.add_subplot(426)

    ax7 = fig1.add_subplot(427)


    ax8 = fig1.add_subplot(428)
    cursor = SnaptoCursor(ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, signal, sr)
    # # # plt.connect('motion_notify_event', cursor.mouse_move)
    plt.connect('button_press_event', cursor.mouse_click)

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.6,
                        wspace=0.25)
    plt.show()


if __name__ == '__main__':
    main()
