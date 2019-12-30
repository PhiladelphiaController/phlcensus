from .core import ACSDataset
import collections

__all__ = ["SNAP"]


class SNAP(CensusDataset):
    """
    Household received Food Stamps/SNAP in the past 12 months
    """

    UNIVERSE = "household"
    TABLE_NAME = "B22003"
    RAW_FIELDS = collections.OrderedDict(
        {"001": "universe", "002": "recipient", "05": "nonrecipient"}
    )
