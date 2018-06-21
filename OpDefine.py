#!/usr/bin/python

from enum import Enum
import requests
from bs4 import BeautifulSoup
import json

__authon__ = "salmansamie"


class ConfigReq(Enum):
    web_query = 'https://www.google.co.uk/search?q=define+{arg}'
    df_parser = 'lxml'


class DFX:

    gl_parser = ConfigReq.df_parser.value

    def __init__(self, vocable):
        self.vocable = vocable

    def dfx_get(self):
        try:
            _uri = (str(ConfigReq.web_query.value)).format(arg=self.vocable)
            return requests.get(_uri, headers=requests.utils.default_headers()).text

        except requests.RequestException as error:
            print(
                """
                Error handled at the superclass of exceptions:
                <http://docs.python-requests.org/en/master/api/#requests.RequestException>
                """ + str(error))

    def define(self):
        _source = str(DFX(self.vocable).dfx_get())
        _r_data = BeautifulSoup(_source, DFX.gl_parser).find("div", {"class": "g"}).find("div")
        return DFX.analyzer(_r_data)

    @staticmethod
    def analyzer(arg):
        word_accn = arg.findAll("h3", {"class": "r"})
        defn_data = list(_x.find('tr').find('td') for _x in arg.findAll("table", style="font-size:14px;width:100%"))
        defn_builder = list(_ol.find('ol').findAll('li') for _ol in defn_data)
        flat_list = [_w.text for _li in defn_builder for _w in _li]

        if flat_list:
            data = {
                "responses": len(word_accn),                    # item count
                "vocables": list(_z.text for _z in word_accn),  # item list
                "definitions": flat_list,
            }
            return data

        else:
            return "No concrete definition found for the entered string"
