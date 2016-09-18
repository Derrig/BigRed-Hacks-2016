#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 yqiu <yqiu@f24-suntzu>
#
# Distributed under terms of the MIT license.
# TODO:
# [x] combine RESS buildings
# [x] combine IVES HALL, EAST WEST ....
# [ ] fix psb
# [ ] create power graphs in python
# [x] cache systems

import pandas as pd
import buildings as bds
import re

no_data = []

def create_url(bd):
    ur1 = "http://portal.emcs.cornell.edu/"
    ur2 = "?cmd=csv&s=1d&b=1474084800&e=1474171200"
    return ur1 + bd + ur2

def parse_csv():
    builds = bds.builds

    pdic = {}
    for bdg in builds:
        psb = bdg == "Physical Sciences"

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
        # for i in xrange(1,len(elec)):
        #     data_keep = data_keep[ data_keep[elec[i]] != "nodata" ]
        data_keep = data_keep[ data_keep[elec[1]] != "nodata" ]

        ############################## psb ###########
        # images
        if psb:
            print "doing physical sciences buildings"
            data_keep = data_keep[ data_keep[elec[2]] != "nodata" ]
            data_keep['sum_kw_system'] = data_keep[elec[1]] + data_keep[elec[2]]
            print data_keep['sum_kw_system']
            elec = data_keep.columns.values[:]
            df.drop(elec[1], axis=1, inplace=True)
            df.drop(elec[2], axis=1, inplace=True)

        # lst.append(data_keep.tail(1))
        data_keep = data_keep.tail(1)
        try:
            pdic[bdg] = float(data_keep.iloc[0][elec[1]])
        except:
            print "in except"
            print bdg
            print data_keep
            no_data.append(bdg)
    return pdic

def sum_exception(dct,rgx,new):
    """ modifies dict with the power values of all regex matched
    buildings summed into one pair

    :dct: dictionary of building,power k-v pairs
    :rgx: regex expression
    """
    cumPow = 0
    print [ k for k in dct.keys() if re.match(rgx,k) ]
    for mvs in [ k for k in dct.keys() if
                re.match(rgx,k) ]:
        cumPow += dct[mvs]
        del dct[mvs]
    dct[new] = cumPow
    # print dct[new]

def time_series(df):

    pass

def main():
    pdic = parse_csv()
    print len(pdic)
    sum_exception(pdic,"^Martha VanRensselaer\s.+","Martha VanRensselaer")
    print len(pdic)
    sum_exception(pdic,"^Vet\s.+","Vet School")
    print len(pdic)
    sum_exception(pdic,"^Ives\s.+","Ives")
    print len(pdic)
    sum_exception(pdic,"^Friedman\s.+","Friedman Wrestling Center")
    # sum_exception(pdic)
    print no_data
    return pdic


if __name__ == "__main__":
    main()

