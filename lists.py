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


def tfmrEventTypeList():
    '''Return the current schema_1 TfmrEventType list for the TfmrServiceHistory table.

    Returns:
            List of strings

    '''
    return(["Relocation",
            "Scrap",
            "Rewind",
            "Retire",
            "Repair",
            "Inspection",
            "Failure",
            "Commissioning",
            "Manufacture",
            "Replacement",
            "Retire"])


def tfmrServiceStatusList():
    '''Return the current schema_1 ServiceStatus list for the TfmrServiceHistory table.

    Returns:
            List of strings

    '''
    return(['Emergency spare',
            'Not returned to service',
            'Other',
            'Repaired and returned to service',
            'Repaired and relocated',
            'Rewound and relocated',
            'Repaired to spare',
            'Rewound to spare',
            'Retired',
            'Returned to service',
            'Rewound and returned to service',
            'Scrapped',
            'Spare',
            'Unknown',
            ])


def tfmrRootCauseList():
    '''Return the current schema_1 RootCause list for the TfmrServiceHistory table.

    Returns:
            List of strings

    '''
    return(['Bushing failure',
            'Winding movement',
            'Dielectric failure',
            'Shield ring overheating',
            'Broken conductor in winding',
            'Unknown',
            'Circulating current',
            'Coking fault',
            'Lightning strike',
            'Contamination',
            'GIC damage',
            'Internal short circuit',
            'Inter-turn fault',
            'Localized conductor errosion',
            'Mechanical failure',
            'Overheating',
            'Partial discharge',
            'Winding collapse',
            'Sulphur corrosion',
            'Solid insulation ageing',
            'Incorrectly positioned oil guide',
            'Tapchanger failure',
            'Tank breach',
            'Fire',
            ])


def tfmrFailedComponentList():
    '''Return the current schema_1 FailedComponent list for the TfmrServiceHistory table.

    Returns:
            List of strings

    '''
    return(['Bushing',
            'Lead',
            'Auxiliary Equipment',
            'Connections',
            'Contacts',
            'Core',
            'Core Insulation',
            'Core steel',
            'Crimps',
            'Current Transformer',
            'Design',
            'Dielectric',
            'Load Tap Changer',
            'Bus',
            'Ground strap',
            'Heat exchanger',
            'Leads board terminal',
            'Magnetic circuit',
            'Tank',
            'Surge Arrestor',
            'Winding',
            'Valves',
            ])


def tfmrFailureConsequenceList():
    '''Return the current schema_1 FailureConsequence list for the TfmrServiceHistory table.

    Returns:
            List of strings

    '''
    return(['Ageing',
            'Collateral',
            'Degraded Condition',
            'Dielectric Breakdown',
            'Excess Temperatures',
            'Expulsion of Insulating Fluid',
            'External short-circuit',
            'Fails To Carry Load',
            'Fails To Regulate Voltage',
            'Fire',
            'Fluid Contamination',
            'Geomagnetic disturbance',
            'High Combustible Gas',
            'Impedence Change',
            'Improper maintenance',
            'Improper repair',
            'Installation at site',
            'Lead',
            'Loss of Fans',
            'Loss of Pumps',
            'LTC',
            'LTC Terminal Board Broke',
            'Other',
            'Overheating',
            'Overload',
            'Overvoltage(switching)',
            'Repeated external-short-circuit',
            'Rupture of Tank',
            'Sulphur corrosion',
            'Tap Changer Malfunction',
            'Tertiary',
            'Tertiary series',
            'Winding',
            'Windings',
            ])


def tfmrTypeList():
    '''Return the current schema_1 TfmrType list for the TfmrServiceHistory table.

    Returns:
            List of strings

    '''
    return(['Auto',
            'Grounding',
            'HVDC Converter',
            'Mobile',
            'Pad Mount',
            'Phase Angle Regulator',
            'Power',
            'Regulator',
            'Series Reactor',
            'Shunt Reactor',
            'TCUL',
            ])


def schema_1TfmrManufacturerList():
    '''Return the current schema_1 TfmrType list for the TfmrServiceHistory table.

    Returns:
            List of strings

    '''
    return(['ABB',
            'AEI',
            'ALCA',
            'ALLIS',
            'ALS',
            'ALST',
            'AREVA',
            'ARV',
            'ASEA',
            'BBC',
            'BBP',
            'BHAR',
            'BRU',
            'BTH',
            'CAP',
            'CG',
            'CHAN',
            'COOP',
            'CP',
            'DS',
            'EBG',
            'EEC',
            'EFACEC',
            'ELIN',
            'FEDPAC',
            'FEDPION',
            'FERR',
            'FORT',
            'FUJI',
            'FUL',
            'GE',
            'GEC',
            'GEH',
            'HANG',
            'HHE',
            'HHI',
            'HICO',
            'HITA',
            'HST',
            'IEM',
            'ILJIN',
            'JAEPS',
            'JSHP',
            'KVAE',
            'MAGN',
            'MCGR',
            'MITSU',
            'MOLO',
            'MVE',
            'NAT',
            'NIT',
            'PAUW',
            'PENN',
            'PING',
            'PPE',
            'PPT',
            'PROLEC',
            'PTTI',
            'RTE',
            'SAG',
            'SAVIG',
            'SCHN',
            'SHAN',
            'SHIH',
            'SIEM',
            'SIEVA',
            'SMI',
            'SMIT',
            'SPX',
            'TBEA',
            'TISH',
            'TRAFO',
            'TRENCH',
            'TTI',
            'TWBB',
            'VAP',
            'VATECH',
            'VAW',
            'VONROLL',
            'VTC',
            'W',
            'WAG',
            'WEG',
            'XD',
            'YET',
            ])
