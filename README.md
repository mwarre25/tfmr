# tfmr module

## purpose
This module was developed to help formulate an ETL process for transformer data (dissolved gas analysis (DGA), oil quality, and bushing test data) using [pandas](https://pandas.pydata.org/).


# installation
To install this package, first download the zip file or clone the repository into your site-packages folder.

Ex. For a typical Anaconda installation this folder would be located at C:\Users\Mike\Anaconda3\Lib\site-packages.

# usage

```python
import tfmr.accdb as accdb
import tfmr.schema_0 as schema_0
import tfmr.lists as lists
import tfmr.schema_1 as schema_1
import tfmr.schema_1_reports as schema_1_reports
import tfmr.transformations as tfmr_t

# initializing blank schema dataframes
TfmrDetails = schema_1.blank_tfmr_details()
TfmrServiceHistory = schema_1.blank_tfmr_service_history()
TfmrDGA = schema_1.blank_tfmr_dga()
TfmrOQ = schema_1.blank_tfmr_oq()
TfmrF = schema_1.blank_tfmr_f()

LTCDetails = schema_1.blank_ltc_details()
LTCServiceHistory = schema_1.blank_ltc_service_history()
LTCModels = schema_1.blank_ltc_models()
LTCDGA = schema_1.blank_ltc_dga()
LTCOQ = schema_1.blank_ltc_oq()

# Pre-Transformation Step: Mapping tfmr_details fields to raw data fields
# to see full tfmrDetails list: list(tfmrs.raw_tfmr_details)

TfmrDetails['TfmrIdentifier'] = "SOURCE_" + raw_data_df['equipnum']
TfmrDetails['TfmrSerialNum'] = raw_data_df['equipnum']
TfmrDetails['TfmrManufacturer'] = raw_data_df['mfr']
TfmrDetails['ManufactureDate'] = raw_data_df['year_mfg']
TfmrDetails['Utility'] = 'SOURCE'
TfmrDetails['OperatingCompany'] = raw_data_df['owner_name']
TfmrDetails['Region'] = raw_data_df['region_name']
TfmrDetails['Substation'] = raw_data_df['substn_name']
TfmrDetails['Designation'] = raw_data_df['designation']
TfmrDetails['CoolingType1'] = raw_data_df['cooling']
TfmrDetails['MVA1'] = raw_data_df['mva_ratings']
TfmrDetails['TfmrType'] = raw_data_df['eqp_desc']
TfmrDetails['HV_kV'] = raw_data_df['kv_ratings']
TfmrDetails['LV1_kV'] = raw_data_df['kv_ratings']
TfmrDetails['IsAuto'] = raw_data_df['eqp_desc']
TfmrDetails['OilType'] = raw_data_df['fluidtype']
TfmrDetails['OilPreservationType'] = raw_data_df['oilpres']
TfmrDetails['DataFileName'] = raw_data_df['DataFileName']
TfmrDetails['CreatedBy'] = 'Michael W'
TfmrDetails['Remarks'] = raw_data_df['eqp_remarks']

TfmrDetails.drop_duplicates(subset=['TfmrIdentifier'], inplace=True)

# Transformation Step: For non-nan string year values convert to datetime like so: ('1/1/' + year).to_datetime
TfmrDetails['ManufactureDate'] = tfmr_t.string_year_to_datetime(TfmrDetails['ManufactureDate'])
```
