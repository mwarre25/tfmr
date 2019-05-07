"""
tfmr.lists
===============================================================
tfmr sub-module for storing common schema_0 and schema_1 lists
"""

def qryTfmrsManufacturerList():
    '''Returns current schema_0 manufacturer list.

    Returns:
        List of strings

    '''
    return(["ABB",
            "Allis Chalmers",
            "ASEA",
            "BBC",
            "ELIN",
            "English Electric",
            "Federal Pacifc", "Federal Pioneer", "Ferranti", "Fuji",
            "GE",
            "HeviDuty", "Hitachi", "Hyundai",
            "Magnetek", "McGraw / Cooper", "Mitsubishi",
            "NEI Parsons", "North American",
            "Other",
            "Prolec",
            "Siemens", "Smit",
            "Toshiba", "Trafo Union",
            "Westinghouse"])


def qryTfmrsCoreTypeList():
    '''Returns the current schema_0 core type list.

    Returns:
        List of strings

    '''
    return(["Core", "Shell"])


def qryLTCsManufacturerList():
    '''Returns the current schema_0 LTC manufacturer list.

    Returns:
        List of strings

    '''
    return(["Allis Chalmers",
            "ASEA", "CGE", "English Electric",
            "Federal Pacific", "Ferranti Packard",
            "GE",
            "Hitachi",
            "Maloney", "McGraw Edison",
            "Reinhausen",
            "Waukesha", "Westinghouse"])


def qryLTCsModelList():
    '''Returns the current schema_0 LTC model list.

    Returns:
        List of strings

    '''
    return(["220", "333", "397",
            "394", "396", "442",
            "494", "496", "550",
            "550B", "550C", "660",
            "995", "996", "A",
            "C", "CLR-100", "D",
            "E", "F", "FDA", "G",
            "H", "K", "LK", "LR-9",
            "LR-27", "LR-29", "LR-38",
            "LR-45", "LR-48", "LR-59",
            "LR-65", "LR-68", "LR-72",
            "LR-79", "LR-83", "LR-85",
            "LR-89",  "LR-91", "LRB",
            "LRN", "LRT-200", "LRT-200-1",
            "LRT-200-2", "LRT-200A",
            "LRT-200A-2", "LRT-300",
            "LRT-400", "LRT-500", "LRT-700",
            "M", "MA1", "MA2", "MB", "MB1",
            "MB2", "MC8", "MH", "MJ-2", "MS",
            "R", "RMS", "RMT", "RMV", "RMV-II",
            "RT 25", "RT 32", "RT 34", "RT 35",
            "RT 69", "T", "TC-15", "TC-23",
            "TC-25", "TC-34", "TC-46", "TC-515",
            "TC-525", "TC-546", "TDR", "TLB", 
            "TLC", "TLF-20", "TLF-30", "TLG",
            "TLH", "TLH-10", "TLH-20", "TLH-21",
            "TLS", "UBB", "UCC", "UCD", "UCG",
            "UCL", "UNR", "UR", "URN", "URS",
            "URT", "USB", "UT", "UTH", "UTS",
            "UTS-A", "UTB", "UTC", "UTT",
            "UTT-A", "UTT-B", "UVT", "UVW",
            "UZDRT", "UZE", "UZF", "UZD",
            "V", "V1", "V2", "V2a", "VV"])


def qryLTCBreatherList():
    '''Returns the current schema_0 LTC breather list.

    Returns:
        List of strings

    '''
    return(["Sealed", "Free"])