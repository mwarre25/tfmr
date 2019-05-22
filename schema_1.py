"""
tfmr.schema_1
===============================================================
tfmr sub-module for creating schema_1 tables
"""
import pandas as pd
import datetime as dt
import tfmr.lists
now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()

def column_check(df_to_check, schema_df):
        """are all columns in the dataframe"""
        left_set = set(df_to_check.columns.values.tolist())
        right_set = set(schema_df.columns.values.tolist())
        if left_set == right_set:
            print('Column Check PASSED!\n')
        else:
            print('Column Check FAILED!\n')

            print('The following fields are in the dataframe under test but not in the schema:\n')
            print(str(left_set.difference(right_set))+'\n')
            
            print('The following fields are in the schema but do not appear in the df under test:\n')
            print(str(right_set.difference(left_set))+ " in schema but not in df under test.\n")

def foreign_key_subset_check(df_column_to_check, foreign_key_value_list):
    """are all the unique values in a foreign key column a subset of the foreign key column list?"""
    left_set = set(df_column_to_check.unique().tolist())
    right_set = set(foreign_key_value_list)
    if left_set.issubset(right_set):
        print(df_column_to_check.name + ' Foreign Key Subset Check PASSED!\n')
    else:
        print(df_column_to_check.name + ' Foreign Key Subset Check FAILED!\n')

        print('The following values are in the dataframe column under test but not in the foreign key value table list:\n')
        print(str(left_set.difference(right_set))+'\n')
        print('These values should be checked for validity then added (as part of a whole entry) to the foreign key table.')


def blank_tfmr_details():
    """initializes blank tfmr_details dataframe
    """
    blank_tfmr_details_list = [
        'TfmrIdentifier', 'TfmrSerialNum', 'TfmrManufacturer',
        'ManufactureDate', 'IdentifierUnknown', 'Utility', 'OperatingCompany',
        'Region', 'Substation', 'Designation', 'CoreType', 'CoolingType1',
        'MVA1', 'CoolingType2', 'MVA2', 'CoolingType3', 'MVA3', 'Application',
        'TfmrType', 'HV_kV', 'LV1_kV', 'LV2_kV', 'TV_kV', 'HV_Connection',
        'LV1_Connection', 'LV2_Connection', 'TV_Connection', 'BuriedTertiary',
        'NumPhases', 'IsAuto', 'OilType', 'OilPreservationType',
        'UtilityCriticality', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_tfmr_details = pd.DataFrame(columns=blank_tfmr_details_list)

    return blank_tfmr_details


def tfmr_details_report(tfmr_details_df):
    """tests a tfmr_details dataframe outputting some summary
    """
    column_check(tfmr_details_df, blank_tfmr_details())

    # TfmrManufacturers
    foreign_key_subset_check(tfmr_details_df['TfmrManufacturer'],tfmr.lists.schema_1TfmrManufacturerList)

    # Utilities
    foreign_key_subset_check(tfmr_details_df['Utility'],tfmr.lists.schema_1UtilitiesList)

    # Application
    foreign_key_subset_check(tfmr_details_df['Application'],tfmr.lists.TfmrApplicationList)

    # TfmrType
    foreign_key_subset_check(tfmr_details_df['TfmrType'],tfmr.lists.tfmrTypeList)



def blank_tfmr_service_history():
    """
    initializes blank_tfmr_service_history dataframe
    """
    blank_tfmr_service_history_list = [
        'TfmrIdentifier', 'TfmrEventType', 'EventDate', 'PreviousStatus',
        'ServiceStatus', 'FirstFailure', 'AgeAtFailure', 'FailureLoc',
        'FailedComponent', 'FailureConsequence', 'FailureCause', 'RepairBy',
        'RepairLoc', 'RootCause', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_tfmr_service_history = pd.DataFrame(
        columns=blank_tfmr_service_history_list)

    return blank_tfmr_service_history


def blank_tfmr_dga():
    """
    initializes blank_tfmr_dga dataframe
    """
    blank_tfmr_dga_list = [
        'TfmrIdentifier', 'SampleFrom', 'SampleDate', 'LabTestDate',
        'OilTempC', 'H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2',
        'N2', 'BadSample', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_tfmr_dga = pd.DataFrame(columns=blank_tfmr_dga_list)

    return blank_tfmr_dga


def blank_tfmr_dga_online():
    """
    initializes blank_tfmr_dga_online dataframe
    """
    blank_tfmr_dga_online_list = [
        'TfmrIdentifier', 'SampleDate', 'LabTestDate', 'OilTempC', 'H2', 'CH4',
        'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2', 'N2', 'Moisture_PPM',
        'RelSaturation', 'MonitorModel', 'BadSample', 'DataFileName',
        'CreatedBy', 'Remarks'
    ]

    blank_tfmr_dga_online = pd.DataFrame(columns=blank_tfmr_dga_online_list)

    return blank_tfmr_dga_online


def blank_tfmr_oq():
    """
    initializes blank_tfmr_oq dataframe
    """
    blank_tfmr_oq_list = [
        'TfmrIdentifier', 'SampleDate', 'LabTestDate', 'OilTempC',
        'MoisturePPM', 'Acidity', 'IFT', 'Color', 'D877', 'D1816_1MM',
        'D1816_2MM', 'IEC156', 'PF_25C', 'PF_100C', 'DataFileName',
        'CreatedBy', 'Remarks'
    ]

    blank_tfmr_oq = pd.DataFrame(columns=blank_tfmr_oq_list)

    return blank_tfmr_oq


def blank_tfmr_f():
    """
    initializes blank_tfmr_f dataframe
    """
    blank_tfmr_f_list = [
        'TfmrIdentifier', 'SampleDate', 'LabTestDate', '2FAL', '5M2F', '5H2F',
        '2ACF', '2FOL', 'CH3OH', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_tfmr_f = pd.DataFrame(columns=blank_tfmr_f_list)

    return blank_tfmr_f


def blank_tfmr_type():
    """
    initializes blank_tfmr_type dataframe
    """
    blank_tfmr_type_list = ['TfmrType', 'DataFileName', 'CreatedBy', 'Remarks']

    blank_tfmr_type = pd.DataFrame(columns=blank_tfmr_type_list)

    return blank_tfmr_type


def blank_utilities():
    """
    initializes blank_utilities dataframe
    """
    blank_utilities_list = [
        'Fullname', 'Region', 'Headquarters', 'PointofContact1',
        'PhoneofContact1', 'PointofContact2', 'PhoneofContact2',
        'DataFileName', 'LUOn', 'LUBy', 'Remarks'
    ]

    blank_utilities = pd.DataFrame(columns=blank_utilities_list)

    return blank_utilities


def blank_application():
    """
    initializes blank_application dataframe
    """
    blank_application_list = [
        'Application', 'DataFileName', 'LUOn', 'LUBy', 'Remarks'
    ]

    blank_application = pd.DataFrame(columns=blank_application_list)

    return blank_application


def blank_tfmr_manuf():
    """
    initializes blank_tfmr_manuf dataframe
    """
    blank_tfmr_manuf_list = [
        'TfmrManufacturer', 'Fullname', 'Headquarters', 'FactoryLoc1',
        'FactoryLoc2', 'CreatedBy', 'Remarks'
    ]

    blank_tfmr_manuf = pd.DataFrame(columns=blank_tfmr_manuf_list)

    return blank_tfmr_manuf


def blank_ltc_details():
    """
    initializes blank_ltc_details dataframe
    """
    blank_ltc_details_list = [
        'LTCIdentifier', 'LTCSerialNum', 'TfmrIdentifier', 'LTCManufacturer',
        'LTCIdentifierUnknown', 'LTCModel', 'Breather', 'Utility',
        'OperatingCompany', 'Region', 'Substation', 'LTC_Designation',
        'ManufactureDate', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_ltc_details = pd.DataFrame(columns=blank_ltc_details_list)

    return blank_ltc_details


def blank_ltc_models():
    """
    initializes blank_ltc_models dataframe
    """
    blank_ltc_models_list = [
        'LTCModel', 'ModelDesc', 'LTCManufacturer', 'DataFileName',
        'CreatedBy', 'Remarks'
    ]

    blank_ltc_models = pd.DataFrame(columns=blank_ltc_models_list)

    return blank_ltc_models


def blank_ltc_dga():
    """
    initializes blank_ltc_dga dataframe
    """
    blank_ltc_dga_list = [
        'LTCIdentifier', 'Compartment', 'SampleDate', 'LabTestDate',
        'OilTempC', 'H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2',
        'N2', 'BadSample', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_ltc_dga = pd.DataFrame(columns=blank_ltc_dga_list)

    return blank_ltc_dga


def blank_ltc_oq():
    """
    initializes blank_ltc_oq dataframe
    """
    blank_ltc_oq_list = [
        'LTCIdentifier', 'Compartment', 'SampleDate', 'LabTestDate',
        'OilTempC', 'MoisturePPM', 'Acidity', 'IFT', 'Color', 'D877',
        'D1816_1MM', 'D1816_2MM', 'IEC156', 'PF_25C', 'PF_100C',
        'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_ltc_oq = pd.DataFrame(columns=blank_ltc_oq_list)

    return blank_ltc_oq


def blank_ltc_tap_pos():
    """
    initializes blank_ltc_tap_pos dataframe
    """
    blank_ltc_tap_pos_list = [
        'LTCIdentifier', 'RecordDate', 'TapPos', 'DataFileName', 'CreatedBy',
        'Remarks'
    ]

    blank_ltc_tap_pos = pd.DataFrame(columns=blank_ltc_tap_pos_list)

    return blank_ltc_tap_pos


def blank_ltc_tap_count():
    """
    initializes blank_ltc_tap_count dataframe
    """
    blank_ltc_tap_count_list = [
        'LTCIdentifier', 'RecordDate', 'CounterReading', 'HighTapPos',
        'LowTapPos', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_ltc_tap_count = pd.DataFrame(columns=blank_ltc_tap_count_list)

    return blank_ltc_tap_count


def blank_ltc_service_history():
    """
    initializes blank_ltc_service_history dataframe
    """
    blank_ltc_service_history_list = [
        'LTCIdentifier', 'LTCEventType', 'EventDate', 'PreviousStatus',
        'ServiceStatus', 'FailureLoc', 'FailureConsequence', 'FailureCause',
        'RepairBy', 'RepairLoc', 'RootCause', 'DataFileName', 'CreatedBy',
        'Remarks'
    ]

    blank_ltc_service_history = pd.DataFrame(
        columns=blank_ltc_service_history_list)

    return blank_ltc_service_history


def blank_ltc_manuf():
    """
    initializes blank_ltc_manuf dataframe
    """
    blank_ltc_manuf_list = [
        'LTCManufacturer', 'Fullname', 'Headquarters', 'FactoryLoc1',
        'FactoryLoc2', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_ltc_manuf = pd.DataFrame(columns=blank_ltc_manuf_list)


    return blank_ltc_manuf


def blank_bush_details():
    """
    initializes blank_bush_details dataframe
    """
    blank_bush_details_list = [
        'BushingIdentifier', 'BushingSerialNum', 'TfmrIdentifier',
        'PhaseInstalled', 'BushingManufacturer', 'BushingModel', 'Utility',
        'OperatingCompany', 'Region', 'Substation', 'BushingDesignation',
        'ManufactureDate', 'ConnectionType', 'BIL', 'RatedVoltage',
        'RatedCurrent', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_bush_details = pd.DataFrame(columns=blank_bush_details_list)

    return blank_bush_details


def blank_bush_models():
    """
    initializes blank_bush_models dataframe
    """
    blank_bush_models_list = [
        'BushingModel'
        'ModelDesc', 'BushingManufacturer', 'DataFileName', 'LUOn', 'LUBy',
        'Remarks'
    ]

    blank_bush_models = pd.DataFrame(columns=blank_bush_models_list)


    return blank_bush_models


def blank_bush_service_history():
    """
    initializes blank_bush_service_history dataframe
    """
    blank_bush_service_history_list = [
        'BushingIdentifier', 'BushingEventType', 'EventDate', 'PreviousStatus',
        'ServiceStatus', 'FailureLoc', 'FailureConsequence', 'FailureCause',
        'RepairBy', 'RepairLoc', 'RootCause', 'DataFileName', 'CreatedBy',
        'Remarks'
    ]

    blank_bush_service_history = pd.DataFrame(
        columns=blank_bush_service_history_list)


    return blank_bush_service_history


def blank_bush_pf():
    """
    initializes blank_bush_pf dataframe
    """
    blank_bush_pf_list = [
        'BushingIdentifier', 'Factoryresult', 'Precommissioning',
        'TempHumidityInfo', 'TestDate', 'TestVoltagekV', 'C1PF', 'C1Cap',
        'C2PF', 'C2Cap', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_bush_pf = pd.DataFrame(columns=blank_bush_pf_list)

    return blank_bush_pf


def blank_bush_manuf():
    """
    initializes raw and final bush_manuf dataframe
    """
    blank_bush_manuf_list = [
        'BushingManufacturer', 'Fullname', 'Headquarters', 'FactoryLoc1',
        'FactoryLoc2', 'DataFileName', 'CreatedBy', 'Remarks'
    ]

    blank_bush_manuf = pd.DataFrame(columns=blank_bush_manuf_list)

    return blank_bush_manuf


def data_file_details():
    """
    initializes data_file_details dataframe
    """
    data_file_details_list = [
        'DataFile', 'FileTypeExtension', 'Utility', 'TypeofData',
        'ReceivedDate', 'ReceivedFrom', 'FilePathStorage'
    ]

    data_file_details = pd.DataFrame(columns=data_file_details_list)

    return data_file_details


def schema_1_workbook(tfmr_details=blank_tfmr_details(),
                      tfmr_service_history=blank_tfmr_service_history(),
                      tfmr_dga=blank_tfmr_dga(),
                      tfmr_dga_online=blank_tfmr_dga_online(),
                      tfmr_oq=blank_tfmr_oq(),
                      tfmr_f=blank_tfmr_f(),
                      tfmr_type=blank_tfmr_type(),
                      utilities=blank_utilities(),
                      application=blank_application(),
                      tfmr_manuf=blank_tfmr_manuf(),
                      ltc_details=blank_ltc_details(),
                      ltc_models=blank_ltc_models(),
                      ltc_dga=blank_ltc_dga(),
                      ltc_oq=blank_ltc_oq(),
                      ltc_tap_pos=blank_ltc_tap_pos(),
                      ltc_tap_count=blank_ltc_tap_count(),
                      ltc_service_history=blank_ltc_service_history(),
                      ltc_manuf=blank_ltc_manuf(),
                      bush_details=blank_bush_details(),
                      bush_models=blank_bush_models(),
                      bush_service_history=blank_bush_service_history(),
                      bush_pf=blank_bush_pf(),
                      bush_manuf=blank_bush_manuf(),
                      data_file_details=data_file_details()):
    """
    This function makes a workbook full of sheets containing field names for the schema_1 fields

    if no assignments a blank workbook is created
    """

    # now = dt.datetime.now().strftime("%Y-%m-%d_%I%M%p").upper()
    if ~(tfmr_details.empty or tfmr_service_history.empty or tfmr_dga.empty
         or tfmr_dga_online.empty or tfmr_oq.empty or tfmr_f.empty
         or tfmr_type.empty or tfmr_model.empty or utilities.empty
         or application.empty or tfmr_manuf.empty or ltc_details.empty or
         ltc_models.empty or ltc_dga.empty or ltc_oq.empty or ltc_tap_pos.empty
         or ltc_tap_count.empty or ltc_service_history.empty or ltc_manuf.empty
         or bush_details.empty or bush_models.empty
         or bush_service_history.empty or bush_pf.empty or bush_oq.empty
         or bush_dga.empty or bush_manuf.empty or data_file_details):
        fname = now + "_schema_1_workbook.xlsx"
    else:
        fname = now + "_blank_schema_1_workbook.xlsx"

    writer = pd.ExcelWriter(fname, engine="xlsxwriter")

    # Convert the dataframe to an XlsxWriter Excel object
    tfmr_details.to_excel(writer, sheet_name="tfmr_details", index=False)
    tfmr_service_history.to_excel(writer,
                                  sheet_name="tfmr_service_history",
                                  index=False)
    tfmr_dga.to_excel(writer, sheet_name="tfmr_dga", index=False)
    tfmr_dga_online.to_excel(writer,
                             sheet_name="qrytfmr_dga_onlineFurans",
                             index=False)
    tfmr_oq.to_excel(writer, sheet_name="tfmr_oq", index=False)
    tfmr_f.to_excel(writer, sheet_name="tfmr_f", index=False)
    tfmr_type.to_excel(writer, sheet_name="tfmr_type", index=False)
    tfmr_model.to_excel(writer, sheet_name="tfmr_model", index=False)
    utilities.to_excel(writer, sheet_name="utilities", index=False)
    application.to_excel(writer, sheet_name="application", index=False)
    tfmr_manuf.to_excel(writer, sheet_name="tfmr_manuf", index=False)
    ltc_details.to_excel(writer, sheet_name="ltc_details", index=False)
    ltc_models.to_excel(writer, sheet_name="ltc_models", index=False)
    ltc_dga.to_excel(writer, sheet_name="ltc_dga", index=False)
    ltc_oq.to_excel(writer, sheet_name="ltc_oq", index=False)
    ltc_tap_pos.to_excel(writer, sheet_name="ltc_tap_pos", index=False)
    ltc_tap_count.to_excel(writer, sheet_name="ltc_tap_count", index=False)
    ltc_service_history.to_excel(writer,
                                 sheet_name="ltc_service_history",
                                 index=False)
    ltc_manuf.to_excel(writer, sheet_name="ltc_manuf", index=False)
    bush_details.to_excel(writer, sheet_name="bush_details", index=False)
    bush_models.to_excel(writer, sheet_name="bush_models", index=False)
    bush_service_history.to_excel(writer,
                                  sheet_name="bush_service_history",
                                  index=False)
    bush_pf.to_excel(writer, sheet_name="bush_pf", index=False)
    bush_oq.to_excel(writer, sheet_name="bush_oq", index=False)
    bush_dga.to_excel(writer, sheet_name="bush_dga", index=False)
    bush_manuf.to_excel(writer, sheet_name="bush_manuf", index=False)
    data_file_details.to_excel(writer,
                               sheet_name="data_file_details",
                               index=False)
    writer.save()
    print('Workbook Saved')