import unittest
import pandas as pd
import tfmr.schema_0


class TestSchema0(unittest.TestCase):
    def test_blank_qryBushing(self):
        '''Making sure schema doesn't change from this version, for qryBushing
        '''
        qryBushing_list = [
            "ID", "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL",
            "CONNECTIONTYPE", "BIL", "RATEDVOLTAGE", "RATEDCURRENT",
            "FACTORYC1PF", "FACTORYC1CAP", "FACTORYC2PF", "FACTORYC2CAP"
        ]

        test_qryBushing = pd.DataFrame(columns=qryBushing_list)

        # strings
        for col in [
                "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL", "CONNECTIONTYPE"
        ]:
            test_qryBushing[col] = test_qryBushing[col].astype("str")

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
            test_qryBushing[col] = test_qryBushing[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryBushing[col] = test_qryBushing[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryBushing, tfmr.schema_0.blank_qryBushing())

    def test_blank_qryBushingPowerFactor(self):
        '''Making sure schema doesn't change from this version, for qryBushingPowerFactor
        '''
        qryBushingPowerFactor_list = [
            "ID", "TESTDATE", "TFMRID", "BUSHINGID", "TEMPERATURE", "TESTVOLTAGE",
            "MEASUREDC1PF", "MEASUREDC1CAP", "MEASUREDC2PF", "MEASUREDC2CAP"
        ]

        test_qryBushingPowerFactor = pd.DataFrame(
            columns=qryBushingPowerFactor_list)

        # strings
        for col in ["TFMRID", "BUSHINGID"]:
            test_qryBushingPowerFactor[col] = test_qryBushingPowerFactor[col].astype(
                "str")

        # dates
        for col in ["TESTDATE"]:
            test_qryBushingPowerFactor[col] = pd.to_datetime(
                test_qryBushingPowerFactor[col])

        # floats
        for col in [
                "TEMPERATURE",
                "TESTVOLTAGE",
                "MEASUREDC1PF",
                "MEASUREDC1CAP",
                "MEASUREDC2PF",
                "MEASUREDC2CAP",
        ]:
            test_qryBushingPowerFactor[col] = test_qryBushingPowerFactor[col].astype(
                "float")

        # ints
        for col in ["ID"]:
            test_qryBushingPowerFactor[col] = test_qryBushingPowerFactor[col].astype(
                "int")

        pd.testing.assert_frame_equal(
            test_qryBushingPowerFactor, tfmr.schema_0.blank_qryBushingPowerFactor())

    def test_blank_qryDGA(self):
        '''Making sure schema doesn't change from this version, for qryDGA
        '''
        qryDGA_list = [
            "ID", "SERIALNUM", "SAMPLEDATE", "H2", "CH4", "C2H6", "C2H4", "C2H2",
            "CO", "CO2", "O2", "N2", "BadSample"
        ]

        test_qryDGA = pd.DataFrame(columns=qryDGA_list)

        # strings
        for col in ["SERIALNUM"]:
            test_qryDGA[col] = test_qryDGA[col].astype("str")

        # dates
        for col in ["SAMPLEDATE"]:
            test_qryDGA[col] = pd.to_datetime(test_qryDGA[col])

        # floats
        for col in ["H2", "CH4", "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"]:
            test_qryDGA[col] = test_qryDGA[col].astype("float")

        # bool
        for col in ["BadSample"]:
            test_qryDGA[col] = test_qryDGA[col].astype("bool")

        # ints
        for col in ["ID"]:
            test_qryDGA[col] = test_qryDGA[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryDGA, tfmr.schema_0.blank_qryDGA())

    def test_blank_qryFurans(self):
        '''Making sure schema doesn't change from this version, for qryFurans
        '''
        qryFurans_list = ["ID", "SERIALNUM", "SAMPLEDATE", "2FAL"]

        test_qryFurans = pd.DataFrame(columns=qryFurans_list)

        # strings
        for col in ["SERIALNUM"]:
            test_qryFurans[col] = test_qryFurans[col].astype("str")

        # dates
        for col in ["SAMPLEDATE"]:
            test_qryFurans[col] = pd.to_datetime(test_qryFurans[col])

        # floats
        for col in ["2FAL"]:
            test_qryFurans[col] = test_qryFurans[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryFurans[col] = test_qryFurans[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryFurans, tfmr.schema_0.blank_qryFurans())

    def test_blank_qryInsulationPF(self):
        '''Making sure schema doesn't change from this version, for qryInsulationPF
        '''
        qryInsulationPF_list = [
        "ID", "TFMRID", "SAMPLEDATE", "CH_MEAS", "CL_MEAS", "CT_MEAS",
        "CHL_MEAS", "CHT_MEAS", "CH_CORR", "CL_CORR", "CT_CORR", "CHL_CORR",
        "CHT_CORR"]

        test_qryInsulationPF = pd.DataFrame(columns=qryInsulationPF_list)

        # strings
        for col in ["TFMRID"]:
            test_qryInsulationPF[col] = test_qryInsulationPF[col].astype("str")

        # dates
        for col in ["SAMPLEDATE"]:
            test_qryInsulationPF[col] = pd.to_datetime(test_qryInsulationPF[col])

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
            test_qryInsulationPF[col] = test_qryInsulationPF[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryInsulationPF[col] = test_qryInsulationPF[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryInsulationPF, tfmr.schema_0.blank_qryInsulationPF())

    def test_blank_qryLTC(self):
        '''Making sure schema doesn't change from this version, for qryLTC
        '''
        qryLTC_list = [
        "ID", "TFMRID", "LTCID", "MANUFACTURER", "MODEL", "BREATHER"]

        test_qryLTC = pd.DataFrame(columns=qryLTC_list)

        # strings
        for col in ["TFMRID", "LTCID", "MANUFACTURER", "MODEL", "BREATHER"]:
            test_qryLTC[col] = test_qryLTC[col].astype("str")

        # ints
        for col in ["ID"]:
            test_qryLTC[col] = test_qryLTC[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryLTC, tfmr.schema_0.blank_qryLTC())

    def test_blank_qryLTCDGA(self):
        '''Making sure schema doesn't change from this version, for qryLTCDGA
        '''
        qryLTCDGA_list = [
        "ID", "TFMRID", "LTCID", "COMPARTMENT", "SAMPLEDATE", "H2", "CH4",
        "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"]

        test_qryLTCDGA = pd.DataFrame(columns=qryLTCDGA_list)

        # strings
        for col in ["TFMRID", "LTCID", "COMPARTMENT"]:
            test_qryLTCDGA[col] = test_qryLTCDGA[col].astype("str")

        # dates
        for col in ["SAMPLEDATE"]:
            test_qryLTCDGA[col] = pd.to_datetime(test_qryLTCDGA[col])

        # floats
        for col in ["H2", "CH4", "C2H6", "C2H4", "C2H2", "CO", "CO2", "O2", "N2"]:
            test_qryLTCDGA[col] = test_qryLTCDGA[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryLTCDGA[col] = test_qryLTCDGA[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryLTCDGA, tfmr.schema_0.blank_qryLTCDGA())

    def test_blank_qryLTCOilQuality(self):
        '''Making sure schema doesn't change from this version, for qryLTCOilQuality
        '''
        qryLTCOilQuality_list = [
        "ID", "TFMRID", "LTCID", "COMPARTMENT", "SAMPLEDATE", "OILTEMP",
        "MOISTURE_PPM", "ACIDITY", "IFT", "COLOR", "D877", "D1816_1MM",
        "D1816_2MM", "IEC156", "PF_25C", "PF_100C"]

        test_qryLTCOilQuality = pd.DataFrame(columns=qryLTCOilQuality_list)

        # strings
        for col in ["TFMRID", "LTCID", "COMPARTMENT"]:
            test_qryLTCOilQuality[col] = test_qryLTCOilQuality[col].astype("str")

        # dates
        for col in ["SAMPLEDATE"]:
            test_qryLTCOilQuality[col] = pd.to_datetime(test_qryLTCOilQuality[col])

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
            test_qryLTCOilQuality[col] = test_qryLTCOilQuality[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryLTCOilQuality[col] = test_qryLTCOilQuality[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryLTCOilQuality, tfmr.schema_0.blank_qryLTCOilQuality())

    def test_blank_qryLTCTapCount(self):
        '''Making sure schema doesn't change from this version, for qryLTCTapCount
        '''
        qryLTCTapCount_list = [
        "ID", "RECORDDATE", "TFMRID", "LTCID", "COUNTERREADING", "HIGHTAPPOS",
        "LOWTAPPOS"]

        test_qryLTCTapCount = pd.DataFrame(columns=qryLTCTapCount_list)

        # strings
        for col in ["TFMRID", "LTCID", "HIGHTAPPOS", "LOWTAPPOS"]:
            test_qryLTCTapCount[col] = test_qryLTCTapCount[col].astype("str")

        # dates
        for col in ["RECORDDATE"]:
            test_qryLTCTapCount[col] = pd.to_datetime(test_qryLTCTapCount[col])

        # ints
        for col in ["ID", "COUNTERREADING"]:
            test_qryLTCTapCount[col] = test_qryLTCTapCount[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryLTCTapCount, tfmr.schema_0.blank_qryLTCTapCount())

    def test_blank_qryLTCTapPosition(self):
        '''Making sure schema doesn't change from this version, for qryLTCTapPosition
        '''
        qryLTCTapPosition_list = [
        "ID", "RECORDDATE", "TFMRID", "LTCID", "TAPPOSITION"]

        test_qryLTCTapPosition = pd.DataFrame(columns=qryLTCTapPosition_list)

        # strings
        for col in ["TFMRID", "LTCID", "TAPPOSITION"]:
            test_qryLTCTapPosition[col] = test_qryLTCTapPosition[col].astype("str")

        # dates
        for col in ["RECORDDATE"]:
            test_qryLTCTapPosition[col] = pd.to_datetime(test_qryLTCTapPosition[col])

        # ints
        for col in ["ID"]:
            test_qryLTCTapPosition[col] = test_qryLTCTapPosition[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryLTCTapPosition, tfmr.schema_0.blank_qryLTCTapPosition())

    def test_blank_qryOilQuality(self):
        '''Making sure schema doesn't change from this version, for qryOilQuality
        '''
        qryLTCOilQuality_list = [
        "ID", "TFMRID", "LTCID", "COMPARTMENT", "SAMPLEDATE", "OILTEMP",
        "MOISTURE_PPM", "ACIDITY", "IFT", "COLOR", "D877", "D1816_1MM",
        "D1816_2MM", "IEC156", "PF_25C", "PF_100C"]

        test_qryLTCOilQuality = pd.DataFrame(columns=qryLTCOilQuality_list)

        # strings
        for col in ["TFMRID", "LTCID", "COMPARTMENT"]:
            test_qryLTCOilQuality[col] = test_qryLTCOilQuality[col].astype("str")

        # dates
        for col in ["SAMPLEDATE"]:
            test_qryLTCOilQuality[col] = pd.to_datetime(test_qryLTCOilQuality[col])

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
            test_qryLTCOilQuality[col] = test_qryLTCOilQuality[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryLTCOilQuality[col] = test_qryLTCOilQuality[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryLTCOilQuality, tfmr.schema_0.blank_qryLTCOilQuality())

    def test_blank_qryTfmrs(self):
        '''Making sure schema doesn't change from this version, for qryTfmrs
        '''
        qryTfmrs_list = [
        "ID", "SERIALNUM", "MANUFACTURER", "MANUFACTUREDATE", "ENERGIZEDATE",
        "REPAIRDATE", "RETIREDATE", "UTILITY", "REGION", "STATION",
        "DESIGNATION", "CORETYPE", "TOPMVA", "COOLINGTYPE", "HV_kV", "LV1_kV",
        "LV2_kV", "TV_kV", "NUMPHASES", "ISAUTO", "CRITICALITY"]

        test_qryTfmrs = pd.DataFrame(columns=qryTfmrs_list)

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
            test_qryTfmrs[col] = test_qryTfmrs[col].astype("str")

        # dates
        for col in ["MANUFACTUREDATE", "ENERGIZEDATE", "REPAIRDATE", "RETIREDATE"]:
            test_qryTfmrs[col] = pd.to_datetime(test_qryTfmrs[col])

        # floats
        for col in ["TOPMVA", "HV_kV", "LV1_kV", "LV2_kV", "TV_kV", "CRITICALITY"]:
            test_qryTfmrs[col] = test_qryTfmrs[col].astype("float")

        # ints
        for col in ["ID", "NUMPHASES"]:
            test_qryTfmrs[col] = test_qryTfmrs[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryTfmrs, tfmr.schema_0.blank_qryTfmrs())

    def test_blank_schema_0_results(self):
        '''Making sure schema doesn't change from this version, for schema_0_results
        '''
        qryBushing_list = [
            "ID", "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL",
            "CONNECTIONTYPE", "BIL", "RATEDVOLTAGE", "RATEDCURRENT",
            "FACTORYC1PF", "FACTORYC1CAP", "FACTORYC2PF", "FACTORYC2CAP"
        ]

        test_qryBushing = pd.DataFrame(columns=qryBushing_list)

        # strings
        for col in [
                "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL", "CONNECTIONTYPE"
        ]:
            test_qryBushing[col] = test_qryBushing[col].astype("str")

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
            test_qryBushing[col] = test_qryBushing[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryBushing[col] = test_qryBushing[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryBushing, tfmr.schema_0.blank_qryBushing())

    def test_blank_tblComments(self):
        '''Making sure schema doesn't change from this version, for tblComments
        '''
        qryBushing_list = [
            "ID", "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL",
            "CONNECTIONTYPE", "BIL", "RATEDVOLTAGE", "RATEDCURRENT",
            "FACTORYC1PF", "FACTORYC1CAP", "FACTORYC2PF", "FACTORYC2CAP"
        ]

        test_qryBushing = pd.DataFrame(columns=qryBushing_list)

        # strings
        for col in [
                "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL", "CONNECTIONTYPE"
        ]:
            test_qryBushing[col] = test_qryBushing[col].astype("str")

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
            test_qryBushing[col] = test_qryBushing[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryBushing[col] = test_qryBushing[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryBushing, tfmr.schema_0.blank_qryBushing())

    def test_blank_tblResultsDetails(self):
        '''Making sure schema doesn't change from this version, for tblResultsDetails
        '''
        qryBushing_list = [
            "ID", "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL",
            "CONNECTIONTYPE", "BIL", "RATEDVOLTAGE", "RATEDCURRENT",
            "FACTORYC1PF", "FACTORYC1CAP", "FACTORYC2PF", "FACTORYC2CAP"
        ]

        test_qryBushing = pd.DataFrame(columns=qryBushing_list)

        # strings
        for col in [
                "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL", "CONNECTIONTYPE"
        ]:
            test_qryBushing[col] = test_qryBushing[col].astype("str")

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
            test_qryBushing[col] = test_qryBushing[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryBushing[col] = test_qryBushing[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryBushing, tfmr.schema_0.blank_qryBushing())

    def test_blank_tblResultsOverTime(self):
        '''Making sure schema doesn't change from this version, for tblResultsOverTime
        '''
        qryBushing_list = [
            "ID", "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL",
            "CONNECTIONTYPE", "BIL", "RATEDVOLTAGE", "RATEDCURRENT",
            "FACTORYC1PF", "FACTORYC1CAP", "FACTORYC2PF", "FACTORYC2CAP"
        ]

        test_qryBushing = pd.DataFrame(columns=qryBushing_list)

        # strings
        for col in [
                "TFMRID", "BUSHINGID", "MANUFACTURER", "MODEL", "CONNECTIONTYPE"
        ]:
            test_qryBushing[col] = test_qryBushing[col].astype("str")

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
            test_qryBushing[col] = test_qryBushing[col].astype("float")

        # ints
        for col in ["ID"]:
            test_qryBushing[col] = test_qryBushing[col].astype("int")

        pd.testing.assert_frame_equal(
            test_qryBushing, tfmr.schema_0.blank_qryBushing())

    def test_blank_workbook(self):
        '''testing test_schema_0_workbook function
        '''
        pass

    def test_schema_0_workbook(self):
        '''testing test_schema_0_workbook function
        '''
        pass

    def test_tblResultsCompare(self):
        '''testing tblResultsCompare function
        '''
        pass


if __name__ == "__main__":
    unittest.main()
