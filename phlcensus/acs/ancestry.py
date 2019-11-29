from .core import ACSDataset
import collections

__all__ = ["Ancestry"]


class Ancestry(ACSDataset):
    """
    People reporting single ancestry.
    """

    AGGREGATION = "count"
    UNIVERSE = "people reporting single ancestry"
    TABLE_NAME = "B04004"
    RAW_FIELDS = collections.OrderedDict(
        {
            "001": "universe",
            "002": "afghan",
            "003": "albanian",
            "004": "alsatian",
            "005": "american",
            "006": "arab",
            "007": "egyptian",
            "008": "iraqi",
            "009": "jordanian",
            "010": "lebanese",
            "011": "moroccan",
            "012": "palestinian",
            "013": "syrian",
            "014": "all_arab",
            "015": "other_arab",
            "016": "armenian",
            "017": "assyrian_chaldean_syriac",
            "018": "australian",
            "019": "austrian",
            "020": "basque",
            "021": "belgian",
            "022": "brazilian",
            "023": "british",
            "024": "bulgarian",
            "025": "cajun",
            "026": "canadian",
            "027": "carpatho_rusyn",
            "028": "celtic",
            "029": "croatian",
            "030": "cypriot",
            "031": "czech",
            "032": "czechoslovakian",
            "033": "danish",
            "034": "dutch",
            "035": "eastern_european",
            "036": "english",
            "037": "estonian",
            "038": "european",
            "039": "finnish",
            "040": "french_except_basque",
            "041": "french_canadian",
            "042": "german",
            "043": "german_russian",
            "044": "greek",
            "045": "guyanese",
            "046": "hungarian",
            "047": "icelander",
            "048": "iranian",
            "049": "irish",
            "050": "israeli",
            "051": "italian",
            "052": "latvian",
            "053": "lithuanian",
            "054": "luxemburger",
            "055": "macedonian",
            "056": "maltese",
            "057": "new_zealander",
            "058": "northern_european",
            "059": "norwegian",
            "060": "pennsylvania_german",
            "061": "polish",
            "062": "portuguese",
            "063": "romanian",
            "064": "russian",
            "065": "scandinavian",
            "066": "scotch-irish",
            "067": "scottish",
            "068": "serbian",
            "069": "slavic",
            "070": "slovak",
            "071": "slovene",
            "072": "soviet_union",
            "073": "subsaharan_african",
            "074": "cape_verdean",
            "075": "ethiopian",
            "076": "ghanaian",
            "077": "kenyan",
            "078": "liberian",
            "079": "nigerian",
            "080": "senegalese",
            "081": "sierra_leonean",
            "082": "somali",
            "083": "south_african",
            "084": "sudanese",
            "085": "ugandan",
            "086": "zimbabwean",
            "087": "african",
            "088": "other_subsaharan_african",
            "089": "swedish",
            "090": "swiss",
            "091": "turkish",
            "092": "ukranian",
            "093": "welsh",
            "094": "west_indian_except_hispanic_groups",
            "095": "bahamian",
            "096": "barbadian",
            "097": "belizean",
            "098": "bermudan",
            "099": "british_west_indian",
            "100": "dutch_west_indian",
            "101": "haitian",
            "102": "jamaican",
            "103": "trinidadian_and_tobagonian",
            "104": "us_virgin_islander",
            "105": "west_indian",
            "106": "other_west_indian",
            "107": "yugoslavian",
            "108": "other_groups",
        }
    )
