'''
Generic helper functions that can later be used in different projects
'''

import logging

def h_convert_if_number(value_to_convert):
    '''
    Converts original input into float or int as the case may be. Returns as is if cannot be converted
    :param   value_to_convert
    :return: converted_value
    '''
    try:
        f = float(value_to_convert)
        i = int(f)
        converted_value = f if ('.' in value_to_convert or f != i) else i
    except:
        converted_value = value_to_convert

    # log datatype of return_value
    logging.debug("{0} is {1}".format(converted_value, h_extract_data_type(converted_value)))
    return converted_value


def h_extract_data_type(value):
    '''
    Extracts the datatype of a value as a string
    :param value: For which datatype is required
    :return value_type: Datatype in string format
    '''
    value_type = str(type(value)).strip()
    # Removing extraneous characters to clean it up
    for e in ["type", "<", ">", "'"]:
        value_type = value_type.replace(e,"")
    return value_type
