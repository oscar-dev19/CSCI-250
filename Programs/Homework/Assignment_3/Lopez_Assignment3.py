"""
A simple stock analyzer that collects data from 3 stock-listed company files
(NASDAQ, NYSE, and AMEX), and parses it into a single delimited file where
a user can search company data from all 3 file sources.

Author: Oscar Lopez
"""


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


def parse_file(filename):
    """
    Parses data from an opened file into a dictionary data.
    Parameters:
        (File) open_file : File of data to be parsed.
    """
    parsed_data_dict = dict()
    #ignore the header of the file
    try:
        fopen = open(filename)
    except:
        print(f'ERROR: Could not parse data from {filename}!')
        return None
    for line in fopen:
        data_list = line.split('\t')
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
    """
    Merges all data from different files into a single list of data.
    Parameters:
        (String) argv: name(s) of files with data to be merged.
    """
    merged_data = list()
    for arg in argv:
        try:
            fopen = open(arg)
        except:
            print(f'ERROR: Could not open {arg}! Disregarding file.')
            continue
        #skipping header line.
        fopen.readline()
        for line in fopen:
            line = clean_data(line)
            merged_data.append(line.split('\t'))
        fopen.close()
    return merged_data


def output_data_file(filename, data):
    """
    Writes data to an output file.
    Parameters:
        (String) filename: Name of file to be written to.
        (list) data: Data to be written to file.
    """
    f_write = open(filename, "w+")
    data.sort()
    for line in data:
        for element in line:
            f_write.write(str(element) + '\t')
        f_write.write('\n')
    f_write.close()
    print(f'Finished writing data to {filename}')


all_data = merge_all_data('companylist_nasdaq.csv', 'companylist_nyse.csv',
                          'companylist_amex.csv')

output_data_file('all_data.tsv',all_data)
print(parse_file('all_data.tsv'))
