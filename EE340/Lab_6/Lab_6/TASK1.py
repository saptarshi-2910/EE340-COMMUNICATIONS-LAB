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
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
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



class TASK1(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "TASK1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 10000
        self.sps = sps = 8
        self.skip_head_count = skip_head_count = 123
        self.noise = noise = 0.01
        self.delay = delay = 11
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################

        self._noise_range = qtgui.Range(0, 1, 0.01, 0.01, 200)
        self._noise_win = qtgui.RangeWidget(self._noise_range, self.set_noise, "noise", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_win)
        self._delay_range = qtgui.Range(0, 1000, 1, 11, 200)
        self._delay_win = qtgui.RangeWidget(self._delay_range, self.set_delay, "delay", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_win)
        self._alpha_range = qtgui.Range(0, 10, 0.5, 1, 200)
        self._alpha_win = qtgui.RangeWidget(self._alpha_range, self.set_alpha, "alpha", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                (sps*symbol_rate),
                symbol_rate,
                alpha,
                (11*sps)))
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=5,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=5,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0_1_0_1 = qtgui.time_sink_f(
            1024, #size
            sps*symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1_0_1.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_1_win)
        self.qtgui_time_sink_x_0_1_0_0 = qtgui.time_sink_f(
            1024, #size
            symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_win)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
            1024, #size
            5*sps*symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1_0.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_win)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
            1024, #size
            sps*symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024, #size
            sps*symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(True)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (sps*symbol_rate), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (5*sps*symbol_rate), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (sps*symbol_rate), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            (sps*symbol_rate), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                (5*sps*symbol_rate),
                100000,
                100,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(sps, [1])
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(sps, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bf([-1,1], 1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_1 = blocks.threshold_ff((-0.11), 0.11, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, skip_head_count)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, (1/1000), 4000, 1)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/sappylappy/Desktop/DESKTOP/EE340/Lab_6/Original_Text.txt', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/sappylappy/Desktop/DESKTOP/EE340/Lab_6/tasktest1.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, delay)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f((5*sps*symbol_rate), analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f((5*sps*symbol_rate), analog.GR_COS_WAVE, 100000, 1, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_0_1_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_threshold_ff_1, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_threshold_ff_1, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_time_sink_x_0_1_0_1, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.rational_resampler_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TASK1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.analog_sig_source_x_0.set_sampling_freq((5*self.sps*self.symbol_rate))
        self.analog_sig_source_x_0_0.set_sampling_freq((5*self.sps*self.symbol_rate))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (5*self.sps*self.symbol_rate), 100000, 100, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, (self.sps*self.symbol_rate))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, (self.sps*self.symbol_rate))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, (5*self.sps*self.symbol_rate))
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(0, (self.sps*self.symbol_rate))
        self.qtgui_time_sink_x_0.set_samp_rate(self.symbol_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.sps*self.symbol_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.sps*self.symbol_rate)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(5*self.sps*self.symbol_rate)
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(self.symbol_rate)
        self.qtgui_time_sink_x_0_1_0_1.set_samp_rate(self.sps*self.symbol_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.analog_sig_source_x_0.set_sampling_freq((5*self.sps*self.symbol_rate))
        self.analog_sig_source_x_0_0.set_sampling_freq((5*self.sps*self.symbol_rate))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (5*self.sps*self.symbol_rate), 100000, 100, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, (self.sps*self.symbol_rate))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, (self.sps*self.symbol_rate))
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, (5*self.sps*self.symbol_rate))
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(0, (self.sps*self.symbol_rate))
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.sps*self.symbol_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.sps*self.symbol_rate)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(5*self.sps*self.symbol_rate)
        self.qtgui_time_sink_x_0_1_0_1.set_samp_rate(self.sps*self.symbol_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))

    def get_skip_head_count(self):
        return self.skip_head_count

    def set_skip_head_count(self, skip_head_count):
        self.skip_head_count = skip_head_count

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(self.noise)

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(int(self.delay))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(3, (self.sps*self.symbol_rate), self.symbol_rate, self.alpha, (11*self.sps)))




def main(top_block_cls=TASK1, options=None):

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
