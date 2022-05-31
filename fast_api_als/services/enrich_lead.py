import calendar
import time
import logging
from dateutil import parser
from fast_api_als.database.db_helper import db_helper_session

from fast_api_als import constants

"""
what exceptions can be thrown here?
"""


def get_enriched_lead_json(adf_json: dict) -> dict:
    if not isinstance(adf_json, dict):
        raise TypeError

    d = dict()
    try:
        d['something']= adf_json['something'] 
    except:
        raise KeyError()
    logging.info("Got enriched lead json.")
    return d 