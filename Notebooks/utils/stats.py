'''
Util module that will include specific functions
'''

def data_range(data:list):
    # Creating a range within a list of numbers
    data.sort()
    return data[-1] - data[0]
