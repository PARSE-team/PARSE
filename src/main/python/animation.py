"""
animation.py -- Custom PyQt5 widget that dynamically visualizes data.
Copyright (C) 2020  Paul Sirri <paulsirri@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# File Description:
# This file contains a custom PyQt5 widget that dynamically
# visualizes data using the Matplotlib backend.

# from __future__ import unicode_literals

import matplotlib

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from process_signal import get_psd
from astropy.time import TimeDelta
import time
import numpy as np


class WorkerDataGenerator(QtCore.QObject):
    """ A class that functions as a worker, generating plots from a separate thread. """

    signal_to_return_plot = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):

        # QtCore.QObject.__init__(self, parent=parent)
        super(WorkerDataGenerator, self).__init__(parent)

        # flags used to control this worker
        self.is_running = False
        self.is_killed = False

        # local copy of data
        self.rcp_data = None
        self.lcp_data = None
        self.filenames = None

        # user input parameters
        self.sample_rate = None
        self.samples_per_raw_fft = None
        self.noverlap = None
        self.seconds_per_hop = None
        self.samples_per_hop = None

        # global time to update each frame
        self.global_time = None
        self.delta_time = None

        # local counters
        self.start_sec_count = None
        self.stop_sec_count = None
        self.start_index_count = None
        self.stop_index_count = None

    def get_plot(self):
        """ A method to return all information needed to plot one frame in the BSRAnimation. """

        if self.stop_index_count < self.rcp_data.size:
            # generate RCP and LCP data for this frame
            rcp_x, rcp_y = get_psd(self.rcp_data[self.start_index_count:self.stop_index_count],
                                   self.sample_rate, self.samples_per_raw_fft, self.noverlap)
            lcp_x, lcp_y = get_psd(self.lcp_data[self.start_index_count:self.stop_index_count],
                                   self.sample_rate, self.samples_per_raw_fft, self.noverlap)

            # format labels for this frame
            seconds_label = self.get_seconds_label()
            date_label = self.global_time
            time_label = str(date_label) + '\n' + seconds_label
            files_label = 'RCP file: ' + self.filenames[0] + '\nLCP file: ' + self.filenames[1]

            # store copy of counters, then update them
            current_second = self.stop_sec_count
            current_index = self.stop_index_count

            # update the counters
            self.update_counters()

            return rcp_x, rcp_y, lcp_x, lcp_y, files_label, time_label, current_index, current_second

    def get_seconds_label(self):
        """ A method that returns formatted seconds label. """
        return 'Seconds in File: {} to {}'.format(round(self.start_sec_count, 3),
                                                  round(self.stop_sec_count, 3))

    def update_counters(self):
        """ A method that updates counters used to generate each frame. """

        # update counters
        self.start_sec_count += self.seconds_per_hop
        self.stop_sec_count += self.seconds_per_hop
        self.start_index_count += self.samples_per_hop
        self.stop_index_count += self.samples_per_hop

        # update global time
        current_time = self.global_time + self.delta_time
        self.global_time = current_time

    def setup(self, s, rcp_data, lcp_data):

        # local copy of data
        self.rcp_data = rcp_data
        self.lcp_data = lcp_data
        self.filenames = s.filenames

        # user input parameters
        self.sample_rate = s.sample_rate
        self.samples_per_raw_fft = s.samples_per_raw_fft
        self.noverlap = s.noverlap
        self.seconds_per_hop = s.seconds_per_hop
        self.samples_per_hop = s.samples_per_hop

        # global time to update each frame
        self.global_time = s.global_time
        self.delta_time = TimeDelta(s.seconds_per_hop, format='sec')

        # local counters
        self.start_sec_count = s.start_sec_count
        self.stop_sec_count = s.stop_sec_count
        self.start_index_count = s.start_index_count
        self.stop_index_count = s.stop_index_count

    @QtCore.pyqtSlot(object, object, object)
    def run(self, s, rcp_data, lcp_data):

        print('SLOT: WorkerDataGenerator.run(s, rcp_data, lcp_data)\n')

        # unpack all data, settings, and parameters required to generate plots
        self.setup(s, rcp_data, lcp_data)

        # reset flags used to control this worker
        self.is_running = False
        self.is_killed = False

        print('is_running: ', self.is_running)

        while self.stop_index_count < self.rcp_data.size:

            print('is_running = ' + str(self.is_running) + ' (inside of loop)')

            # this worker is paused, exit loop if worker is set to resume or is killed
            while not self.is_running:
                # check every 50 milliseconds for changes to status
                time.sleep(0.05)
                # listen for flag to kill the worker
                if self.is_killed:
                    print('worker killed 1')
                    break

            # check to see if the loop broke because the worker was killed
            if self.is_killed:
                print('worker killed 2')
                break

            if self.is_running:
                print('worker returned next plot')
                self.signal_to_return_plot.emit(self.get_plot())
            else:
                print('\nerror error error\n')

        if self.stop_index_count >= self.rcp_data.size:
            print("\n\n----------------------\n ALL PLOTS GENERATED\n---------------------- ")

        if self.is_killed:
            print('\nthe worker was killed\n')
        else:
            print('\nthe worker was NOT killed\n')


class BSRAnimation(FigureCanvas):
    """ A canvas that updates itself every second with a new plot. """

    signal_to_run_worker = QtCore.pyqtSignal(object, object, object)

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        print("\nBSRAnimation.__init__()")

        # super(BSRAnimation, self).__init__(parent)

        # instantiate artist containers
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.signal_plot = self.fig.add_subplot(20, 1, (1, 14))
        self.overview_plot = self.fig.add_subplot(20, 1, (18, 20))
        # self.toolbar = NavigationToolbar(self.canvas,self)
        # gridlayout.addWidget(self.toolbar,0,0,1,2)

        # connect the Figure to the FigureCanvas (used for GUI only)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        # set the animation properties
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        # initialize settings and data
        self.s = None
        self.rcp_data = None
        self.lcp_data = None
        self.msmt = None

        # initialize queue to store plots the animation will draw each frame
        self.plots = None
        self.frame_index = None

        # the initial empty frame has not yet been setup
        self.was_setup = False

        # Create a WorkerDataGenerator object and a thread
        self.worker_datagen = WorkerDataGenerator()
        self.worker_datagen_thread = QtCore.QThread()

        # Assign the worker_datagen to the thread and start the thread
        self.worker_datagen.moveToThread(self.worker_datagen_thread)
        self.worker_datagen_thread.start()

        print('connecting signals to slots')

        # Connect signals & slots AFTER moving the object to the thread
        # connect worker_datagen.signal_to_return_plot (signal) to self.add_plot_to_queue (slot)
        self.worker_datagen.signal_to_return_plot.connect(self.add_plot_to_queue)
        # connect self.signal_to_run_worker (signal) to worker_datagen.run (slot)
        self.signal_to_run_worker.connect(self.worker_datagen.run)

    @QtCore.pyqtSlot(object)
    def add_plot_to_queue(self, data_tuple):
        """ A method to queue up frames for the animation to plot. """
        self.plots.append(data_tuple)

    def setup(self, s, rcp_data, lcp_data):
        """ A method to setup the BSRAnimation and its DataGeneratorWorker with new settings. """

        print("\nBSRAnimation.setup()")

        # kill the worker's current tasks
        self.kill_worker()

        # allow remaining plots to arrive from worker thread
        time.sleep(0.5)

        # pause the animation
        self.pause()

        # pass all IQ data and new user settings into the animation
        self.run_worker(s, rcp_data, lcp_data)

        # allow time for signal to send and process
        time.sleep(0.5)

        # save raw data and signal processing parameters
        self.s = s
        self.rcp_data = rcp_data
        self.lcp_data = lcp_data

        # remove any old plots from queue
        self.plots = []
        self.frame_index = 0

        # draw the initial empty frame
        self.was_setup = False
        self.update_frame()

    def play(self):
        self.start_worker()

        print("BSRAnimation.play()")
        if not self.timer.isActive():
            # the animation was paused, so play it
            self.timer.start(self.s.interval)

    def pause(self):
        self.pause_worker()

        print("BSRAnimation.pause()")
        if self.timer.isActive():
            # the animation was playing, so pause it
            self.timer.stop()

    def start_worker(self):
        print('\nBSRAnimation.start_worker()')
        if not self.worker_datagen.is_running:
            # the worker was paused, so start it
            self.worker_datagen.is_running = True

    def pause_worker(self):
        print('\nBSRAnimation.pause_worker()')
        if self.worker_datagen.is_running:
            # the worker was running, so pause it
            self.worker_datagen.is_running = False

    def kill_worker(self):
        print('\nBSRAnimation.kill_worker()\n')
        # kill the worker's run() method
        self.worker_datagen.is_killed = True

    def run_worker(self, s, rcp_data, lcp_data):
        print('\nBSRAnimation.run_worker()')
        print('\nSIGNAL: BSRAnimation.signal_to_run_worker.emit(s, rcp_data, lcp_data)')

        # begin generating plots, once the animation is run the first time
        self.signal_to_run_worker.emit(s, rcp_data, lcp_data)

    def show_previous_frame(self):
        self.pause()
        self.update_frame(plot_previous_frame=True)

    def show_next_frame(self):
        self.pause()
        print('\n\nshow_next_frame!')
        if self.frame_index == len(self.plots) - 1:
            print('no plots 1')
            self.start_worker()
            # FIXME: have the list emit a signal every time it's incremented?
            time.sleep(0.5)
            self.pause_worker()
        elif (len(self.plots) - 1 - self.frame_index) < 10:
            self.start_worker()
            time.sleep(0.1)
            self.pause_worker()
        self.update_frame(plot_next_frame=True)

    # @QtCore.pyqtSlot(object)
    def plot_analysis_results(self, msmt):
        """ A method to plot the measurements of the spectral analysis. """
        print("plot_analysis_results()")
        self.msmt = msmt
        self.update_frame(repeat=True, results=True)

    # @QtCore.pyqtSlot()
    def hide_analysis_results(self):
        """ A method to hide the measurements of the spectral analysis. """
        print("hide_analysis_results()")
        self.update_frame(repeat=True)

    def update_frame(self, plot_previous_frame=False, plot_next_frame=False, repeat=False,
                     results=False):
        """ A method to call each time the interval timer finishes. """

        # choose what to draw on the FigureCanvas
        if (self.s.stop_index_count < self.rcp_data.size) and (self.plots or not self.was_setup):

            print('plotting frame')

            ####################################
            # Get Data for Plotting this Frame
            ####################################

            if plot_previous_frame:
                # the user would like to redraw the previous frame
                if self.frame_index > 1:
                    # can only rewind to the first data plot
                    self.frame_index -= 1
                    rcp_x, rcp_y, lcp_x, lcp_y, files_label, time_label, current_index, \
                    current_second = self.plots[self.frame_index]
                else:
                    print('cannot rewind further')
            elif plot_next_frame:
                if self.frame_index == len(self.plots) - 1:
                    print('no more frames ready')
                    self.start_worker()
                    time.sleep(0.5)
                    self.pause_worker()
                if self.frame_index < len(self.plots) - 1:
                    # there are plots in queue
                    self.frame_index += 1
                    rcp_x, rcp_y, lcp_x, lcp_y, files_label, time_label, current_index, \
                    current_second = self.plots[self.frame_index]
            elif repeat:
                # plot the same frame, without updating any counters
                rcp_x, rcp_y, lcp_x, lcp_y, files_label, time_label, current_index, \
                current_second = self.plots[self.frame_index]
            elif self.plots:
                # samples remaining in file, draw next plot in queue or setup initial empty figure
                # save recent plots so the user can rewind if needed

                self.frame_index += 1

                # worker_datagen thread has queued a plot, unpack result
                rcp_x, rcp_y, lcp_x, lcp_y, files_label, time_label, current_index, \
                current_second = self.plots[self.frame_index]

            elif not self.was_setup:
                # FIXME: what's the point of having an initial empty frame?

                print("\ndrawing the initial empty frame \n")

                self.frame_index = 0
                self.plots.append((None, None))

                # do not plot any data on the initial frame
                rcp_x, rcp_y, lcp_x, lcp_y = [], [], [], []

                # format labels for this frame
                seconds_label = 'Seconds in File: {} to {}'.format(self.s.start_sec_count,
                                                                   self.s.stop_sec_count)
                date_label = self.s.global_time
                time_label = str(date_label) + '\n' + seconds_label
                files_label = 'RCP file: ' + self.s.filenames[0] + '\nLCP file: ' + \
                              self.s.filenames[1]

                # set index and second counters for the initial frame
                current_index = self.s.stop_index_count
                current_second = self.s.start_sec_count

                # only display an empty frame on the initial setup
                self.was_setup = True

            else:
                print('an error has occurred')
                # error has occurred
                rcp_x, rcp_y, lcp_x, lcp_y, files_label, time_label, current_index, \
                current_second = None

            print('frame index: ', self.frame_index)

            # clear the active axes in figure
            self.signal_plot.cla()
            self.overview_plot.cla()

            # set font
            font_mono = {'fontname': 'monospace'}
            font_arial = {'fontname': 'Arial'}

            ################################################
            # Plot the Power Spectral Density and Metadata
            ################################################

            # plot signal data for current frame
            self.signal_plot.plot(rcp_x, rcp_y, lw=0.7, label='RCP', color='black')
            self.signal_plot.plot(lcp_x, lcp_y, lw=0.7, label='LCP', color='red')
            self.signal_plot.legend(loc=2, fontsize=13)

            # mark the estimated direct signal
            # self.signal_plot.axvline(x=self.s.freq_plot_center, lw=0.1, color='blue')
            if self.frame_index != 0:
                direct_signal = rcp_x[np.argmax(rcp_y)]
                self.signal_plot.axvline(x=direct_signal, lw=0.1, color='blue')

            # plot labels to display metadata for this frame
            self.signal_plot.patch.set_visible(False)
            self.signal_plot.text(0.26, 1.10, s=files_label, **font_mono, fontsize=10,
                                  horizontalalignment='center',
                                  verticalalignment='center',
                                  transform=self.signal_plot.transAxes,
                                  bbox=(dict(facecolor='white', alpha=0.2)))
            self.signal_plot.text(0.77, 1.10, s=time_label, **font_mono, fontsize=10,
                                  horizontalalignment='center',
                                  verticalalignment='center',
                                  transform=self.signal_plot.transAxes,
                                  bbox=(dict(facecolor='white', alpha=0.2)))

            # label the axes for the signal plot
            self.signal_plot.set_xlabel("Frequency (Hz)", fontsize=15, **font_arial)
            self.signal_plot.set_ylabel("Power (dB)", fontsize=15, **font_arial)

            # reset the window properties, which are cleared each frame
            self.signal_plot.set_xlim(self.s.xlim_min, self.s.xlim_max)
            self.signal_plot.set_ylim(self.s.ylim_min, self.s.ylim_max)

            ######################################################
            # Plot the Direct Signal Over the Entire Time Series
            ######################################################

            # plot the signal in file over time
            self.overview_plot.plot(self.s.overview_seconds, self.s.overview_pxx, lw=0.7,
                                    color='blue')

            # mark current frame's location in the time series
            self.overview_plot.axvline(x=current_second, lw=1, color='red')

            # add label for the file's start time and end times
            self.overview_plot.text(0.11, -0.54, s=str(self.s.file_start_time)[:-4], **font_arial,
                                    fontsize=11,
                                    horizontalalignment='center',
                                    verticalalignment='center',
                                    transform=self.signal_plot.transAxes,
                                    bbox=(dict(facecolor='white', alpha=0.2)))
            self.overview_plot.text(0.89, -0.54, s=str(self.s.file_end_time)[:-4], **font_arial,
                                    fontsize=11,
                                    horizontalalignment='center',
                                    verticalalignment='center',
                                    transform=self.signal_plot.transAxes,
                                    bbox=(dict(facecolor='white', alpha=0.2)))

            # label the axes for the overview plot
            self.overview_plot.set_xlabel("Time in File (seconds)", fontsize=13, **font_arial)
            self.overview_plot.set_ylabel("Maximum\nPower\n(dB)", fontsize=12, **font_arial,
                                          rotation=0, labelpad=33)
            self.overview_plot.yaxis.set_label_coords(-0.1, 0)

            # set padding options for both axes
            seconds_domain = self.s.overview_seconds[-1] - self.s.overview_seconds[0]
            time_pad = seconds_domain * 0.01
            signal_range = np.max(self.s.overview_pxx) - np.min(self.s.overview_pxx)
            signal_pad = signal_range * 0.1

            # set the window properties
            self.overview_plot.set_xlim(self.s.overview_seconds[0] - time_pad,
                                        self.s.overview_seconds[-1] + time_pad)
            self.overview_plot.set_ylim(np.min(self.s.overview_pxx) - signal_pad,
                                        np.max(self.s.overview_pxx) + signal_pad)

            # update the counter
            self.s.stop_index_count = current_index

            if results:
                # mark and label the selected range
                self.signal_plot.axvline(x=self.msmt.freq_local_min, lw=0.7, color='blue',
                                         linestyle='--')
                self.signal_plot.axvline(x=self.msmt.freq_local_max, lw=0.7, color='blue',
                                         linestyle='--')
                self.signal_plot.text(x=(((self.msmt.freq_local_max - self.msmt.freq_local_min) / 3) + self.msmt.freq_local_min),
                                      y=self.msmt.Pxx_max * 1.3,
                                      s='Selected Range', **font_arial, fontsize=10,
                                      horizontalalignment='center',
                                      verticalalignment='top',
                                      color='blue')

                # mark and label both peaks
                self.signal_plot.plot([self.msmt.freq_at_max, self.msmt.freq_at_max],
                                      [-150, self.msmt.Pxx_max],
                                      lw=1.4, color='black', linestyle='-', marker="D", markersize=3)
                self.signal_plot.text(x=self.msmt.freq_at_max,
                                      y=self.msmt.Pxx_max * 1.15,
                                      s='global max', **font_arial, fontsize=10,
                                      horizontalalignment='center',
                                      verticalalignment='top',
                                      color='black')
                self.signal_plot.plot([self.msmt.freq_at_local_max, self.msmt.freq_at_local_max],
                                      [-150, self.msmt.Pxx_local_max],
                                      lw=1.4, color='black', linestyle='-', marker="D", markersize=3)
                self.signal_plot.text(x=self.msmt.freq_at_local_max,
                                      y=self.msmt.Pxx_local_max * 1.1,
                                      s='local max', **font_arial, fontsize=10,
                                      horizontalalignment='center',
                                      verticalalignment='top',
                                      color='black')

                # mark and label delta-f
                self.signal_plot.plot(
                    [self.msmt.freq_at_max, self.msmt.freq_at_local_max], [(self.s.ylim_min + (self.s.ylim_max - self.s.ylim_min) * 0.1), (self.s.ylim_min + (self.s.ylim_max - self.s.ylim_min) * 0.1)],
                    lw=1.4, color='black', linestyle='-', marker="D", markersize=4)
                self.signal_plot.text(x=(np.max([self.msmt.freq_at_max, self.msmt.freq_at_local_max]) + 1),
                                      y=(self.s.ylim_min + (self.s.ylim_max - self.s.ylim_min) * 0.1),
                                      s='delta_f',
                                      **font_arial, fontsize=11,
                                      horizontalalignment='right',
                                      verticalalignment='center',
                                      color='black')

                # mark and label the bandwidth of both peaks
                self.signal_plot.plot([self.msmt.bandwidth_of_max_start, self.msmt.bandwidth_of_max_stop],
                                      [(self.msmt.Pxx_max - self.msmt.NdB_below), (self.msmt.Pxx_max - self.msmt.NdB_below)],
                                      lw=1.3, color='black', linestyle='-', marker="D", markersize=3)
                self.signal_plot.text(x=(self.msmt.bandwidth_of_max_start + (self.msmt.bandwidth_of_max_stop - self.msmt.bandwidth_of_max_start) / 2),
                                      y=(self.msmt.Pxx_max - self.msmt.NdB_below),
                                      s='bandwidth\nat -' + str(self.msmt.NdB_below) + ' dB', **font_arial, fontsize=10,
                                      horizontalalignment='center',
                                      verticalalignment='center',
                                      color='black')
                self.signal_plot.plot(
                    [self.msmt.bandwidth_local_peak_start, self.msmt.bandwidth_local_peak_stop],
                    [(self.msmt.Pxx_local_max - self.msmt.NdB_below),
                     (self.msmt.Pxx_local_max - self.msmt.NdB_below)],
                    lw=1.3, color='black', linestyle='-', marker="D", markersize=3)
                self.signal_plot.text(x=(self.msmt.bandwidth_local_peak_start + (self.msmt.bandwidth_local_peak_stop - self.msmt.bandwidth_local_peak_start) / 2),
                                      y=(self.msmt.Pxx_local_max - self.msmt.NdB_below),
                                      s='bandwidth\nat -' + str(self.msmt.NdB_below) + ' dB',
                                      **font_arial, fontsize=10,
                                      horizontalalignment='center',
                                      verticalalignment='center',
                                      color='black')

                # testing
                # self.signal_plot.plot(self.msmt.resamp_freq, self.msmt.resamp_pxx, lw=0.2,
                # color='green')

                print()
                self.msmt.pprint()
                print()

            # draw canvas each frame
            self.draw()

        elif self.s.stop_index_count < self.rcp_data.size:
            # the animation is waiting for the worker_datagen thread to queue another plot
            print('...waiting for worker_datagen thread...')
            pass

        else:
            print("\n\n------------------\n  ANIMATION COMPLETED\n------------------ ")
            # animation completed, no frames remaining
            self.timer.stop()

# https://matplotlib.org/3.1.1/gallery/user_interfaces/embedding_in_qt_sgskip.html
