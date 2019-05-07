"""
tfmr.validation
===============================================================
tfmr sub-module previously used for validating the software using schema_0 tables
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.tree import export_graphviz
from graphviz import render, Source
from sklearn.metrics import classification_report

def failure_check(tblResults):
    """
    This function checks for a column 'F' in a ptx tblResults df.

    If no 'F' in the df it creates one by looping through the df looking 
    for the string '_F' in the 'SERIALNUM' column.

    If there is an '_F', a 1 is appended to a list, else a 0.
    This list is then appended to the tblResults df.
    """
    tblResults = tblResults[:]
    if 'F' in tblResults.columns:
        print('Failure Check Passed! | A column indicating failure or non-failure status is present in dataset.\n')
        print('There are ' + str(sum(i == 1 for i in tblResults.F)) +
              " failures present dataset.")
        print('There are ' + str(sum(i == 0 for i in tblResults.F)) +
              " non-failures present dataset.\n")
    else:
        print('Failure Check Failed! | A column indicating failure or non-failure status is not initially present in dataset.\n')
        F_NF = []

        for sn in tblResults.itertuples():
            SERIALNUM = getattr(sn, 'SERIALNUM')

            if '_F' in SERIALNUM:
                F_NF.append(1)
            else:
                F_NF.append(0)
        print('Failure column, "F" successfully added to data frame.\n')
        # print('Failure Check (Second Run) Passed! | A column indicating failure or non-failure status is now present in dataset.\n')
        print('There are ' + str(sum(i == 1 for i in F_NF)) +
              " failures present dataset.")
        print('There are ' + str(sum(i == 0 for i in F_NF)) +
              " non-failures present dataset.\n")
        tblResults['F'] = F_NF
    return tblResults


def dupe_check(tblResults):
    """
    This function groups a tblResults df by SN and gets the count of SERIALNUM occurrence.

    If an SN count is > 1 it prints that the check has failed.

    It then copies a notnull version of a dga df and the tblResults df. This needs to be changed!
    """
    tblResults = tblResults[:]
    dupes = tblResults.groupby('SERIALNUM').SERIALNUM.count()
    for sn in dupes:
        if sn > 1:
            print('Dupe Check Failed! | There are duplicate SNs in this dataset.\n')
            # Removing null SNs
            # dga = dga[dga['SERIALNUM'].notnull()]
            tblResults = tblResults[tblResults['SERIALNUM'].notnull()]

            print(
                'Dupe Check (Second Run) Passed! | There are no duplicate SNs in this dataset.\n')

    print('Dupe Check Passed! | There are no duplicate SNs in this dataset.\n')
    return tblResults


def gas_check(dga):
    """
    This function checks for set ['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2',
            'O2', 'N2'] in a dga df.

    If any gas not present a failure text is printed.
    """
    if set(['H2',
            'CH4',
            'C2H6',
            'C2H4',
            'C2H2',
            'CO',
            'CO2',
            'O2',
            'N2']).issubset(dga.columns):
        print('Gas Check Passed! | All DGA gases necessary to compute DGA diagnostic results are present in dataset.\n')
    else:
        print('Gas Check Failed! | Not all DGA gases necessary to compute DGA diagnostic results are present in this dataset.\n')


def ptx_check(tblResults):
    """
    This function checks for set ['ABNORMALTHERMAL', 'ABNORMALELECTRICAL',
    'ABNORMALCORE'] in a dga df.

    If any gas not present a failure text is printed.
    """
    if set(['ABNORMALTHERMAL',
            'ABNORMALELECTRICAL',
            'ABNORMALCORE']).issubset(tblResults.columns):
        print('PTX Check Passed! | All PTX index values are present in dataset.')
    else:
        print('PTX Check Failed! | Not all PTX index values are present in dataset. PTX cannot be evaluated until AT, AE, and AC present.')


def get_ratios_medians(dga):
    """
    This function takes a dga dataframe and computes two columns: 
     - N2_O2_RATIO
     - C2H6_CH4_RATIO
     - C2H4_C2H2_RATIO
     - CO2_CO_RATIO
     - O2_N2_RATIO

     - N2_O2_MEDIAN
     - C2H6_CH4_MEDIAN
     - C2H4_C2H2_MEDIAN
     - CO2_CO_MEDIAN
     - O2_N2_MEDIAN

    If there are NaN values present in the N2_O2_RATIO column they are filled with 1's.

    The median of these ratios is calculated for each serial number be grouping the column by SN and using transform
    """
    dga = dga[:]
    # Creating N2/O2 column in dga
    dga['N2_O2_RATIO'] = dga.N2/dga.O2
    dga['C2H6_CH4_RATIO'] = dga.C2H6/dga.CH4
    dga['C2H4_C2H2_RATIO'] = dga.C2H4/dga.C2H2
    dga['CO2_CO_RATIO'] = dga.CO2/dga.CO
    dga['O2_N2_RATIO'] = dga.O2/dga.N2

    # Fill Nan N2/O2 values with 1
    dga['N2_O2_RATIO'] = dga['N2_O2_RATIO'].fillna(1)
    dga['C2H6_CH4_RATIO'] = dga['C2H6_CH4_RATIO'].fillna(1)
    dga['C2H4_C2H2_RATIO'] = dga['C2H4_C2H2_RATIO'].fillna(1)
    dga['CO2_CO_RATIO'] = dga['CO2_CO_RATIO'].fillna(1)
    dga['O2_N2_RATIO'] = dga['O2_N2_RATIO'].fillna(1)

    # # Get median N2/O2
    dga['N2_O2_MEDIAN'] = dga.groupby(
        'SERIALNUM')['N2_O2_RATIO'].transform('median')
    dga['C2H6_CH4_MEDIAN'] = dga.groupby(
        'SERIALNUM')['C2H6_CH4_RATIO'].transform('median')
    dga['C2H4_C2H2_MEDIAN'] = dga.groupby(
        'SERIALNUM')['C2H4_C2H2_RATIO'].transform('median')
    dga['CO2_CO_MEDIAN'] = dga.groupby(
        'SERIALNUM')['CO2_CO_RATIO'].transform('median')
    dga['O2_N2_MEDIAN'] = dga.groupby(
        'SERIALNUM')['O2_N2_RATIO'].transform('median')

    return dga


def rand_forest(train_data, test_data):
    """
     - this function takes a training and a test set where the sets are gases and failure flag (currently; needs to be more general for new ideas (trends etc))

     - it makes the classifier, runs the fit, generates predictions, and a confisuon matrix to get the tp, fp, tn, fn values. Outputs these as a table
    """
    cols = ['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'F']
    train_subset = train_data[cols]
    train_X = train_subset[['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2']]
    train_y = train_subset[['F']]

    test_subset = test_data[cols]
    test_X = test_subset[['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2']]
    test_y = test_subset[['F']]

    dga_clf = RandomForestClassifier(
        max_depth=None, random_state=0,
        oob_score=True, n_jobs=-1)
    dga_clf.fit(train_X, np.ravel(train_y))

    predictions = dga_clf.predict(test_X)

    confusion_mat = pd.crosstab(index=np.ravel(test_y), columns=predictions,
                                rownames=['actual'], colnames=['preds'])

    tp = confusion_mat[1][1]
    fp = confusion_mat[1][0]
    tn = confusion_mat[0][0]
    fn = confusion_mat[0][1]
    performance = {'DIAG_METHOD': 'SKL Rand Forest', 'TN_COUNT': [
        tn], 'FP_COUNT': [fp], 'TP_COUNT': [tp], 'FN_COUNT': [fn]}
    rand_forest_performance = pd.DataFrame(data=performance)
    return rand_forest_performance


def ptx_rules(tblResults):
    """
    this function calculates True and False for each sample based on PTX rules past and present
    """
    PTX_MAX_0_5 = []
    PTX_CURRENT = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        AT = getattr(sn, 'ABNORMALTHERMAL')
        AE = getattr(sn, 'ABNORMALELECTRICAL')
        AC = getattr(sn, 'ABNORMALCORE')

        if (AT >= 0.5 or AE >= 0.5 or AC >= 0.5):
            PTX_MAX_0_5.append('TRUE')
        else:
            PTX_MAX_0_5.append('FALSE')

        if (AT >= 0.7 or AE >= 0.5 or AC >= 0.8):
            PTX_CURRENT.append('TRUE')
        else:
            PTX_CURRENT.append('FALSE')

    print('There are ' + str(sum(i == 'TRUE' for i in PTX_MAX_0_5)) +
          " TRUE values for PTX MAX(AT, AE, AT) rule")
    tblResults['PTX_MAX_0_5'] = PTX_MAX_0_5

    print('There are ' + str(sum(i == 'TRUE' for i in PTX_CURRENT)) +
          " TRUE values for PTX OR(AT > 0.7, AE > 0.5, AT > 0.8) rule")
    tblResults['PTX_CURRENT'] = PTX_CURRENT
    return tblResults


def ieee_rules(tblResults):
    """
    this function calculates 1, 2, 3, or 4 for each sample based on IEEE OLD rules
    """
    score = 0
    IEEE = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        H2 = getattr(sn, 'H2')
        CH4 = getattr(sn, 'CH4')
        C2H6 = getattr(sn, 'C2H6')
        C2H4 = getattr(sn, 'C2H4')
        C2H2 = getattr(sn, 'C2H2')
        CO = getattr(sn, 'CO')
        CO2 = getattr(sn, 'CO2')
        sum_gases = [H2, CH4, C2H6, C2H2, CO]
        if (H2 > 1800 or CH4 > 1000 or C2H6 > 150 or C2H4 > 200 or C2H2 > 35
                or CO > 1400 or CO2 > 10000 or sum(sum_gases) > 4630):
            score = 4
            IEEE.append(score)
        elif (H2 > 700 or CH4 > 400 or C2H6 > 100 or C2H4 > 100 or C2H2 > 9
              or CO > 570 or CO2 > 4000 or sum(sum_gases) > 1920):
            score = 3
            IEEE.append(score)
        elif (H2 > 100 or CH4 > 120 or C2H6 > 65 or C2H4 > 50 or C2H2 > 1
              or CO > 350 or CO2 > 2500 or sum(sum_gases) > 720):
            score = 2
            IEEE.append(score)
        else:
            score = 1
            IEEE.append(score)
    print('There are ' + str(sum(i > 2 for i in IEEE)) +
          " SNs with score > 2 for IEEE rules")
    tblResults['IEEE'] = IEEE
    return tblResults


def duval_cat3_rules(tblResults):
    """
    this function calculates True or False for each sample using the Duval Category 3 rules
    """
    DUVAL_CAT_3 = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        H2 = getattr(sn, 'H2')
        CH4 = getattr(sn, 'CH4')
        C2H6 = getattr(sn, 'C2H6')
        C2H4 = getattr(sn, 'C2H4')
        C2H2 = getattr(sn, 'C2H2')
        CO = getattr(sn, 'CO')
        CO2 = getattr(sn, 'CO2')
        if (H2 > 237 or CH4 > 158 or C2H6 > 201 or C2H4 > 212 or C2H2 > 29 or
                CO > 1245 or CO2 > 16294):
            DUVAL_CAT_3.append('TRUE')
        else:
            DUVAL_CAT_3.append('FALSE')
    print('There are ' + str(sum(i == 'TRUE' for i in DUVAL_CAT_3)) +
          " TRUE values for Duval Cat 3 rules")
    tblResults['DUVAL_CAT_3'] = DUVAL_CAT_3
    return tblResults


def duval_prefail_rules(tblResults):
    """
    this function calculates True or False for each sample using the Duval Prefailure rules
    """
    DUVAL_PREFAIL = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        H2 = getattr(sn, 'H2')
        CH4 = getattr(sn, 'CH4')
        C2H6 = getattr(sn, 'C2H6')
        C2H4 = getattr(sn, 'C2H4')
        C2H2 = getattr(sn, 'C2H2')
        CO = getattr(sn, 'CO')
        CO2 = getattr(sn, 'CO2')
        if (H2 > 725 or CH4 > 400 or C2H6 > 900 or C2H4 > 800 or C2H2 > 450 or
                CO > 2100 or CO2 > 50000):
            DUVAL_PREFAIL.append('TRUE')
        else:
            DUVAL_PREFAIL.append('FALSE')
    print('There are ' + str(sum(i == 'TRUE' for i in DUVAL_PREFAIL)) +
          " TRUE values for Duval Pre-failure rules")
    tblResults['DUVAL_PREFAIL'] = DUVAL_PREFAIL
    return tblResults


def ninetieth_pct_rules(tblResults):
    """
    this function calculates True or False for each sample using the 90th pct rules
    """
    NINETIETH_PCT = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        H2 = getattr(sn, 'H2')
        CH4 = getattr(sn, 'CH4')
        C2H6 = getattr(sn, 'C2H6')
        C2H4 = getattr(sn, 'C2H4')
        C2H2 = getattr(sn, 'C2H2')
        CO = getattr(sn, 'CO')
        CO2 = getattr(sn, 'CO2')
        if (H2 > 36 or CH4 > 65 or C2H6 > 73 or C2H4 > 34 or C2H2 > 2 or
                CO > 216 or CO2 > 4788.6):
            NINETIETH_PCT.append('TRUE')
        else:
            NINETIETH_PCT.append('FALSE')
    print('There are ' + str(sum(i == 'TRUE' for i in NINETIETH_PCT)) +
          " TRUE values for Ninetieth Pct rules")
    tblResults['NINETIETH_PCT'] = NINETIETH_PCT
    return tblResults


def iec60599_low_rules(tblResults):
    """
    this function calculates True or False for each sample using the IEC60599 low rules
    """
    IEC60599_LOW = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        H2 = getattr(sn, 'H2')
        CH4 = getattr(sn, 'CH4')
        C2H6 = getattr(sn, 'C2H6')
        C2H4 = getattr(sn, 'C2H4')
        C2H2 = getattr(sn, 'C2H2')
        CO = getattr(sn, 'CO')
        CO2 = getattr(sn, 'CO2')
        if (H2 > 50 or CH4 > 30 or C2H6 > 20 or C2H4 > 60 or C2H2 > 2 or
                CO > 400 or CO2 > 3800):
            IEC60599_LOW.append('TRUE')
        else:
            IEC60599_LOW.append('FALSE')
    print('There are ' + str(sum(i == 'TRUE' for i in IEC60599_LOW)) +
          " TRUE values for IEC60599 low-range rules")
    tblResults['IEC60599_LOW'] = IEC60599_LOW
    return tblResults


def iec60599_high_rules(tblResults):
    """
    this function calculates True or False for each sample using the IEC60599 high rules
    """
    IEC60599_HIGH = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        H2 = getattr(sn, 'H2')
        CH4 = getattr(sn, 'CH4')
        C2H6 = getattr(sn, 'C2H6')
        C2H4 = getattr(sn, 'C2H4')
        C2H2 = getattr(sn, 'C2H2')
        CO = getattr(sn, 'CO')
        CO2 = getattr(sn, 'CO2')
        if (H2 > 150 or CH4 > 130 or C2H6 > 90 or C2H4 > 280 or C2H2 > 20 or
                CO > 600 or CO2 > 14000):
            IEC60599_HIGH.append('TRUE')
        else:
            IEC60599_HIGH.append('FALSE')
    print('There are ' + str(sum(i == 'TRUE' for i in IEC60599_HIGH)) +
          " TRUE values for IEC60599 high-range rules")
    tblResults['IEC60599_HIGH'] = IEC60599_HIGH
    return tblResults

# 2018-11-14: runs but still too slow


def nei_rules(tblResults):
    """
    this function calculates NEI, NEI Score, NEI Alt Score, CH4 Score,
    C2H6 Score, C2H4 Score, C2H2 Score and HC Score for each sample using
    the NEI rules
    """
    NEI_VAL = []
    NEI_SCORE = []
    NEI_ALT_SCORE = []
    CH4_SCORE = []
    C2H6_SCORE = []
    C2H4_SCORE = []
    C2H2_SCORE = []
    HC_SCORE = []
    tblResults = tblResults[:]
    for sn in tblResults.itertuples():
        CH4 = getattr(sn, 'CH4')
        C2H6 = getattr(sn, 'C2H6')
        C2H4 = getattr(sn, 'C2H4')
        C2H2 = getattr(sn, 'C2H2')
        N2_O2_MEDIAN = getattr(sn, 'N2_O2_MEDIAN')

        NEI = (((77.7 * CH4) + (93.5 * C2H6) + (104.1 * C2H4) + (278.3 * C2H2))
               / 22400)
        NEI_VAL.append(NEI)

        if (N2_O2_MEDIAN < 0.54):
            # NEI Score High O2 thresholds
            L1 = 0.39
            L2 = 0.72
            L3 = 1.98

            # NEI Alt Score High O2 thresholds
            ALT_L1 = 0.2
            ALT_L2 = 0.39
            ALT_L3 = 0.72

            # CH4 Score High O2 thresholds
            CH4_L1 = 18
            CH4_L2 = 37
            CH4_L3 = 102

            # C2H6 Score High O2 thresholds
            C2H6_L1 = 24
            C2H6_L2 = 56
            C2H6_L3 = 146

            # C2H4 Score High O2 thresholds
            C2H4_L1 = 43
            C2H4_L2 = 78
            C2H4_L3 = 179

            # C2H2 Score High O2 thresholds
            C2H2_L1 = 2
            C2H2_L2 = 10
            C2H2_L3 = 36

            if NEI >= L3:
                NEI_SCORE.append(4)
            elif (NEI >= L2 and NEI < L3):
                NEI_SCORE.append((3 + (NEI - L2))/(L3 - L2))
            elif (NEI >= L1 and NEI < L2):
                NEI_SCORE.append((2 + (NEI - L1))/(L2 - L1))
            elif (NEI < L1):
                NEI_SCORE.append((1 + NEI)/L1)
            else:
                NEI_SCORE.append(0)
                print('NEI Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= ALT_L3:
                NEI_ALT_SCORE.append(4)
            elif (NEI >= ALT_L2 and NEI < ALT_L3):
                NEI_ALT_SCORE.append((3 + (NEI - ALT_L2))/(ALT_L3 - ALT_L2))
            elif (NEI >= ALT_L1 and NEI < ALT_L2):
                NEI_ALT_SCORE.append((2 + (NEI - ALT_L1))/(ALT_L2 - ALT_L1))
            elif (NEI < ALT_L1):
                NEI_ALT_SCORE.append((1 + NEI)/ALT_L1)
            else:
                NEI_ALT_SCORE.append(0)
                print('NEI Alt Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= CH4_L3:
                ch4_num = 4
                CH4_SCORE.append(ch4_num)
            elif (NEI >= CH4_L2 and NEI < CH4_L3):
                ch4_num = (3 + (NEI - CH4_L2))/(CH4_L3 - CH4_L2)
                CH4_SCORE.append(ch4_num)
            elif (NEI >= CH4_L1 and NEI < CH4_L2):
                ch4_num = (2 + (NEI - CH4_L1))/(CH4_L2 - CH4_L1)
                CH4_SCORE.append(ch4_num)
            elif (NEI < CH4_L1):
                ch4_num = (1 + NEI)/CH4_L1
                CH4_SCORE.append(ch4_num)
            else:
                ch4_num = 0
                CH4_SCORE.append(ch4_num)
                print('CH4 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= C2H6_L3:
                c2h6_num = 4
                C2H6_SCORE.append(c2h6_num)
            elif (NEI >= C2H6_L2 and NEI < C2H6_L3):
                c2h6_num = (3 + (NEI - C2H6_L2))/(C2H6_L3 - C2H6_L2)
                C2H6_SCORE.append(c2h6_num)
            elif (NEI >= C2H6_L1 and NEI < C2H6_L2):
                c2h6_num = (2 + (NEI - C2H6_L1))/(C2H6_L2 - C2H6_L1)
                C2H6_SCORE.append(c2h6_num)
            elif (NEI < C2H6_L1):
                c2h6_num = (1 + NEI)/C2H6_L1
                C2H6_SCORE.append(c2h6_num)
            else:
                c2h6_num = 0
                C2H6_SCORE.append(c2h6_num)
                print('C2H6 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= C2H4_L3:
                c2h4_num = 4
                C2H4_SCORE.append(c2h4_num)
            elif (NEI >= C2H4_L2 and NEI < C2H4_L3):
                c2h4_num = (3 + (NEI - C2H4_L2))/(C2H4_L3 - C2H4_L2)
                C2H4_SCORE.append(c2h4_num)
            elif (NEI >= C2H4_L1 and NEI < C2H4_L2):
                c2h4_num = (2 + (NEI - C2H4_L1))/(C2H4_L2 - C2H4_L1)
                C2H4_SCORE.append(c2h4_num)
            elif (NEI < C2H4_L1):
                c2h4_num = (1 + NEI)/C2H4_L1
                C2H4_SCORE.append(c2h4_num)
            else:
                c2h4_num = 0
                C2H4_SCORE.append(c2h4_num)
                print('C2H4 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= C2H2_L3:
                c2h2_num = 4
                C2H2_SCORE.append(c2h2_num)
            elif (NEI >= C2H2_L2 and NEI < C2H2_L3):
                c2h2_num = (3 + (NEI - C2H2_L2))/(C2H2_L3 - C2H2_L2)
                C2H2_SCORE.append(c2h2_num)
            elif (NEI >= C2H2_L1 and NEI < C2H2_L2):
                c2h2_num = (2 + (NEI - C2H2_L1))/(C2H2_L2 - C2H2_L1)
                C2H2_SCORE.append(c2h2_num)
            elif (NEI < C2H2_L1):
                c2h2_num = (1 + NEI)/C2H2_L1
                C2H2_SCORE.append(c2h2_num)
            else:
                c2h2_num = 0
                C2H2_SCORE.append(c2h2_num)
                print('C2H2 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            HC_SCORE.append(max(ch4_num, c2h6_num, c2h4_num, c2h2_num))
        else:
            # NEI Score Low O2 thresholds
            L1 = 1.02
            L2 = 1.87
            L3 = 4

            # NEI Alt Score Low O2 thresholds
            ALT_L1 = 0.51
            ALT_L2 = 1.02
            ALT_L3 = 1.87

            # CH4 Score Low O2 thresholds
            CH4_L1 = 72
            CH4_L2 = 120
            CH4_L3 = 221

            # C2H6 Score Low O2 thresholds
            C2H6_L1 = 120
            C2H6_L2 = 277
            C2H6_L3 = 433

            # C2H4 Score Low O2 thresholds
            C2H4_L1 = 44
            C2H4_L2 = 91
            C2H4_L3 = 295

            # C2H2 Score Low O2 thresholds
            C2H2_L1 = 2
            C2H2_L2 = 10
            C2H2_L3 = 36

            if NEI >= L3:
                NEI_SCORE.append(4)
            elif (NEI >= L2 and NEI < L3):
                NEI_SCORE.append((3 + (NEI - L2))/(L3 - L2))
            elif (NEI >= L1 and NEI < L2):
                NEI_SCORE.append((2 + (NEI - L1))/(L2 - L1))
            elif (NEI < L1):
                NEI_SCORE.append((1 + NEI)/L1)
            else:
                NEI_SCORE.append(0)
                print('NEI Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= ALT_L3:
                NEI_ALT_SCORE.append(4)
            elif (NEI >= ALT_L2 and NEI < ALT_L3):
                NEI_ALT_SCORE.append((3 + (NEI - ALT_L2))/(ALT_L3 - ALT_L2))
            elif (NEI >= ALT_L1 and NEI < ALT_L2):
                NEI_ALT_SCORE.append((2 + (NEI - ALT_L1))/(ALT_L2 - ALT_L1))
            elif (NEI < ALT_L1):
                NEI_ALT_SCORE.append((1 + NEI)/ALT_L1)
            else:
                NEI_ALT_SCORE.append(0)
                print('NEI Alt Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= CH4_L3:
                ch4_num = 4
                CH4_SCORE.append(ch4_num)
            elif (NEI >= CH4_L2 and NEI < CH4_L3):
                ch4_num = (3 + (NEI - CH4_L2))/(CH4_L3 - CH4_L2)
                CH4_SCORE.append(ch4_num)
            elif (NEI >= CH4_L1 and NEI < CH4_L2):
                ch4_num = (2 + (NEI - CH4_L1))/(CH4_L2 - CH4_L1)
                CH4_SCORE.append(ch4_num)
            elif (NEI < CH4_L1):
                ch4_num = (1 + NEI)/CH4_L1
                CH4_SCORE.append(ch4_num)
            else:
                ch4_num = 0
                CH4_SCORE.append(ch4_num)
                print('CH4 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= C2H6_L3:
                c2h6_num = 4
                C2H6_SCORE.append(c2h6_num)
            elif (NEI >= C2H6_L2 and NEI < C2H6_L3):
                c2h6_num = (3 + (NEI - C2H6_L2))/(C2H6_L3 - C2H6_L2)
                C2H6_SCORE.append(c2h6_num)
            elif (NEI >= C2H6_L1 and NEI < C2H6_L2):
                c2h6_num = (2 + (NEI - C2H6_L1))/(C2H6_L2 - C2H6_L1)
                C2H6_SCORE.append(c2h6_num)
            elif (NEI < C2H6_L1):
                c2h6_num = (1 + NEI)/C2H6_L1
                C2H6_SCORE.append(c2h6_num)
            else:
                c2h6_num = 0
                C2H6_SCORE.append(c2h6_num)
                print('C2H6 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= C2H4_L3:
                c2h4_num = 4
                C2H4_SCORE.append(c2h4_num)
            elif (NEI >= C2H4_L2 and NEI < C2H4_L3):
                c2h4_num = (3 + (NEI - C2H4_L2))/(C2H4_L3 - C2H4_L2)
                C2H4_SCORE.append(c2h4_num)
            elif (NEI >= C2H4_L1 and NEI < C2H4_L2):
                c2h4_num = (2 + (NEI - C2H4_L1))/(C2H4_L2 - C2H4_L1)
                C2H4_SCORE.append(c2h4_num)
            elif (NEI < C2H4_L1):
                c2h4_num = (1 + NEI)/C2H4_L1
                C2H4_SCORE.append(c2h4_num)
            else:
                c2h4_num = 0
                C2H4_SCORE.append(c2h4_num)
                print('C2H4 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            if NEI >= C2H2_L3:
                c2h2_num = 4
                C2H2_SCORE.append(c2h2_num)
            elif (NEI >= C2H2_L2 and NEI < C2H2_L3):
                c2h2_num = (3 + (NEI - C2H2_L2))/(C2H2_L3 - C2H2_L2)
                C2H2_SCORE.append(c2h2_num)
            elif (NEI >= C2H2_L1 and NEI < C2H2_L2):
                c2h2_num = (2 + (NEI - C2H2_L1))/(C2H2_L2 - C2H2_L1)
                C2H2_SCORE.append(c2h2_num)
            elif (NEI < C2H2_L1):
                c2h2_num = (1 + NEI)/C2H2_L1
                C2H2_SCORE.append(c2h2_num)
            else:
                c2h2_num = 0
                C2H2_SCORE.append(c2h2_num)
                print('C2H2 Score calculation error for SN: ' +
                      str(getattr(sn, 'SN_CLEAN')))

            HC_SCORE.append(max(ch4_num, c2h6_num, c2h4_num, c2h2_num))

    tblResults['NEI_VAL'] = NEI_VAL

    print('There are ' + str(sum(i > 3 for i in NEI_SCORE)) +
          " '>3' values for the NEI Score rules")
    tblResults['NEI_SCORE'] = NEI_SCORE

    print('There are ' + str(sum(i > 3 for i in NEI_ALT_SCORE)) +
          " '>3' values for the NEI Alt Score rules")
    tblResults['NEI_ALT_SCORE'] = NEI_ALT_SCORE

    print('There are ' + str(sum(i > 3 for i in CH4_SCORE)) +
          " '>3' values for the CH4 Score rules")
    tblResults['CH4_SCORE'] = CH4_SCORE

    print('There are ' + str(sum(i > 3 for i in C2H6_SCORE)) +
          " '>3' values for the C2H6 Score rules")
    tblResults['C2H6_SCORE'] = C2H6_SCORE

    print('There are ' + str(sum(i > 3 for i in C2H4_SCORE)) +
          " '>3' values for the C2H4 Score rules")
    tblResults['C2H4_SCORE'] = C2H4_SCORE

    print('There are ' + str(sum(i > 3 for i in C2H2_SCORE)) +
          " '>3' values for the C2H2 Score rules")
    tblResults['C2H2_SCORE'] = C2H2_SCORE

    print('There are ' + str(sum(i > 3 for i in HC_SCORE)) +
          " '>3' values for the HC Score rules")
    tblResults['HC_SCORE'] = HC_SCORE
    return tblResults


def performance_creation(dga_last_samples):

    confusion_input = dga_last_samples[['SERIALNUM',
                                        'F',
                                        'NEW_IEEE_RULES']]

    diag_method_names = list(confusion_input)
    diag_method_names.remove('SERIALNUM', inplace=True)
    diag_method_names.remove('F', inplace=True)

    performance_table_names = ['TN_COUNT',
                               'FP_COUNT',
                               'TP_COUNT',
                               'FN_COUNT']

    performance_table = pd.DataFrame(columns=performance_table_names)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    for name in diag_method_names:
        TN_COUNT = 0
        FP_COUNT = 0
        TP_COUNT = 0
        FN_COUNT = 0
        for sn in confusion_input.itertuples():

            failure = getattr(sn, 'F')
            T_F = getattr(sn, name)
            if failure == 1:
                if T_F == 'TRUE' or (is_number(T_F) == True and T_F >= 3):
                    TP_COUNT += 1
                else:
                    FN_COUNT += 1
            else:
                if T_F == 'TRUE' or (is_number(T_F) == True and T_F >= 3):
                    FP_COUNT += 1
                else:
                    TN_COUNT += 1

        performance_table.at[name, 'TN_COUNT'] = TN_COUNT
        performance_table.at[name, 'FP_COUNT'] = FP_COUNT
        performance_table.at[name, 'TP_COUNT'] = TP_COUNT
        performance_table.at[name, 'FN_COUNT'] = FN_COUNT
    return performance_table

# not done yet


def get_last_samples(df):
    """
    This function returns a df of last samples from input of a
    df with 'SERIALNUM'
    and 'SAMPLEDATE' fields
    """
    # DGA
    try:
        df_last_samples = df.groupby('SERIALNUM').agg(
            lambda x: x.loc[x.SAMPLEDATE.idxmax()])
        df_last_samples = df_last_samples.reset_index()
    except Exception as e:
        print(str(e))

    return df_last_samples