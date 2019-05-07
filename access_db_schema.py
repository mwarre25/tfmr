"""
tfmr.ptx_schema
===============================================================
tfmr sub-module for creating ptx schema tables
"""

import pandas as pd
import numpy as np
import datetime as dt
import os


def blank_qryTfmrs():
    """Creates a blank qryTfmrs dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryTfmrs schema
    """
    qryTfmrs_list = [
        "ID", "SERIALNUM", "MANUFACTURER", "MANUFACTUREDATE", "ENERGIZEDATE",
        "REPAIRDATE", "RETIREDATE", "UTILITY", "REGION", "STATION",
        "DESIGNATION", "CORETYPE", "TOPMVA", "COOLINGTYPE", "HV_kV", "LV1_kV",
        "LV2_kV", "TV_kV", "NUMPHASES", "ISAUTO", "CRITICALITY"
    ]

    qryTfmrs = pd.DataFrame(columns=qryTfmrs_list)

    # strings
    for col in [
            "SERIALNUM",
            "MANUFACTURER",
            "UTILITY",
            "REGION",
            "STATION",
            "DESIGNATION",
            "CORETYPE",
    ]:
        qryTfmrs[col] = qryTfmrs[col].astype("str")

    # dates
    for col in ["MANUFACTUREDATE", "ENERGIZEDATE", "REPAIRDATE", "RETIREDATE"]:
        qryTfmrs[col] = pd.to_datetime(qryTfmrs[col])

    # floats
    for col in ["TOPMVA", "HV_kV", "LV1_kV", "LV2_kV", "TV_kV", "CRITICALITY"]:
        qryTfmrs[col] = qryTfmrs[col].astype("float")

    # ints
    for col in ["ID", "NUMPHASES"]:
        qryTfmrs[col] = qryTfmrs[col].astype("int")

    return qryTfmrs


def blank_qryDGA():
    """Creates a blank qryDGA dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryDGA schema
    """
    qryDGA_list = [
        "ID", "SERIALNUM", "SAMPLEDATE", "H2", "CH4", "C2H6", "C2H4", "C2H2",
        "CO", "CO2", "O2", "N2", "BadSample"
    ]

    qryDGA = pd.DataFrame(columns=qryDGA_list)

    # strings
    for col in ["SERIALNUM"]:
        qryDGA[col] = qryDGA[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryDGA[col] = pd.to_datetime(qryDGA[col])

    # floats
    for col in ["H2", "CH4", "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"]:
        qryDGA[col] = qryDGA[col].astype("float")

    # bool
    for col in ["BadSample"]:
        qryDGA[col] = qryDGA[col].astype("bool")

    # ints
    for col in ["ID"]:
        qryDGA[col] = qryDGA[col].astype("int")

    return qryDGA


def blank_qryOilQuality():
    """Creates a blank qryOilQuality dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryOilQuality schema
    """
    qryOilQuality_list = [
        "ID", "SERIALNUM", "SAMPLEDATE", "OILTEMP", "MOISTURE_PPM", "ACIDITY",
        "IFT", "COLOR", "D877", "D1816_1MM", "D1816_2MM", "IEC156", "PF_25C",
        "PF_100C"
    ]

    qryOilQuality = pd.DataFrame(columns=qryOilQuality_list)

    # strings
    for col in ["SERIALNUM"]:
        qryOilQuality[col] = qryOilQuality[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryOilQuality[col] = pd.to_datetime(qryOilQuality[col])

    # floats
    for col in [
            "OILTEMP",
            "MOISTURE_PPM",
            "ACIDITY",
            "IFT",
            "COLOR",
            "D877",
            "D1816_1MM",
            "D1816_2MM",
            "IEC156",
            "PF_25C",
            "PF_100C",
    ]:
        qryOilQuality[col] = qryOilQuality[col].astype("float")

    # ints
    for col in ["ID"]:
        qryOilQuality[col] = qryOilQuality[col].astype("int")

    return qryOilQuality


def blank_qryFurans():
    """Creates a blank qryFurans dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryFurans schema
    """
    qryFurans_list = ["ID", "SERIALNUM", "SAMPLEDATE", "2FAL"]

    qryFurans = pd.DataFrame(columns=qryFurans_list)

    # strings
    for col in ["SERIALNUM"]:
        qryFurans[col] = qryFurans[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryFurans[col] = pd.to_datetime(qryFurans[col])

    # floats
    for col in ["2FAL"]:
        qryFurans[col] = qryFurans[col].astype("float")

    # ints
    for col in ["ID"]:
        qryFurans[col] = qryFurans[col].astype("int")

    return qryFurans


def blank_qryLTC():
    """Creates a blank qryLTC dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryLTC schema
    """
    qryLTC_list = [
        "ID", "TFMRID", "LTCID", "MANUFACTURER", "MODEL", "BREATHER"
    ]

    qryLTC = pd.DataFrame(columns=qryLTC_list)

    # strings
    for col in ["TFMRID", "LTCID", "MANUFACTURER", "MODEL", "BREATHER"]:
        qryLTC[col] = qryLTC[col].astype("str")

    # ints
    for col in ["ID"]:
        qryLTC[col] = qryLTC[col].astype("int")

    return qryLTC


def blank_qryLTCTapCount():
    """Creates a blank qryLTCTapCount dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryLTCTapCount schema
    """
    qryLTCTapCount_list = [
        "ID", "RECORDDATE", "TFMRID", "LTCID", "COUNTERREADING", "HIGHTAPPOS",
        "LOWTAPPOS"
    ]

    qryLTCTapCount = pd.DataFrame(columns=qryLTCTapCount_list)

    # strings
    for col in ["TFMRID", "LTCID", "HIGHTAPPOS", "LOWTAPPOS"]:
        qryLTCTapCount[col] = qryLTCTapCount[col].astype("str")

    # dates
    for col in ["RECORDDATE"]:
        qryLTCTapCount[col] = pd.to_datetime(qryLTCTapCount[col])

    # ints
    for col in ["ID", "COUNTERREADING"]:
        qryLTCTapCount[col] = qryLTCTapCount[col].astype("int")

    return qryLTCTapCount


def blank_qryLTCTapPosition():
    """Creates a blank qryLTCTapPosition dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryLTCTapPosition schema
    """
    qryLTCTapPosition_list = [
        "ID", "RECORDDATE", "TFMRID", "LTCID", "TAPPOSITION"
    ]

    qryLTCTapPosition = pd.DataFrame(columns=qryLTCTapPosition_list)

    # strings
    for col in ["TFMRID", "LTCID", "TAPPOSITION"]:
        qryLTCTapPosition[col] = qryLTCTapPosition[col].astype("str")

    # dates
    for col in ["RECORDDATE"]:
        qryLTCTapPosition[col] = pd.to_datetime(qryLTCTapPosition[col])

    # ints
    for col in ["ID"]:
        qryLTCTapPosition[col] = qryLTCTapPosition[col].astype("int")

    return qryLTCTapPosition


def blank_qryInsulationPF():
    """Creates a blank qryInsulatorPF dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryInsulatorPF schema
    """
    qryInsulationPF_list = [
        "ID", "TFMRID", "SAMPLEDATE", "CH_MEAS", "CL_MEAS", "CT_MEAS",
        "CHL_MEAS", "CHT_MEAS", "CH_CORR", "CL_CORR", "CT_CORR", "CHL_CORR",
        "CHT_CORR"
    ]

    qryInsulationPF = pd.DataFrame(columns=qryInsulationPF_list)

    # strings
    for col in ["TFMRID"]:
        qryInsulationPF[col] = qryInsulationPF[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryInsulationPF[col] = pd.to_datetime(qryInsulationPF[col])

    # floats
    for col in [
            "CH_MEAS",
            "CL_MEAS",
            "CT_MEAS",
            "CHL_MEAS",
            "CHT_MEAS",
            "CH_CORR",
            "CL_CORR",
            "CT_CORR",
            "CHL_CORR",
            "CHT_CORR",
    ]:
        qryInsulationPF[col] = qryInsulationPF[col].astype("float")

    # ints
    for col in ["ID"]:
        qryInsulationPF[col] = qryInsulationPF[col].astype("int")

    return qryInsulationPF


def blank_qryLTCDGA():
    """Creates a blank qryLTCDGA dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryLTCDGA schema
    """
    qryLTCDGA_list = [
        "ID", "TFMRID", "LTCID", "COMPARTMENT", "SAMPLEDATE", "H2", "CH4",
        "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"
    ]

    qryLTCDGA = pd.DataFrame(columns=qryLTCDGA_list)

    # strings
    for col in ["TFMRID", "LTCID", "COMPARTMENT"]:
        qryLTCDGA[col] = qryLTCDGA[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryLTCDGA[col] = pd.to_datetime(qryLTCDGA[col])

    # floats
    for col in ["H2", "CH4", "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"]:
        qryLTCDGA[col] = qryLTCDGA[col].astype("float")

    # ints
    for col in ["ID"]:
        qryLTCDGA[col] = qryLTCDGA[col].astype("int")

    return qryLTCDGA


def blank_qryLTCOilQuality():
    """Creates a blank qryLTCOilQuality dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryLTCOilQuality schema
    """
    qryLTCOilQuality_list = [
        "ID", "TFMRID", "LTCID", "COMPARTMENT", "SAMPLEDATE", "OILTEMP",
        "MOISTURE_PPM", "ACIDITY", "IFT", "COLOR", "D877", "D1816_1MM",
        "D1816_2MM", "IEC156", "PF_25C", "PF_100C"
    ]

    qryLTCOilQuality = pd.DataFrame(columns=qryLTCOilQuality_list)

    # strings
    for col in ["TFMRID", "LTCID", "COMPARTMENT"]:
        qryLTCOilQuality[col] = qryLTCOilQuality[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryLTCOilQuality[col] = pd.to_datetime(qryLTCOilQuality[col])

    # floats
    for col in [
            "OILTEMP",
            "MOISTURE_PPM",
            "ACIDITY",
            "IFT",
            "COLOR",
            "D877",
            "D1816_1MM",
            "D1816_2MM",
            "IEC156",
            "PF_25C",
            "PF_100C",
    ]:
        qryLTCOilQuality[col] = qryLTCOilQuality[col].astype("float")

    # ints
    for col in ["ID"]:
        qryLTCOilQuality[col] = qryLTCOilQuality[col].astype("int")

    return qryLTCOilQuality


def blank_qrySelectorDGA():
    """Creates a blank qrySelectorDGA dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qrySelectorDGA schema
    """
    qrySelectorDGA_list = [
        "ID", "TFMRID", "LTCID", "SAMPLEDATE", "H2", "CH4", "C2H6", "C2H4",
        "C2H2", "CO", "CO2", "O2", "N2"
    ]

    qrySelectorDGA = pd.DataFrame(columns=qrySelectorDGA_list)

    # strings
    for col in ["TFMRID", "LTCID"]:
        qrySelectorDGA[col] = qrySelectorDGA[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qrySelectorDGA[col] = pd.to_datetime(qrySelectorDGA[col])

    # floats
    for col in ["H2", "CH4", "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"]:
        qrySelectorDGA[col] = qrySelectorDGA[col].astype("float")

    # ints
    for col in ["ID"]:
        qrySelectorDGA[col] = qrySelectorDGA[col].astype("int")

    return qrySelectorDGA


def blank_qrySelectorOilQuality():
    """Creates a blank qrySelectorOilQuality dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qrySelectorOilQuality schema
    """
    qrySelectorOilQuality_list = [
        "ID", "TFMRID", "LTCID", "SAMPLEDATE", "OILTEMP", "MOISTURE_PPM",
        "ACIDITY", "IFT", "COLOR", "D877", "D1816_1MM", "D1816_2MM", "IEC156",
        "PF_25C", "PF_100C"
    ]

    qrySelectorOilQuality = pd.DataFrame(columns=qrySelectorOilQuality_list)

    # strings
    for col in ["TFMRID", "LTCID"]:
        qrySelectorOilQuality[col] = qrySelectorOilQuality[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qrySelectorOilQuality[col] = pd.to_datetime(qrySelectorOilQuality[col])

    # floats
    for col in [
            "OILTEMP",
            "MOISTURE_PPM",
            "ACIDITY",
            "IFT",
            "COLOR",
            "D877",
            "D1816_1MM",
            "D1816_2MM",
            "IEC156",
            "PF_25C",
            "PF_100C",
    ]:
        qrySelectorOilQuality[col] = qrySelectorOilQuality[col].astype("float")

    # ints
    for col in ["ID"]:
        qrySelectorOilQuality[col] = qrySelectorOilQuality[col].astype("int")

    return qrySelectorOilQuality


def blank_qryDiverterDGA():
    """Creates a blank qryDiverterDGA dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryDiverterDGA schema
    """
    qryDiverterDGA_list = [
        "ID", "TFMRID", "LTCID", "SAMPLEDATE", "H2", "CH4", "C2H6", "C2H4",
        "C2H2", "CO", "CO2", "O2", "N2"
    ]

    qryDiverterDGA = pd.DataFrame(columns=qryDiverterDGA_list)

    # strings
    for col in ["TFMRID", "LTCID"]:
        qryDiverterDGA[col] = qryDiverterDGA[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryDiverterDGA[col] = pd.to_datetime(qryDiverterDGA[col])

    # floats
    for col in ["H2", "CH4", "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"]:
        qryDiverterDGA[col] = qryDiverterDGA[col].astype("float")

    # ints
    for col in ["ID"]:
        qryDiverterDGA[col] = qryDiverterDGA[col].astype("int")

    return qryDiverterDGA


def blank_qryDiverterOilQuality():
    """Creates a blank qryDiverterOilQuality dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryDiverterOilQuality schema
    """
    qryDiverterOilQuality_list = [
        "ID", "TFMRID", "LTCID", "SAMPLEDATE", "OILTEMP", "MOISTURE_PPM",
        "ACIDITY", "IFT", "COLOR", "D877", "D1816_1MM", "D1816_2MM", "IEC156",
        "PF_25C", "PF_100C"
    ]

    qryDiverterOilQuality = pd.DataFrame(columns=qryDiverterOilQuality_list)

    # strings
    for col in ["TFMRID", "LTCID"]:
        qryDiverterOilQuality[col] = qryDiverterOilQuality[col].astype("str")

    # dates
    for col in ["SAMPLEDATE"]:
        qryDiverterOilQuality[col] = pd.to_datetime(qryDiverterOilQuality[col])

    # floats
    for col in [
            "OILTEMP",
            "MOISTURE_PPM",
            "ACIDITY",
            "IFT",
            "COLOR",
            "D877",
            "D1816_1MM",
            "D1816_2MM",
            "IEC156",
            "PF_25C",
            "PF_100C",
    ]:
        qryDiverterOilQuality[col] = qryDiverterOilQuality[col].astype("float")

    # ints
    for col in ["ID"]:
        qryDiverterOilQuality[col] = qryDiverterOilQuality[col].astype("int")

    return qryDiverterOilQuality


def blank_qryBushing():
    """Creates a blank qryBushing dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryBushing schema
    """
    qryBushing_list = [
        "ID", "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL", "CONNECTIONTYPE",
        "BIL", "RATEDVOLTAGE", "RATEDCURRENT", "FACTORYC1PF", "FACTORYC1CAP",
        "FACTORYC2PF", "FACTORYC2CAP"
    ]

    qryBushing = pd.DataFrame(columns=qryBushing_list)

    # strings
    for col in [
            "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL", "CONNECTIONTYPE"
    ]:
        qryBushing[col] = qryBushing[col].astype("str")

    # floats
    for col in [
            "BIL",
            "RATEDVOLTAGE",
            "RATEDCURRENT",
            "FACTORYC1PF",
            "FACTORYC1CAP",
            "FACTORYC2PF",
            "FACTORYC2CAP",
    ]:
        qryBushing[col] = qryBushing[col].astype("float")

    # ints
    for col in ["ID"]:
        qryBushing[col] = qryBushing[col].astype("int")

    return qryBushing


def blank_qryBushingPowerFactor():
    """Creates a blank qryBushingPowerFactor dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with qryBushingPowerFactor schema
    """
    qryBushingPowerFactor_list = [
        "ID", "TESTDATE", "TFMRID", "BUSHINGID", "TEMPERATURE", "TESTVOLTAGE",
        "MEASUREDC1PF", "MEASUREDC1CAP", "MEASUREDC2PF", "MEASUREDC2CAP"
    ]

    qryBushingPowerFactor = pd.DataFrame(columns=qryBushingPowerFactor_list)

    # strings
    for col in ["TFMRID", "BUSHINGID"]:
        qryBushingPowerFactor[col] = qryBushingPowerFactor[col].astype("str")

    # dates
    for col in ["TESTDATE"]:
        qryBushingPowerFactor[col] = pd.to_datetime(qryBushingPowerFactor[col])

    # floats
    for col in [
            "TEMPERATURE",
            "TESTVOLTAGE",
            "MEASUREDC1PF",
            "MEASUREDC1CAP",
            "MEASUREDC2PF",
            "MEASUREDC2CAP",
    ]:
        qryBushingPowerFactor[col] = qryBushingPowerFactor[col].astype("float")

    # ints
    for col in ["ID"]:
        qryBushingPowerFactor[col] = qryBushingPowerFactor[col].astype("int")

    return qryBushingPowerFactor


def blank_tblResults():
    """Creates a blank tblResults dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with tblResults schema
    """
    tblResults_list = [
        "ID", "SERIALNUM", "RUNDATETIME", "DIAGNOSISDATE", "RESULTVALIDDATE",
        "NORMALDEGRADATION", "ABNORMALTHERMAL", "ABNORMALELECTRICAL",
        "ABNORMALCORE", "ABNORMALCONDITION", "OILQUALITY", "BUSHINGCONDITION",
        "LTCCONDITION", "ABNORMALCONDITIONCODE", "ABNORMALTHERMALCODE",
        "ABNORMALELECTRICALCODE", "ABNORMALCORECODE"
    ]

    tblResults = pd.DataFrame(columns=tblResults_list)

    # strings
    for col in ["SERIALNUM"]:
        tblResults[col] = tblResults[col].astype("str")

    # dates
    for col in ["RUNDATETIME", "DIAGNOSISDATE", "RESULTVALIDDATE"]:
        tblResults[col] = pd.to_datetime(tblResults[col])

    # floats
    for col in [
            "NORMALDEGRADATION",
            "ABNORMALTHERMAL",
            "ABNORMALELECTRICAL",
            "ABNORMALCORE",
            "ABNORMALCONDITION",
            "OILQUALITY",
            "BUSHINGCONDITION",
            "LTCCONDITION",
    ]:
        tblResults[col] = tblResults[col].astype("float")

    # ints
    for col in [
            "ID",
            "ABNORMALCONDITIONCODE",
            "ABNORMALTHERMALCODE",
            "ABNORMALELECTRICALCODE",
            "ABNORMALCORECODE",
    ]:
        tblResults[col] = tblResults[col].astype("int")

    return tblResults


def blank_tblResultsOverTime():
    """Creates a blank tblResultsOverTime dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with tblResultsOverTime schema
    """
    tblResults_list = [
        "ID", "SERIALNUM", "RUNDATETIME", "RESULTDATETIME",
        "NORMALDEGRADATION", "ABNORMALTHERMAL", "ABNORMALELECTRICAL",
        "ABNORMALCORE", "OILQUALITY", "BUSHINGCONDITION", "LTCCONDITION"
    ]

    tblResultsOverTime = pd.DataFrame(columns=tblResultsOverTime_list)

    # strings
    for col in ["SERIALNUM"]:
        tblResultsOverTime[col] = tblResultsOverTime[col].astype("str")

    # dates
    for col in ["RUNDATETIME", "RESULTDATETIME"]:
        tblResultsOverTime[col] = pd.to_datetime(tblResultsOverTime[col])

    # floats
    for col in [
            "NORMALDEGRADATION",
            "ABNORMALTHERMAL",
            "ABNORMALELECTRICAL",
            "ABNORMALCORE",
            "ABNORMALCONDITION",
            "OILQUALITY",
            "BUSHINGCONDITION",
            "LTCCONDITION",
    ]:
        tblResultsOverTime[col] = tblResultsOverTime[col].astype("float")

    return tblResultsOverTime


def blank_tblResultsDetails():
    """Creates a blank tblResultsDetails dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with tblResultsDetails schema
    """
    tblResultsDetails_list = [
        "ID", "RUNDATETIME", "DIAGNOSISDATE", "SERIALNUM", "RESULTVALIDDATE",
        "FAILUREMECHANISM", "BELIEF"
    ]

    tblResultsDetails = pd.DataFrame(columns=tblResultsDetails_list)

    # strings
    for col in ["SERIALNUM", "FAILUREMECHANISM"]:
        tblResultsDetails[col] = tblResultsDetails[col].astype("str")

    # dates
    for col in ["RUNDATETIME", "DIAGNOSISDATE", "RESULTVALIDDATE"]:
        tblResultsDetails[col] = pd.to_datetime(tblResultsDetails[col])

    # floats
    for col in ["BELIEF"]:
        tblResultsDetails[col] = tblResultsDetails[col].astype("float")

    # ints
    for col in ["ID"]:
        tblResultsDetails[col] = tblResultsDetails[col].astype("int")

    return tblResultsDetails


def blank_ptxResults():
    """Creates a blank ptxResults dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with ptxResults schema
    """
    ptxResults_list = [
        'Region',
        'Station',
        'Designation',
        'Serial Number',
        'Vintage',
        'Manufacturer',
        'HV Voltage (kV)',
        'Failure Consequence',
        'Normal Degradation',
        'NDI Data Quality',
        'Abnormal Condition Code',
        'Abnormal Thermal Code',
        'Abnormal Thermal',
        'Abnormal Electrical Code',
        'Abnormal Electrical',
        'Abnormal Core Code',
        'Abnormal Core',
        'Abnormal Index Data Quality',
        'Oil Quality',
        'LTC(s)',
        'Bushing(s)',
        'Result Valid Until',
    ]

    ptxResults = pd.DataFrame(columns=ptxResults_list)

    # strings
    for col in [
            'Region',
            'Station',
            'Designation',
            'Serial Number',
            'Manufacturer',
            'NDI Data Quality',
            'Abnormal Index Data Quality',
    ]:
        ptxResults[col] = ptxResults[col].astype("str")

    # dates
    for col in ['Result Valid Until']:
        ptxResults[col] = pd.to_datetime(ptxResults[col])

    # floats
    for col in [
            'HV Voltage (kV)', 'Failure Consequence', 'Normal Degradation',
            'Abnormal Thermal', 'Abnormal Electrical', 'Abnormal Core',
            'Oil Quality', 'LTC(s)', 'Bushing(s)'
    ]:
        ptxResults[col] = ptxResults[col].astype("float")

    # ints
    for col in [
            'Vintage',
            'Abnormal Condition Code',
            'Abnormal Thermal Code',
            'Abnormal Electrical Code',
            'Abnormal Core Code',
    ]:
        ptxResults[col] = tptxResults[col].astype("int")

    return ptxResults


def blank_tblComments():
    """Creates a blank tblComments dataframe
    Args:
        none

    Returns:
        dataframe: dataframe with tblComments schema
    """
    tblComments_list = ['COMPONENTID', 'COMMENTDATE', 'COMMENTTEXT']

    tblComments = pd.DataFrame(columns=tblComments_list)

    # strings
    for col in [
            'COMPONENTID',
            'COMMENTTEXT',
    ]:
        tblComments[col] = tblComments[col].astype("str")

    # dates
    for col in ["COMMENTDATE"]:
        tblComments[col] = pd.to_datetime(tblComments[col])

    return tblComments


def blank_ptx_workbook():
    """Creates a workbook full of blank PTX schema sheets

    Args:
        none

    Returns:
        Excel workbook: Excel workbook containing PTX schema sheets
    """
    qryTfmrs = blank_qryTfmrs(),
    qryDGA = blank_qryDGA(),
    qryOilQuality = blank_qryOilQuality(),
    qryFurans = blank_qryFurans(),
    qryLTC = blank_qryLTC(),
    qryLTCDGA = blank_qryLTCDGA(),
    qryLTCOilQuality = blank_qryLTCOilQuality(),
    qryLTCTapCount = blank_qryLTCTapCount(),
    qryLTCTapPosition = blank_qryLTCTapPosition(),
    qryInsulationPF = blank_qryInsulationPF(),
    qrySelectorDGA = blank_qrySelectorDGA(),
    qrySelectorOilQuality = blank_qrySelectorOilQuality(),
    qryDiverterDGA = blank_qryDiverterDGA(),
    qryDiverterOilQuality = blank_qryDiverterOilQuality(),
    qryBushing = blank_qryBushing(),
    qryBushingPowerFactor = blank_qryBushingPowerFactor(),
    tblComments = blank_tblComments()

    now = dt.datetime.now().strftime("%Y-%m-%d_%I%M%p").upper()
    fname = now + "_ptx_workbook.xlsx"

    writer = pd.ExcelWriter(fname, engine="xlsxwriter")

    # Convert the dataframe to an XlsxWriter Excel object
    qryTfmrs.to_excel(writer, sheet_name="qryTfmrs", index=False)
    qryDGA.to_excel(writer, sheet_name="qryDGA", index=False)
    qryOilQuality.to_excel(writer, sheet_name="qryOilQuality", index=False)
    qryFurans.to_excel(writer, sheet_name="qryFurans", index=False)
    qryLTC.to_excel(writer, sheet_name="qryLTC", index=False)
    qryLTCDGA.to_excel(writer, sheet_name="qryLTCDGA", index=False)
    qryLTCOilQuality.to_excel(writer,
                              sheet_name="qryLTCOilQuality",
                              index=False)
    qryLTCTapCount.to_excel(writer, sheet_name="qryLTCTapCount", index=False)
    qryLTCTapPosition.to_excel(writer,
                               sheet_name="qryLTCTapPosition",
                               index=False)
    qryInsulationPF.to_excel(writer, sheet_name="qryInsulationPF", index=False)
    qrySelectorDGA.to_excel(writer, sheet_name="qrySelectorDGA", index=False)
    qrySelectorOilQuality.to_excel(writer,
                                   sheet_name="qrySelectorOilQuality",
                                   index=False)
    qryDiverterDGA.to_excel(writer, sheet_name="qryDiverterDGA", index=False)
    qryDiverterOilQuality.to_excel(writer,
                                   sheet_name="qryDiverterOilQuality",
                                   index=False)
    qryBushing.to_excel(writer, sheet_name="qryBushing", index=False)
    qryBushingPowerFactor.to_excel(writer,
                                   sheet_name="qryBushingPowerFactor",
                                   index=False)
    tblComments.to_excel(writer, sheet_name="tblComments", index=False)
    writer.save()
    print('Workbook Saved')


def ptx_workbook(**kwargs):
    """Creates a workbook full of PTX schema sheets populated from pandas dataframes

    Args:
        qryTfmrs (kwarg) (dataframe): Dataframe with qryTfmrs fields and data
        qryDGA (kwarg) (dataframe): Dataframe with qryDGA fields and data
        qryOilQuality (kwarg) (dataframe):  Dataframe with qryOilQuality fields and data
        qryFurans (kwarg) (dataframe):  Dataframe with qryFurans fields and data
        qryLTC (kwarg) (dataframe):  Dataframe with qryLTC fields and data
        qryLTCDGA (kwarg) (dataframe): Dataframe with qryLTCDGA fields and data
        qryLTCOilQuality (kwarg) (dataframe): Dataframe with qryLTCOilQuality fields and data
        qryLTCTapCount (kwarg) (dataframe): Dataframe with qryLTCTapCount fields and data
        qryLTCTapPosition (kwarg) (dataframe): Dataframe with qryLTCTapPosition fields and data
        qryInsulationPF (kwarg) (dataframe): Dataframe with qryInsulationPF fields and data
        qrySelectorDGA (kwarg) (dataframe): Dataframe with qrySelectorDGA fields and data
        qrySelectorOilQuality (kwarg) (dataframe): Dataframe with qrySelectorOilQuality fields and data
        qryDiverterDGA (kwarg) (dataframe): Dataframe with qryDiverterDGA fields and data
        qryDiverterOilQuality (kwarg) (dataframe): Dataframe with qryDiverterOilQuality fields and data
        qryBushing (kwarg) (dataframe): Dataframe with qryBushing fields and data
        qryBushingPowerFactor (kwarg) (dataframe): Dataframe with qryBushingPowerFactor fields and data
        tblComments  (kwarg) (dataframe): Dataframe with tblComments fields and data

    Returns:
        Excel workbook: Excel workbook with only populated PTX schema query sheets
    """

    now = dt.datetime.now().strftime("%Y-%m-%d_%I%M%p").upper()

    fname = now + "_ptx_workbook.xlsx"

    writer = pd.ExcelWriter(fname, engine="xlsxwriter")

    # Convert the dataframe to an XlsxWriter Excel object
    if 'qryTfmrs' in kwargs:
        try:
            qryTfmrs.to_excel(writer, sheet_name="qryTfmrs", index=False)
        except Exception as e:
            print('loading qryTfmrs failed b/c: ' + str(e))

    if 'qryDGA' in kwargs:
        try:
            qryDGA.to_excel(writer, sheet_name="qryDGA", index=False)
        except Exception as e:
            print('loading qryDGA failed b/c: ' + str(e))

    if 'qryOilQuality' in kwargs:
        try:
            qryOilQuality.to_excel(writer,
                                   sheet_name="qryOilQuality",
                                   index=False)
        except Exception as e:
            print('loading qryOilQuality failed b/c: ' + str(e))

    if 'qryFurans' in kwargs:
        try:
            qryFurans.to_excel(writer, sheet_name="qryFurans", index=False)
        except Exception as e:
            print('loading qryFurans failed b/c: ' + str(e))

    if 'qryLTC' in kwargs:
        try:
            qryLTC.to_excel(writer, sheet_name="qryLTC", index=False)
        except Exception as e:
            print('loading qryLTC failed b/c: ' + str(e))

    if 'qryLTCDGA' in kwargs:
        try:
            qryLTCDGA.to_excel(writer, sheet_name="qryLTCDGA", index=False)
        except Exception as e:
            print('loading qryLTCDGA failed b/c: ' + str(e))

    if 'qryLTCOilQuality' in kwargs:
        try:
            qryLTCOilQuality.to_excel(writer,
                                      sheet_name="qryLTCOilQuality",
                                      index=False)
        except Exception as e:
            print('loading qryLTCOilQuality failed b/c: ' + str(e))

    if 'qryLTCTapCount' in kwargs:
        try:
            qryLTCTapCount.to_excel(writer,
                                    sheet_name="qryLTCTapCount",
                                    index=False)
        except Exception as e:
            print('loading qryLTCTapCount failed b/c: ' + str(e))

    if 'qryLTCTapPosition' in kwargs:
        try:
            qryLTCTapPosition.to_excel(writer,
                                       sheet_name="qryLTCTapPosition",
                                       index=False)
        except Exception as e:
            print('loading qryLTCTapPosition failed b/c: ' + str(e))

    if 'qryInsulationPF' in kwargs:
        try:
            qryInsulationPF.to_excel(writer,
                                     sheet_name="qryInsulationPF",
                                     index=False)
        except Exception as e:
            print('loading qryInsulationPF failed b/c: ' + str(e))

    if 'qrySelectorDGA' in kwargs:
        try:
            qrySelectorDGA.to_excel(writer,
                                    sheet_name="qrySelectorDGA",
                                    index=False)
        except Exception as e:
            print('loading qrySelectorDGA failed b/c: ' + str(e))

    if 'qrySelectorOilQuality' in kwargs:
        try:
            qrySelectorOilQuality.to_excel(writer,
                                           sheet_name="qrySelectorOilQuality",
                                           index=False)
        except Exception as e:
            print('loading qrySelectorOilQuality failed b/c: ' + str(e))

    if 'qryDiverterDGA' in kwargs:
        try:
            qryDiverterDGA.to_excel(writer,
                                    sheet_name="qryDiverterDGA",
                                    index=False)
        except Exception as e:
            print('loading qryDiverterDGA failed b/c: ' + str(e))

    if 'qryDiverterOilQuality' in kwargs:
        try:
            qryDiverterOilQuality.to_excel(writer,
                                           sheet_name="qryDiverterOilQuality",
                                           index=False)
        except Exception as e:
            print('loading qryDiverterOilQuality failed b/c: ' + str(e))

    if 'qryBushing' in kwargs:
        try:
            qryBushing.to_excel(writer, sheet_name="qryBushing", index=False)
        except Exception as e:
            print('loading qryBushing failed b/c: ' + str(e))

    if 'qryBushingPowerFactor' in kwargs:
        try:
            qryBushingPowerFactor.to_excel(writer,
                                           sheet_name="qryBushingPowerFactor",
                                           index=False)
        except Exception as e:
            print('loading qryBushingPowerFactor failed b/c: ' + str(e))

    if 'tblComments' in kwargs:
        try:
            tblComments.to_excel(writer, sheet_name="tblComments", index=False)
        except Exception as e:
            print('loading tblComments failed b/c: ' + str(e))

    writer.save()
    print('Workbook Saved')


def tblResultsCompare(tblResults_old, tblResults_new):
    """Compares two tblResults tables and outputs a table with the serial numbers that show a change.

    Args:
        tblResults_old (dataframe): Old tblResults to be compared
        tblResults_new (dataframe): New tblREsults to be compared

    Returns:
        Excel workbook: Workbook with sheets ["abs_chg_gt_0", "tblResults_old", "tblResults_new"] saves to current working directory
    """

    columns_to_delete = [
        # "ID",
        "RUNDATETIME",
        "DIAGNOSISDATE",
        "OILQUALITY",
        "BUSHINGCONDITION",
        "LTCCONDITION",
        "ABNORMALCONDITION",
        "ABNORMALCONDITIONCODE",
        "ABNORMALTHERMALCODE",
        "ABNORMALELECTRICALCODE",
        "ABNORMALCORECODE",
    ]
    try:
        tblResults_old = tblResults_old.drop(columns_to_delete, axis=1)
    except Exception as e:
        print('failed to drop columns. skipping:\n' + str(e))
        pass

    try:
        tblResults_new = tblResults_new.drop(columns_to_delete, axis=1)
    except Exception as e:
        print('failed to drop columns. skipping:\n' + str(e))
        pass

    tblR_both = tblResults_old.merge(
        tblResults_new,
        left_on="SERIALNUM",
        right_on="SERIALNUM",
        suffixes=("_old", "_new"),
        indicator=True,
    )

    tblR_both["NDI_Chg"] = (tblR_both["NORMALDEGRADATION_new"] -
                            tblR_both["NORMALDEGRADATION_old"])
    tblR_both["AT_Chg"] = (tblR_both["ABNORMALTHERMAL_new"] -
                           tblR_both["ABNORMALTHERMAL_old"])
    tblR_both["ACore_Chg"] = (tblR_both["ABNORMALCORE_new"] -
                              tblR_both["ABNORMALCORE_old"])
    tblR_both["AE_Chg"] = (tblR_both["ABNORMALELECTRICAL_new"] -
                           tblR_both["ABNORMALELECTRICAL_old"])

    tblR_both = tblR_both[[
        "SERIALNUM",
        "NDI_Chg",
        "AT_Chg",
        "ACore_Chg",
        "AE_Chg",
        "RESULTVALIDDATE_old",
        "RESULTVALIDDATE_new",
        "NORMALDEGRADATION_old",
        "NORMALDEGRADATION_new",
        "ABNORMALTHERMAL_old",
        "ABNORMALTHERMAL_new",
        "ABNORMALELECTRICAL_old",
        "ABNORMALELECTRICAL_new",
        "ABNORMALCORE_old",
        "ABNORMALCORE_new",
    ]]

    NDI_Chg = np.abs(tblR_both["NDI_Chg"]) > 0
    AT_Chg = np.abs(tblR_both["AT_Chg"]) > 0
    AE_Chg = np.abs(tblR_both["AE_Chg"]) > 0
    ACore_Chg = np.abs(tblR_both["ACore_Chg"]) > 0
    Has_Index_Chg = tblR_both[NDI_Chg | AT_Chg | AE_Chg | ACore_Chg]
    Has_Index_Chg.SERIALNUM.count()

    # Create a Pandas Excel writer using XlsxWriter as the engine
    now = dt.datetime.now().strftime('%Y-%m-%d_%I%M%p').upper()
    fname = now + "_tblResultsComparison" + ".xlsx"
    writer = pd.ExcelWriter(fname, engine="xlsxwriter")

    # Convert the dataframe to an XlsxWriter Excel object
    Has_Index_Chg.to_excel(writer, sheet_name="abs_chg_gt_0", index=False)
    tblResults_old.to_excel(writer, sheet_name="tblResults_old", index=False)
    tblResults_new.to_excel(writer, sheet_name="tblResults_new", index=False)
    writer.save()
    print("Analysis Complete. Please find " + fname + " in " + os.getcwd())
    return Has_Index_Chg
