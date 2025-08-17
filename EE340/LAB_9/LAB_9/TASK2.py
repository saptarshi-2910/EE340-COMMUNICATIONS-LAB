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
from gnuradio.filter import pfb
import sip



class TASK2(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "TASK2")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist([1,-1], [0, 1],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.variable_constellation_0.set_npwr(1.0)
        self.symbrate = symbrate = 50000
        self.samp_rate = samp_rate = 32000
        self.ntaps = ntaps = sps*11
        self.nfilts = nfilts = 32
        self.gain = gain = 3

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccf(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
            1024, #size
            400000, #samp_rate
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
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


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


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_fff(
            sps,
            taps=firdes.root_raised_cosine(gain,sps*symbrate,symbrate,1,ntaps),
            flt_size=32,
            atten=100)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                10,
                (8*1e6),
                25000,
                5000,
                window.WIN_HAMMING,
                6.76))
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(8, (2*3.14/100), firdes.root_raised_cosine(gain,nfilts*sps*symbrate,symbrate,1,ntaps), 32, 16, 1.5, 1)
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2, digital.DIFF_DIFFERENTIAL)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc((2*3.14/100), 2, False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(variable_constellation_0)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc([1,-1], 1)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 19)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/sappylappy/Desktop/DESKTOP/EE340/LAB_9/Original_Text.txt', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'OUTPUT2.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c((8*1e6), analog.GR_COS_WAVE, 500001, 1, 0, 3.14)
        self.analog_sig_source_x_0 = analog.sig_source_f((8*1e6), analog.GR_COS_WAVE, 500000, 3, 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.digital_diff_encoder_bb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TASK2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_ntaps(self.sps*11)
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symbrate,self.symbrate,1,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symbrate,self.symbrate,1,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0
        self.digital_constellation_decoder_cb_0.set_constellation(self.variable_constellation_0)

    def get_symbrate(self):
        return self.symbrate

    def set_symbrate(self, symbrate):
        self.symbrate = symbrate
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symbrate,self.symbrate,1,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symbrate,self.symbrate,1,self.ntaps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symbrate,self.symbrate,1,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symbrate,self.symbrate,1,self.ntaps))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symbrate,self.symbrate,1,self.ntaps))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.digital_pfb_clock_sync_xxx_0.update_taps(firdes.root_raised_cosine(self.gain,self.nfilts*self.sps*self.symbrate,self.symbrate,1,self.ntaps))
        self.pfb_arb_resampler_xxx_0.set_taps(firdes.root_raised_cosine(self.gain,self.sps*self.symbrate,self.symbrate,1,self.ntaps))




def main(top_block_cls=TASK2, options=None):

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
