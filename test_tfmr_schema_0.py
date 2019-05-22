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

        pd.testing.assert_frame_equal(test_qryBushing, tfmr.schema_0.blank_qryBushing())
    def test_blank_qryBushingPowerFactor(self):
        '''Making sure schema doesn't change from this version, for qryBushingPowerFactor
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

        pd.testing.assert_frame_equal(test_qryBushing, tfmr.schema_0.blank_qryBushing())
        pass
    
    def test_blank_qryDGA(self):
        '''Making sure schema doesn't change from this version, for qryDGA
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

        pd.testing.assert_frame_equal(test_qryBushing, tfmr.schema_0.blank_qryBushing())
        pass
    
    def test_blank_qryFurans(self):
        '''Making sure schema doesn't change from this version, for qryFurans
        '''
        pass
    
    def test_blank_qryInsulationPF(self):
        '''Making sure schema doesn't change from this version, for qryInsulationPF
        '''
        pass
    
    def test_blank_qryLTC(self):
        '''Making sure schema doesn't change from this version, for qryLTC
        '''
        pass
    
    def test_blank_qryLTCDGA(self):
        '''Making sure schema doesn't change from this version, for qryLTCDGA
        '''
        pass
    
    def test_blank_qryLTCOilQuality(self):
        '''Making sure schema doesn't change from this version, for qryLTCOilQuality
        '''
        pass
    
    def test_blank_qryLTCTapCount(self):
        '''Making sure schema doesn't change from this version, for qryLTCTapCount
        '''
        pass
    
    def test_blank_qryLTCTapPosition(self):
        '''Making sure schema doesn't change from this version, for qryLTCTapPosition
        '''
        pass
    
    def test_blank_qryOilQuality(self):
        '''Making sure schema doesn't change from this version, for qryOilQuality
        '''
        pass
    
    def test_blank_qryTfmrs(self):
        '''Making sure schema doesn't change from this version, for qryTfmrs
        '''
        pass
    
    def test_blank_schema_0_results(self):
        '''Making sure schema doesn't change from this version, for schema_0_results
        '''
        pass

    def test_blank_tblComments(self):
        '''Making sure schema doesn't change from this version, for tblComments
        '''
        pass
        
    def test_blank_tblResultsDetails(self):
        '''Making sure schema doesn't change from this version, for tblResultsDetails
        '''
        pass
    
    def test_blank_tblResultsOverTime(self):
        '''Making sure schema doesn't change from this version, for tblResultsOverTime
        '''
        pass
    
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
