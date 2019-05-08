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
    def test_blank_qryBushingPowerFactor():
        '''Making sure schema doesn't change from this version, for qryBushingPowerFactor
        '''
        pass
    
    def test_blank_qryDGA():
        '''Making sure schema doesn't change from this version, for qryDGA
        '''
        pass
    
    def test_blank_qryDiverterDGA():
        '''Making sure schema doesn't change from this version, for qryDiverterDGA
        '''
        pass

    def test_blank_qryDiverterOilQuality():
        '''Making sure schema doesn't change from this version, for qryDiverterOilQuality
        '''
        pass
    
    def test_blank_qryFurans():
        '''Making sure schema doesn't change from this version, for qryFurans
        '''
        pass
    
    def test_blank_qryInsulationPF():
        '''Making sure schema doesn't change from this version, for qryInsulationPF
        '''
        pass
    
    def test_blank_qryLTC():
        '''Making sure schema doesn't change from this version, for qryLTC
        '''
        pass
    
    def test_blank_qryLTCDGA():
        '''Making sure schema doesn't change from this version, for qryLTCDGA
        '''
        pass
    
    def test_blank_qryLTCOilQuality():
        '''Making sure schema doesn't change from this version, for qryLTCOilQuality
        '''
        pass
    
    def test_blank_qryLTCTapCount():
        '''Making sure schema doesn't change from this version, for qryLTCTapCount
        '''
        pass
    
    def test_blank_qryLTCTapPosition():
        '''Making sure schema doesn't change from this version, for qryLTCTapPosition
        '''
        pass
    
    def test_blank_qryOilQuality():
        '''Making sure schema doesn't change from this version, for qryOilQuality
        '''
        pass
    
    def test_blank_qrySelectorDGA():
        '''Making sure schema doesn't change from this version, for qrySelectorDGA
        '''
        pass
    
    def test_blank_qrySelectorOilQuality():
        '''Making sure schema doesn't change from this version, for qrySelectorOilQuality
        '''
        pass
    
    def test_blank_qryTfmrs():
        '''Making sure schema doesn't change from this version, for qryTfmrs
        '''
        pass
    
    def test_blank_schema_0_results():
        '''Making sure schema doesn't change from this version, for schema_0_results
        '''
        pass

    def test_blank_tblComments():
        '''Making sure schema doesn't change from this version, for tblComments
        '''
        pass
        
    def test_blank_tblResultsDetails():
        '''Making sure schema doesn't change from this version, for tblResultsDetails
        '''
        pass
    
    def test_blank_tblResultsOverTime():
        '''Making sure schema doesn't change from this version, for tblResultsOverTime
        '''
        pass
    
    def test_blank_workbook():
        '''testing test_schema_0_workbook function
        '''
        pass

    def test_schema_0_workbook():
        '''testing test_schema_0_workbook function
        '''
        pass
    
    def test_tblResultsCompare():
        '''testing tblResultsCompare function
        '''
        pass


if __name__ == "__main__":
    unittest.main()
