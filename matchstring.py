# !/usr/bin/python
# -*- coding: utf-8 -*-
# --------------------------------------------------  # {{{
# Name:        matchstring.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     04/11/2016
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10017
# --------------------------------------------------
# }}}
""" 正規表現による文字列のマッチング """

# モジュール インポート
import re


class MatchString:
    def __init__(self):
        pass

    def c59k1_lens_id(self, read):
        self.read = read

        desit = 13
        # search_1 = re.compile("[PAVCX][A-Z1-9]{2,2}[0-9][A-L]34")
        search_1 = re.compile("[PAVCX][A-Z1-9]{2,2}[0-9][A-L][0-9]{2,2}")
        search_2 = re.compile("[0-9]{2,2}")
        # search_3 = re.compile("0005")
        search_3 = re.compile("[0-9]{4,4}")

        if len(self.read) == desit:
            read_1 = self.read[:7]
            read_2 = self.read[7:9]
            read_3 = self.read[9:]

            print(read_1)
            print(read_2)
            print(read_3)

            match_1 = search_1.search(read_1)
            match_2 = search_2.search(read_2)
            match_3 = search_3.search(read_3)
            match = match_1, match_2, match_3

            if None not in match:
                print("Code is match")
                print("")
                return True, match_1, match_2, match_3

            else:
                print("NG code")
                print("")
                return False, match_1, match_2, match_3

        else:
            print("NG disit")
            print("")
            return False, None, None, None


def main():
    mst = MatchString()
    print("OK test1: ")
    print(mst.c59k1_lens_id("X126A34010006"))
    print("")

    print("OK test2: ")
    print(mst.c59k1_lens_id("X126A24040005"))
    print("")

    print("NG code1: ")
    print(mst.c59k1_lens_id("X126M34409999"))
    print("")

    print("NG code2: ")
    print(mst.c59k1_lens_id("X126A00400005"))
    print("")

    print("NG disit: ")
    print(mst.c59k1_lens_id("X126X99199999"))
    print("")

if __name__ == "__main__":
    main()
