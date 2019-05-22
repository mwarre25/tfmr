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
    '''Return the current schema_1 TfmrType list for the TfmrDetails table.

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
    '''Return the current schema_1 TfmrType list for the TfmrDetails table.

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


def TfmrApplicationList():
    '''Return the current schema_1 TfmrApplication list for the TfmrDetails table.

    Returns:
            List of strings

    '''
    return(['Auxiliary',
            'Distribution',
            'Grounding',
            'GSU',
            'Spare',
            'Sub Transmission',
            'Substation',
            'Transmission',
            'Zig-Zag',
            ])


def schema_1LTCManufacturersList():
    '''Return the current schema_1 LTCManufacturers list for the LTCDetails table.

    Returns:
            List of strings

    '''
    return(['ABB',
            'ALLIS',
            'ASEA',
            'CG',
            'COOP',
            'EE',
            'FEDPAC',
            'FEDPION',
            'FERR',
            'GE',
            'HITA',
            'MAGN',
            'MCGR',
            'MOLO',
            'MR',
            'NATCO',
            'PENN',
            'SIEM',
            'TU',
            'WAUK',
            'WEST',
            ])


def schema_1LTCModelsList():
    '''Return the current schema_1 LTCModels list for the LTCDetails table.

    Returns:
            List of strings

    '''
    return(['220',
            '333',
            '393',
            '394',
            '396',
            '397',
            '397D',
            '442',
            '494',
            '496',
            '550',
            '550B',
            '550C',
            '660',
            '995',
            '996',
            'A',
            'AVT',
            'C',
            'CLR100',
            'CRND702',
            'D',
            'DIII200',
            'E',
            'F',
            'FDA',
            'G',
            'H',
            'K',
            'L700',
            'LK',
            'LR27',
            'LR29',
            'LR300',
            'LR38',
            'LR45',
            'LR48',
            'LR500',
            'LR59',
            'LR65',
            'LR68',
            'LR72',
            'LR79',
            'LR83',
            'LR85',
            'LR89',
            'LR9',
            'LR91',
            'LRB',
            'LRN',
            'LRT200',
            'LRT2001',
            'LRT2002',
            'LRT200A',
            'LRT200A2',
            'LRT300',
            'LRT400',
            'LRT500',
            'LRT59',
            'LRT69',
            'LRT700',
            'LRT72',
            'LRT81',
            'LRT9',
            'M',
            'MA1',
            'MA2',
            'MB',
            'MB1',
            'MB2',
            'MC8',
            'MH',
            'MJ2',
            'MLPN77',
            'MS',
            'R',
            'RM',
            'RMS',
            'RMT',
            'RMVA',
            'RMVII',
            'RT25',
            'RT32',
            'RT34',
            'RT35',
            'RT69',
            'T',
            'TC15',
            'TC23',
            'TC25',
            'TC322',
            'TC34',
            'TC342',
            'TC343',
            'TC34M',
            'TC46',
            'TC515',
            'TC525',
            'TC546',
            'TDR',
            'TIII600',
            'TLB',
            'TLC',
            'TLF20',
            'TLF30',
            'TLG',
            'TLH',
            'TLH10',
            'TLH20',
            'TLH21',
            'TLS',
            'TR',
            'UB',
            'UBB',
            'UC',
            'UCC',
            'UCD',
            'UCG',
            'UCGRT',
            'UCL',
            'UNR',
            'UR',
            'URH',
            'URN',
            'URS',
            'URT',
            'URTHC',
            'USB',
            'UT',
            'UTB',
            'UTC',
            'UTH',
            'UTR',
            'UTS',
            'UTSA',
            'UTT',
            'UTTA',
            'UTTB',
            'UVT',
            'UVW',
            'UZ',
            'UZD',
            'UZDRT',
            'UZE',
            'UZERN',
            'UZF',
            'UZG',
            'V',
            'V1',
            'V2',
            'V2A',
            'VRC',
            'VUCG',
            'VV', ])


def schema_1UtilitiesList():
    '''Return the current schema_1 Utilities list for the TfmrDetails table.

    Returns:
            List of strings

    '''
    return(['A2A','AADC','ABE','ABM','ACE','ADDC','ADERROER','AEC','AEIND','AELP','AEP','AESSE','AESSS','AGM','AHU','AIA','AIO','AKDAS','AKDENIZ','AKN','ALACHUA','ALBAIN','ALEC','ALEX','ALG','ALLI','ALPAP','ALROR','AMBIT','AMEA','AMEREN','AMIGO','ANEC','ANTIGONISH','APA','APC','APDCL','APN','APPA','APQ','APS','APSEB','APURONUO','ARAS','ASHB','ASI','ATC','ATCO','ATLA','ATM','ATR','ATTLE','ATW','AUA','AURORA','AUSGRID','AUSNET','AVANGRID','AVISTA','AVVN','AWY','AXPOP','AYDEM','BAH','BAK','BAN','BANAT','BANGOR','BARCR','BART','BARTOW','BASIN','BC Y','BDO','BELK','BERLIN','BGE','BIA','BIHAR','BKW','BLE','BLI','BLOUNT','BLRDGEE','BLRDGEMTN','BNA','BNE','BNL','BNN','BNO','BOGAZI','BOK','BORA','BOYLE','BPA','BRA','BRANT','BRANTFRD','BRAZ','BRUN','BRYAN','BTE','BURL','BURLHY','BUS','BUSH','BUW','BYS','CAE','CAG','CAK','CALCU','CALIK','CANOO','CANP','CAPE','CAR','CARUNA','CASRS','CASTE','CATLK','CCEC','CECOOP','CEDC','CELESC','CELPE','CEM','CEMC','CEMIG','CENT','CENTALINES','CENTMN','CENTRALNR','CEZ','CEZZV','CFLEC','CGEO','CGZ','CHAM','CHAMP','CHAP','CHATT','CHE','CHELAN','CHESA','CHEY','CHGE','CHICO','CHINAS','CHOC','CHOP','CHUBU','CHUDS','CHUG','CHURCH','CIGA','CITI','CITIZEN','CITYLP','CLAY','CLAYEC','CLECO','CLEW','CLOVER','CLP','CMEL','CMI','CMR','CNET','CNFL','CNL','CNP','CNR','CNRED','CNU','COAST','COBB','COELBA','COELCE','COGAS','COLLUS','COLQU','COLUMBIA','COMANCH','COMED','COMISION','COMMEC','CONC','CONED','CONN','COOKE','COPEL','CORN','COSERN','COSERV','COUNTIES','COW','CPEC','CPFL','CPSE','CSU','CURENT','CWE','CYPR','DAIRY','DAMODAR','DANVERS','DANVLLE','DAVAO','DAYTON','DCPUD','DEDDIE','DEER','DELA','DELMARVA','DENTON','DEWA','DGVCL','DHAKA','DHBVN','DICLE','DIRECT','DIVERSE','DMEC','DOBROGEA','DOM','DORA','DOVER','DPSC','DTE','DUB','DUKE','DUQ','E A','EAST','EASTLND','ECE','ECL','ECM','EDCO','EDF','EDL','EDN','EDR','EDS','EEJ','EET','EFR','EFTTF','EGAT','EGC','EGCB','EGN','EI','EIO','ELECPLSRL','ELECTRA','ELECTROMAGNETICAET','ELEK','ELENIA','Elia','ELK','ELV','EME','EnBW','END','ENEA','ENED','ENEKODEO','Enel','ENELE','ENERBRZ','ENERGA','ENERGIA','ENERGISA','ENERPORT','ENEX','ENEXE','ENGIE','ENMAXMX','ENOLO','ENTEGR','ENTERGY','ENTREXTE','ENU','ENWI','EOE','EOG','EON','EPCORCR','EPHR','EPN','EPR','EQUSU','ES','ESCEL','ESE','ESKOM','ESL','ESO','ESPH','ESRO','ESS','ESSEN','ESTI','ESX','ETG','ETSA','ETU','EUT','EUU','EVAAE','EVER','EVNNG','EVS','EWEB','EWR','EXELON','FE','FEC','FEWA','FFP','FIA','FIDELIS','FIRAT','FIVE','FLINT','FLOR','FMPA','FOBC','FORTIS','FOUR','FPL','FRANK','FROG','FRS','FSI','FYN','GAINS','GAR','GASEL','GAT','GAY','GAZ','GDFFS','GDM','GDZ','GES','GETICATC','GIS','GJA','GL','gLA','GLADES','GLE','GMTN','GOA','GOE','GOG','GOO','GOP','GP','GRE','GRNCOVE','GRNVLLE','GSA','GSO','GTC','GTN','GULF','HAIGER','HALD','HALTON','HAS','HAT','HATF','HAVANA','HAWK','HBI','HBR','HDL','HECO','HELCO','HELS','HEPPO','HGR','HILCOLO','HKA','HKR','HL','HLA','HLE','HLF','HLN','HLWD','HME','HML','HMS','HNH','HNK','HOLY','HONI','HOOS','HORZED','HR','HRZPWR','HUBPWR','HUDSON','HURUP','HYDER','HYDRO2K','HYDROOTT','HYDROQC','HYDROWEST','HYO','IAA','ICE','IDAHO','IDECO','IDGCG','IDIDEG','IEIEH','IGIGH','IID','IKEJA','ILLUM','IMATRA','IMEWO','IMIMEA','INDUSTRIALDS','INDY','INFRAX','INR','INS','INTER','INTEREST','INTERGEM','INTERLUX','INTERMO','INTERRAO','INVER','IPA','IPL','IPLC','IPSWIC','IRE','IRWIN','ISLAM','ITN','IVEKA','IVERLEK','IVIVEG','JAC','JASECSC','JCPL','JCS','JEA','JEPCO','JFE','JMN','JNS','JOVVN','JRM','JSE','JUST','JVVN','KADUNA','KANO','KANSAI','KARNPCL','KBN','KCPL','KELEC','KENYA','KEPCO','KEYS','KHA','KINGSPORT','KINGSTON','KIUC','KKM','KNR','KNU','KOV','KRL','KRØ','KSI','KTA','KTH','KUH','KUTZ','KY','KYE','KYI','LAD','LADWP','LAKE','LAKES','LANKO','LANSD','LCL','LCRA','LEB','LEC','LES','LESCA','LETH','LGT','LHR','LIBERTY','LIBPA','LIPA','LKL','LKLNDPD','LKWRTH','LMA','LME','LMN','LNI','LNN','LPÄ','LPE','LTE','LTLELWD','LUS','LVL','LWL','LWRCHRCH','LWRCRA','LWS','LXE','MADH','MADI','MAINZ','MANIC','MANITOBA','MANWEB','MARBLE','MARIT','MARL','MDS','MDU','MEADE','MEAG','MECK','MECO','MEDHAT','MEMP','MERA','MERAM','MERRI','METED','METRO','METTR','MGVCL','MHR','MICHP','MIDAM','MIDDLE','MIDGA','MIDLND','MIDSTH','MIDT','MIDTWN','MIDWEST','MILFORD','MILO','MILT','MILTON','MINK','MINN','MIP','MISS','MITCH','MMLD','MNA','MNF','MNP','MOHAWK','MONP','MONS','MOORE','MOSCOW','MRE','MULTAN','MUNTE','NAM','NARRA','NASH','NATUR','NAVA','NAVARRO','NBP','NCEMC','NDPL','NECK','NEGROEC','NELD','NELSON','NELSONHY','NEPTUN','NEREC','NERGEX','NESCL','NETWAIT','NEUK','NEWARK','NEWBRY','NEWCSTLE','NEXTERA','NEXTPWR','NEXTX','NFLLH','NFLP','NGEMC','NGPHILIP','NGSA','NGUK','NGUS','NHEC','NIA','NIAG','NIAGPEN','NORD','NORDSA','NORFOLK','NORTHERNRH','NORWEB','NOVA','NOW','NPCPHILIP','NPL','NPOW','NPPD','NRD','NRGi','NRI','NSPC','NSTAR','NSU','NTHBAYHY','NTPC','NVEC','NVP','NWA','NWREC','NWSTRN','NWT','NWTPC','NYE','NYFORS','NYPA','NYSE','OAKVLLE','OCALA','OCMU','OCMUEMC','OCONEE','ODISHA','ÖEU','OGLE','OHIOED','OHW','OIL','OIN','OKEF','OKIN','OKLA','OLDDOM','OLN','OMAHA','OMN','ONCOR','ONTARIO','OPALCO','ORANGE','ORPC','ORSTED','OSHEEHE','OTAGO','OTTER','PACIF','PACPCPS','PACPWR','PAE','PAO','PARRY','PASCH','PBE','PDD','PDR','PECO','PED','PEM','PENELEC','PENNPWR','PENTIC','PEPCO','PEPCOPO','PGCBL','PGEC','PGEED','PGT','PGVCL','PHILIP','PHO','PHOTOVOLTAICOO','PIERCE','PK','PKRDGE','PLANT','PLATTE','PLINK','PME','PNA','PNL','PNN','POI','POORV','POTO','POWERWR','POWS','PPL','PPLLE','PR','PRA','PREEI','PRINCELD','PRL','PRS','PSA','PSCC','PSCNH','PSCNM','PSCOKLA','PSEG','PSEGC','PSO','PT','PTIIE','PTR','PUC','PWC','PWRCO','PWRCORE','PWRGDCI','PWRSTH','PXO','QET','QLI','QUAKE','QUIN','RAI','RAJDH','RAO','RCKYMTN','RCSS&','RDA','REAAE','rEE','RENDO','RENOVATIONV','RESA','RESTARTSA','REY','RGE','RLA','RNO','RNR','ROCK','ROMELECTROML','ROWL','RPA','RRL','RSE','RTE','RUIZ','RWE','RYE','SAC','SALL','SAM','SANTOS','SARAW','SASK','SASKA','SAVON','SAWNEE','SBPDCL','SC','SCA','SCAN','SCE','SCEGC','SCM','SCOTHY','SCOTPWR','SDCC','SEAFRD','SEASA','SEASD','SEATCL','SELD','SES','SESCO','SEUD','SEWA','SGCC','SGO','SHELD','SHEN','SHIK','SHREWS','SIBEL','SILLA','SIMO','SINGA','SIOUX','SJI','SKR','SL-','SLASH','SMECO','SMED','SMN','SMYRNA','SMYRNAEC','SNAP','SND','SNOHOM','SOCO','SOLLEN','SOMER','SOREG','SORGE','SPEC','SPRING','SREMC','SRP','SSES','STARKE','STCLOUD','STEDIN','STHRVR','STHRVRS','STJEAN','STJOE','STOCK','STRUER','STTHOMAS','SUDBURY','SUKKUR','SULLICREC','SUMMER','SUMTEREC','SURRY','SUSS','SUWVEC','SWEPC','SWEPCO','SWEUK','SWIFT','SWLSE','SWPSC','SYDFYNS','TACOMA','TALLA','TALQ','TAMIL','TANESCO','TANNER','TARA','TASMAN','TATA','TAUNT','TAUR','TAVAN','TECO','TEMPMLC','TENNET','TEOLL','TEPCO','TERNA','THREE','THUND','THURMLC','TIAWAN','TIDE','TIDWP','TIEK','TILLS','TINM','TLC','TNMP','TOHOKU','TOHYDRO','TOLEDO','TOLEDOED','TOP','TOROS','TORRENT','TPC','TRAKYA','TRANSALTA','TRANSCA','TRANSENERGOAS','TRANSGRID','TRANSILVNORD','TRANSIVSUD','TREFOR','TRIBE','TRIECOOP','TRIEMC','TRIREC','TRISTATE','TSECL','TSENER','TUSC','TVA','TVPPA','TWIN','TXUE','TYUM','UCS','UEDC','UGIU','UGVCL','UHBVN','UI','UNION','UNISON','UNISRC','UNITED','UNITEDCOOP','UNITEDU','UNITIL','UNTIL','UPPC','UPPENPC','UPRMISSPC','UPSON','VALLEY','VANT','VARA','VATA','VATTEN','VCO','VEC','VECO','VENTUSNU','VERDO','VERI','VERO','VGEDC','VINE','VKA','VKGE','WACH','WAIPA','WAKE','WAKEMGLD','WALTON','WAPA','WARREN','WASAGA','WASHEMC','WATERLOO','WBSEDCL','WEC','WELL','WELLES','WELLI','WELLNTHP','WELLS','WELN','WENER','WERKR','WESPD','WEST','WESTAR','WESTARIO','WESTFLD','WESTINFRA','WESTMIN','WESTNETZ','WESTPOW','WFEC','WHIT','WILLI','WILLUTIL','WINDHOEK','WIRE','WISC','WISE','WITHLA','WNTRPRK','WOOD','WPDA','WPSC','WSTFLEC','WSTPENNPWR','WYAN','XCEL','YAMUNA','YELLOW','YNA','YOLA','YORK','YUKON','ZONE'])


def BushingManufacturerList():
    '''Return the current schema_1 BushingManufacturer list for the BushingDetails table.

    Returns:
            List of strings

    '''
    return(['ABB',
            'ECI',
            'GE',
            'HEAFT',
            'HSP',
            'LAPP',
            'MCGR',
            'MICA',
            'OHIO',
            'PCORE',
            'PENN',
            'PIED',
            'PROLEC',
            'SIEM',
            'TRENCH',
            'WAUK',
            'WEST',
            ])


def BushingModelList():
    '''Return the current schema_1 BushingModel list for the BushingDetails table.

    Returns:
            List of strings

    '''
    return(['A',
            'AB',
            'COTA',
            'F',
            'FS',
            'G',
            'GK',
            'GK30',
            'GK40',
            'LCRJ',
            'O',
            'OF',
            'OPLUSC',
            'OS',
            'P',
            'PA',
            'PB',
            'POC',
            'POCA',
            'PRC',
            'PRCA',
            'R10',
            'RTF',
            'RTXF',
            'S',
            'SDC',
            'SETFTA',
            'T',
            'U',
            ])
