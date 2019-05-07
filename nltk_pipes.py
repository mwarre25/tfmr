"""
tfmr.nltk_pipes
=====================================================================
tfmr sub-module initially created for identifying TfmrEventType words
from large text fields using pdpipe module. working on other pipes
"""

import pdpipe as pdp


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
