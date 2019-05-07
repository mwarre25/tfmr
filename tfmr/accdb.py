"""
tfmr.accdb
=====================================================
tfmr sub-module for import to/export from accdb files.

The main assumption here is that we're working with PTX schema Access databases 
so some of the code may not have been abstracted enough to accomodate all Access 
databases.

The module write_to_ptx_accdb_tbls is currently broken because of a pyodbc issue:


The ODBC module used is pyodbc: https://github.com/mkleehammer/pyodbc.
The GUI module used is PySimpleGUI: https://github.com/PySimpleGUI/PySimpleGUI 
"""


import pyodbc
from win32com.client import Dispatch
import pandas as pd
import PySimpleGUI as sg
import os


def get_accdb_tbl_list():
    '''Returns list of accdb tables for single db

    Returns:
        List of strings of each table in the database.
        If exception prints to console.

    '''
    try:
        filename = sg.PopupGetFile(
            '',
            initial_folder=os.path.dirname(os.path.abspath(__file__)),
            no_window=True)
        conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + filename + ';')

        cnxn = pyodbc.connect(conn_str)
        crsr = cnxn.cursor()
        tbl_list = [tbl.table_name for tbl in crsr.tables(tableType='TABLE')]
        cnxn.close()
        return tbl_list
    except Exception as e:
        print('Creation of table list failed b/c:')
        print(str(e))
        cnxn.close()


def read_accdb_tbl(tbl_selection, **kwargs):
    '''Load a table from an accdb

    This function loads a table from an access db.
    The only implemented **kwarg checked for right now is filename.
    Add the filename to bypass the popup prompt.

    If exception, string prints to console.
    The function then tries to pull the selected
    file's table list. It then prompts you to enter a table name.
    If this fails it will fail again in a less pretty way.

    Args:
        tbl_selection (string): Name of table to read. 
        filename (kwarg): relative or absolute path of accdb filename of table.

    Returns:
        data (dataframe): Selected table in dataframe.
        
    '''

    try:
        print('Attempting load of ' + tbl_selection)
        if 'filename' in kwargs:
            filename = kwargs.get('filename')
            filename = os.path.dirname(
                os.path.abspath(filename)) + "\\" + filename
            print('filename: ' + filename)
        else:
            filename = sg.PopupGetFile(
                '',
                initial_folder=os.path.dirname(os.path.abspath(__file__)),
                no_window=True)
        conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + filename + ';')

        cnxn = pyodbc.connect(conn_str)
        crsr = cnxn.cursor()

        col_list = crsr.columns(table=tbl_selection)

        sql = "Select *"
        sql = sql + " From " + str(tbl_selection)
        crsr.execute(sql)
        data = pd.read_sql(sql, cnxn)

        cnxn.close()
        print(tbl_selection + " successfully loaded from " + filename)
    except Exception as e:
        print('Loading of ' + tbl_selection + ' failed\n')
        print(str(e))

        tbl_list = [table_info.table_name for table_info in crsr.tables(
            tableType='TABLE')]

        pprint(tbl_list)

        cnxn.close()
        try_input = input('What table do you want to load?: ')
        read_accdb_tbl(tbl_selection=try_input)

    return data


def write_to_schema_0_accdb_tbls(**kwargs):
    '''BROKEN! Writes pandas dataframes to an Access db

    Note: All datetime fields broken, pyodbc module error.

    This function attempts to load pandas dataframes into an Access accdb file
    if it sees the dataframe.

    Args:
        filename (kwarg) (string): Access db filename
        qryBushingPowerFactor (kwarg) (pandas dataframe): pandas dataframe with qryBushingPowerFactor schema.
        qryDGA (kwarg) (pandas dataframe): pandas dataframe with qryDGA schema. 
        qryFurans (kwarg) (pandas dataframe): pandas dataframe with qryFurans schema. 
        qryInsulationPF (kwarg) (pandas dataframe): pandas dataframe with qryInsulationPF schema. 
        qryLTC (kwarg) (pandas dataframe): pandas dataframe with qryLTC schema. 
        qryLTCDGA (kwarg) (pandas dataframe): pandas dataframe with qryLTCDGA schema. 
        qryLTCOilQuality (kwarg) (pandas dataframe): pandas dataframe with qryLTCOilQuality schema. 
        qryLTCTapCount (kwarg) (pandas dataframe): pandas dataframe with qryLTCTapCount schema. 
        qryLTCTapPosition (kwarg) (pandas dataframe): pandas dataframe with qryLTCTapPosition schema. 
        qryOilQuality (kwarg) (pandas dataframe): pandas dataframe with qryOilQuality schema. 
        qryTfmrs (kwarg) (pandas dataframe): pandas dataframe with qryTfmrs schema. 
        tblComments (kwarg) (pandas dataframe): pandas dataframe with tblComments schema. 
        tblOptions (kwarg) (pandas dataframe): pandas dataframe with tblOptions schema. 
        tblResultDetails (kwarg) (pandas dataframe): pandas dataframe with tblResultDetails schema. 
        tblResults (kwarg) (pandas dataframe): pandas dataframe with tblResults schema. 
        tblResultsOverTime (kwarg) (pandas dataframe): pandas dataframe with tblResultsOverTime schema. 
    '''
    try:
        if 'filename' in kwargs:
            filename = kwargs.get('filename')
            filename = os.path.dirname(
                os.path.abspath(filename)) + "\\" + filename
            print('filename: ' + filename)
        else:
            filename = sg.PopupGetFile(
                '',
                initial_folder=os.path.dirname(os.path.abspath(__file__)),
                no_window=True)
        conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                    r'DBQ=' + filename + ';')

        cnxn = pyodbc.connect(conn_str)
        crsr = cnxn.cursor()

    except Exception as e:
        print(str(e))
        cnxn.close()

    if 'qryBushingPowerFactor' in kwargs:
        try:
            qryBushingPowerFactor = kwargs.get('qryBushingPowerFactor')
            for _, row in qryBushingPowerFactor.iterrows():
                TESTDATE = row['TESTDATE']
                TFMRID = row['TFMRID']
                BUSHINGID = row['BUSHINGID']
                TEMPERATURE = row['TEMPERATURE']
                TESTVOLTAGE = row['TESTVOLTAGE']
                MEASUREDC1PF = row['MEASUREDC1PF']
                MEASUREDC1CAP = row['MEASUREDC1CAP']
                MEASUREDC2PF = row['MEASUREDC2PF']
                MEASUREDC2CAP = row['MEASUREDC2CAP']

                crsr.execute(
                    """
                    insert into qryBushingPowerFactor(
                        TESTDATE,
                        TFMRID,
                        BUSHINGID,
                        TEMPERATURE,
                        TESTVOLTAGE,
                        MEASUREDC1PF,
                        MEASUREDC1CAP,
                        MEASUREDC2PF,
                        MEASUREDC2CAP)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    TESTDATE,
                    TFMRID,
                    BUSHINGID,
                    TEMPERATURE,
                    TESTVOLTAGE,
                    MEASUREDC1PF,
                    MEASUREDC1CAP,
                    MEASUREDC2PF,
                    MEASUREDC2CAP)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryBushingPowerFactor')
            print(str(e))

    if 'qryDGA' in kwargs:
        try:
            qryDGA = kwargs.get('qryDGA')
            for _, row in qryDGA.iterrows():
                SERIALNUM = row['SERIALNUM']
                SAMPLEDATE = row['SAMPLEDATE']
                H2 = row['H2']
                CH4 = row['CH4']
                C2H6 = row['C2H6']
                C2H4 = row['C2H4']
                C2H2 = row['C2H2']
                CO = row['CO']
                CO2 = row['CO2']
                O2 = row['O2']
                N2 = row['N2']
                BadSample = row['BadSample']

                crsr.execute(
                    """insert into qryDGA(
                        SERIALNUM,
                        SAMPLEDATE,
                        H2,
                        CH4,
                        C2H6,
                        C2H4,
                        C2H2,
                        CO,
                        CO2,
                        O2,
                        N2,
                        BadSample)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    SERIALNUM,
                    SAMPLEDATE,
                    H2,
                    CH4,
                    C2H6,
                    C2H4,
                    C2H2,
                    CO,
                    CO2,
                    O2,
                    N2,
                    BadSample)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryDGA')
            print(str(e))

    if 'qryFurans' in kwargs:
        try:
            qryFurans = kwargs.get('qryFurans')
            for _, row in qryFurans.iterrows():
                SERIALNUM = row['SERIALNUM']
                SAMPLEDATE = row['SAMPLEDATE']
                TWOFAL = row['2FAL']

                crsr.execute(
                    """insert into qryFurans(
                        SERIALNUM,
                        SAMPLEDATE,
                        2FAL)
                        values(?,
                            ?,
                            ?)""",
                    SERIALNUM,
                    SAMPLEDATE,
                    TWOFAL)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryFurans')
            print(str(e))

    if 'qryInsulationPF' in kwargs:
        try:
            qryInsulationPF = kwargs.get('qryInsulationPF')
            for _, row in qryDGA.iterrows():
                SERIALNUM = row['SERIALNUM']
                SAMPLEDATE = row['TESTDATE']
                AIRTEMP = row['AIRTEMP']
                OILTEMP = row['OILTEMP']
                TEST_KV = row['TEST_KV']
                INSULATION = row['INSULATION']
                PF_MEAS = row['PF_MEAS']
                PF_CORR = row['PF_CORR']
                CAPACITANCE = row['CAPACITANCE']
                ISBASELINE = row['ISBASELINE']

                crsr.execute(
                    """insert into qryInsulationPF(
                        SERIALNUM,
                        TESTDATE,
                        AIRTEMP,
                        OILTEMP,
                        TEST_KV,
                        INSULATION,
                        PF_MEAS,
                        PF_CORR,
                        CAPACITANCE,
                        ISBASELINE)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    SERIALNUM,
                    TESTDATE,
                    AIRTEMP,
                    OILTEMP,
                    TEST_KV,
                    INSULATION,
                    PF_MEAS,
                    PF_CORR,
                    CAPACITANCE,
                    ISBASELINE)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryInsulationPF')
            print(str(e))

    if 'qryLTC' in kwargs:
        try:
            qryLTC = kwargs.get('qryLTC')
            for _, row in qryLTC.iterrows():
                TFMRID = row['TFMRID']
                LTCID = row['LTCID']
                MANUFACTURER = row['MANUFACTURER']
                MODEL = row['MODEL']
                BREATHER = row['BREATHER']

                crsr.execute(
                    """insert into qryLTC(
                        TFMRID,
                        LTCID,
                        MANUFACTURER,
                        MODEL,
                        BREATHER)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    TFMRID,
                    LTCID,
                    MANUFACTURER,
                    MODEL,
                    BREATHER)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryLTC')
            print(str(e))

    if 'qryLTCDGA' in kwargs:
        try:
            qryLTCDGA = kwargs.get('qryLTCDGA')
            for _, row in qryLTCDGA.iterrows():
                TFMRID = row['TFMRID']
                LTCID = row['LTCID']
                SAMPLEDATE = row['SAMPLEDATE']
                COMPARTMENT = row['COMPARTMENT']
                H2 = row['H2']
                CH4 = row['CH4']
                C2H6 = row['C2H6']
                C2H4 = row['C2H4']
                C2H2 = row['C2H2']
                CO = row['CO']
                CO2 = row['CO2']
                O2 = row['O2']
                N2 = row['N2']

                crsr.execute(
                    """insert into qryLTCDGA(
                        TFMRID,
                        LTCID,
                        SAMPLEDATE,
                        COMPARTMENT,
                        H2,
                        CH4,
                        C2H6,
                        C2H4,
                        C2H2,
                        CO,
                        CO2,
                        O2,
                        N2)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    TFMRID,
                    LTCID,
                    SAMPLEDATE,
                    COMPARTMENT,
                    H2,
                    CH4,
                    C2H6,
                    C2H4,
                    C2H2,
                    CO,
                    CO2,
                    O2,
                    N2)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryLTCDGA')
            print(str(e))

    if 'qryLTCOilQuality' in kwargs:
        try:
            qryLTCOilQuality = kwargs.get('qryLTCOilQuality')
            for _, row in qryLTCOilQuality.iterrows():
                TFMRID = row['TFMRID']
                LTCID = row['LTCID']
                SAMPLEDATE = row['SAMPLEDATE']
                COMPARTMENT = row['COMPARTMENT']
                OILTEMP = row['OILTEMP']
                MOISTURE_PPM = row['MOISTURE_PPM']
                ACIDITY = row['ACIDITY']
                IFT = row['IFT']
                COLOR = row['COLOR']
                D877 = row['D877']
                D1816_1MM = row['D1816_1MM']
                D1816_2MM = row['D1816_2MM']
                IEC156 = row['IEC156']
                PF_25C = row['PF_25C']
                PF_100C = row['PF_100C']

                crsr.execute(
                    """insert into qryLTCOilQuality(
                        TFMRID,
                        LTCID,
                        SAMPLEDATE,
                        COMPARTMENT,
                        OILTEMP,
                        MOISTURE_PPM,
                        ACIDITY,
                        IFT,
                        COLOR,
                        D877,
                        D1816_1MM,
                        D1816_2MM,
                        IEC156,
                        PF_25C,
                        PF_100C)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    TFMRID,
                    LTCID,
                    SAMPLEDATE,
                    COMPARTMENT,
                    OILTEMP,
                    MOISTURE_PPM,
                    ACIDITY,
                    IFT,
                    COLOR,
                    D877,
                    D1816_1MM,
                    D1816_2MM,
                    IEC156,
                    PF_25C,
                    PF_100C)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryLTCOilQuality')
            print(str(e))

    if 'qryLTCTapCount' in kwargs:
        try:
            qryLTCTapCount = kwargs.get('qryLTCTapCount')
            for _, row in qryLTCTapCount.iterrows():
                RECORDDATE = row['RECORDDATE']
                TFMRID = row['TFMRID']
                LTCID = row['LTCID']
                COUNTERREADING = row['COUNTERREADING']
                HIGHTAPPOS = row['HIGHTAPPOS']
                LOWTAPPOS = row['LOWTAPPOS']

                crsr.execute(
                    """insert into qryLTCTapCount(
                        RECORDDATE,
                        TFMRID,
                        LTCID,
                        COUNTERREADING,
                        HIGHTAPPOS,
                        LOWTAPPOS)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    RECORDDATE,
                    TFMRID,
                    LTCID,
                    COUNTERREADING,
                    HIGHTAPPOS,
                    LOWTAPPOS)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryLTCTapCount')
            print(str(e))

    if 'qryLTCTapPosition' in kwargs:
        try:
            qryLTCTapPosition = kwargs.get('qryLTCTapPosition')
            for _, row in qryLTCTapPosition.iterrows():
                RECORDDATE = row['RECORDDATE']
                TFMRID = row['TFMRID']
                LTCID = row['LTCID']
                TAPPOSITION = row['TAPPOSITION']

                crsr.execute(
                    """insert into qryLTCTapPosition(
                        RECORDDATE,
                        TFMRID,
                        LTCID,
                        TAPPOSITION)
                        values(?,
                            ?,
                            ?,
                            ?)""",
                    RECORDDATE,
                    TFMRID,
                    LTCID,
                    TAPPOSITION)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryLTCTapPosition')
            print(str(e))

    if 'qryOilQuality' in kwargs:
        try:
            qryOilQuality = kwargs.get('qryOilQuality')
            for _, row in qryOilQuality.iterrows():
                SERIALNUM = row['SERIALNUM']
                SAMPLEDATE = row['SAMPLEDATE']
                OILTEMP = row['OILTEMP']
                MOISTURE_PPM = row['MOISTURE_PPM']
                ACIDITY = row['ACIDITY']
                IFT = row['IFT']
                COLOR = row['COLOR']
                D877 = row['D877']
                D1816_1MM = row['D1816_1MM']
                D1816_2MM = row['D1816_2MM']
                IEC156 = row['IEC156']
                PF_25C = row['PF_25C']
                PF_100C = row['PF_100C']

                crsr.execute(
                    """insert into qryOilQuality(
                        SERIALNUM,
                        SAMPLEDATE,
                        OILTEMP,
                        MOISTURE_PPM,
                        ACIDITY,
                        IFT,
                        COLOR,
                        D877,
                        D1816_1MM,
                        D1816_2MM,
                        IEC156,
                        PF_25C,
                        PF_100C)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    SERIALNUM,
                    SAMPLEDATE,
                    OILTEMP,
                    MOISTURE_PPM,
                    ACIDITY,
                    IFT,
                    COLOR,
                    D877,
                    D1816_1MM,
                    D1816_2MM,
                    IEC156,
                    PF_25C,
                    PF_100C)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryOilQuality')
            print(str(e))

    if 'qryTfmrs' in kwargs:
        try:
            qryTfmrs = kwargs.get('qryTfmrs')
            for _, row in qryTfmrs.iterrows():
                SERIALNUM = row['SERIALNUM']
                MANUFACTURER = row['MANUFACTURER']
                MANUFACTUREDATE = row['MANUFACTUREDATE']
                ENERGIZEDATE = row['ENERGIZEDATE']
                REPAIRDATE = row['REPAIRDATE']
                RETIREDATE = row['RETIREDATE']
                UTILITY = row['UTILITY']
                REGION = row['REGION']
                STATION = row['STATION']
                DESIGNATION = row['DESIGNATION']
                CORETYPE = row['CORETYPE']
                TOPMVA = row['TOPMVA']
                COOLINGTYPE = row['COOLINGTYPE']
                HV_kV = row['HV_kV']
                LV1_kV = row['LV1_kV']
                LV2_kV = row['LV2_kV']
                TV_kV = row['TV_kV']
                NUMPHASES = row['NUMPHASES']
                ISAUTO = row['ISAUTO']
                CRITICALITY = row['CRITICALITY']

                crsr.execute(
                    """insert into qryTfmrs(
                        SERIALNUM,
                        MANUFACTURER,
                        MANUFACTUREDATE,
                        ENERGIZEDATE,
                        REPAIRDATE,
                        RETIREDATE,
                        UTILITY,
                        REGION,
                        STATION,
                        DESIGNATION,
                        CORETYPE,
                        TOPMVA,
                        COOLINGTYPE,
                        HV_kV,
                        LV1_kV,
                        LV2_kV,
                        TV_kV,
                        NUMPHASES,
                        ISAUTO,
                        CRITICALITY)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    SERIALNUM,
                    MANUFACTURER,
                    MANUFACTUREDATE,
                    ENERGIZEDATE,
                    REPAIRDATE,
                    RETIREDATE,
                    UTILITY,
                    REGION,
                    STATION,
                    DESIGNATION,
                    CORETYPE,
                    TOPMVA,
                    COOLINGTYPE,
                    HV_kV,
                    LV1_kV,
                    LV2_kV,
                    TV_kV,
                    NUMPHASES,
                    ISAUTO,
                    CRITICALITY)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to qryTfmrs')
            print(str(e))

    if 'tblComments' in kwargs:
        try:
            tblComments = kwargs.get('tblComments')
            for _, row in tblComments.iterrows():
                COMPONENTID = row['COMPONENTID']
                COMMENTDATE = row['COMMENTDATE']
                COMMENTTEXT = row['COMMENTTEXT']

                crsr.execute(
                    """insert into tblComments(
                        COMPONENTID,
                        COMMENTDATE,
                        COMMENTTEXT)
                        values(?,
                            ?,
                            ?)""",
                    COMPONENTID,
                    COMMENTDATE,
                    COMMENTTEXT)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to tblComments')
            print(str(e))

    if 'tblOptions' in kwargs:
        try:
            tblOptions = kwargs.get('tblOptions')
            for _, row in tblOptions.iterrows():
                OptionKey = row['OptionKey']
                OptionValue = row['OptionValue']

                crsr.execute(
                    """insert into tblOptions(
                        OptionKey,
                        OptionValue)
                        values(?,
                        ?)""",
                    OptionKey,
                    OptionValue)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to tblOptions')
            print(str(e))

    if 'tblResultDetails' in kwargs:
        try:
            tblResultDetails = kwargs.get('tblResultDetails')
            for _, row in tblResultDetails.iterrows():
                RUNDATETIME = row['RUNDATETIME']
                DIAGNOSISDATE = row['DIAGNOSISDATE']
                SERIALNUM = row['SERIALNUM']
                RESULTVALIDDATE = row['RESULTVALIDDATE']
                FAILUREMECHANISM = row['FAILUREMECHANISM']
                BELIEF = row['BELIEF']

                crsr.execute(
                    """insert into tblResultDetails(
                        RUNDATETIME,
                        DIAGNOSISDATE,
                        SERIALNUM,
                        RESULTVALIDDATE,
                        FAILUREMECHANISM,
                        BELIEF)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    RUNDATETIME,
                    DIAGNOSISDATE,
                    SERIALNUM,
                    RESULTVALIDDATE,
                    FAILUREMECHANISM,
                    BELIEF)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to tblResultDetails')
            print(str(e))

    if 'tblResults' in kwargs:
        try:
            tblResults = kwargs.get('tblResults')
            for _, row in tblResults.iterrows():
                SERIALNUM = row['SERIALNUM']
                RUNDATETIME = row['RUNDATETIME']
                DIAGNOSISDATE = row['DIAGNOSISDATE']
                RESULTVALIDDATE = row['RESULTVALIDDATE']
                NORMALDEGRADATION = row['NORMALDEGRADATION']
                ABNORMALTHERMAL = row['ABNORMALTHERMAL']
                ABNORMALELECTRICAL = row['ABNORMALELECTRICAL']
                ABNORMALCORE = row['ABNORMALCORE']
                ABNORMALCONDITION = row['ABNORMALCONDITION']
                OILQUALITY = row['OILQUALITY']
                BUSHINGCONDITION = row['BUSHINGCONDITION']
                LTCCONDITION = row['LTCCONDITION']
                ABNORMALCONDITIONCODE = row['ABNORMALCONDITIONCODE']
                ABNORMALTHERMALCODE = row['ABNORMALTHERMALCODE']
                ABNORMALELECTRICALCODE = row['ABNORMALELECTRICALCODE']
                ABNORMALCORECODE = row['ABNORMALCORECODE']

                crsr.execute(
                    """insert into tblResults(
                        SERIALNUM,
                        RUNDATETIME,
                        DIAGNOSISDATE,
                        RESULTVALIDDATE,
                        NORMALDEGRADATION,
                        ABNORMALTHERMAL,
                        ABNORMALELECTRICAL,
                        ABNORMALCORE,
                        ABNORMALCONDITION,
                        OILQUALITY,
                        BUSHINGCONDITION,
                        LTCCONDITION,
                        ABNORMALCONDITIONCODE,
                        ABNORMALTHERMALCODE,
                        ABNORMALELECTRICALCODE,
                        ABNORMALCORECODE)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    SERIALNUM,
                    RUNDATETIME,
                    DIAGNOSISDATE,
                    RESULTVALIDDATE,
                    NORMALDEGRADATION,
                    ABNORMALTHERMAL,
                    ABNORMALELECTRICAL,
                    ABNORMALCORE,
                    ABNORMALCONDITION,
                    OILQUALITY,
                    BUSHINGCONDITION,
                    LTCCONDITION,
                    ABNORMALCONDITIONCODE,
                    ABNORMALTHERMALCODE,
                    ABNORMALELECTRICALCODE,
                    ABNORMALCORECODE)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to tblResults')
            print(str(e))

    if 'tblResultsOverTime' in kwargs:
        try:
            tblResultsOverTime = kwargs.get('tblResultsOverTime')
            for _, row in tblResultsOverTime.iterrows():
                SERIALNUM = row['SERIALNUM']
                RUNDATETIME = row['RUNDATETIME']
                RESULTDATETIME = row['RESULTDATETIME']
                NORMALDEGRADATION = row['NORMALDEGRADATION']
                ABNORMALTHERMAL = row['ABNORMALTHERMAL']
                ABNORMALELECTRICAL = row['ABNORMALELECTRICAL']
                ABNORMALCORE = row['ABNORMALCORE']
                OILQUALITY = row['OILQUALITY']
                BUSHINGCONDITION = row['BUSHINGCONDITION']
                LTCCONDITION = row['LTCCONDITION']

                crsr.execute(
                    """insert into tblResultsOverTime(
                        SERIALNUM,
                        RUNDATETIME,
                        RESULTDATETIME,
                        NORMALDEGRADATION,
                        ABNORMALTHERMAL,
                        ABNORMALELECTRICAL,
                        ABNORMALCORE,
                        OILQUALITY,
                        BUSHINGCONDITION,
                        LTCCONDITION)
                        values(?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?,
                            ?)""",
                    SERIALNUM,
                    RUNDATETIME,
                    RESULTDATETIME,
                    NORMALDEGRADATION,
                    ABNORMALTHERMAL,
                    ABNORMALELECTRICAL,
                    ABNORMALCORE,
                    OILQUALITY,
                    BUSHINGCONDITION,
                    LTCCONDITION)
                cnxn.commit()
        except Exception as e:
            print('write_to_ptx_accdb_tbls failed writing to tblResultsOverTime')
            print(str(e))

    cnxn.close()


def create_ptx_accdb(filename):
    '''BROKEN! Error with win32client
    Creates an Access db

    This function creates a blank Access database with the latest PTX schema.
    
    Args:
        filename (kwarg) (string): Access db filename
    '''
    try:
        folder = os.getcwd()
        dbpath = folder + '\\' + filename

        accApp = Dispatch("Access.Application")
        dbEngine = accApp.DBEngine
        workspace = dbEngine.Workspaces(0)

        dbLangGeneral = ';LANGID=0x0409;CP=1252;COUNTRY=0'
        newdb = workspace.CreateDatabase(dbpath, dbLangGeneral, 64)

        qryBushingPowerFactor_sql = ("""CREATE TABLE qryBushingPowerFactor(
                      TESTDATE date,
                      BUSHINGID varchar(255),
                      TEMPERATURE double,
                      TESTVOLTAGE double,
                      MEASUREDC1PF double,
                      MEASUREDC1CAP double,
                      MEASUREDC2PF double,
                      MEASUREDC2CAP double
                      ); """)

        qryDGA_sql = ("""CREATE TABLE qryDGA(
                      SERIALNUM varchar(255),
                      SAMPLEDATE date,
                      H2 double,
                      CH4 double,
                      C2H6 double,
                      C2H4 double,
                      C2H2 double,
                      CO double,
                      CO2 double,
                      O2 double,
                      N2 double,
                      BadSample bit
                      ); """)

        qryFurans_sql = ("""CREATE TABLE qryFurans(
                    SERIALNUM varchar(255),
                    SAMPLEDATE date,
                    2FAL double
                    ); """)

        qryInsulationPF_sql = ("""CREATE TABLE qryInsulationPF(
                               SERIALNUM varchar(255),
                               TESTDATE date,
                               AIRTEMP double,
                               OILTEMP double,
                               TEST_KV double,
                               INSULATION varchar(255),
                               PF_MEAS double,
                               PF_CORR double,
                               CAPACITANCE double,
                               ISBASELINE bit
                               ); """)
        qryLTC_sql = ("""CREATE TABLE qryLTC(
                    TFMRID varchar(255),
                    LTCID varchar(255),
                    MANUFACTURER varchar(255),
                    MODEL varchar(255),
                    BREATHER varchar(255)
                    ); """)

        qryLTCDGA_sql = ("""CREATE TABLE qryLTCDGA(
               TFMRID varchar(255),
               LTCID varchar(255),
               SAMPLEDATE date,
               COMPARTMENT varchar(255),
               H2 double,
               CH4 double,
               C2H6 double,
               C2H4 double,
               C2H2 double,
               CO double,
               CO2 double,
               O2 double,
               N2 double
               ); """)

        qryLTCOilQuality_sql = ("""CREATE TABLE qryLTCOilQuality(
               TFMRID varchar(255),
               LTCID varchar(255),
               SAMPLEDATE date,
               COMPARTMENT varchar(255),
               OILTEMP double,
               MOISTURE_PPM double,
               ACIDITY double,
               IFT double,
               COLOR double,
               D877 double,
               D1816_1MM double,
               D1816_2MM double,
               IEC156 double,
               PF_25C double,
               PF_100C double
               ); """)

        qryLTCTapCount_sql = ("""CREATE TABLE qryLTCTapCount(
               RECORDDATE date,
               TFMRID varchar(255),
               LTCID varchar(255),
               COUNTERREADING double,
               HIGHTAPPOS varchar(255),
               LOWTAPPOS varchar(255)
               ); """)

        qryLTCTapPosition_sql = ("""CREATE TABLE qryLTCTapPosition(
               RECORDDATE date,
               TFMRID varchar(255),
               LTCID varchar(255),
               TAPPOSITION varchar(255)
               ); """)

        qryOilQuality_sql = ("""CREATE TABLE qryOilQuality(
                     SERIALNUM varchar(255),
                     SAMPLEDATE date,
                     OILTEMP double,
                     MOISTURE_PPM double,
                     ACIDITY double,
                     IFT double,
                     COLOR double,
                     D877 double,
                     D1816_1MM double,
                     D1816_2MM double,
                     IEC156 double,
                     PF_25C double,
                     PF_100C double
                     ); """)
        qryTfmrs_sql = ("""CREATE TABLE qryTfmrs(
               SERIALNUM varchar(255),
               MANUFACTURER varchar(255),
               MANUFACTUREDATE date,
               ENERGIZEDATE date,
               REPAIRDATE date,
               RETIREDATE date,
               UTILITY varchar(255),
               REGION varchar(255),
               STATION varchar(255),
               DESIGNATION varchar(255),
               CORETYPE varchar(255),
               TOPMVA double,
               COOLINGTYPE varchar(255),
               HV_kV double,
               LV1_kV double,
               LV2_kV double,
               TV_kV double,
               NUMPHASES int,
               ISAUTO bit,
               CRITICALITY double
               ); """)

        tblComments_sql = ("""CREATE TABLE tblComments(
               COMPONENTID varchar(255),
               COMMENTDATE date,
               COMMENTTEXT varchar(255)
               ); """)

        tblOptions_sql = ("""CREATE TABLE tblOptions(
               OptionKey varchar(255),
               OptionValue varchar(255)
               ); """)

        tblResultDetails_sql = ("""CREATE TABLE tblResultDetails(
               RUNDATETIME date,
               DIAGNOSISDATE date,
               SERIALNUM varchar(255),
               RESULTVALIDDATE date,
               FAILUREMECHANISM varchar(255),
               BELIEF varchar(255)
               ); """)

        tblResults_sql = ("""CREATE TABLE tblResults(
               SERIALNUM varchar(255),
               RUNDATETIME date,
               DIAGNOSISDATE date,
               RESULTVALIDDATE date,
               NORMALDEGRADATION double,
               ABNORMALTHERMAL double,
               ABNORMALELECTRICAL double,
               ABNORMALCORE double,
               ABNORMALCONDITION double,
               OILQUALITY double,
               BUSHINGCONDITION double,
               LTCCONDITION double,
               ABNORMALCONDITIONCODE int,
               ABNORMALTHERMALCODE int,
               ABNORMALELECTRICALCODE int,
               ABNORMALCORECODE int
               ); """)

        tblResultsOverTime_sql = ("""CREATE TABLE tblResultsOverTime(
               SERIALNUM varchar(255),
               RUNDATETIME date,
               DIAGNOSISDATE date,
               RESULTVALIDDATE date,
               NORMALDEGRADATION double,
               ABNORMALTHERMAL double,
               ABNORMALELECTRICAL double,
               ABNORMALCORE double,
               ABNORMALCONDITION double,
               OILQUALITY double,
               BUSHINGCONDITION double,
               LTCCONDITION double
               );""")

        statement_list = [qryBushingPowerFactor_sql,
                          qryDGA_sql,
                          qryFurans_sql,
                          qryInsulationPF_sql,
                          qryLTC_sql,
                          qryLTCDGA_sql,
                          qryLTCOilQuality_sql,
                          qryLTCTapCount_sql,
                          qryLTCTapPosition_sql,
                          qryOilQuality_sql,
                          qryTfmrs_sql,
                          tblComments_sql,
                          tblOptions_sql,
                          tblResultDetails_sql,
                          tblResults_sql,
                          tblResultsOverTime_sql,
                          ]
        for statement in statement_list:
            try:
                newdb.Execute(statement)
            except Exception as e:
                print('Failed writing ' + str(statement))

    except Exception as e:
        print('Db creation failed in create_ptx_accdb')
        print(str(e))
        accApp.DoCmd.CloseDatabase
        accApp.Quit
        newdb = None
        workspace = None
        dbEngine = None
        accApp = None
        print('Closing connection')

    finally:
        try:
            accApp.DoCmd.CloseDatabase
            accApp.Quit
            newdb = None
            workspace = None
            dbEngine = None
            accApp = None
        except Exception as e:
            print('Connection already closed\n' + str(e))
