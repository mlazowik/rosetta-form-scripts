#!/usr/bin/env python
import os
import sys

import pandas

def run_conversion(xls_file, dir_path):
    sheets = pandas.read_excel(xls_file, sheetname=None)
    for sheetname, dataframe in sheets.items():
        destination_path = os.path.join(dir_path, sheetname + '.csv')
        print('Exporting sheet \"{}\" to {}'.format(sheetname, destination_path))
        dataframe.to_csv(destination_path)

def print_usage():
    print("Usage: {} <input_xls_path> <output_path>".format(sys.argv[0]))

def main():
    if len(sys.argv) != 3:
        print_usage()
        exit(1)
    input_xls_path = sys.argv[1]
    output_path = sys.argv[2]
    # TODO handle missing files etc.
    input_xls_file = open(input_xls_path, 'rb')
    os.mkdir(output_path)
    run_conversion(input_xls_file, output_path)

if __name__ == '__main__':
    main()
