#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Send simple sine
# Author: vvs
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

from gnuradio import qtgui

class tx_simple(gr.top_block, Qt.QWidget):

    def __init__(self, server_ip="127.0.0.1"):
        gr.top_block.__init__(self, "Send simple sine")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Send simple sine")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
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

        self.settings = Qt.QSettings("GNU Radio", "tx_simple")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.server_ip = server_ip

        ##################################################
        # Variables
        ##################################################
        self.server_port_base = server_port_base = 10000
        self.server_bw_per_port = server_bw_per_port = 1000000
        self.freq_carrier = freq_carrier = 400000000
        self.server_port = server_port = int(server_port_base + (freq_carrier / server_bw_per_port))
        self._server_address_format_config = configparser.ConfigParser()
        self._server_address_format_config.read('config_file')
        try: server_address_format = self._server_address_format_config.get("main", "server_address_format")
        except: server_address_format = "tcp://%s:%d"
        self.server_address_format = server_address_format
        self.variable_tag_object_0 = variable_tag_object_0 = gr.tag_utils.python_to_tag((0, pmt.intern("key"), pmt.intern("value"), pmt.intern("src")))
        self.server_address = server_address = server_address_format % (server_ip, server_port) if server_address_format != "" else ""
        self.samp_rate = samp_rate = 32000
        self.freq_signal = freq_signal = 1000

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, server_address, 100, True, -1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


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
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            4096, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            freq_signal, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(True)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tags_strobe_0 = blocks.tags_strobe(gr.sizeof_gr_complex*1, pmt.to_pmt(samp_rate), 1000, pmt.intern("rx_rate"))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq_signal, 1, 0, 0.1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_tags_strobe_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.zeromq_pub_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "tx_simple")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_server_ip(self):
        return self.server_ip

    def set_server_ip(self, server_ip):
        self.server_ip = server_ip
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")

    def get_server_port_base(self):
        return self.server_port_base

    def set_server_port_base(self, server_port_base):
        self.server_port_base = server_port_base
        self.set_server_port(int(self.server_port_base + (self.freq_carrier / self.server_bw_per_port)))

    def get_server_bw_per_port(self):
        return self.server_bw_per_port

    def set_server_bw_per_port(self, server_bw_per_port):
        self.server_bw_per_port = server_bw_per_port
        self.set_server_port(int(self.server_port_base + (self.freq_carrier / self.server_bw_per_port)))

    def get_freq_carrier(self):
        return self.freq_carrier

    def set_freq_carrier(self, freq_carrier):
        self.freq_carrier = freq_carrier
        self.set_server_port(int(self.server_port_base + (self.freq_carrier / self.server_bw_per_port)))

    def get_server_port(self):
        return self.server_port

    def set_server_port(self, server_port):
        self.server_port = server_port
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")

    def get_server_address_format(self):
        return self.server_address_format

    def set_server_address_format(self, server_address_format):
        self.server_address_format = server_address_format
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")

    def get_variable_tag_object_0(self):
        return self.variable_tag_object_0

    def set_variable_tag_object_0(self, variable_tag_object_0):
        self.variable_tag_object_0 = variable_tag_object_0

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_tags_strobe_0.set_value(pmt.to_pmt(self.samp_rate))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_freq_signal(self):
        return self.freq_signal

    def set_freq_signal(self, freq_signal):
        self.freq_signal = freq_signal
        self.analog_sig_source_x_0.set_frequency(self.freq_signal)
        self.qtgui_sink_x_0.set_frequency_range(0, self.freq_signal)




def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--server-ip", dest="server_ip", type=str, default="127.0.0.1",
        help="Set Server IP [default=%(default)r]")
    return parser


def main(top_block_cls=tx_simple, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(server_ip=options.server_ip)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
