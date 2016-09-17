#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 yqiu <yqiu@f24-suntzu>
#
# Distributed under terms of the MIT license.
# TODO: combine RESS buildings
# combine IVES HALL, EAST WEST ....

import pandas as pd
import buildings as bds
import re

builds = bds.builds

def create_url(bd):
    ur1 = "http://portal.emcs.cornell.edu/"
    ur2 = "?cmd=csv&s=1d&b=1474084800&e=1474171200"
    return ur1 + bd + ur2

pdic = {}
for bdg in builds:
    bd = "".join(bdg.split())

    url = create_url(bd)
    print url, "is the url"
    data = pd.read_csv(url)

    # rename unnamed to timestamp
    new_cols = data.columns.values
    new_cols[0] = 'timestamp'
    data.columns = new_cols

    # drop columns except for timestamp and electric
    data_keep = data.filter(regex='kW|timestamp')
    # if only 1 col (timestamp) so no elec pass
    if len(data_keep.columns.values[:]) <= 1:
        continue

    elec = data_keep.columns.values[:]
    data_keep = data_keep[ data_keep[elec[1]] != "nodata" ]

    # lst.append(data_keep.tail(1))
    data_keep = data_keep.tail(1)
    try:
        pdic[bdg] = float(data_keep.iloc[0][elec[1]])
    except:
        print "in except"

def sum_exception(dct,rgx,new):
    """ returns a modified dict with the power values of all regex matched
    buildings summed into one pair

    :dct: dictionary of building,power k-v pairs
    :rgx: regex expression

    :returns: modified dict
    """
    cumPow = 0
    # print [ k for k in pdic.keys() if re.match(rgx,k) ]
    for mvs in [ k for k in pdic.keys() if
                re.match(rgx,k) ]:
        cumPow += dct[mvs]
        del dct[mvs]
    dct[new] = cumPow
    # print dct[new]

sum_exception(pdic,"Martha VanRensselaer\s.+","Martha VanRensselaer")
sum_exception(pdic,"^Vet\s.+","Vet School")

# print pdic


if __name__ == "__main__":
    pass
