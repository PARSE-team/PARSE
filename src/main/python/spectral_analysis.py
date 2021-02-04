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

        # Analysis Results
        self.Pxx_max_RCP = None
        self.freq_at_max = None

        self.bandwidth_RCP_at_max = None
        self.bandwidth_RCP_at_max_start = None
        self.bandwidth_RCP_at_max_stop = None
        self.Pxx_noise_var_RCP = None
        self.df_calc = None

        # Selected Range
        self.Pxx_local_max_RCP = None
        self.freq_at_local_max = None
        self.bandwidth_RCP_local_max = None
        self.bandwidth_RCP_local_max_start = None
        self.bandwidth_RCP_local_max_stop = None
        self.Pxx_local_var = None
        self.delta_Pxx_max_RCP = None
        self.df_obsv = None

        # LCP copies
        self.Pxx_LCP_at_max = None
        self.bandwidth_LCP_at_max = None
        self.Pxx_noise_var_LCP = None
        self.Pxx_LCP_at_local_max = None
        self.bandwidth_LCP_at_local_max = None
        self.delta_Pxx_LCP = None

        # user errors
        self.error_NdB_below = False
        self.error_direct_signal = False
        self.error_finding_bandwidth = False

        # testing
        self.resamp_freq = None
        self.resamp_pxx = None

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


def set_value(value, default):
    if value:
        return value
    else:
        return default


# screen4results_v1.py
def get_spectral_analysis_results(s, freqs, Pxx, freqs_LCP, Pxx_LCP, NdB_below=None,
                                  freq_local_min=None, freq_local_max=None):
    """
    A function that generates all results for the Signal Analysis pipeline.

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

    # ----------------------- SIGNAL ANALYSIS RESULTS -----------------------

    # save signal analysis results to object, which is passed between functions
    # “msmt” is shorthand for “measurement” of the signal characteristics:
    msmt = SpectralAnalysis()

    # ----- Analysis Settings -----

    # This parameter tells the program what “height” along the peak to measure its
    # width. In this example, we are telling the program to measure bandwidths at a
    # height of 10 dB below the top of the peak.
    # Display Name in GUI: “Measure bandwidths at <___> (dB) below peaks”
    msmt.NdB_below = set_value(NdB_below, default=10)  # default	# TODO: ADJUSTABLE

    # Find local maximum between these next two variables
    # Display Name in GUI: “X-Axis min (Hz)”
    msmt.freq_local_min = set_value(freq_local_min, default=s.xlim_min)  # TODO: ADJUSTABLE
    # Display Name in GUI: “X-Axis max (Hz)”
    msmt.freq_local_max = set_value(freq_local_max, default=s.xlim_max)  # TODO: ADJUSTABLE
    in_selected_range = np.argwhere((freqs > msmt.freq_local_min) & (freqs < msmt.freq_local_max))

    freqs_in_range = freqs[in_selected_range]
    Pxx_in_range = Pxx[in_selected_range]

    # FIXME: could be error above!

    # ----- Analysis Results -----

    # simply the maximum y value over the full x-range of frequencies
    # Display Name in GUI: “Y-Max (global)”
    msmt.Pxx_max_RCP = Pxx[np.argmax(Pxx)]
    msmt.Pxx_LCP_at_max = Pxx_LCP[np.argmax(Pxx)]

    # simply the x-value (frequency) of the max(y) we just found
    # Display Name in GUI: “X at Y-Max”
    msmt.freq_at_max = freqs[Pxx.argmax()]

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

    # Get the width of the peak we just found (aka frequency spread) measured at the
    # height that is set by “NdB_below”:
    def get_bandwidth(x, y, n_dB, exclude_zero=False):
        # x = np.array(x)
        # y = np.array(y)

        if exclude_zero:
            # FIXME: remove the false peak at 0
            where_to_look1, where_to_look2 = 0, 0
            if np.any(x < -0.5):
                where_to_look1 = np.max(np.argwhere(x < -0.5))
            else:
                print('error1')

            if np.any(x > 0.5):
                where_to_look2 = np.min(np.argwhere(x > 0.5))
            else:
                print('error2')
            # where_to_look = np.max(y[where_to_look1:where_to_look2])

            for i in range(where_to_look1, where_to_look2):
                y[i] = 0

        # height at which to measure bandwidth (aka bw)
        bw_height = max(y) - n_dB
        if bw_height < 0:
            print('Error: Bandwidth cannot be measured this far below peak. 1')
            # TODO: display errors to user
            msmt.error_NdB_below = True
            # and make the user try a new msmt.NdB_below value
            # PAUL WRITE THIS CODE ABOVE, I DON’T KNOW HOW XD

        # add 10x more intermediate points in our plot for higher resolution
        resamp_resolution = 100
        n_resamp_pts = len(x) * resamp_resolution
        y_resamp = signal.resample(y, num=n_resamp_pts)  # , domain='freq')
        x_resamp = np.linspace(min(x), max(x), n_resamp_pts)

        # testing
        msmt.resamp_freq = x_resamp
        msmt.resamp_pxx = y_resamp

        # print(np.where((y_resamp >= (bw_height - 1)) & (y_resamp <= (bw_height + 1))))

        # find any x values where y = bw_height
        indexes = []

        # find index of peaks in resampled array, iterate L/R to find first instances of n_dB
        # then max-min to find bandwidth
        index_of_resamp_peak = y.argmax() * resamp_resolution

        for i in range(index_of_resamp_peak, len(y_resamp)):
            if (y_resamp[i] >= (bw_height - 0.5)) and (y_resamp[i] <= (bw_height + 0.5)):
                indexes.append(i)
                print('\n\nFOUND1\n\n')
                break

        for i in range(index_of_resamp_peak, 1, -1):
            if (y_resamp[i] >= (bw_height - 0.5)) and (y_resamp[i] <= (bw_height + 0.5)):
                indexes.append(i)
                print('\n\nFOUND2\n\n')
                break

        if len(indexes) == 2:
            print('\nFOUND BANDWIDTH\n')
        else:
            print('\nDID NOT FIND BANDWIDTH\n')
            msmt.error_finding_bandwidth = True

        x_at_bw_height = x_resamp[indexes]

        bw_start = min(x_at_bw_height)
        bw_stop = max(x_at_bw_height)

        bw = bw_stop - bw_start

        return bw, bw_start, bw_stop

    # Display Name in GUI: “Bandwidth”
    bw_of_max = get_bandwidth(freqs, Pxx, msmt.NdB_below)  # , exclude_zero=True)
    msmt.bandwidth_RCP_at_max = bw_of_max[0]
    msmt.bandwidth_RCP_at_max_start = bw_of_max[1]
    msmt.bandwidth_RCP_at_max_stop = bw_of_max[2]
    # TODO: implement
    msmt.bandwidth_LCP_at_max = 0

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

    # This is the predicted/calculated frequency separation between the direct
    # signal and the echo signal and has already been calculated in the Processing
    # Settings object (Screen 3) as s.df_calc:
    # Display Name in GUI: "delta_X Predicted (𝛿f)"
    msmt.df_calc = s.df_calc

    # ----- Selected Range -----

    # After the user selects an x-range in the Settings panel, this output parameter
    # will be the maximum y value in between those bounds.
    # Display Name in GUI: "Y-Max (local)"
    msmt.Pxx_local_max_RCP = Pxx[np.argmax(Pxx[in_selected_range])]
    msmt.Pxx_LCP_at_local_max = Pxx_LCP[np.argmax(Pxx[in_selected_range])]

    # A signal is considered to be "buried in the noise" unless it is more than 3 dB
    # above the noise level.
    detectability_threshold = msmt.Pxx_noise_var_RCP + 3.0
    if msmt.Pxx_local_max_RCP <= detectability_threshold:
        print("Warning: local max may not be a signal; "
              "detectability limit is >= 3 dB above the noise.")
        # TODO: display errors to user
        msmt.error_direct_signal = True

    # x-value of the max(y_local) we just found.
    # Display Name in GUI: “X at Y-Max”
    msmt.freq_at_local_max = freqs_in_range[Pxx[in_selected_range].argmax()]

    # Same as the bandwidth formula above, but confined within the selected x-range.
    if msmt.Pxx_local_max_RCP <= msmt.NdB_below:
        print("Error: Bandwidth cannot be measured this far below peak. 2")
        # TODO: display errors to user
        msmt.error_NdB_below = True
        # and make the user try a new msmt.NdB_below value
        # PAUL WRITE THIS CODE ABOVE, I DON’T KNOW HOW

    # Display Name in GUI: “Bandwidth”
    bw_of_local = get_bandwidth(freqs[in_selected_range], Pxx[in_selected_range], msmt.NdB_below)
    msmt.bandwidth_RCP_local_max = bw_of_local[0]
    msmt.bandwidth_RCP_local_max_start = bw_of_local[1]
    msmt.bandwidth_RCP_local_max_stop = bw_of_local[2]
    # TODO: implement
    msmt.bandwidth_LCP_at_local_max = 0

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
