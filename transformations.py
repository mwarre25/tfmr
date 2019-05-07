import pandas as import pd
import pdpipe as pdp

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
    '''NOT CURRENTLY IMPLEMENTED: 
    Takes as input list of year strings, i.e. '1950',
    then appends '1/1' to string and changes string to datetime.

    Args:
        string_list (pandas series): 

    Returns:
        list of tuples: list of tuples where first value is original string
        and second is the new datetime. If original value is not a year string
        only the original value is passed back.
    '''
    date_list = []
    for row in string_list:
        try:
            date_list.append((row, pd.to_datetime('1/1/' + row)))
        except Exception as e:
            print(str(row) + ' might not be year string, appending original value')
            date_list.append(row)
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
