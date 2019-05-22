import unittest
import pandas as pd
import tfmr.schema_1


class TestSchema1(unittest.TestCase):
    def test_blank_tfmr_details(self):
        '''Making sure schema doesn't change from this version, for tfmr_details
        '''
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

        test_blank_tfmr_details = pd.DataFrame(columns=blank_tfmr_details_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_details, tfmr.schema_1.blank_tfmr_details())

    def test_blank_tfmr_service_history(self):
        '''Making sure schema doesn't change from this version, for tfmr_service_history
        '''
        blank_tfmr_service_history_list = [
        'TfmrIdentifier', 'TfmrEventType', 'EventDate', 'PreviousStatus',
        'ServiceStatus', 'FirstFailure', 'AgeAtFailure', 'FailureLoc',
        'FailedComponent', 'FailureConsequence', 'FailureCause', 'RepairBy',
        'RepairLoc', 'RootCause', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_tfmr_service_history = pd.DataFrame(
            columns=blank_tfmr_service_history_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_service_history, tfmr.schema_1.blank_tfmr_service_history())

    def test_blank_tfmr_dga(self):
        '''Making sure schema doesn't change from this version, for tfmr_dga
        '''
        blank_tfmr_dga_list = [
        'TfmrIdentifier', 'SampleFrom', 'SampleDate', 'LabTestDate',
        'OilTempC', 'H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2',
        'N2', 'BadSample', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_tfmr_dga = pd.DataFrame(columns=blank_tfmr_dga_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_dga, tfmr.schema_1.blank_tfmr_dga())
    
    def test_blank_tfmr_dga_online(self):
        '''Making sure schema doesn't change from this version, for tfmr_dga_online
        '''
        blank_tfmr_dga_online_list = [
        'TfmrIdentifier', 'SampleDate', 'LabTestDate', 'OilTempC', 'H2', 'CH4',
        'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2', 'N2', 'Moisture_PPM',
        'RelSaturation', 'MonitorModel', 'BadSample', 'DataFileName',
        'CreatedBy', 'Remarks'
        ]

        test_blank_tfmr_dga_online = pd.DataFrame(columns=blank_tfmr_dga_online_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_dga_online, tfmr.schema_1.blank_tfmr_dga_online())

    def test_blank_tfmr_oq(self):
        '''Making sure schema doesn't change from this version, for tfmr_oq
        '''
        blank_tfmr_oq_list = [
        'TfmrIdentifier', 'SampleDate', 'LabTestDate', 'OilTempC',
        'MoisturePPM', 'Acidity', 'IFT', 'Color', 'D877', 'D1816_1MM',
        'D1816_2MM', 'IEC156', 'PF_25C', 'PF_100C', 'DataFileName',
        'CreatedBy', 'Remarks'
        ]

        test_blank_tfmr_oq = pd.DataFrame(columns=blank_tfmr_oq_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_oq, tfmr.schema_1.blank_tfmr_oq())
    
    def test_blank_tfmr_f(self):
        '''Making sure schema doesn't change from this version, for tfmr_f
        '''
        blank_tfmr_f_list = [
        'TfmrIdentifier', 'SampleDate', 'LabTestDate', '2FAL', '5M2F', '5H2F',
        '2ACF', '2FOL', 'CH3OH', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_tfmr_f = pd.DataFrame(columns=blank_tfmr_f_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_f, tfmr.schema_1.blank_tfmr_f())
    
    def test_blank_tfmr_type(self):
        '''Making sure schema doesn't change from this version, for tfmr_type
        '''
        blank_tfmr_type_list = ['TfmrType', 'DataFileName', 'CreatedBy', 'Remarks']

        test_blank_tfmr_type = pd.DataFrame(columns=blank_tfmr_type_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_type, tfmr.schema_1.blank_tfmr_type())
    
    def test_blank_utilities(self):
        '''Making sure schema doesn't change from this version, for utilities
        '''
        blank_utilities_list = [
        'Fullname', 'Region', 'Headquarters', 'PointofContact1',
        'PhoneofContact1', 'PointofContact2', 'PhoneofContact2',
        'DataFileName', 'LUOn', 'LUBy', 'Remarks'
        ]

        test_blank_utilities = pd.DataFrame(columns=blank_utilities_list)

        pd.testing.assert_frame_equal(
            test_blank_utilities, tfmr.schema_1.blank_utilities())
    
    def test_blank_application(self):
        '''Making sure schema doesn't change from this version, for application
        '''
        blank_application_list = [
        'Application', 'DataFileName', 'LUOn', 'LUBy', 'Remarks'
        ]

        test_blank_application = pd.DataFrame(columns=blank_application_list)

        pd.testing.assert_frame_equal(
            test_blank_application, tfmr.schema_1.blank_application())

    def test_blank_tfmr_manuf(self):
        '''Making sure schema doesn't change from this version, for tfmr_manuf
        '''
        blank_tfmr_manuf_list = [
        'TfmrManufacturer', 'Fullname', 'Headquarters', 'FactoryLoc1',
        'FactoryLoc2', 'CreatedBy', 'Remarks'
        ]

        test_blank_tfmr_manuf = pd.DataFrame(columns=blank_tfmr_manuf_list)

        pd.testing.assert_frame_equal(
            test_blank_tfmr_manuf, tfmr.schema_1.blank_tfmr_manuf())

    def test_blank_ltc_details(self):
        '''Making sure schema doesn't change from this version, for ltc_details
        '''
        blank_ltc_details_list = [
        'LTCIdentifier', 'LTCSerialNum', 'TfmrIdentifier', 'LTCManufacturer',
        'LTCIdentifierUnknown', 'LTCModel', 'Breather', 'Utility',
        'OperatingCompany', 'Region', 'Substation', 'LTC_Designation',
        'ManufactureDate', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_ltc_details = pd.DataFrame(columns=blank_ltc_details_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_details, tfmr.schema_1.blank_ltc_details())
    
    def test_blank_ltc_models(self):
        '''Making sure schema doesn't change from this version, for ltc_models
        '''
        blank_ltc_models_list = [
        'LTCModel', 'ModelDesc', 'LTCManufacturer', 'DataFileName',
        'CreatedBy', 'Remarks'
        ]

        test_blank_ltc_models = pd.DataFrame(columns=blank_ltc_models_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_models, tfmr.schema_1.blank_ltc_models())
    
    def test_blank_ltc_dga(self):
        '''Making sure schema doesn't change from this version, for ltc_dga
        '''
        blank_ltc_dga_list = [
        'LTCIdentifier', 'Compartment', 'SampleDate', 'LabTestDate',
        'OilTempC', 'H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2',
        'N2', 'BadSample', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_ltc_dga = pd.DataFrame(columns=blank_ltc_dga_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_dga, tfmr.schema_1.blank_ltc_dga())
    
    def test_blank_ltc_oq(self):
        '''Making sure schema doesn't change from this version, for ltc_oq
        '''
        blank_ltc_oq_list = [
        'LTCIdentifier', 'Compartment', 'SampleDate', 'LabTestDate',
        'OilTempC', 'MoisturePPM', 'Acidity', 'IFT', 'Color', 'D877',
        'D1816_1MM', 'D1816_2MM', 'IEC156', 'PF_25C', 'PF_100C',
        'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_ltc_oq = pd.DataFrame(columns=blank_ltc_oq_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_oq, tfmr.schema_1.blank_ltc_oq())
    
    def test_blank_ltc_tap_pos(self):
        '''Making sure schema doesn't change from this version, for ltc_tap_pos
        '''
        blank_ltc_tap_pos_list = [
        'LTCIdentifier', 'RecordDate', 'TapPos', 'DataFileName', 'CreatedBy',
        'Remarks'
        ]

        test_blank_ltc_tap_pos = pd.DataFrame(columns=blank_ltc_tap_pos_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_tap_pos, tfmr.schema_1.blank_ltc_tap_pos())

    def test_blank_ltc_tap_count(self):
        '''Making sure schema doesn't change from this version, for ltc_tap_count
        '''
        blank_ltc_tap_count_list = [
        'LTCIdentifier', 'RecordDate', 'CounterReading', 'HighTapPos',
        'LowTapPos', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_ltc_tap_count = pd.DataFrame(columns=blank_ltc_tap_count_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_tap_count, tfmr.schema_1.blank_ltc_tap_count())
    
    def test_blank_ltc_service_history(self):
        '''Making sure schema doesn't change from this version, for ltc_service_history
        '''
        blank_ltc_service_history_list = [
        'LTCIdentifier', 'LTCEventType', 'EventDate', 'PreviousStatus',
        'ServiceStatus', 'FailureLoc', 'FailureConsequence', 'FailureCause',
        'RepairBy', 'RepairLoc', 'RootCause', 'DataFileName', 'CreatedBy',
        'Remarks'
        ]

        test_blank_ltc_service_history = pd.DataFrame(
            columns=blank_ltc_service_history_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_service_history, tfmr.schema_1.blank_ltc_service_history())
    
    def test_blank_ltc_manuf(self):
        '''Making sure schema doesn't change from this version, for ltc_manuf
        '''
        blank_ltc_manuf_list = [
        'LTCManufacturer', 'Fullname', 'Headquarters', 'FactoryLoc1',
        'FactoryLoc2', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_ltc_manuf = pd.DataFrame(columns=blank_ltc_manuf_list)

        pd.testing.assert_frame_equal(
            test_blank_ltc_manuf, tfmr.schema_1.blank_ltc_manuf())
    
    def test_blank_bush_details(self):
        '''Making sure schema doesn't change from this version, for bush_details
        '''
        blank_bush_details_list = [
        'BushingIdentifier', 'BushingSerialNum', 'TfmrIdentifier',
        'PhaseInstalled', 'BushingManufacturer', 'BushingModel', 'Utility',
        'OperatingCompany', 'Region', 'Substation', 'BushingDesignation',
        'ManufactureDate', 'ConnectionType', 'BIL', 'RatedVoltage',
        'RatedCurrent', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_bush_details = pd.DataFrame(columns=blank_bush_details_list)

        pd.testing.assert_frame_equal(
            test_blank_bush_details, tfmr.schema_1.blank_bush_details())

    def test_blank_bush_models(self):
        '''Making sure schema doesn't change from this version, for bush_models
        '''
        blank_bush_models_list = [
        'BushingModel'
        'ModelDesc', 'BushingManufacturer', 'DataFileName', 'LUOn', 'LUBy',
        'Remarks'
        ]

        test_blank_bush_models = pd.DataFrame(columns=blank_bush_models_list)

        pd.testing.assert_frame_equal(
            test_blank_bush_models, tfmr.schema_1.blank_bush_models())
    
    def test_blank_bush_service_history(self):
        '''Making sure schema doesn't change from this version, for bush_service_history
        '''
        blank_bush_service_history_list = [
        'BushingIdentifier', 'BushingEventType', 'EventDate', 'PreviousStatus',
        'ServiceStatus', 'FailureLoc', 'FailureConsequence', 'FailureCause',
        'RepairBy', 'RepairLoc', 'RootCause', 'DataFileName', 'CreatedBy',
        'Remarks'
        ]

        test_blank_bush_service_history = pd.DataFrame(
            columns=blank_bush_service_history_list)

        pd.testing.assert_frame_equal(
            test_blank_bush_service_history, tfmr.schema_1.blank_bush_service_history())
    
    def test_blank_bush_pf(self):
        '''Making sure schema doesn't change from this version, for bush_pf
        '''
        blank_bush_pf_list = [
        'BushingIdentifier', 'Factoryresult', 'Precommissioning',
        'TempHumidityInfo', 'TestDate', 'TestVoltagekV', 'C1PF', 'C1Cap',
        'C2PF', 'C2Cap', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_bush_pf = pd.DataFrame(columns=blank_bush_pf_list)

        pd.testing.assert_frame_equal(
            test_blank_bush_pf, tfmr.schema_1.blank_bush_pf())
    
    def test_blank_bush_manuf(self):
        '''Making sure schema doesn't change from this version, for bush_manuf
        '''
        blank_bush_manuf_list = [
        'BushingManufacturer', 'Fullname', 'Headquarters', 'FactoryLoc1',
        'FactoryLoc2', 'DataFileName', 'CreatedBy', 'Remarks'
        ]

        test_blank_bush_manuf = pd.DataFrame(columns=blank_bush_manuf_list)

        pd.testing.assert_frame_equal(
            test_blank_bush_manuf, tfmr.schema_1.blank_bush_manuf())

    def test_data_file_details(self):
        '''Making sure schema doesn't change from this version, for bush_manuf
        '''
        data_file_details_list = [
        'DataFile', 'FileTypeExtension', 'Utility', 'TypeofData',
        'ReceivedDate', 'ReceivedFrom', 'FilePathStorage'
        ]

        test_data_file_details = pd.DataFrame(columns=data_file_details_list)

        pd.testing.assert_frame_equal(
            test_data_file_details, tfmr.schema_1.data_file_details())

if __name__ == "__main__":
    unittest.main()
