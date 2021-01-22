"""
process_signal.py -- Generates results for the Signal Processing tab.
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
# Generates results for the Signal Processing tab.

import numpy as np
from matplotlib.mlab import psd
# from matplotlib.pyplot import psd
import math
from scipy.constants import speed_of_light


class ProgramSettings:
    """ A class that stores the user settings for running the animation. """

    def __init__(self):
        # TODO: write a description of each setting
        # by order in which they appear in get_settings()

        # RCP and LCP filenames
        self.filenames = None

        # date and time
        self.global_time = None
        self.file_start_time = None
        self.file_end_time = None

        # General Variables
        self.delta_f_calc = None
        self.sample_rate = None
        self.time_step = None

        # Sliding Window Size “L”
        self.samples_per_raw_fft = None
        self.freq_res = None
        self.seconds_per_raw_fft = None

        # Sliding Window Step-Size “D”
        self.min_hop_percent = None
        self.percent_window_per_hop = None
        self.seconds_per_hop = None
        self.samples_per_hop = None

        # Windows to Average Together “K”
        self.raw_fft_per_average = None

        # Welch Periodogram Calculation
        self.seconds_for_welch = None
        self.samples_for_welch = None
        self.noverlap = None
        # user-defined indexes
        self.start_sec_user = None
        self.stop_sec_user = None
        self.start_index_user = None
        self.stop_index_user = None
        # updated each frame
        self.start_sec_count = None
        self.stop_sec_count = None
        self.start_index_count = None
        self.stop_index_count = None
        self.interval = None

        # Plot Settings
        self.freq_plot_center = None
        self.xlim_min = None
        self.xlim_max = None
        self.ylim_min = None
        self.ylim_max = None

        # Signal Overview Calculation
        self.overview_seconds = None
        self.overview_pxx = None
        self.overview_freqs = None
        self.overview_seconds = None
        self.ppx_min = None
        self.ppx_max = None

        # Acquisition Geometry
        self.target = None
        self.mission = None
        self.dt_occ = None
        self.radius_target = None
        self.v_sc_orbital = None
        self.altitude_sc = None

    def print_debug(self, flag):
        print('\n\nDEBUG ' + flag)
        print('delta_f_calc:                           ', self.delta_f_calc)
        print('dt_occ:                            ', self.dt_occ)
        print('sample_rate:                       ', self.sample_rate)
        # the old value was probably near 320000?
        print('samples_per_raw_fft:               ', self.samples_per_raw_fft)
        # the old value was 20, hardcoded
        print('seconds_per_raw_fft:               ', self.seconds_per_raw_fft)
        # should be less than 1
        print('freq_res:                          ', self.freq_res)
        # old value was 5
        print('seconds_per_hop:                   ', self.seconds_per_hop)
        # the old value was 30, now it's hardcoded as 2
        # we can hardcode this as 30 and see if that helps!
        print('raw_fft_per_average:               ', self.raw_fft_per_average)
        # old hardcoded value was 600
        print('seconds_for_welch:                 ', self.seconds_for_welch)

        print('freq_plot_center:                  ', self.freq_plot_center)

        print()
        print()


def round_to_nearest_n(x, n):
    return n * round(x / n)


def get_psd(data, sample_rate, samples_per_raw_fft, noverlap):
    """ A function that performs a series of mathematical operations
    on a subset of raw IQ data, then returns an x-axis and y-axis. """

    # power spectral density
    psd_frame = psd(data,
                    Fs=sample_rate,
                    NFFT=samples_per_raw_fft,
                    noverlap=noverlap)

    # unpack into separate arrays, performing simple operations on y-values
    x_data = psd_frame[1]
    y_data = 10 * np.log10(psd_frame[0])

    # TODO: check that "concatenate" isn't creating a multidimensional array
    # subtract the noise from the plot
    noise_index_1 = np.where((x_data > -400) & (x_data < -200))
    noise_index_2 = np.where((x_data > 200) & (x_data < 400))
    noise_indexes = np.concatenate((noise_index_1[0], noise_index_2[0]))
    noise_average = np.mean(y_data[noise_indexes])
    y_data -= noise_average

    return x_data, y_data


def signal_overview(rcp_data, lcp_data, samples_for_welch, sample_rate, samples_per_raw_fft,
                    noverlap, samples_per_hop, mission, rate=25):
    ##############################
    # Signal Overview Calculation
    ##############################

    print('signal_overview()')

    # find the duration and frequency of the direct signal in file
    start_i = 0
    stop_i = samples_for_welch
    overview_seconds = []
    overview_pxx = []
    overview_freqs = []
    ppx_min = 0

    print('indexes of first psd: [ ' + str(start_i) + ' : ' + str(stop_i) + ' ]\n')
    while stop_i < rcp_data.size:
        # generate RCP and LCP data for plotting each frame
        rcp_x, rcp_y = get_psd(rcp_data[start_i:stop_i], sample_rate, samples_per_raw_fft,
                               noverlap)
        lcp_x, lcp_y = get_psd(lcp_data[start_i:stop_i], sample_rate, samples_per_raw_fft,
                               noverlap)

        # find direct signal
        if mission == 'Rosetta':
            # avoid recognizing a false peak in the Rosetta dataset
            where_to_look = np.max(np.argwhere(rcp_x < -1))
            max_signal = np.max([np.max(rcp_y[0:where_to_look]), np.max(lcp_y[0:where_to_look])])
            freq_of_max = None
            if max_signal == np.max(rcp_y[0:where_to_look]):
                argmax = np.argmax(rcp_y[0:where_to_look])
                freq_of_max = rcp_x[argmax]
            elif max_signal == np.max(lcp_y[0:where_to_look]):
                argmax = np.argmax(lcp_y[0:where_to_look])
                freq_of_max = lcp_x[argmax]
            else:
                print('ERROR FINDING DIRECT SIGNAL')
        elif mission == 'Dawn':
            max_signal = np.max([np.max(rcp_y), np.max(lcp_y)])
            freq_of_max = None
            if max_signal == np.max(rcp_y):
                argmax = np.argmax(rcp_y)
                freq_of_max = rcp_x[argmax]
            elif max_signal == np.max(lcp_y):
                argmax = np.argmax(lcp_y)
                freq_of_max = lcp_x[argmax]
            else:
                print('ERROR FINDING DIRECT SIGNAL')

        # find minimum signal
        min_signal = np.min([np.min(rcp_y), np.min(lcp_y)])
        if min_signal < ppx_min:
            ppx_min = min_signal

        overview_seconds.append(start_i / sample_rate)
        overview_pxx.append(max_signal)
        overview_freqs.append(freq_of_max)

        start_i += samples_per_hop * rate
        stop_i += samples_per_hop * rate

    # store these in the program settings
    return overview_pxx, overview_freqs, overview_seconds, ppx_min, np.max(overview_pxx)


def get_freq_plot_center(overview_freqs, overview_pxx, mission):
    """ A function to find the frequency of the direct signal of the plot. """

    # TODO: Developer will need to choose a suitable automated peak detection algorithm.
    #  For now, just hardcode the values for each mission.

    ind = np.argmax(overview_pxx)
    freq_plot_center = overview_freqs[ind]
    if overview_pxx[ind] < 9:
        if mission == 'Rosetta':
            freq_plot_center = -18.95
        if mission == 'Dawn':
            freq_plot_center = 50
        print("no direct signal identified, default value assigned")
    return freq_plot_center


def get_plot_window(freq_plot_center, delta_f_calc, ppx_min, ppx_max):
    """ A function that sets the recommended window properties for the plot. """

    """
    Choose x-range slightly beyond the frequency of the predicted echo signal. 
    The default will be to go 20% further beyond the echo, or 1.2 x delta_f_calc.

    EXAMPLE: 
    If the direct signal is centered at 250 Hz, and delta_f_calc is ± 100 Hz,
    then the echo signal is predicted to have a frequency of 150 Hz or 350 Hz.
    So, we will choose an x-range for the plot to display from:
    a minimum of 250-1.2*(100) = 130 Hz, to a maximum of 250+1.2*(100) = 370 Hz.
    """

    # Display Name in GUI: “X-Axis min (Hz)”  # TODO: adjustable
    xlim_min = freq_plot_center - 1.5 * delta_f_calc  # default value
    xlim_min = (freq_plot_center - 80)

    # Display Name in GUI: “X-Axis max (Hz)”  # TODO: adjustable
    xlim_max = freq_plot_center + 1.5 * delta_f_calc  # default value
    xlim_max = (freq_plot_center + 80)

    """
    Set y-range as the lowest measured power (rounded to the nearest 5dB) 
    to 20% higher than the highest measured power value (also rounded to 
    nearest 5 dB)
    """

    # Display Name in GUI: “Y-Axis min (dB)”  # TODO: adjustable
    ylim_min = round_to_nearest_n(ppx_min, n=5)
    ylim_min = -10  # FIXME: return to original value
    # Display Name in GUI: “Y-Axis max (dB)”  # TODO: adjustable
    ylim_max = round_to_nearest_n(ylim_min + 1.2 * (ppx_max - ppx_min), n=5)
    ylim_max = 70  # FIXME: return to original value

    return xlim_min, xlim_max, ylim_min, ylim_max


def set_value(value, default):
    if value:
        return value
    else:
        return default


def round_to_hundreds_place(n):
    """ A function to round to the nearest tens place.  """

    # Smaller multiple
    a = (n // 100) * 100

    # Larger multiple
    b = a + 100

    # Return of closest of two
    return b if n - a > b - n else a


def get_settings(filenames=None,
                 rcp_data=None,
                 lcp_data=None,
                 sample_rate=None,
                 band_name=None,
                 global_time=None,
                 target=None, mission=None,
                 dt_occ=None, radius_target=None,
                 v_sc_orbital=None, altitude_sc=None,
                 delta_f_calc=None, freq_res=None,
                 samples_per_raw_fft=None, seconds_per_raw_fft=None,
                 raw_fft_per_average=None, seconds_for_welch_user=None,
                 percent_window_per_hop=None, seconds_per_hop=None,
                 xlim_min=None, xlim_max=None,
                 ylim_min=None, ylim_max=None,
                 start_sec_user=None, interval=None,
                 file_start_time=None, file_end_time=None, window=None):
    """ A function that stores all parameters for the radar analysis pipeline. """

    """
    NOTE:   settings are chosen according to RCP file (ie. sample_rate)

    NOTE:   Python 3 now supports any unicode character in variable names:
            python-3-for-scientists.readthedocs.io/en/latest/python3_features.html

    #############
    # NOTATIONS:
    #############

    sc      spacecraft
    occ	    occultation
    v		velocity (m/s)
    t		time (sec)
    dt	    change in time; duration (sec)
    theta		angle (radians)
    delta_f	    differential Doppler shift (aka the frequency separation 
            between the direct and echo peaks)

    ###############
    # DEFINITIONS:
    ###############

    wavelength              transmitting wavelength of the spacecraft antenna (meters)

    theta_beamwidth     angular width of the spacecraft antenna’s beam (typically 1-2°)

    radius_target   equatorial or average radius of the target body

    v_sc_orbital    spacecraft’s orbital velocity around the target body at the time 
                    of these observations

    altitude_sc     spacecraft’s altitude above the target body at the time of 
                    these observations

    dt_occ          duration of the “quiet period” when the spacecraft’s antenna 
                    is completely obscured behind the target body, aka the occultation 
                    duration in seconds (usually on the order of 1-30 min)
    """

    #######################
    # PROCESSING SETTINGS
    #######################

    print('\nget_settings()')

    # save settings to object, which is passed between functions
    s = ProgramSettings()

    # set metadata
    s.filenames = filenames
    s.global_time = global_time
    s.file_start_time = file_start_time
    s.file_end_time = file_end_time

    # constants
    percent2frac = 1 / 100
    mhz2hz = 1000000

    if mission == 'Rosetta':
        # values are in hertz
        x_band_freq = 8400 * mhz2hz
        s_band_freq = 2300 * mhz2hz
    elif mission == 'Dawn':
        # values are in hertz
        x_band_freq = 8435 * mhz2hz
        s_band_freq = 2300 * mhz2hz
    else:
        # values are in hertz
        x_band_freq = 8400 * mhz2hz
        s_band_freq = 2300 * mhz2hz

    # set the frequency of the antenna (hertz)
    if band_name == 'X':
        band_freq = x_band_freq
    elif band_name == 'S':
        band_freq = s_band_freq
    else:
        band_freq = None
        print("Data from this antenna is not yet supported")

    # set mission dependent variables
    if mission == 'Rosetta':
        print('using Rosetta parameters')
        s.target = '67P'
        s.mission = mission
        theta_beamwidth = math.radians(1)  # radians
        s.radius_target = set_value(radius_target, default=2000)  # meters
        s.v_sc_orbital = set_value(v_sc_orbital, default=2)  # meters/second
        s.altitude_sc = set_value(altitude_sc, default=10000)  # meters
        s.dt_occ = set_value(dt_occ, default=300)  # seconds
    elif mission == 'Dawn':
        print('using Dawn parameters')
        s.target = 'Vesta'
        s.mission = mission
        theta_beamwidth = math.radians(1.6)  # radians
        s.radius_target = set_value(radius_target, default=285000)  # meters
        s.v_sc_orbital = set_value(v_sc_orbital, default=200)  # meters/second
        s.altitude_sc = set_value(altitude_sc, default=200000)  # meters
        s.dt_occ = set_value(dt_occ, default=2000)  # seconds
    else:
        print('mission error')

    # for detailed descriptions of these variables, see docstring above
    wavelength = speed_of_light / band_freq  # meters

    # predicted/calculated frequency separation between the direct signal and the echo signal,
    # aka the differential Doppler shift (delta_f)
    theta_sc_orbital_phase = (s.v_sc_orbital * s.dt_occ) / (2 * (s.radius_target + s.altitude_sc))
    theta_tilt = np.arccos((s.radius_target - (s.v_sc_orbital * s.dt_occ / (2 * math.pi)))
                       / (s.radius_target + s.altitude_sc))

    print()
    print('band_freq:                                ', band_freq)
    print('(s.v_sc_orbital / wavelength):            ', (s.v_sc_orbital / wavelength))
    print('np.sin(theta_sc_orbital_phase):           ', np.sin(theta_sc_orbital_phase))
    print('np.sin(theta_tilt):                       ', np.sin(theta_tilt))
    print('np.sin(theta_tilt + theta_beamwidth / 2): ', np.sin(theta_tilt + theta_beamwidth / 2))
    print('theta_sc_orbital_phase:                   ', theta_sc_orbital_phase)
    print('theta_tilt:                               ', theta_tilt)

    # Display name in GUI: “Calc. freq. separation (Hz)”   # TODO: adjustable
    s.delta_f_calc = (s.v_sc_orbital / wavelength) * np.sin(theta_sc_orbital_phase) * abs(
        np.sin(theta_tilt) - np.sin(theta_tilt + theta_beamwidth / 2))

    if mission == 'Rosetta':
        # set to fixed value for Rosetta to ensure accurate parameter recommendations
        s.delta_f_calc = 2  # FIXME: improve Rosetta pipeline

    # number of IQ samples recorded per second
    s.sample_rate = sample_rate

    # number of seconds between when each IQ sample was recorded
    s.time_step = 1 / s.sample_rate

    ###########################
    # Sliding Window Size “L”
    ###########################

    # suggested frequency resolution
    freq_res_suggested = s.delta_f_calc / 30

    # Display name in GUI: “L (# samples per FFT)”
    # samples of data used to calculate a single raw FFT
    # provide DEFAULT number of samples per raw FFT, using the suggested frequency resolution
    s.samples_per_raw_fft = int(np.floor(s.sample_rate / freq_res_suggested))

    # Display name in GUI: “Freq. resolution (Hz)”  # TODO: adjustable
    # recalculate the spectral frequency resolution (freq_res) to get integer value
    s.freq_res = set_value(freq_res, default=(s.sample_rate / s.samples_per_raw_fft))

    # if the user manually adjusts the the frequency resolution, recalculate number samples too
    s.samples_per_raw_fft = int(np.floor(s.sample_rate / s.freq_res))

    # Display name in GUI: “t_int (seconds per FFT)”
    # convert from samples to seconds
    s.seconds_per_raw_fft = 1 / s.freq_res

    ################################
    # Sliding Window Step-Size “D”
    ################################

    # variables used to calculate moving average (see Matplotlib's PSD function)

    # the minimum hop size, aka 1 sample, converted to a percent %
    s.min_hop_percent = 100 * (s.sample_rate / s.samples_per_raw_fft)

    # Display name in GUI: “Sliding window step-size (%)”  # TODO: adjustable
    # can be any value from min_hop_percent to 100, where 100% means no overlap.
    s.percent_window_per_hop = set_value(percent_window_per_hop, default=20)

    # Display name in GUI: “t_hop (window step-size, sec)”
    # old version = s.seconds_per_hop = s.percent_window_per_hop * s.seconds_per_raw_fft
    if mission == 'Rosetta':
        s.seconds_per_hop = (s.percent_window_per_hop * percent2frac) * s.seconds_per_raw_fft
    elif mission == 'Dawn':
        s.seconds_per_hop = 1
    else:
        print('mission error')

    s.samples_per_hop = int(np.floor(s.seconds_per_hop * s.sample_rate))
    # seconds_per_hop = seconds_per_raw_fft	# (if no moving average)

    ###################################
    # Windows to Average Together “K”
    ###################################

    # Display name in GUI: “K (# spectra to average)”
    # TODO: adjustable (integers ≥ 1)
    if mission == 'Rosetta':
        s.raw_fft_per_average = set_value(raw_fft_per_average, default=2)
    elif mission == 'Dawn':
        s.raw_fft_per_average = set_value(raw_fft_per_average, default=2)
    else:
        print('mission error')

    # Alternatively, user can suggest an approximate seconds_for_welch_user (“Timespan per plot”)
    # in which case, K must be calculated (rounded to the nearest integer). Then, the actual
    # value of seconds_for_welch (based on this K) will be stored in s.second_for_welch.
    # Solving for K:
    #   seconds_for_welch = L + (D * (K - 1))
    #   (D * (K - 1)) = seconds_for_welch - L
    #   (K - 1) = (seconds_for_welch - L)/D
    # >> K = 1 + ((seconds_for_welch - L)/D)
    if seconds_for_welch_user:
        s.raw_fft_per_average = int(np.rint(1 + (seconds_for_welch_user - s.seconds_per_raw_fft) / s.seconds_per_hop))

    # >> Example: The user wants approx. 5 seconds to be the timespan per plot. If each raw FFT
    # spans 2.25 seconds (L), and each hop-size is 1 second (D), then working backwards,
    # the closest integer number of FFTs to average together (K) is 3, spanning a total time of
    # 5.25 per plot (seconds_for_welch).

    #################################
    # Welch Periodogram Calculation
    #################################

    # TODO: Is the following docstring still accurate, or does it need to be updated?
    """
    formula for number of samples to slice for each Welch calculation:

    L = samples_per_raw_fft
    D = samples_per_hop
    K = raw_fft_per_average
    samples_for_welch = L + (D * (K - 1))
    """

    # Display name in GUI: “Timespan per plot (sec)”
    s.seconds_for_welch = s.seconds_per_raw_fft + s.seconds_per_hop * (s.raw_fft_per_average - 1)
    # convert to samples
    s.samples_for_welch = int(s.samples_per_raw_fft + s.samples_per_hop * (s.raw_fft_per_average - 1))

    # number of samples of overlap between segments
    s.noverlap = s.samples_per_raw_fft - s.samples_per_hop

    # when to start and stop the animation
    s.start_sec_user = set_value(start_sec_user, 0)  # TODO: adjustable

    s.stop_sec_user = s.start_sec_user + s.seconds_for_welch

    # indexes of IQ data subset upon which to perform Welch's method
    s.start_index_user = int(np.floor(s.start_sec_user * s.sample_rate))
    s.stop_index_user = s.start_index_user + s.samples_for_welch

    # basic placeholder counters to update each frame of the animation
    s.start_sec_count = s.start_sec_user
    s.stop_sec_count = s.stop_sec_user
    s.start_index_count = s.start_index_user
    s.stop_index_count = s.stop_index_user

    s.print_debug('1')

    ###################################
    # Generating Signal Overview Plot
    ###################################

    # FIXME: EXPERIMENTAL
    # get an overview of the direct signal over time, used for plotting
    overview = signal_overview(rcp_data, lcp_data, s.samples_for_welch, s.sample_rate,
                               s.samples_per_raw_fft, s.noverlap, s.samples_per_hop, s.mission)
    s.overview_pxx = overview[0]
    s.overview_freqs = overview[1]
    s.overview_seconds = overview[2]
    s.ppx_min = overview[3]
    s.ppx_max = overview[4]

    #################
    # Plot Settings
    #################

    # find the frequency of the direct signal
    s.freq_plot_center = get_freq_plot_center(s.overview_freqs, s.overview_pxx, s.mission)

    # get default plot window settings
    default_window_settings = get_plot_window(s.freq_plot_center, s.delta_f_calc, s.ppx_min, s.ppx_max)
    default_x_min, default_x_max, default_y_min, default_y_max = default_window_settings

    # use default window dimensions, except if user has entered other values
    s.xlim_min = set_value(xlim_min, default=default_x_min)
    s.xlim_max = set_value(xlim_max, default=default_x_max)
    s.ylim_min = set_value(ylim_min, default=default_y_min)
    s.ylim_max = set_value(ylim_max, default=default_y_max)

    # milliseconds between frames in the animation
    # NOTE: this may be limited due to intensive computational processes
    s.interval = set_value(interval, default=500)

    return s
