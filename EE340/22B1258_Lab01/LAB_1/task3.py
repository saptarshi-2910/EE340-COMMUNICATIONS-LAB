#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class task3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "task3")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.gain_band_5_range = gain_band_5_range = 1
        self.gain_band_4_range = gain_band_4_range = 1
        self.gain_band_3_range = gain_band_3_range = 1
        self.gain_band_2_range = gain_band_2_range = 1
        self.gain_band_1_range = gain_band_1_range = 1

        ##################################################
        # Blocks
        ##################################################

        self._gain_band_5_range_range = qtgui.Range(0, 2, 0.1, 1, 200)
        self._gain_band_5_range_win = qtgui.RangeWidget(self._gain_band_5_range_range, self.set_gain_band_5_range, "Gain Band 5", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_band_5_range_win)
        self._gain_band_4_range_range = qtgui.Range(0, 2, 0.1, 1, 200)
        self._gain_band_4_range_win = qtgui.RangeWidget(self._gain_band_4_range_range, self.set_gain_band_4_range, "Gain Band 4", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_band_4_range_win)
        self._gain_band_3_range_range = qtgui.Range(0, 2, 0.1, 1, 200)
        self._gain_band_3_range_win = qtgui.RangeWidget(self._gain_band_3_range_range, self.set_gain_band_3_range, "Gain Band 3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_band_3_range_win)
        self._gain_band_2_range_range = qtgui.Range(0, 2, 0.1, 1, 200)
        self._gain_band_2_range_win = qtgui.RangeWidget(self._gain_band_2_range_range, self.set_gain_band_2_range, "Gain Band 2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_band_2_range_win)
        self._gain_band_1_range_range = qtgui.Range(0, 2, 0.1, 1, 200)
        self._gain_band_1_range_win = qtgui.RangeWidget(self._gain_band_1_range_range, self.set_gain_band_1_range, "Gain Band 1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gain_band_1_range_win)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_wavfile_source_0_3 = blocks.wavfile_source('/home/saptarshi-biswas/Desktop/DESKTOP/EE340/LAB_1/Bach.wav', True)
        self.blocks_wavfile_source_0_2 = blocks.wavfile_source('/home/saptarshi-biswas/Desktop/DESKTOP/EE340/LAB_1/Bach.wav', True)
        self.blocks_wavfile_source_0_1 = blocks.wavfile_source('/home/saptarshi-biswas/Desktop/DESKTOP/EE340/LAB_1/Bach.wav', True)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source('/home/saptarshi-biswas/Desktop/DESKTOP/EE340/LAB_1/Bach.wav', True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/saptarshi-biswas/Desktop/DESKTOP/EE340/LAB_1/Bach.wav', True)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            '/home/saptarshi-biswas/Desktop/DESKTOP/EE340/LAB_1/equalizer.wav',
            1,
            samp_rate,
            blocks.FORMAT_RF64,
            blocks.FORMAT_PCM_16,
            False
            )
        self.blocks_throttle2_0_3 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_2 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_multiply_const_vxx_0_3 = blocks.multiply_const_ff(gain_band_3_range)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_ff(gain_band_2_range)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(gain_band_4_range)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(gain_band_5_range)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(gain_band_1_range)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_2_1 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                6000,
                9000,
                500,
                window.WIN_KAISER,
                6.76))
        self.band_pass_filter_2_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                9000,
                15000,
                1000,
                window.WIN_KAISER,
                6.76))
        self.band_pass_filter_2 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                3000,
                6000,
                500,
                window.WIN_KAISER,
                6.76))
        self.band_pass_filter_1 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                500,
                3000,
                500,
                window.WIN_KAISER,
                6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                20,
                500,
                100,
                window.WIN_KAISER,
                6.76))
        self.audio_sink_0 = audio.sink(samp_rate, '', True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_const_vxx_0_2, 0))
        self.connect((self.band_pass_filter_2, 0), (self.blocks_multiply_const_vxx_0_3, 0))
        self.connect((self.band_pass_filter_2_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.band_pass_filter_2_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_3, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_throttle2_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_throttle2_0_1, 0), (self.band_pass_filter_2, 0))
        self.connect((self.blocks_throttle2_0_2, 0), (self.band_pass_filter_2_1, 0))
        self.connect((self.blocks_throttle2_0_3, 0), (self.band_pass_filter_2_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.blocks_throttle2_0_3, 0))
        self.connect((self.blocks_wavfile_source_0_1, 0), (self.blocks_throttle2_0_2, 0))
        self.connect((self.blocks_wavfile_source_0_2, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.blocks_wavfile_source_0_3, 0), (self.blocks_throttle2_0_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task3")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 20, 500, 100, window.WIN_KAISER, 6.76))
        self.band_pass_filter_1.set_taps(firdes.band_pass(1, self.samp_rate, 500, 3000, 500, window.WIN_KAISER, 6.76))
        self.band_pass_filter_2.set_taps(firdes.band_pass(1, self.samp_rate, 3000, 6000, 500, window.WIN_KAISER, 6.76))
        self.band_pass_filter_2_0.set_taps(firdes.band_pass(1, self.samp_rate, 9000, 15000, 1000, window.WIN_KAISER, 6.76))
        self.band_pass_filter_2_1.set_taps(firdes.band_pass(1, self.samp_rate, 6000, 9000, 500, window.WIN_KAISER, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_3.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_gain_band_5_range(self):
        return self.gain_band_5_range

    def set_gain_band_5_range(self, gain_band_5_range):
        self.gain_band_5_range = gain_band_5_range
        self.blocks_multiply_const_vxx_0_0.set_k(self.gain_band_5_range)

    def get_gain_band_4_range(self):
        return self.gain_band_4_range

    def set_gain_band_4_range(self, gain_band_4_range):
        self.gain_band_4_range = gain_band_4_range
        self.blocks_multiply_const_vxx_0_1.set_k(self.gain_band_4_range)

    def get_gain_band_3_range(self):
        return self.gain_band_3_range

    def set_gain_band_3_range(self, gain_band_3_range):
        self.gain_band_3_range = gain_band_3_range
        self.blocks_multiply_const_vxx_0_3.set_k(self.gain_band_3_range)

    def get_gain_band_2_range(self):
        return self.gain_band_2_range

    def set_gain_band_2_range(self, gain_band_2_range):
        self.gain_band_2_range = gain_band_2_range
        self.blocks_multiply_const_vxx_0_2.set_k(self.gain_band_2_range)

    def get_gain_band_1_range(self):
        return self.gain_band_1_range

    def set_gain_band_1_range(self, gain_band_1_range):
        self.gain_band_1_range = gain_band_1_range
        self.blocks_multiply_const_vxx_0.set_k(self.gain_band_1_range)




def main(top_block_cls=task3, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
