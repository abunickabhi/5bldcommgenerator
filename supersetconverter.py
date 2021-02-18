# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:44:35 2021

@author: abhij
"""

import re
string = "L NF2 L NU' L' NF2 L NR2 NU R2 NU' NR2 NU SR2 "

string = re.sub(r'(NF )(?!\')', '2F ', string)
string = re.sub(r'(NF\' )(?!\')', '2F\' ', string)
string = re.sub(r'(NF2 )(?!\')', '2F2 ', string)
string = re.sub(r'(NR )(?!\')', '2R ', string)
string = re.sub(r'(NR\' )(?!\')', '2R\' ', string)
string = re.sub(r'(NR2 )(?!\')', '2R2 ', string)
string = re.sub(r'(NL )(?!\')', '2L ', string)
string = re.sub(r'(NL\' )(?!\')', '2L\' ', string)
string = re.sub(r'(NL2 )(?!\')', '2L2 ', string)
string = re.sub(r'(NU )(?!\')', '2U ', string)
string = re.sub(r'(NU\' )(?!\')', '2U\' ', string)
string = re.sub(r'(NU2 )(?!\')', '2U2 ', string)
string = re.sub(r'(ND )(?!\')', '2D ', string)
string = re.sub(r'(ND\' )(?!\')', '2D\' ', string)
string = re.sub(r'(ND2 )(?!\')', '2D2 ', string)
string = re.sub(r'(NB )(?!\')', '2B ', string)
string = re.sub(r'(NB\' )(?!\')', '2B\' ', string)
string = re.sub(r'(NB2 )(?!\')', '2B2 ', string)

string = re.sub(r'(TF )(?!\')', 'f ', string)
string = re.sub(r'(TF\' )(?!\')', 'f\' ', string)
string = re.sub(r'(TF2 )(?!\')', 'f2 ', string)
string = re.sub(r'(TR )(?!\')', 'r ', string)
string = re.sub(r'(TR\' )(?!\')', 'r\' ', string)
string = re.sub(r'(TR2 )(?!\')', 'r2 ', string)
string = re.sub(r'(TL )(?!\')', 'l ', string)
string = re.sub(r'(TL\' )(?!\')', 'l\' ', string)
string = re.sub(r'(TL2 )(?!\')', 'l2 ', string)
string = re.sub(r'(TU )(?!\')', 'u ', string)
string = re.sub(r'(TU\' )(?!\')', 'u\' ', string)
string = re.sub(r'(TU2 )(?!\')', 'u2 ', string)
string = re.sub(r'(TD )(?!\')', 'd ', string)
string = re.sub(r'(TD\' )(?!\')', 'd\' ', string)
string = re.sub(r'(TD2 )(?!\')', 'd2 ', string)
string = re.sub(r'(TB )(?!\')', 'b ', string)
string = re.sub(r'(TB\' )(?!\')', 'b\' ', string)
string = re.sub(r'(TB2 )(?!\')', 'b2 ', string)

string = re.sub(r'(SF )(?!\')', 'F B\' ', string)
string = re.sub(r'(SF\' )(?!\')', 'F\' B ', string)
string = re.sub(r'(SF2 )(?!\')', 'F2 B2 ', string)
string = re.sub(r'(SR )(?!\')', 'R L\' ', string)
string = re.sub(r'(SR\' )(?!\')', 'R\' L ', string)
string = re.sub(r'(SR2 )(?!\')', 'L2 R2 ', string)
string = re.sub(r'(SU )(?!\')', 'U D\' ', string)
string = re.sub(r'(SU\' )(?!\')', 'U\' D ', string)
string = re.sub(r'(SU2 )(?!\')', 'U2 D2 ', string)
print(string)