"""
tfmr.transformations
===============================================================
tfmr sub-module for transforming tfmr data
"""
import pandas as pd
import re
import pdpipe as pdp
import numpy as np

import tfmr.lists as lists


def application_map():
    '''NOT CURRENTLY IMPLEMENTED: 
    Takes as input unique raw data strings representing tfmr application and
    attempts to map them to current application list in tfmr_db

    Args:
        pass

    Returns:
        pass
    '''
    pass


def manufacturer_map():
    '''NOT CURRENTLY IMPLEMENTED:
    Input manufacturer list; output mapping list
    to use for pandas replace transformation

    Takes as input unique manufacturers and attempts
    to map them to current manufacturer list in tfmr_db

    Args:
        pass

    Returns:
        pass
    '''
    pass


def numphases_map():
    '''NOT CURRENTLY IMPLEMENTED: 
    Takes as input unique strings representing number of phases
    and maps to 1, 3 or np.Nan

    Args:
        pass

    Returns:
        pass
    '''
    pass


def tfmrtype_map():
    '''NOT CURRENTLY IMPLEMENTED: 
    Takes as input unique raw data strings representing tfmr type and
    attempts to map them to current tfmrtype list in tfmr_db

    Args:
        pass

    Returns:
        pass
    '''
    pass


def split_string_to_float():
    '''NOT CURRENTLY IMPLEMENTED: 
    Takes as input a string with potential HV_kV, LV_kV or TV_kV values and
    returns HV_kV, LV_kV, TV_kV or np.Nan

    Args:
        pass

    Returns:
        pass
    '''
    pass


def string_to_bool():
    '''NOT CURRENTLY IMPLEMENTED: 
    Takes as input unique raw data strings representing a PTX boolean like
    'IsAuto' and attempts to map them to True/False

    Args:
        pass

    Returns:
        pass
    '''
    pass


def string_year_to_datetime(string_list):
    '''Takes as input list of year strings, i.e. '1950',
    then appends '1/1' to string and changes string to datetime.

    Args:
        string_list (pandas series): 

    Returns:
        list of tuples: list of tuples where first value is original string
        and second is the new datetime. If original value is not a year string
        only the original value is passed back.
    '''
    date_list = []
    exception_list = []
    for row in string_list:
        try:
            date_list.append(pd.to_datetime('1/1/' + row))
        except Exception as e:
            # print(str(row) + ' might not be year string, appending original value')
            date_list.append(np.NaN)
            exception_list.append(row)
    print('List of incompatible values. Replaced with nan in output:')
    print(exception_list)
    return date_list

def get_stems(df, column):
    '''Input string column, output word stems using pdpipe
    https://github.com/shaypal5/pdpipe

    This function uses pdpipe, an easy to use pandas piping library,
    to in turn use nltk to convert sentances into a list of word stems using
    ntltk functions tokenizer, remove stopwords and english snowball stemmer.
    
    - TokenizeWords (https://www.nltk.org/api/nltk.tokenize.html),
    - RemoveStopWords (https://stackoverflow.com/questions/5486337/how-to-remove-stop-words-using-nltk-or-python),
    - SnowballStemmer/EnglishStemmer (http://www.nltk.org/howto/stem.html)}

    Args:
        df (dataframe): dataframe of column to be stemmed
        column (dataframe): column to be stemmed
    
    Returns:
        dataframe: Copied dataframe with new columns for each step (tokenize, remove stop words, stemmer)
    '''
    pipeline = pdp.TokenizeWords(columns=[column], drop=False)


    pipeline += pdp.RemoveStopwords(language='english',
                                    columns=[column + '_tok'],
                                    drop=False)
    pipeline += pdp.SnowballStem('EnglishStemmer',
                                columns=[column + '_tok' + '_nostop'],
                                drop=False)
    
    new_df = pipeline(df.copy())
    return new_df

def regex_date_tester(string):
    '''This function takes a string that might be a date and 
    tries to match it with different date style regex strings.
    current pattern list: yyyy_mm_dd, yyyymmdd_or_yyyyddmm,
    mmddyyyy_or_ddmmyyyy, yyyy, mm_yyyy, mmMONyy
    '''
    yyyy_mm_dd_pattern = (
        '^(19|20)\d\d[- /.](0[1-9]|1[0-2])[- /.](0[1-9]|[12][0-9]|3[01])$',
        'yyyy-mm-dd with "[- /.]" as separator')
    yyyymmdd_or_yyyyddmm_pattern = (
        '^(19|20)\d\d(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$',
        'yyyymmdd or yyyyddmm')
    mmddyyyy_or_ddmmyyyy_pattern = (
        '^(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])(19|20)\d\d$',
        'mmddyyyy or ddmmyyyy')
    yyyy_pattern = ('^(19|20)\d{2}$', 'yyyy')
    mm_yyyy_pattern = (
        '^(((0[1-9]|10|11|12)([- /.])(([1][9][0-9][0-9])|([2][0-9][0-9][0-9]))))',
        'mm-yyyy with "[- /.]" as separator')
    mmMONyy_pattern = (
        '^(\d{2})(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(\d{2})$',
        'mmMONyy')
    monthyyyy_pattern = (
        '^(january|february|march|april|may|june|july|august|september|october|november|december)(\d{4})$',
        'monthyyyy')
    monthyy_pattern = (
        '^(january|february|march|april|may|june|july|august|september|october|november|december)(\d{2})$',
        'monthyy')
    month_pattern = (
        '^january$|^february$|^march$|^april$|^may$|^june$|^july$|^august$|^september$|^october$|^november$|^december$|^jan$|^feb$|^mar$|^apr$|^may$|^jun$|^jul$|^aug$|^sep$|^oct$|^nov$|^dec$',
        'month')
    myyyy_or_mmyyyy_pattern = ('^([1-9]|1[0-2])(19|20)\d{2}$', 'myyyy')
    mmdyyyy_or_mddyyyy_pattern = (
        '^([1-9]|0[1-9]|1[0-2])([1-9]|1[0-9]|2[0-9]|3[0-1])(19|20)\d{2}$',
        'mmdyyyy_mddyyyy')
    mmddyy_or_ddmmyy_pattern = ('^()()(\d{2})$', 'mmddyy_ddmmyy')
    mdyyyy_or_dmyyyy_pattern = ('^([0-9])([0-9])(19|20)\d{2}$',
                                'mdyyyy_dmyyyy')
    mdyy_or_dmyy_pattern = ('^([0-9])([0-9])(\d{2})$', 'mdyy_dmyy')

    pattern_list = [
        yyyy_mm_dd_pattern, yyyymmdd_or_yyyyddmm_pattern,
        mmddyyyy_or_ddmmyyyy_pattern, yyyy_pattern, mm_yyyy_pattern,
        mmMONyy_pattern, monthyyyy_pattern, monthyy_pattern, month_pattern,
        myyyy_or_mmyyyy_pattern, mmdyyyy_or_mddyyyy_pattern,
        mmddyy_or_ddmmyy_pattern, mdyyyy_or_dmyyyy_pattern,
        mdyy_or_dmyy_pattern
    ]

    for pattern in pattern_list:
        if re.match(pattern[0], string):
            return pattern[1], pattern[0], True
            break
    else:
        return "No match", "", False
