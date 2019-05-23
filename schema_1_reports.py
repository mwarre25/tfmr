"""
tfmr.schema_1_reports
===============================================================
tfmr sub-module for checking dataframes created to import to a
schema 1 database
"""
import pandas as pd
import datetime as dt
import tfmr.lists
import numpy as np
now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()


def column_check(df_to_check, schema_df):
        """are all columns in the dataframe"""
        left_set = set(df_to_check.columns.values.tolist())
        right_set = set(schema_df.columns.values.tolist())
        if left_set == right_set:
            print('Column Check PASSED!\n--------------------\n')
        else:
            print('Column Check FAILED!\n--------------------\n')

            print('The following fields are in the dataframe under test but not in the schema:\n')
            print(str(left_set.difference(right_set))+'\n')
            
            print('The following fields are in the schema but do not appear in the df under test:\n')
            print(str(right_set.difference(left_set))+ " in schema but not in df under test.\n")

def foreign_key_subset_check(df_column_to_check, foreign_key_value_list):
    """are all the unique values in a foreign key column a subset of the foreign key column list?"""
    left_set = set(df_column_to_check.unique().tolist())
    right_set = set(foreign_key_value_list)
    if left_set.issubset(right_set):
        print(df_column_to_check.name + ' Foreign Key Subset Check PASSED!\n'+'-'*len(df_column_to_check.name)+'---------------------------------\n')
    else:
        print(df_column_to_check.name + ' Foreign Key Subset Check FAILED!\n'+'-'*len(df_column_to_check.name)+'---------------------------------\n')

        print('The following values are in the dataframe column under test but not in the foreign key value table list:\n')
        print(str(left_set.difference(right_set))+'\n')
        print('These values should be checked for validity then added (as part of a whole entry) to the foreign key table.\n')

def dtype_check(df_to_check, corresponding_blank_df):
    """do all columns' data types match schema?
    """

    # I need to first assign the dtypes to the columns names like I do in schema_0
    pass

def tfmr_details_report(tfmr_details_df):
    """tests a tfmr_details dataframe outputting some summary
    """
    column_check(tfmr_details_df, blank_tfmr_details())

    # foreign key checks
    # TfmrManufacturers
    foreign_key_subset_check(tfmr_details_df['TfmrManufacturer'],tfmr.lists.schema_1TfmrManufacturerList())

    # Utilities
    foreign_key_subset_check(tfmr_details_df['Utility'],tfmr.lists.schema_1UtilitiesList())

    # Application
    foreign_key_subset_check(tfmr_details_df['Application'],tfmr.lists.TfmrApplicationList())

    # TfmrType
    foreign_key_subset_check(tfmr_details_df['TfmrType'],tfmr.lists.tfmrTypeList())

    # data type checks