"""
tfmr.regex
================================================================================
tfmr sub-module initially created for containing various regex related functions
"""
import re

def regex_date_tester(string):
    '''
    This function takes a string that might be a date and 
    tries to match it with different date style regex strings.
    current pattern list:
     - yyyy_mm_dd
     - yyyymmdd_or_yyyyddmm
     - mmddyyyy_or_ddmmyyyy
     - yyyy
     - mm_yyyy
     - mmMONyy
     - 
     - 
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
    yyyy_pattern = ('^(19|20)\d{2}$',
                    'yyyy')
    mm_yyyy_pattern = (
        '^(((0[1-9]|10|11|12)([- /.])(([1][9][0-9][0-9])|([2][0-9][0-9][0-9]))))',
        'mm-yyyy with "[- /.]" as separator')
    mmMONyy_pattern = (
        '^(\d{2})(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(\d{2})$',
        'mmMONyy')
    monthyyyy_pattern = ('^(january|february|march|april|may|june|july|august|september|october|november|december)(\d{4})$',
                         'monthyyyy')
    monthyy_pattern = ('^(january|february|march|april|may|june|july|august|september|october|november|december)(\d{2})$',
                       'monthyy')
    month_pattern = (
        '^january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec$',
        'month')
    myyyy_or_mmyyyy_pattern = ('^([1-9]|1[0-2])(19|20)\d{2}$',
                               'myyyy')
    mmdyyyy_or_mddyyyy_pattern = (
        '^([1-9]|0[1-9]|1[0-2])([1-9]|1[0-9]|2[0-9]|3[0-1])(19|20)\d{2}$',
        'mmdyyyy_mddyyyy')
#     mmdyy_or_mddyy_pattern = (
#         '^(([1-9]|1[0-2]|[0-9])|([1-9]|2[0-9]|3[0-1]))(([1-9]|1[0-2]|[0-9])|([1-9]|2[0-9]|3[0-1]))([1-9]|1[0-2]|[0-9])|([1-9]|2[0-9]|3[0-1])(\d{2})$',
#         'mmdyy_mddyy')
    mmddyy_or_ddmmyy_pattern = (
        '^()()(\d{2})$',
        'mmddyy_ddmmyy')
    mdyyyy_or_dmyyyy_pattern = (
        '^([0-9])([0-9])(19|20)\d{2}$',
        'mdyyyy_dmyyyy')
    mdyy_or_dmyy_pattern = ('^([0-9])([0-9])(\d{2})$',
                            'mdyy_dmyy')

    pattern_list = [yyyy_mm_dd_pattern,
                    yyyymmdd_or_yyyyddmm_pattern,
                    mmddyyyy_or_ddmmyyyy_pattern,
                    yyyy_pattern,
                    mm_yyyy_pattern,
                    mmMONyy_pattern,
                    monthyyyy_pattern,
                    monthyy_pattern,
                    month_pattern,
                    myyyy_or_mmyyyy_pattern,
                    mmdyyyy_or_mddyyyy_pattern,
                    # mmdyy_or_mddyy_pattern,
                    mmddyy_or_ddmmyy_pattern,
                    mdyyyy_or_dmyyyy_pattern,
                    mdyy_or_dmyy_pattern
                   ]

    for pattern in pattern_list:
        if re.match(pattern[0], string):
            print(pattern[1])
            return True
            break
    else:
        return False
