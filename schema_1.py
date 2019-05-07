"""
tfmr.schema_1
===============================================================
tfmr sub-module for creating schema_1 tables
"""
import pandas as pd
import datetime as dt
now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()

def raw_tfmr_details():
    """
    initializes raw and final tfmr_details dataframes
    """
    raw_tfmr_details_list = ['TfmrIdentifier_Raw',
                             'TfmrSerialNum_Raw',
                             'TfmrManufacturer_Raw',
                             'ManufactureDate_Raw',
                             'IdentifierUnknown_Raw',
                             'Utility_Raw',
                             'OperatingCompany_Raw',
                             'Region_Raw',
                             'Substation_Raw',
                             'Designation_Raw',
                             'CoreType_Raw',
                             'CoolingType1_Raw',
                             'MVA1_Raw',
                             'CoolingType2_Raw',
                             'MVA2_Raw',
                             'CoolingType3_Raw',
                             'MVA3_Raw',
                             'Application_Raw',
                             'TfmrType_Raw',
                             'HV_kV_Raw',
                             'LV1_kV_Raw',
                             'LV2_kV_Raw',
                             'TV_kV_Raw',
                             'HV_Connection_Raw',
                             'LV1_Connection_Raw',
                             'LV2_Connection_Raw',
                             'TV_Connection_Raw',
                             'BuriedTertiary_Raw',
                             'NumPhases_Raw',
                             'IsAuto_Raw',
                             'OilType_Raw',
                             'OilPreservationType_Raw',
                             'UtilityCriticality_Raw',
                             'DataFileName_Raw',
                             'CreatedBy_Raw',
                             'Remarks_Raw']

    raw_tfmr_details = pd.DataFrame(columns=raw_tfmr_details_list)

    tfmr_details_list = [field.replace('_Raw', '')
                         for field in raw_tfmr_details_list]
    tfmr_details = pd.DataFrame(columns=tfmr_details_list)

    return raw_tfmr_details, tfmr_details


def raw_tfmr_service_history():
    """
    initializes raw_tfmr_service_history dataframe
    """
    raw_tfmr_service_history_list = ['TfmrIdentifier_Raw',
                                     'TfmrEventType_Raw',
                                     'EventDate_Raw',
                                     'PreviousStatus_Raw',
                                     'ServiceStatus_Raw',
                                     'FirstFailure_Raw',
                                     'AgeAtFailure_Raw',
                                     'FailureLoc_Raw',
                                     'FailedComponent_Raw',
                                     'FailureConsequence_Raw',
                                     'FailureCause_Raw',
                                     'RepairBy_Raw',
                                     'RepairLoc_Raw',
                                     'RootCause_Raw',
                                     'DataFileName_Raw',
                                     'CreatedBy_Raw',
                                     'Remarks_Raw']

    raw_tfmr_service_history = pd.DataFrame(
        columns=raw_tfmr_service_history_list)

    tfmr_service_history_list = [field.replace(
        '_Raw', '') for field in raw_tfmr_service_history_list]
    tfmr_service_history = pd.DataFrame(columns=tfmr_service_history_list)

    return raw_tfmr_service_history, tfmr_service_history


def raw_tfmr_dga():
    """
    initializes raw_tfmr_dga dataframe
    """
    raw_tfmr_dga_list = ['TfmrIdentifier_Raw',
                         'SampleFrom_Raw',
                         'SampleDate_Raw',
                         'LabTestDate_Raw',
                         'OilTempC_Raw',
                         'H2_Raw',
                         'CH4_Raw',
                         'C2H6_Raw',
                         'C2H4_Raw',
                         'C2H2_Raw',
                         'CO_Raw',
                         'CO2_Raw',
                         'O2_Raw',
                         'N2_Raw',
                         'BadSample_Raw',
                         'DataFileName_Raw',
                         'CreatedBy_Raw',
                         'Remarks_Raw']

    raw_tfmr_dga = pd.DataFrame(columns=raw_tfmr_dga_list)

    tfmr_dga_list = [field.replace('_Raw', '') for field in raw_tfmr_dga_list]
    tfmr_dga = pd.DataFrame(columns=tfmr_dga_list)

    return raw_tfmr_dga, tfmr_dga


def raw_tfmr_dga_online():
    """
    initializes raw_tfmr_dga_online dataframe
    """
    raw_tfmr_dga_online_list = ['TfmrIdentifier_Raw',
                                'SampleDate_Raw',
                                'LabTestDate_Raw',
                                'OilTempC_Raw',
                                'H2_Raw',
                                'CH4_Raw',
                                'C2H6_Raw',
                                'C2H4_Raw',
                                'C2H2_Raw',
                                'CO_Raw',
                                'CO2_Raw',
                                'O2_Raw',
                                'N2_Raw',
                                'Moisture_PPM_Raw',
                                'RelSaturation_Raw',
                                'MonitorModel_Raw',
                                'BadSample_Raw',
                                'DataFileName_Raw',
                                'CreatedBy_Raw',
                                'Remarks_Raw']

    raw_tfmr_dga_online = pd.DataFrame(columns=raw_tfmr_dga_online_list)

    tfmr_dga_online_list = [field.replace(
        '_Raw', '') for field in raw_tfmr_dga_online_list]
    tfmr_dga_online = pd.DataFrame(columns=tfmr_dga_online_list)

    return raw_tfmr_dga_online, tfmr_dga_online


def raw_tfmr_oq():
    """
    initializes raw_tfmr_oq dataframe
    """
    raw_tfmr_oq_list = ['TfmrIdentifier_Raw',
                        'SampleDate_Raw',
                        'LabTestDate_Raw',
                        'OilTempC_Raw',
                        'MoisturePPM_Raw',
                        'Acidity_Raw',
                        'IFT_Raw',
                        'Color_Raw',
                        'D877_Raw',
                        'D1816_1MM_Raw',
                        'D1816_2MM_Raw',
                        'IEC156_Raw',
                        'PF_25C_Raw',
                        'PF_100C_Raw',
                        'DataFileName_Raw',
                        'CreatedBy_Raw',
                        'Remarks_Raw']

    raw_tfmr_oq = pd.DataFrame(columns=raw_tfmr_oq_list)

    tfmr_oq_list = [field.replace('_Raw', '') for field in raw_tfmr_oq_list]
    tfmr_oq = pd.DataFrame(columns=tfmr_oq_list)

    return raw_tfmr_oq, tfmr_oq


def raw_tfmr_f():
    """
    initializes raw_tfmr_f dataframe
    """
    raw_tfmr_f_list = ['TfmrIdentifier_Raw',
                       'SampleDate_Raw',
                       'LabTestDate_Raw',
                       '2FAL_Raw',
                       '5M2F_Raw',
                       '5H2F_Raw',
                       '2ACF_Raw',
                       '2FOL_Raw',
                       'CH3OH_Raw',
                       'DataFileName_Raw',
                       'CreatedBy_Raw',
                       'Remarks_Raw']

    raw_tfmr_f = pd.DataFrame(columns=raw_tfmr_f_list)

    tfmr_f_list = [field.replace('_Raw', '') for field in raw_tfmr_f_list]
    tfmr_f = pd.DataFrame(columns=tfmr_f_list)

    return raw_tfmr_f, tfmr_f


def raw_tfmr_type():
    """
    initializes raw_tfmr_type dataframe
    """
    raw_tfmr_type_list = ['TfmrType_Raw',
                          'DataFileName_Raw',
                          'CreatedBy_Raw',
                          'Remarks_Raw']

    raw_tfmr_type = pd.DataFrame(columns=raw_tfmr_type_list)

    tfmr_type_list = [field.replace('_Raw', '')
                      for field in raw_tfmr_type_list]
    tfmr_type = pd.DataFrame(columns=tfmr_type_list)

    return raw_tfmr_type, tfmr_type


def raw_utilities():
    """
    initializes raw_utilities dataframe
    """
    raw_utilities_list = ['Fullname_Raw',
                          'Region_Raw',
                          'Headquarters_Raw',
                          'PointofContact1_Raw',
                          'PhoneofContact1_Raw',
                          'PointofContact2_Raw',
                          'PhoneofContact2_Raw',
                          'DataFileName_Raw',
                          'LUOn_Raw',
                          'LUBy_Raw',
                          'Remarks_Raw']

    raw_utilities = pd.DataFrame(columns=raw_utilities_list)

    utilities_list = [field.replace('_Raw', '')
                      for field in raw_utilities_list]
    utilities = pd.DataFrame(columns=utilities_list)

    return raw_utilities, utilities


def raw_application():
    """
    initializes raw_application dataframe
    """
    raw_application_list = ['Application_Raw',
                            'DataFileName_Raw',
                            'LUOn_Raw',
                            'LUBy_Raw',
                            'Remarks_Raw']

    raw_application = pd.DataFrame(columns=raw_application_list)

    application_list = [field.replace('_Raw', '')
                        for field in raw_application_list]
    application = pd.DataFrame(columns=application_list)

    return raw_application, application


def raw_tfmr_manuf():
    """
    initializes raw_tfmr_manuf dataframe
    """
    raw_tfmr_manuf_list = ['TfmrManufacturer_Raw',
                           'Fullname_Raw',
                           'Headquarters_Raw',
                           'FactoryLoc1_Raw',
                           'FactoryLoc2_Raw',
                           'CreatedBy_Raw',
                           'Remarks_Raw']

    raw_tfmr_manuf = pd.DataFrame(columns=raw_tfmr_manuf_list)

    tfmr_manuf_list = [field.replace('_Raw', '')
                       for field in raw_tfmr_manuf_list]
    tfmr_manuf = pd.DataFrame(columns=tfmr_manuf_list)

    return raw_tfmr_manuf, tfmr_manuf


def raw_ltc_details():
    """
    initializes raw_ltc_details dataframe
    """
    raw_ltc_details_list = ['LTCIdentifier_Raw',
                            'LTCSerialNum_Raw',
                            'TfmrIdentifier_Raw',
                            'LTCManufacturer_Raw',
                            'LTCIdentifierUnknown_Raw',
                            'LTCModel_Raw',
                            'Breather_Raw',
                            'Utility_Raw',
                            'OperatingCompany_Raw',
                            'Region_Raw',
                            'Substation_Raw',
                            'LTC_Designation_Raw',
                            'ManufactureDate_Raw',
                            'DataFileName_Raw',
                            'CreatedBy_Raw',
                            'Remarks_Raw']

    raw_ltc_details = pd.DataFrame(columns=raw_ltc_details_list)

    ltc_details_list = [field.replace('_Raw', '')
                        for field in raw_ltc_details_list]
    ltc_details = pd.DataFrame(columns=ltc_details_list)

    return raw_ltc_details, ltc_details


def raw_ltc_models():
    """
    initializes raw_ltc_models dataframe
    """
    raw_ltc_models_list = ['LTCModel_Raw',
                           'ModelDesc_Raw',
                           'LTCManufacturer_Raw',
                           'DataFileName_Raw',
                           'CreatedBy_Raw',
                           'Remarks_Raw']

    raw_ltc_models = pd.DataFrame(columns=raw_ltc_models_list)

    ltc_models_list = [field.replace('_Raw', '')
                       for field in raw_ltc_models_list]
    ltc_models = pd.DataFrame(columns=ltc_models_list)

    return raw_ltc_models, ltc_models


def raw_ltc_dga():
    """
    initializes raw_ltc_dga dataframe
    """
    raw_ltc_dga_list = ['LTCIdentifier_Raw',
                        'Compartment_Raw',
                        'SampleDate_Raw',
                        'LabTestDate_Raw',
                        'OilTempC_Raw',
                        'H2_Raw',
                        'CH4_Raw',
                        'C2H6_Raw',
                        'C2H4_Raw',
                        'C2H2_Raw',
                        'CO_Raw',
                        'CO2_Raw',
                        'O2_Raw',
                        'N2_Raw',
                        'BadSample_Raw',
                        'DataFileName_Raw',
                        'CreatedBy_Raw',
                        'Remarks_Raw']

    raw_ltc_dga = pd.DataFrame(columns=raw_ltc_dga_list)

    ltc_dga_list = [field.replace('_Raw', '') for field in raw_ltc_dga_list]
    ltc_dga = pd.DataFrame(columns=ltc_dga_list)

    return raw_ltc_dga, ltc_dga


def raw_ltc_oq():
    """
    initializes raw_ltc_oq dataframe
    """
    raw_ltc_oq_list = ['LTCIdentifier_Raw',
                       'Compartment_Raw',
                       'SampleDate_Raw',
                       'LabTestDate_Raw',
                       'OilTempC_Raw',
                       'MoisturePPM_Raw',
                       'Acidity_Raw',
                       'IFT_Raw',
                       'Color_Raw',
                       'D877_Raw',
                       'D1816_1MM_Raw',
                       'D1816_2MM_Raw',
                       'IEC156_Raw',
                       'PF_25C_Raw',
                       'PF_100C_Raw',
                       'DataFileName_Raw',
                       'CreatedBy_Raw',
                       'Remarks_Raw']

    raw_ltc_oq = pd.DataFrame(columns=raw_ltc_oq_list)

    ltc_oq_list = [field.replace('_Raw', '') for field in raw_ltc_oq_list]
    ltc_oq = pd.DataFrame(columns=ltc_oq_list)

    return raw_ltc_oq, ltc_oq


def raw_ltc_tap_pos():
    """
    initializes raw_ltc_tap_pos dataframe
    """
    raw_ltc_tap_pos_list = ['LTCIdentifier_Raw',
                            'RecordDate_Raw',
                            'TapPos_Raw',
                            'DataFileName_Raw',
                            'CreatedBy_Raw',
                            'Remarks_Raw']

    raw_ltc_tap_pos = pd.DataFrame(columns=raw_ltc_tap_pos_list)

    ltc_tap_pos_list = [field.replace('_Raw', '')
                        for field in raw_ltc_tap_pos_list]
    ltc_tap_pos = pd.DataFrame(columns=ltc_tap_pos_list)

    return raw_ltc_tap_pos, ltc_tap_pos


def raw_ltc_tap_count():
    """
    initializes raw_ltc_tap_count dataframe
    """
    raw_ltc_tap_count_list = ['LTCIdentifier_Raw',
                              'RecordDate_Raw',
                              'CounterReading_Raw',
                              'HighTapPos_Raw',
                              'LowTapPos_Raw',
                              'DataFileName_Raw',
                              'CreatedBy_Raw',
                              'Remarks_Raw']

    raw_ltc_tap_count = pd.DataFrame(columns=raw_ltc_tap_count_list)

    ltc_tap_count_list = [field.replace('_Raw', '')
                          for field in raw_ltc_tap_count_list]
    ltc_tap_count = pd.DataFrame(columns=ltc_tap_count_list)

    return raw_ltc_tap_count, ltc_tap_count


def raw_ltc_service_history():
    """
    initializes raw_ltc_service_history dataframe
    """
    raw_ltc_service_history_list = ['LTCIdentifier_Raw',
                                    'LTCEventType_Raw',
                                    'EventDate_Raw',
                                    'PreviousStatus_Raw',
                                    'ServiceStatus_Raw',
                                    'FailureLoc_Raw',
                                    'FailureConsequence_Raw',
                                    'FailureCause_Raw',
                                    'RepairBy_Raw',
                                    'RepairLoc_Raw',
                                    'RootCause_Raw',
                                    'DataFileName_Raw',
                                    'CreatedBy_Raw',
                                    'Remarks_Raw']

    raw_ltc_service_history = pd.DataFrame(
        columns=raw_ltc_service_history_list)

    ltc_service_history_list = [field.replace(
        '_Raw', '') for field in raw_ltc_service_history_list]
    ltc_service_history = pd.DataFrame(columns=ltc_service_history_list)

    return raw_ltc_service_history, ltc_service_history


def raw_ltc_manuf():
    """
    initializes raw_ltc_manuf dataframe
    """
    raw_ltc_manuf_list = ['LTCManufacturer_Raw',
                          'Fullname_Raw',
                          'Headquarters_Raw',
                          'FactoryLoc1_Raw',
                          'FactoryLoc2_Raw',
                          'DataFileName_Raw',
                          'CreatedBy_Raw',
                          'Remarks_Raw']

    raw_ltc_manuf = pd.DataFrame(columns=raw_ltc_manuf_list)

    ltc_manuf_list = [field.replace('_Raw', '')
                      for field in raw_ltc_manuf_list]
    ltc_manuf = pd.DataFrame(columns=ltc_manuf_list)

    return raw_ltc_manuf, ltc_manuf


def raw_bush_details():
    """
    initializes raw_bush_details dataframe
    """
    raw_bush_details_list = ['BushingIdentifier_Raw',
                             'BushingSerialNum_Raw',
                             'TfmrIdentifier_Raw',
                             'PhaseInstalled_Raw',
                             'BushingManufacturer_Raw',
                             'BushingModel_Raw',
                             'Utility_Raw',
                             'OperatingCompany_Raw',
                             'Region_Raw',
                             'Substation_Raw',
                             'BushingDesignation_Raw',
                             'ManufactureDate_Raw',
                             'ConnectionType_Raw',
                             'BIL_Raw',
                             'RatedVoltage_Raw',
                             'RatedCurrent_Raw',
                             'DataFileName_Raw',
                             'CreatedBy_Raw',
                             'Remarks_Raw']

    raw_bush_details = pd.DataFrame(columns=raw_bush_details_list)

    bush_details_list = [field.replace('_Raw', '')
                         for field in raw_bush_details_list]
    bush_details = pd.DataFrame(columns=bush_details_list)

    return raw_bush_details, bush_details


def raw_bush_models():
    """
    initializes raw_bush_models dataframe
    """
    raw_bush_models_list = ['BushingModel_Raw'
                            'ModelDesc_Raw',
                            'BushingManufacturer_Raw',
                            'DataFileName_Raw',
                            'LUOn_Raw',
                            'LUBy_Raw',
                            'Remarks_Raw']

    raw_bush_models = pd.DataFrame(columns=raw_bush_models_list)

    bush_models_list = [field.replace('_Raw', '')
                        for field in raw_bush_models_list]
    bush_models = pd.DataFrame(columns=bush_models_list)

    return raw_bush_models, bush_models


def raw_bush_service_history():
    """
    initializes raw_bush_service_history dataframe
    """
    raw_bush_service_history_list = ['BushingIdentifier_Raw',
                                     'BushingEventType_Raw',
                                     'EventDate_Raw',
                                     'PreviousStatus_Raw',
                                     'ServiceStatus_Raw',
                                     'FailureLoc_Raw',
                                     'FailureConsequence_Raw',
                                     'FailureCause_Raw',
                                     'RepairBy_Raw',
                                     'RepairLoc_Raw',
                                     'RootCause_Raw',
                                     'DataFileName_Raw',
                                     'CreatedBy_Raw',
                                     'Remarks_Raw']

    raw_bush_service_history = pd.DataFrame(
        columns=raw_bush_service_history_list)

    bush_service_history_list = [field.replace(
        '_Raw', '') for field in raw_bush_service_history_list]
    bush_service_history = pd.DataFrame(columns=bush_service_history_list)

    return raw_bush_service_history, bush_service_history


def raw_bush_pf():
    """
    initializes raw_bush_pf dataframe
    """
    raw_bush_pf_list = ['BushingIdentifier_Raw',
                        'Factoryresult_Raw',
                        'Precommissioning_Raw',
                        'TempHumidityInfo_Raw',
                        'TestDate_Raw',
                        'TestVoltagekV_Raw',
                        'C1PF_Raw',
                        'C1Cap_Raw',
                        'C2PF_Raw',
                        'C2Cap_Raw',
                        'DataFileName_Raw',
                        'CreatedBy_Raw',
                        'Remarks_Raw']

    raw_bush_pf = pd.DataFrame(columns=raw_bush_pf_list)

    bush_pf_list = [field.replace('_Raw', '') for field in raw_bush_pf_list]
    bush_pf = pd.DataFrame(columns=bush_pf_list)

    return raw_bush_pf, bush_pf


def raw_bush_manuf():
    """
    initializes raw and final bush_manuf dataframe
    """
    raw_bush_manuf_list = ['BushingManufacturer_Raw',
                           'Fullname_Raw',
                           'Headquarters_Raw',
                           'FactoryLoc1_Raw',
                           'FactoryLoc2_Raw',
                           'DataFileName_Raw',
                           'CreatedBy_Raw',
                           'Remarks_Raw']

    raw_bush_manuf = pd.DataFrame(columns=raw_bush_manuf_list)

    bush_manuf_list = [field.replace('_Raw', '')
                       for field in raw_bush_manuf_list]
    bush_manuf = pd.DataFrame(columns=bush_manuf_list)

    return raw_bush_manuf, bush_manuf


def data_file_details():
    """
    initializes data_file_details dataframe
    """
    data_file_details_list = ['DataFile',
                              'FileTypeExtension',
                              'Utility',
                              'TypeofData',
                              'ReceivedDate',
                              'ReceivedFrom',
                              'FilePathStorage']

    data_file_details = pd.DataFrame(columns=data_file_details_list)

    return data_file_details


def schema_1_workbook(
        tfmr_details=raw_tfmr_details()[1],
        tfmr_service_history=raw_tfmr_service_history()[1],
        tfmr_dga=raw_tfmr_dga()[1],
        tfmr_dga_online=raw_tfmr_dga_online()[1],
        tfmr_oq=raw_tfmr_oq()[1],
        tfmr_f=raw_tfmr_f()[1],
        tfmr_type=raw_tfmr_type()[1],
        utilities=raw_utilities()[1],
        application=raw_application()[1],
        tfmr_manuf=raw_tfmr_manuf()[1],
        ltc_details=raw_ltc_details()[1],
        ltc_models=raw_ltc_models()[1],
        ltc_dga=raw_ltc_dga()[1],
        ltc_oq=raw_ltc_oq()[1],
        ltc_tap_pos=raw_ltc_tap_pos()[1],
        ltc_tap_count=raw_ltc_tap_count()[1],
        ltc_service_history=raw_ltc_service_history()[1],
        ltc_manuf=raw_ltc_manuf()[1],
        bush_details=raw_bush_details()[1],
        bush_models=raw_bush_models()[1],
        bush_service_history=raw_bush_service_history()[1],
        bush_pf=raw_bush_pf()[1],
        bush_manuf=raw_bush_manuf()[1],
        data_file_details=data_file_details()):
    """
    This function makes a workbook full of sheets containing field names for the schema_1 fields

    if no assignments a blank workbook is created
    """

    # now = dt.datetime.now().strftime("%Y-%m-%d_%I%M%p").upper()
    if ~(tfmr_details.empty or
         tfmr_service_history.empty or
         tfmr_dga.empty or
         tfmr_dga_online.empty or
         tfmr_oq.empty or
         tfmr_f.empty or
         tfmr_type.empty or
         tfmr_model.empty or
         utilities.empty or
         application.empty or
         tfmr_manuf.empty or
         ltc_details.empty or
         ltc_models.empty or
         ltc_dga.empty or
         ltc_oq.empty or
         ltc_tap_pos.empty or
         ltc_tap_count.empty or
         ltc_service_history.empty or
         ltc_manuf.empty or
         bush_details.empty or
         bush_models.empty or
         bush_service_history.empty or
         bush_pf.empty or
         bush_oq.empty or
         bush_dga.empty or
         bush_manuf.empty or
         data_file_details):
        fname = now + "_schema_1_workbook.xlsx"
    else:
        fname = now + "_blank_schema_1_workbook.xlsx"

    writer = pd.ExcelWriter(fname, engine="xlsxwriter")

    # Convert the dataframe to an XlsxWriter Excel object
    tfmr_details.to_excel(writer, sheet_name="tfmr_details", index=False)
    tfmr_service_history.to_excel(
        writer, sheet_name="tfmr_service_history", index=False)
    tfmr_dga.to_excel(writer, sheet_name="tfmr_dga", index=False)
    tfmr_dga_online.to_excel(
        writer, sheet_name="qrytfmr_dga_onlineFurans", index=False)
    tfmr_oq.to_excel(writer, sheet_name="tfmr_oq", index=False)
    tfmr_f.to_excel(writer, sheet_name="tfmr_f", index=False)
    tfmr_type.to_excel(
        writer, sheet_name="tfmr_type", index=False)
    tfmr_model.to_excel(writer, sheet_name="tfmr_model", index=False)
    utilities.to_excel(
        writer, sheet_name="utilities", index=False)
    application.to_excel(writer, sheet_name="application", index=False)
    tfmr_manuf.to_excel(writer, sheet_name="tfmr_manuf", index=False)
    ltc_details.to_excel(
        writer, sheet_name="ltc_details", index=False
    )
    ltc_models.to_excel(writer, sheet_name="ltc_models", index=False)
    ltc_dga.to_excel(
        writer, sheet_name="ltc_dga", index=False
    )
    ltc_oq.to_excel(writer, sheet_name="ltc_oq", index=False)
    ltc_tap_pos.to_excel(
        writer, sheet_name="ltc_tap_pos", index=False
    )
    ltc_tap_count.to_excel(
        writer, sheet_name="ltc_tap_count", index=False
    )
    ltc_service_history.to_excel(
        writer, sheet_name="ltc_service_history", index=False
    )
    ltc_manuf.to_excel(
        writer, sheet_name="ltc_manuf", index=False
    )
    bush_details.to_excel(
        writer, sheet_name="bush_details", index=False
    )
    bush_models.to_excel(
        writer, sheet_name="bush_models", index=False
    )
    bush_service_history.to_excel(
        writer, sheet_name="bush_service_history", index=False
    )
    bush_pf.to_excel(
        writer, sheet_name="bush_pf", index=False
    )
    bush_oq.to_excel(
        writer, sheet_name="bush_oq", index=False
    )
    bush_dga.to_excel(
        writer, sheet_name="bush_dga", index=False
    )
    bush_manuf.to_excel(
        writer, sheet_name="bush_manuf", index=False
    )
    data_file_details.to_excel(
        writer, sheet_name="data_file_details", index=False
    )
    writer.save()
    print('Workbook Saved')