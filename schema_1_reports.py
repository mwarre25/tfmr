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
            # print(str(value)+' is empty; dropping from dtype_check\n')
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


def tfmr_details_report(tfmr_details_df, data_file_details_df):
    """tests a tfmr_details dataframe outputting summary reports
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

    # DataFileName
    foreign_key_subset_check(
        tfmr_details_df['DataFileName'], data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(tfmr_details_df, schema_1.blank_tfmr_details())


def tfmr_service_history_report(tfmr_service_history_df, tfmr_details_df, data_file_details_df):
    """tests a tfmr_service_history dataframe outputting summary reports
    """
    column_check(
        tfmr_service_history_df,
        schema_1.blank_tfmr_service_history())

    # foreign key checks
    # TfmrIdentifier
    foreign_key_subset_check(
        tfmr_service_history_df['TfmrIdentifier'], tfmr_details_df.TfmrIdentifier.unique().tolist())

    # DataFileName
    foreign_key_subset_check(
        tfmr_service_history_df['DataFileName'], data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(
        tfmr_service_history_df,
        schema_1.blank_tfmr_service_history())


def tfmr_dga_report(tfmr_dga_df, tfmr_details_df, data_file_details_df):
    """tests a tfmr_dga dataframe outputting summary reports
    """
    column_check(
        tfmr_dga_df,
        schema_1.blank_tfmr_dga())

    # foreign key checks
    # TfmrIdentifier
    foreign_key_subset_check(
        tfmr_dga_df['TfmrIdentifier'],
        tfmr_details_df.TfmrIdentifier.unique().tolist())

    # DataFileName
    foreign_key_subset_check(
        tfmr_dga_df['DataFileName'],
        data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(
        tfmr_dga_df,
        schema_1.blank_tfmr_dga())


def tfmr_oq_report(tfmr_oq_df, tfmr_details_df, data_file_details_df):
    """tests a tfmr_oq dataframe outputting summary reports
    """
    column_check(
        tfmr_oq_df,
        schema_1.blank_tfmr_oq())

    # foreign key checks
    # TfmrIdentifier
    foreign_key_subset_check(
        tfmr_oq_df['TfmrIdentifier'],
        tfmr_details_df.TfmrIdentifier.unique().tolist())

    # DataFileName
    foreign_key_subset_check(
        tfmr_oq_df['DataFileName'],
        data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(
        tfmr_oq_df,
        schema_1.blank_tfmr_oq())


def tfmr_f_report(tfmr_f_df, tfmr_details_df, data_file_details_df):
    """tests a tfmr_f dataframe outputting summary reports
    """
    column_check(
        tfmr_f_df,
        schema_1.blank_tfmr_f())

    # foreign key checks
    # TfmrIdentifier
    foreign_key_subset_check(
        tfmr_f_df['TfmrIdentifier'],
        tfmr_details_df.TfmrIdentifier.unique().tolist())

    # DataFileName
    foreign_key_subset_check(
        tfmr_f_df['DataFileName'],
        data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(
        tfmr_f_df,
        schema_1.blank_tfmr_f())


def ltc_details_report(ltc_details_df, tfmr_details_df, data_file_details_df):
    """tests a tfmr_details dataframe outputting summary reports
    """
    column_check(ltc_details_df, schema_1.blank_ltc_details())

    # foreign key checks
    # TfmrIdentifier
    foreign_key_subset_check(
        ltc_details_df['TfmrIdentifier'],
        tfmr_details_df.TfmrIdentifier.unique().tolist())

    # LTCManufacturers
    foreign_key_subset_check(
        ltc_details_df['LTCManufacturer'], tfmr.lists.schema_1LTCManufacturersList())

    # LTCModels
    foreign_key_subset_check(
        ltc_details_df['LTCModel'], tfmr.lists.schema_1LTCModelsList())

    # Utilities
    foreign_key_subset_check(
        ltc_details_df['Utility'], tfmr.lists.schema_1UtilitiesList())

    # DataFileName
    foreign_key_subset_check(
        ltc_details_df['DataFileName'], data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(ltc_details_df, schema_1.blank_ltc_details())


def ltc_service_history_report(ltc_service_history_df, ltc_details_df, data_file_details_df):
    """tests a ltc_service_history dataframe outputting summary reports
    """
    column_check(ltc_service_history_df,
                 schema_1.blank_ltc_service_history())

    # foreign key checks
    # LTCIdentifier
    foreign_key_subset_check(
        ltc_service_history_df['LTCIdentifier'],
        ltc_details_df.LTCIdentifier.unique().tolist())

    # LTCManufacturers
    foreign_key_subset_check(
        ltc_details_df['LTCManufacturer'], tfmr.lists.schema_1LTCManufacturersList())

    # LTCModels
    foreign_key_subset_check(
        ltc_details_df['LTCModel'], tfmr.lists.schema_1LTCModelsList())

    # Utilities
    foreign_key_subset_check(
        ltc_details_df['Utility'], tfmr.lists.schema_1UtilitiesList())

    # DataFileName
    foreign_key_subset_check(
        ltc_details_df['DataFileName'], data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(ltc_details_df, schema_1.blank_ltc_details())


def ltc_dga_report(ltc_dga_df, ltc_details_df, data_file_details_df):
    """tests a ltc_dga dataframe outputting summary reports
    """
    column_check(
        ltc_dga_df,
        schema_1.blank_ltc_dga())

    # foreign key checks
    # LTCIdentifier
    foreign_key_subset_check(
        ltc_dga_df['LTCIdentifier'],
        ltc_details_df.LTCIdentifier.unique().tolist())

    # DataFileName
    foreign_key_subset_check(
        ltc_dga_df['DataFileName'],
        data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(
        ltc_dga_df,
        schema_1.blank_ltc_dga())


def ltc_oq_report(ltc_oq_df, ltc_details_df, data_file_details_df):
    """tests a tfmr_oq dataframe outputting summary reports
    """
    column_check(
        ltc_oq_df,
        schema_1.blank_ltc_oq())

    # foreign key checks
    # LTCIdentifier
    foreign_key_subset_check(
        ltc_oq_df['LTCIdentifier'],
        ltc_details_df.LTCIdentifier.unique().tolist())

    # DataFileName
    foreign_key_subset_check(
        ltc_oq_df['DataFileName'],
        data_file_details_df.DataFileName.unique().tolist())

    # data type checks
    dtype_check(
        ltc_oq_df,
        schema_1.blank_ltc_oq())