"""
spectral_analysis.py -- Generates results for the Spectral Analysis tab.
Copyright (C) 2021  Paul Sirri <paulsirri@gmail.com>

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
# This file contains functions to generate results for the Spectral Analysis pipeline.


import numpy as np
from scipy import signal
import copy


class SpectralAnalysis:

    def __init__(self):
        # Analysis Settings
        self.NdB_below = None
        self.freq_local_min = None
        self.freq_local_max = None
        self.df_calc = None

        # Noise Variability Calculations
        self.Pxx_noise_var_RCP = None
        self.Pxx_noise_var_LCP = None

        # Global Calculations
        self.Pxx_max_RCP = None
        self.Pxx_LCP_at_max = None
        self.freq_at_max = None
        # Global Bandwidth RCP
        self.bandwidth_RCP_at_max = None
        self.bandwidth_start_RCP_at_max = None
        self.bandwidth_stop_RCP_at_max = None
        # Global Bandwidth LCP
        self.bandwidth_LCP_at_max = None
        self.bandwidth_start_LCP_at_max = None
        self.bandwidth_stop_LCP_at_max = None

        # Selected Range Calculations
        self.Pxx_local_max_RCP = None
        self.Pxx_LCP_at_local_max = None
        self.freq_at_local_max = None
        # Selected Range Bandwidth RCP
        self.bandwidth_RCP_local_max = None
        self.bandwidth_start_RCP_local_max = None
        self.bandwidth_stop_RCP_local_max = None
        # Selected Range Bandwidth LCP
        self.bandwidth_LCP_local_max = None
        self.bandwidth_start_LCP_local_max = None
        self.bandwidth_stop_LCP_local_max = None

        # Other
        self.Pxx_local_var = None
        self.delta_Pxx_max_RCP = None
        self.delta_Pxx_LCP = None
        self.df_obsv = None

        # User Errors
        self.error_NdB_below = False
        self.error_global_RCP = False
        self.error_global_LCP = False
        self.error_local_RCP = False
        self.error_local_LCP = False
        self.error_finding_bandwidth = False

        # testing effects of resampling the pxx
        self.resamp_freq = None
        self.resamp_pxx = None
        # other testing
        self.x = None
        self.y = None

    def pprint(self):
        print('\nPlot Analysis: ')
        print('NdB_below:               ', self.NdB_below)
        print('freq_local_min:          ', self.freq_local_min)
        print('freq_local_max:          ', self.freq_local_max)
        print('Pxx_max_RCP:             ', self.Pxx_max_RCP)
        print('freq_at_max:             ', self.freq_at_max)
        print('bandwidth_RCP_at_max:    ', self.bandwidth_RCP_at_max)
        print('Pxx_noise_var_RCP:       ', self.Pxx_noise_var_RCP)
        print('df_calc:                 ', self.df_calc)
        print('Pxx_local_max_RCP:       ', self.Pxx_local_max_RCP)
        print('freq_at_local_max:       ', self.freq_at_local_max)
        print('bandwidth_RCP_local_max: ', self.bandwidth_RCP_local_max)
        print('Pxx_local_var:           ', self.Pxx_local_var)
        print('delta_Pxx_max_RCP:       ', self.delta_Pxx_max_RCP)
        print('df_obsv:                 ', self.df_obsv)
        print()


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


def confirm_ndb_acceptable(y, noise_var):
    # height at which to measure bandwidth (aka bw)
    bw_height = max(y) - noise_var
    if (bw_height <= 0) or (bw_height <= noise_var):
        """print('Error: Cannot measure bandwidth at or below noise levels. '
              'Too far below peak. Setting default to 2 dB below peak.')"""
        error_NdB_below = True
        return error_NdB_below
    else:
        error_NdB_below = False
        return error_NdB_below


def set_value(value, default):
    if value:
        return value
    else:
        return default


def get_bandwidth(msmt, x, y, n_dB):
    # ensure np.ndarray shape=(n,)
    x = np.squeeze(x)
    y = np.squeeze(y)

    # height at which to measure bandwidth (aka bw)
    bw_height = max(y) - n_dB

    # find any x values where y = bw_height
    bw_start = None
    bw_stop = None

    msmt.x = []
    msmt.y = []

    # find left side of bandwidth (iterate right to left)
    for ind in range(y.argmax(), 0, -1):
        if y[ind] < bw_height:
            # iterate until finding a value below the bandwidth height
            i1 = ind + 1
            x1 = x[i1]
            y1 = y[i1]
            i2 = ind
            x2 = x[i2]
            y2 = y[i2]

            # interpolate data to find accurate measurement for bandwidth
            x_interp = np.interp(bw_height, [y2, y1], [x2, x1])
            bw_start = x_interp

        if bw_start:
            break
    # find right side of bandwidth (iterate left to right)
    for ind in range(y.argmax(), y.size):
        if y[ind] < bw_height:
            # iterate until finding a value below the bandwidth height
            i1 = ind - 1
            x1 = x[i1]
            y1 = y[i1]
            i2 = ind
            x2 = x[i2]
            y2 = y[i2]

            # interpolate data to find accurate measurement for bandwidth
            x_interp = np.interp(bw_height, [y2, y1], [x2, x1])
            bw_stop = x_interp

        if bw_stop:
            break

    if bw_start and bw_stop:
        print('\nFOUND BANDWIDTH\n')
    else:
        print('\nDID NOT FIND BANDWIDTH\n')
        msmt.error_finding_bandwidth = True

    bw = np.abs(bw_stop - bw_start)

    return bw, bw_start, bw_stop


def get_spectral_analysis_results(s, freqs, Pxx, freqs_LCP, Pxx_LCP, NdB_below=None,
                                  freq_local_min=None, freq_local_max=None):
    """
    A function that generates all results for the Spectral Analysis pipeline.

    NOTATION:
    dB          decibels; herein defined as 10*log10(power/average_noise_power)
    Pxx         1D array of power values (dB) from Matplotlib’s PSD function
    freqs       1D array of x-axis frequencies (Hz) from Matplotlib’s PSD function
    freq_       frequency of something (Hz)
    df          differential Doppler shift (aka frequency separation
                between the direct and echo peaks)
    bw          bandwidth (Hz); frequency width of a peak measured at a predefined
                height on said peak
    """

    # save signal analysis results to object, which is passed between functions
    # “msmt” is shorthand for “measurement” of the signal characteristics:
    msmt = SpectralAnalysis()

    # ----------------------- ANALYSIS PARAMETERS -----------------------

    # This parameter tells the program what “height” along the peak to measure its
    # width. In this example, we are telling the program to measure bandwidths at a
    # height of 10 dB below the top of the peak.
    # Display Name in GUI: “Measure bandwidths at <___> (dB) below peaks”
    msmt.NdB_below = set_value(NdB_below, default=2)  # default	# TODO: ADJUSTABLE

    # Find local maximum between these next two variables
    # Display Name in GUI: “X-Axis min (Hz)”
    msmt.freq_local_min = set_value(freq_local_min, default=s.xlim_min)  # TODO: ADJUSTABLE
    # Display Name in GUI: “X-Axis max (Hz)”
    msmt.freq_local_max = set_value(freq_local_max, default=s.xlim_max)  # TODO: ADJUSTABLE

    # signal considered "buried in the noise" unless it is more than 3 dB above the noise level
    # detectability_threshold = 3.0

    # if the user has default x-range set, be sure that default appears on initial plot window
    if not freq_local_min and not freq_local_max:
        # ensure the selected range can fit within default plot window by adding a fixed-length pad
        range_pad = round((s.xlim_max - s.xlim_min) * 0.15)
        msmt.freq_local_min = copy.deepcopy(s.xlim_min) + range_pad
        msmt.freq_local_max = copy.deepcopy(s.xlim_max) - range_pad

    in_selected_range = np.argwhere((freqs > msmt.freq_local_min) & (freqs < msmt.freq_local_max))

    # This is the predicted/calculated frequency separation between the direct
    # signal and the echo signal and has already been calculated in the Processing
    # Settings object (Screen 3) as s.df_calc:
    # Display Name in GUI: "delta_X Predicted (𝛿f)"
    msmt.df_calc = s.df_calc

    # ----------------------- ANALYSIS RESULTS: GLOBAL -----------------------

    # simply the maximum y value over the full x-range of frequencies
    # Display Name in GUI: “Y-Max (global)”
    msmt.Pxx_max_RCP = Pxx[np.argmax(Pxx)]
    msmt.Pxx_LCP_at_max = Pxx_LCP[np.argmax(Pxx)]

    # simply the x-value (frequency) of the max(y) we just found
    # Display Name in GUI: “X at Y-Max”
    msmt.freq_at_max = freqs[np.argmax(Pxx)]

    # todo: remove?
    if s.mission == 'Rosetta':
        # FIXME: multiple points?
        # FIXME: remove the false peak at 0
        where_to_look1, where_to_look2 = 0, 0
        if np.any(freqs < -0.5):
            where_to_look1 = np.max(np.argwhere(freqs < -0.5))
        else:
            print('errorA')
        if np.any(freqs > 0.5):
            where_to_look2 = np.min(np.argwhere(freqs > 0.5))
        else:
            print('errorB')
        # where_to_look = np.max(y[where_to_look1:where_to_look2])

        Pxx_copy = copy.deepcopy(Pxx)

        for i in range(where_to_look1, where_to_look2):
            Pxx_copy[i] = 0

        msmt.freq_at_max = freqs[Pxx_copy.argmax()]

    # Analyze signal noise characteristics
    # First define the x-ranges where there should be ONLY noise and never a signal
    in_noise_range = np.where(
        ((freqs > -0.8 * s.sample_rate / 2) & (freqs < (msmt.freq_at_max - 1.2 * s.df_calc))) |
        ((freqs < 0.8 * s.sample_rate / 2) & (freqs > (msmt.freq_at_max + 1.2 * s.df_calc))))

    # This next variable will tell us how much the noise power oscillates above and
    # below its mean value in dB. You can only safely distinguish a signal from the
    # noise if that signal is at least 3dB higher than the noise’s standard deviation.
    # Display Name in GUI: "Noise Variation"
    msmt.Pxx_noise_var_RCP = np.std(Pxx[in_noise_range])
    msmt.Pxx_noise_var_LCP = np.std(Pxx_LCP[in_noise_range])

    # confirm the user/default parameter for NdB Below will work for all data subsets
    if not msmt.error_NdB_below:
        msmt.error_NdB_below = confirm_ndb_acceptable(Pxx, msmt.Pxx_noise_var_RCP)
    if not msmt.error_NdB_below:
        msmt.error_NdB_below = confirm_ndb_acceptable(Pxx_LCP, msmt.Pxx_noise_var_LCP)
    if not msmt.error_NdB_below:
        msmt.error_NdB_below = confirm_ndb_acceptable(Pxx[in_selected_range], msmt.Pxx_noise_var_RCP)
    if not msmt.error_NdB_below:
        msmt.error_NdB_below = confirm_ndb_acceptable(Pxx_LCP[in_selected_range], msmt.Pxx_noise_var_LCP)

    # Get the width of the peak we just found (aka frequency spread) measured at the
    # height that is set by “NdB_below”
    # Display Name in GUI: “Bandwidth”
    if msmt.Pxx_max_RCP > (msmt.Pxx_noise_var_RCP + 3.0):
        # if the peak is detectable above the noise level, retrieve bandwidth
        bw_RCP_at_max = get_bandwidth(msmt, freqs, Pxx, msmt.NdB_below)
    else:
        msmt.error_global_RCP = True
        bw_RCP_at_max = (0, 0, 0)
    msmt.bandwidth_RCP_at_max = bw_RCP_at_max[0]
    msmt.bandwidth_start_RCP_at_max = bw_RCP_at_max[1]
    msmt.bandwidth_stop_RCP_at_max = bw_RCP_at_max[2]

    # repeat bandwidth calculation for LCP signal
    if msmt.Pxx_LCP_at_max > (msmt.Pxx_noise_var_LCP + 3.0):
        # if the peak is detectable above the noise level, retrieve bandwidth
        bw_LCP_at_max = get_bandwidth(msmt, freqs, Pxx_LCP, msmt.NdB_below)
    else:
        msmt.error_global_LCP = True
        bw_LCP_at_max = (0, 0, 0)
    msmt.bandwidth_LCP_at_max = bw_LCP_at_max[0]
    msmt.bandwidth_start_LCP_at_max = bw_LCP_at_max[1]
    msmt.bandwidth_stop_LCP_at_max = bw_LCP_at_max[2]

    # ----------------------- ANALYSIS RESULTS: SELECTED RANGE (LOCAL) -----------------------

    # After the user selects an x-range in the Settings panel, this output parameter
    # will be the maximum y value in between those bounds.
    # Display Name in GUI: "Y-Max (local)"
    msmt.Pxx_local_max_RCP = Pxx[in_selected_range][np.argmax(Pxx[in_selected_range])]
    msmt.Pxx_LCP_at_local_max = Pxx_LCP[in_selected_range][np.argmax(Pxx[in_selected_range])]

    # A signal is considered to be "buried in the noise" unless it is more than 3 dB
    # above the noise level.
    detectability_threshold = msmt.Pxx_noise_var_RCP + 3.0
    if msmt.Pxx_local_max_RCP <= detectability_threshold:
        msmt.error_local_RCP = True

    # x-value of the max(y_local) we just found.
    # Display Name in GUI: “X at Y-Max”
    msmt.freq_at_local_max = freqs[in_selected_range][np.argmax(Pxx[in_selected_range])]

    # Same as the bandwidth formula above, but confined within the selected x-range.
    if msmt.Pxx_local_max_RCP <= msmt.NdB_below:
        msmt.error_NdB_below = True

    # Display Name in GUI: “Bandwidth”
    if msmt.Pxx_local_max_RCP > (msmt.Pxx_noise_var_RCP + 3.0):
        # if the peak is detectable above the noise level, retrieve bandwidth
        bw_RCP_local_max = get_bandwidth(msmt, freqs[in_selected_range], Pxx[in_selected_range], msmt.NdB_below)
    else:
        msmt.error_local_RCP = True
        bw_RCP_local_max = [0, 0, 0]
    msmt.bandwidth_RCP_local_max = bw_RCP_local_max[0]
    msmt.bandwidth_start_RCP_local_max = bw_RCP_local_max[1]
    msmt.bandwidth_stop_RCP_local_max = bw_RCP_local_max[2]

    # repeat bandwidth calculation for LCP signal
    if msmt.Pxx_LCP_at_local_max > (msmt.Pxx_noise_var_LCP + 3.0):
        # if the peak is detectable above the noise level, retrieve bandwidth
        bw_LCP_local_max = get_bandwidth(msmt, freqs[in_selected_range], Pxx_LCP[in_selected_range], msmt.NdB_below)
    else:
        msmt.error_local_LCP = True
        bw_LCP_local_max = [0, 0, 0]
    msmt.bandwidth_LCP_local_max = bw_LCP_local_max[0]
    msmt.bandwidth_start_LCP_local_max = bw_LCP_local_max[1]
    msmt.bandwidth_stop_LCP_local_max = bw_LCP_local_max[2]

    # This will tell us how much the power oscillates from its mean value within the
    # selected x-range. The higher the variance, the harder it is to accurately
    # state a single maximum power for this second peak.
    # Display Name in GUI: “Variability”
    msmt.Pxx_local_var = np.std(Pxx[in_selected_range])

    # This is the difference between the height of the two peaks in this graph.
    # Display Name in GUI: “delta_Y-Max”
    msmt.delta_Pxx_max_RCP = msmt.Pxx_max_RCP - msmt.Pxx_local_max_RCP
    msmt.delta_Pxx_LCP = msmt.Pxx_LCP_at_max - msmt.Pxx_LCP_at_local_max

    # This is the measured frequency separation between the two peaks in this graph.
    # Display Name in GUI: “delta_X Observed (𝛿f)”
    msmt.df_obsv = msmt.freq_at_max - msmt.freq_at_local_max

    return msmt
