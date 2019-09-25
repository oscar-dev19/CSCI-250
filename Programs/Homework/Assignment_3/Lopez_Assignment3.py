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
    Parses data from an opened file into a dictionary data.
    Parameters:
        (File) open_file : File of data to be parsed.
    """
    parsed_data_dict = dict()
    #ignore the header of the file
    open_file.readline()
    for line in open_file:
        data = clean_data(line)
        data_list = data.split('\t')
        symbol = data_list[0]
        parsed_data_dict.update(
            {
                symbol:{
                    'Name': data_list[1],
                    'Last Sale': data_list[2],
                    'Market Cap': data_list[3],
                    'ADR TSO': data_list[4],
                    'IPO Year': data_list[5],
                    'Sector': data_list[6],
                    'Industry': data_list[7],
                    'Summary Quote': data_list[8]
                }
            }
        )
    return parsed_data_dict


def merge_all_data(*argv):
    merged_data = list()
    for arg in argv:
        for line in arg:


nasdaq_open = open_file('companylist_nasdaq.csv')
nyse_open = open_file('companylist_nyse.csv')
amex_open = open_file('companylist_amex.csv')

nasdaq_dict = parse_file(nasdaq_open)
nyse_dict = parse_file(nyse_open)
amex_dict = parse_file(amex_open)

#print(nasdaq_dict.items())
#print(nasdaq_dict['ZVO']['Market Cap'])
print(merge_all_data(nasdaq_open, nyse_open, amex_open))
