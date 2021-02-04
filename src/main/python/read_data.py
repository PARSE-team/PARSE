"""
read_data.py -- Contains helper functions for reading BSR data files.
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
# This file contains utility functions for reading and processing bistatic 
# radar data files. It currently supports certain ASCII and binary formats.

# NOTE: This file uses a dependency to read label files from the Rosetta Mission, which 
# were formatted using the official PDS3 "detached label" sub-format (see chapter 5.1 in 
# the PDS3 documentation for more info). The aforementioned dependency is available at
# https://github.com/mkelley/pds3

import numpy as np
from os import scandir
from pds3_mkelley.pds3.core import read_label
from astropy.time import Time
from datetime import datetime, timedelta
import time


class DataLabel:
    """ A class that references one data file and the corresponding label file. """

    def __init__(self, file_name, label=None, path_to_label=None, path_to_data=None, mission=None,
                 band_name=None, polarization=None, start_time=None, stop_time=None):
        self.file_name = file_name  # shared file prefix
        self.label = label  # processed label file
        self.path_to_label = path_to_label  # path to .lbl file
        self.path_to_data = path_to_data  # path to .dat file
        self.mission = mission

        # metadata to read from label file
        self.band_name = band_name
        self.polarization = polarization
        self.start_time = start_time
        self.stop_time = stop_time

    def set_metadata(self):
        self.band_name = self.label['BAND_NAME']
        self.polarization = self.label['RECEIVED_POLARIZATION_TYPE']
        self.start_time = Time(self.label['START_TIME'], format='iso')
        self.stop_time = Time(self.label['STOP_TIME'], format='iso')


def get_files(source, ctx):
    # list of available files, stored as DataLabel objects
    datalabels = []

    if source == 'dawn':
        directory = ctx.get_resource('data/dawn/')
        return get_files_dawn(directory)
    if source == 'rosetta':
        directory = ctx.get_resource('data/rosetta/')
        return get_files_rosetta(directory)
    if source == 'userfile':
        pass

    return datalabels


def get_files_rosetta(directory):
    """ A function that scans the given directory, pairs label files
     to data files, processes metadata from the label, then returns
     a list of DataLabel objects. """

    # a list of DataLabel objects, generated from the given directory
    paired_files = []
    # a list of the file ID numbers that the loop has already encountered
    pair_pending = []

    # scan the given directory, pairing data files to label files
    for file in scandir(directory):
        # scan for data or label files, ignore  sub-directories, roots, etc
        if file.is_file and (file.name.endswith('.lbl') or file.name.endswith('.dat')):
            # ignore the file extensions for pairing data and label files
            file_name = file.name[:-4]
            # pair file names
            if file_name not in pair_pending:
                # create a new DataLabel object
                if file.name.endswith('.lbl'):
                    # label file found
                    paired_files.append(DataLabel(file_name, None, file.path, None))
                    pair_pending.append(file_name)
                elif file.name.endswith('.dat'):
                    # data file found
                    paired_files.append(DataLabel(file_name, None, None, file.path))
                    pair_pending.append(file_name)
            else:
                # update an existing DataLabel object from pair_pending
                for pair in paired_files:
                    if pair.file_name == file_name:
                        # found corresponding file in pair
                        if file.name.endswith('.lbl'):
                            # label file found
                            pair.path_to_label = file.path
                            pair_pending.remove(file_name)
                        elif file.name.endswith('.dat'):
                            # data file found
                            pair.path_to_data = file.path
                            pair_pending.remove(file_name)

    # FIXME: does this slow down the program?
    # for each DataLabel, process the label and store any useful metadata
    for pair in paired_files:
        pair.label = read_label(pair.path_to_label)
        pair.set_metadata()
        pair.mission = 'Rosetta'

    # sort the list by order of file start time, then order of file end time
    data_labels = sorted(paired_files, key=time_order)

    return data_labels


def get_files_dawn(directory):
    # a list of DataLabel objects, generated from the given directory
    dawn_files = []

    # scan the given directory, pairing data files to label files
    for file in scandir(directory):

        if file.is_file and file.name.endswith('.npy'):

            print(file.name)

            file_name = file.name[:-4]

            label = None

            path_to_label = None

            path_to_data = file.path

            mission = 'Dawn'

            # type of antenna was X-band for all Dawn files
            band_name = 'X'

            # polarization
            print(file.name)
            print(len(file.name))
            print(type(file.name))
            polarization = file.name[25]
            if polarization is 'R':
                polarization = 'RIGHT CIRCULAR'
            elif polarization is 'L':
                polarization = 'LEFT CIRCULAR'

            # get lines from original ASCII file (only binary version kept in project repository)
            # first_line, last_line = read_dawn_ascii(path_to_data)

            first_line = '2011 358 12601.00003'
            last_line = '2011 358 19260.99997'
            start_time = yds_to_ymdhms(first_line)
            stop_time = yds_to_ymdhms(last_line)

            # create a new DataLabel object
            dawn_files.append(DataLabel(file_name=file_name,
                                        label=None,
                                        path_to_label=None,
                                        path_to_data=path_to_data,
                                        mission=mission,
                                        band_name=band_name,
                                        polarization=polarization,
                                        start_time=start_time,
                                        stop_time=stop_time))

    # sort the list by order of file start time, then order of file end time
    dawn_files = sorted(dawn_files, key=time_order)

    return dawn_files


def read_dawn_ascii(path_to_data):
    # get lines from the original Dawn ASCII file (only binary version kept in project repository)
    # start and stop times for this data series
    """with open(path_to_data, 'r') as f:
        first_line = f.readline().strip()
    with open(path_to_data, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        last_line = f.readline().decode()
    return first_line, last_line"""
    pass


def yds_to_ymdhms(year_day_second):
    """ A function to convert Dawn's time format (year:day:second) to standard format. """

    # read from string
    year = year_day_second[0:4]
    day_in_year = year_day_second[5:8]
    seconds_in_day = year_day_second[9:20]

    # convert seconds_in_day to regular hms
    hms = str(timedelta(seconds=float(seconds_in_day)))
    concatenate = year + ':' + day_in_year + ':' + hms

    ymdhms = Time(concatenate, in_subfmt='date_hms', precision=5)
    ymdhms.format = 'iso'

    return ymdhms


def time_order(data_label):
    # used as key function for sorted()
    # sort by each file's start time and end time, then group by band name
    return data_label.start_time, data_label.stop_time, data_label.band_name, \
           data_label.polarization


def find_polar_pair(chosen_file, dl_list):
    """ A function that pairs an RCP file to the corresponding LCP file. """

    print('finding polar pair...')

    if chosen_file.mission == 'Rosetta':
        return find_polar_pair_rosetta(chosen_file, dl_list)
    elif chosen_file.mission == 'Dawn':
        return find_polar_pair_dawn(chosen_file, dl_list)
    else:
        print('error')


def find_polar_pair_rosetta(chosen_file, dl_list):
    for dl in dl_list:
        if dl is not chosen_file:
            # it's not the exact same file the user requested
            if chosen_file.stop_time == dl.stop_time:
                if chosen_file.start_time == dl.start_time:
                    # both files share same time series
                    if dl.label['FILE_RECORDS'] == chosen_file.label['FILE_RECORDS']:
                        # both files share same number of rows
                        if dl.label['RECORD_BYTES'] == chosen_file.label['RECORD_BYTES']:
                            # both files share same record bytes
                            if chosen_file.band_name == dl.band_name:
                                # both files share same frequency band
                                # so these two files must be a polar match
                                if dl.polarization == 'RIGHT CIRCULAR':
                                    # always return RCP then LCP
                                    return dl, chosen_file
                                elif dl.polarization == 'LEFT CIRCULAR':
                                    # always return RCP then LCP
                                    return chosen_file, dl
                                else:
                                    print('error')


def find_polar_pair_dawn(chosen_file, dl_list):
    for dl in dl_list:
        if dl is not chosen_file:
            # it's not the exact same file the user requested
            if chosen_file.stop_time == dl.stop_time:
                if chosen_file.start_time == dl.start_time:
                    # both files share same time series
                    # TODO: handle edge case where files have different sample rates (rows)
                    # FIXME: too slow, find a better solution
                    # if rows_in_file(dl.path_to_data) == rows_in_file(chosen_file.path_to_data):
                    # both files share same number of rows
                    if chosen_file.band_name == dl.band_name:
                        # both files share same frequency band
                        # so these two files must be a polar match
                        if dl.polarization == 'RIGHT CIRCULAR':
                            # always return RCP then LCP
                            return dl, chosen_file
                        elif dl.polarization == 'LEFT CIRCULAR':
                            # always return RCP then LCP
                            return chosen_file, dl
                        else:
                            print('error')


def get_polar_compliment(file, dl_list):
    rcp, lcp = find_polar_pair(file, dl_list)
    if file is rcp:
        return lcp
    elif file is lcp:
        return rcp


def rows_in_file(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_dtypes(data_label):
    if data_label.mission == 'Rosetta':
        return get_dtypes_rosetta(data_label)
    elif data_label.mission == 'Dawn':
        return get_dtypes_dawn()
    else:
        print('error')


def get_dtypes_rosetta(data_label):
    """ A function that accesses the processed info from label file,
    then returns the Numpy dtype for each column of the binary data table. """

    # dictionary of PDS3 --> Numpy.dtype translations
    pds3_to_dtype = {
        'CHARACTER': 'S',
        'IEEE_REAL': '>f',
        'LSB_INTEGER': '<i',
        'LSB_UNSIGNED_INTEGER': '<u',
        'MAC_INTEGER': '>i',
        'MAC_REAL': '>f',
        'MAC_UNSIGNED_INTEGER': '>u',
        'MSB_UNSIGNED_INTEGER': '>u',
        'MSB_INTEGER': '>i',
        'PC_INTEGER': '<i',
        'PC_UNSIGNED_INTEGER': '<u',
        'SUN_INTEGER': '>i',
        'SUN_REAL': '>f',
        'SUN_UNSIGNED_INTEGER': '>u',
        'VAX_INTEGER': '<i',
        'VAX_UNSIGNED_INTEGER': '<u',
    }

    # assign shortcut to quickly access columns of TABLE object
    pds_columns = data_label.label['TABLE']['COLUMN']

    # list to hold tuples, one for each PDS column's data type
    dtype_raw = []

    # for each column, append the formatted string to the list
    for column in pds_columns:
        items = ''
        if column.get('ITEMS', 1) != 1:
            # this column contains multiple items per row, format accordingly
            if column['NAME'] == 'SAMPLE WORDS':
                # this column contains the raw IQ data, use custom dtype to store complex values
                """ NOTE: Do not use column['ITEM'] in the "SAMPLE WORDS" column, 
                the dataset is inaccurate and this particular figure cannot be trusted. """
                # manually calculate the number of items in this column
                sample_words_per_row = int((int(data_label.label['RECORD_BYTES']) - 260)
                                           / int(column['ITEM_BYTES']))
                # concatenate the substrings into a complete string representation of a dtype
                dtype_raw.append(
                    (column['NAME'], [('imag', '>u2'), ('real', '>u2')], (sample_words_per_row,)))

            else:
                # this column also has multiple items per row, but uses a standard dtype
                items = '({},)'.format(column['ITEMS'])
                # concatenate the substrings into a complete string representation of a dtype
                item_bytes = column.get('ITEM_BYTES', column['BYTES'])
                x = pds3_to_dtype[column['DATA_TYPE']] + str(item_bytes)
                dtype_raw.append((column['NAME'], items + x))
        else:
            # only 1 item per column
            # concatenate the substrings into a complete string representation of a dtype
            item_bytes = column.get('ITEM_BYTES', column['BYTES'])
            x = pds3_to_dtype[column['DATA_TYPE']] + str(item_bytes)
            dtype_raw.append((column['NAME'], items + x))

    # cast list to Numpy dtype object to use in data table
    return np.dtype(dtype_raw)


def get_dtypes_dawn():
    dt = np.dtype([('Year', np.int32), ('Day of Year', np.int32), ('Second in Day', np.float64),
                   ('I', np.int32), ('Q', np.int32)])
    return dt


def file_to_numpy(data_label):
    """ A function that reads the entire data file into a Numpy array. """

    if data_label.mission == 'Rosetta':
        return file_to_numpy_rosetta(data_label)
    elif data_label.mission == 'Dawn':
        return file_to_numpy_dawn(data_label)
    else:
        print('error')


def file_to_numpy_rosetta(data_label):
    # set the Numpy dtype for all columns
    dt = np.dtype(get_dtypes(data_label))

    # read from binary file
    with open(data_label.path_to_data, 'rb') as inf:
        table = np.fromfile(inf, dtype=dt, count=-1)

    return table


def file_to_numpy_dawn(data_label, use_binary_version=True):
    if use_binary_version:
        return np.load(data_label.path_to_data)
    else:
        # set the Numpy dtype for all columns
        dt = np.dtype(get_dtypes(data_label))

        # read from ASCII file
        start_time = time.time()
        table = np.loadtxt(data_label.path_to_data, dtype=dt)
        end_time = time.time()

        if data_label.file_name == '203VSOC2011358_0330NNNX43LD.2B2':
            np.save('203VSOC2011358_0330NNNX43LD.2B2.npy', table)
        elif data_label.file_name == '203VSOC2011358_0330NNNX43RD.2A2':
            np.save('203VSOC2011358_0330NNNX43RD.2A2.npy', table)

        return table


def get_iq_data(table, mission):
    """ A function that isolates the IQ data from the processed file,
    combining the imaginary and real parts into a memory efficient complex number. """

    if mission == 'Rosetta':
        return get_iq_data_rosetta(table)
    elif mission == 'Dawn':
        return get_iq_data_dawn(table)
    else:
        print('error')


def get_iq_data_rosetta(table):
    # add the I and Q vectors, cast as imaginary
    iq_data = (table['SAMPLE WORDS']['real']
               + table['SAMPLE WORDS']['imag'] * 1.j).astype(np.complex64)
    return iq_data.flatten()


def get_iq_data_dawn(table):
    # add the I and Q vectors, cast as imaginary
    return (table['I'] + table['Q'] * 1.j).flatten()


def get_sample_rate(table, mission):
    if mission == 'Rosetta':
        return get_sample_rate_rosetta(table)
    elif mission == 'Dawn':
        return get_sample_rate_dawn(table)
    else:
        print('error')


def get_sample_rate_rosetta(table):
    return table['SAMPLE RATE'][0] * 1000


def get_sample_rate_dawn(data):
    count = 0
    second_zero = None
    second_one = None
    second_two = None

    for row in data:
        if np.around(row['Second in Day'] - np.around(row['Second in Day']), 7) == 0.00003:
            if not second_zero:
                second_zero = count
            elif not second_one:
                second_one = count
            elif not second_two:
                second_two = count
            else:
                sample_rate_one = second_one - second_zero
                sample_rate_two = second_two - second_one
                if sample_rate_one == sample_rate_two:
                    return sample_rate_one
                else:
                    print('error finding sample rate for dawn files')
        count += 1


def strftime_DOY(astropy_datetime):
    return astropy_datetime.strftime('%j')


def strftime_timestamp(astropy_datetime):
    return astropy_datetime.strftime('%Y-%m-%d %H:%M:%S')


def strftime_hhmmss(astropy_datetime):
    return astropy_datetime.strftime('%H:%M:%S')


def strftime_yyyyDOYhhmmss(astropy_datetime):
    return astropy_datetime.strftime('(%Y-%j) %H:%M:%S')


def strftime_yyyyDOYhhmmssff(astropy_datetime):
    return astropy_datetime.strftime('(%Y-%j) %H:%M:%S.%f')


def strftime_yyyyDOY(astropy_datetime):
    return astropy_datetime.strftime('%Y-%j')


def astropy_to_python(astropy_datetime):
    return datetime.strptime(str(astropy_datetime), '%Y-%m-%d %H:%M:%S.%f')
