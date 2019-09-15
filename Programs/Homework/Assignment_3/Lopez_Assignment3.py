"""
A simple stock analyzer that collects data from 3 stock-listed company files
(NASDAQ, NYSE, and AMEX), and parses it into a single delimited file where
a user can search company data from all 3 file sources.

Author: Oscar Lopez
"""


def open_file(filename):
    """
    Opens a file and returns the opened file.
    Parameters:
        filename : String name of file to be opened.
    """
    try:
        fopen = open(filename)
    except:
        print("ERROR: %s cannot be opened!"%(filename))
    return fopen


def clean_data(data):
    """
    Removes any trailing new lines, replaces '"' with tab delimiter, and
    removes trailing commas and unnecessary quotation marks.
    Parameters:
        data: String of data.
    """
    data = data.strip("\n")
    data = data.replace('","', "\t")
    data = data.replace('"', '')
    # remove unnecessary comma at end of data.
    data = data[:len(data) -1]
    return data


def parse_file(open_file):
    """
    Parses data from an opened file into a list of data.
    Parameters:
        open_file : File of data to be parsed.
    """
    parsed_data = list()
    # Read pass the header line and ignore it.
    open_file.readline()
    for line in open_file:
        line = clean_data(line)
        parsed_data.append(line.split('\t'))
    return parsed_data


def merge_data(*argv):
    """
    Merges many data files into a single sorted list of data.
    Parameters:
    *argv : Lists of data that will be parsed into merged_data list.
    """
    merged_data = list()
    for arg in argv:
        for data_list in arg:
            merged_data.append(data_list)
    return merged_data

def output_data(filename, data):
    """
    Writes data to an output file.
    Parameters:
        (String) filename: Name of file to be written to.
        (list) data: Data to be written to file.
    """
    f_write = open(filename, "w+")
    for line in data:
        for element in line:
            f_write.write(str(element) + '\t')
        f_write.write('\n')
    print('Finished writing data to %s'%(filename))


nasdaq_open = open_file('companylist_nasdaq.csv')
nyse_open = open_file('companylist_nyse.csv')
amex_open = open_file('companylist_amex.csv')
nasdaq_data = parse_file(nasdaq_open)
nyse_data = parse_file(nyse_open)
amex_data = parse_file(amex_open)
output_data('All_Data.tsv', sorted(merge_data(nasdaq_data, nyse_data, amex_data)))
