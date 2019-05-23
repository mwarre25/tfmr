"""
tfmr.schema_1_reports
===============================================================
tfmr sub-module for checking dataframes created to import to a
schema 1 database
"""
import pandas as pd
import datetime as dt
import tfmr.lists
import tfmr.schema_1 as schema_1
import numpy as np
now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()


def column_check(df_to_check, schema_df):
    """are all columns in the dataframe"""
    left_set = set(df_to_check.columns.values.tolist())
    right_set = set(schema_df.columns.values.tolist())
    if left_set == right_set:
        print('Column Check PASSED!\n')
        print('This function compares the list of hard coded schema tables in' +
              ' tfmr.schema_0\nor tfmr.schema_1 to the dataframe under test using set comparison.\n')
    else:
        print('Column Check FAILED!\n--------------------\n')

        print(
            'The following fields are in the dataframe under test but not in the schema:\n')
        print(str(left_set.difference(right_set))+'\n')

        print('The following fields are in the schema but do not appear in the df under test:\n')
        print(str(right_set.difference(left_set)) +
              " in schema but not in df under test.\n")


def foreign_key_subset_check(df_column_to_check, foreign_key_value_list):
    """are all the unique values in a foreign key column a subset of the foreign key column list?"""
    left_set = set(df_column_to_check.unique().tolist())
    right_set = set(foreign_key_value_list)
    if left_set.issubset(right_set):
        print(df_column_to_check.name + ' Foreign Key Subset Check PASSED!\n')

        print('This function compares the list of hard coded foreign key lists' +
              ' in tfmr.lists to the unique values in ' + df_column_to_check.name +
              ' column using set comparison.\nNote that you will need to update ' +
              'these lists every time the database is updated.\n')
    else:
        print(df_column_to_check.name + ' Foreign Key Subset Check FAILED!\n' +
              '-'*len(df_column_to_check.name)+'---------------------------------\n')

        print('The following values are in the dataframe column under test\nbut not in the foreign key value table list:\n')
        print(str(list(left_set.difference(right_set)))+'\n')
        print('These values should be checked for validity then added (as part of a whole entry) to the foreign key table.\n')


def dtype_check(df_to_check, corresponding_blank_df):
    """do all columns' data types match schema?
    """

    # I need to first assign the dtypes to the columns names like I do in schema_0
    # starting with tfmr_details
    test = df_to_check.dtypes == corresponding_blank_df.dtypes
    mismatch_list = list(test[test.values == False].index)
    # check for empty fields; if empty remove from list
    for value in mismatch_list:
            if not df_to_check[value].any():
                print(str(value)+' is empty; dropping from dtype_check\n')
                mismatch_list.remove(value)
                test = test.drop(labels=[value])

    if False not in test.values:
        print('Data Type Check PASSED!\n')
    else:
        print('Data Type Check FAILED!\n------------------------\n')
        print('The following columns have a mismatch:\n')
        print(mismatch_list)

        print("\nDataframe under test's column datatypes are:\n")
        print(list(zip(df_to_check.dtypes[test[test.values == False].index].index,
                       df_to_check.dtypes[test[test.values == False].index].values)))
        print("\nThey should be changed to the following datatypes to match the schema:\n")
        # print(corresponding_blank_df.dtypes[test[test.values == False].index])
        print(list(zip(corresponding_blank_df.dtypes[test[test.values == False].index].index,
                       corresponding_blank_df.dtypes[test[test.values == False].index].values)))
        print("\nPlease perform the necessary data transformations to align\n" +
              "each field's datatype to the schema datatype then re-run the report.")


def tfmr_details_report(tfmr_details_df):
    """tests a tfmr_details dataframe outputting some summary
    """
    column_check(tfmr_details_df, schema_1.blank_tfmr_details())

    # foreign key checks
    # TfmrManufacturers
    foreign_key_subset_check(
        tfmr_details_df['TfmrManufacturer'], tfmr.lists.schema_1TfmrManufacturerList())

    # Utilities
    foreign_key_subset_check(
        tfmr_details_df['Utility'], tfmr.lists.schema_1UtilitiesList())

    # Application
    foreign_key_subset_check(
        tfmr_details_df['Application'], tfmr.lists.TfmrApplicationList())

    # TfmrType
    foreign_key_subset_check(
        tfmr_details_df['TfmrType'], tfmr.lists.tfmrTypeList())

    # data type checks
    dtype_check(tfmr_details_df, schema_1.blank_tfmr_details())
