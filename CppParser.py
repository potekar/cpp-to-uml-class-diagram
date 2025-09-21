# Generated from grammar/CppParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,72,476,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,1,0,3,0,88,8,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,5,1,97,8,1,10,1,12,1,100,9,1,1,2,1,2,3,2,104,8,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,3,3,114,8,3,1,3,3,3,117,8,3,1,3,1,3,1,3,
        1,3,3,3,123,8,3,1,4,1,4,1,5,1,5,1,5,5,5,130,8,5,10,5,12,5,133,9,
        5,1,6,3,6,136,8,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,144,8,7,10,7,12,7,
        147,9,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,161,
        8,9,1,9,3,9,164,8,9,1,10,1,10,1,10,3,10,169,8,10,1,11,1,11,1,11,
        3,11,174,8,11,1,12,1,12,1,12,3,12,179,8,12,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,3,13,188,8,13,1,14,1,14,1,14,5,14,193,8,14,10,14,12,
        14,196,9,14,1,15,1,15,1,15,1,16,5,16,202,8,16,10,16,12,16,205,9,
        16,1,16,1,16,1,16,1,16,3,16,211,8,16,1,16,1,16,5,16,215,8,16,10,
        16,12,16,218,9,16,1,17,5,17,221,8,17,10,17,12,17,224,9,17,1,17,1,
        17,1,18,5,18,229,8,18,10,18,12,18,232,9,18,1,18,1,18,1,18,1,18,1,
        18,3,18,239,8,18,1,18,5,18,242,8,18,10,18,12,18,245,9,18,1,19,1,
        19,1,19,5,19,250,8,19,10,19,12,19,253,9,19,1,20,1,20,1,20,1,20,3,
        20,259,8,20,1,21,1,21,3,21,263,8,21,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        296,8,23,1,24,1,24,1,24,5,24,301,8,24,10,24,12,24,304,9,24,1,25,
        5,25,307,8,25,10,25,12,25,310,9,25,1,25,1,25,3,25,314,8,25,1,25,
        1,25,3,25,318,8,25,1,26,1,26,1,27,5,27,323,8,27,10,27,12,27,326,
        9,27,1,27,1,27,1,27,1,27,3,27,332,8,27,1,28,1,28,1,28,3,28,337,8,
        28,1,28,1,28,1,28,3,28,342,8,28,1,28,1,28,1,28,1,28,3,28,348,8,28,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,358,8,29,1,30,1,30,
        1,30,5,30,363,8,30,10,30,12,30,366,9,30,1,31,1,31,1,31,3,31,371,
        8,31,1,31,1,31,1,32,1,32,1,32,5,32,378,8,32,10,32,12,32,381,9,32,
        1,33,1,33,1,34,5,34,386,8,34,10,34,12,34,389,9,34,1,34,1,34,1,34,
        1,34,3,34,395,8,34,1,34,1,34,5,34,399,8,34,10,34,12,34,402,9,34,
        1,34,1,34,1,34,1,34,1,35,5,35,409,8,35,10,35,12,35,412,9,35,1,35,
        1,35,1,35,1,35,3,35,418,8,35,1,35,1,35,5,35,422,8,35,10,35,12,35,
        425,9,35,1,35,1,35,1,35,1,35,1,36,5,36,432,8,36,10,36,12,36,435,
        9,36,1,37,5,37,438,8,37,10,37,12,37,441,9,37,1,38,5,38,444,8,38,
        10,38,12,38,447,9,38,1,39,1,39,1,39,1,39,3,39,453,8,39,1,39,1,39,
        1,39,1,39,1,39,1,40,5,40,461,8,40,10,40,12,40,464,9,40,1,41,1,41,
        1,41,1,41,3,41,470,8,41,1,41,1,41,1,42,1,42,1,42,0,0,43,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,0,13,1,0,1,2,
        1,0,3,5,2,0,1,1,71,71,2,0,8,10,19,23,2,0,8,9,18,18,1,0,7,9,1,0,8,
        9,1,0,64,65,2,0,39,39,51,52,1,0,60,65,2,0,7,9,21,23,1,0,6,10,4,0,
        24,40,42,60,63,65,70,70,524,0,87,1,0,0,0,2,98,1,0,0,0,4,101,1,0,
        0,0,6,109,1,0,0,0,8,124,1,0,0,0,10,126,1,0,0,0,12,135,1,0,0,0,14,
        145,1,0,0,0,16,148,1,0,0,0,18,160,1,0,0,0,20,165,1,0,0,0,22,170,
        1,0,0,0,24,175,1,0,0,0,26,180,1,0,0,0,28,189,1,0,0,0,30,197,1,0,
        0,0,32,203,1,0,0,0,34,222,1,0,0,0,36,230,1,0,0,0,38,246,1,0,0,0,
        40,258,1,0,0,0,42,262,1,0,0,0,44,264,1,0,0,0,46,295,1,0,0,0,48,297,
        1,0,0,0,50,308,1,0,0,0,52,319,1,0,0,0,54,324,1,0,0,0,56,333,1,0,
        0,0,58,349,1,0,0,0,60,359,1,0,0,0,62,367,1,0,0,0,64,374,1,0,0,0,
        66,382,1,0,0,0,68,387,1,0,0,0,70,410,1,0,0,0,72,433,1,0,0,0,74,439,
        1,0,0,0,76,445,1,0,0,0,78,448,1,0,0,0,80,462,1,0,0,0,82,465,1,0,
        0,0,84,473,1,0,0,0,86,88,3,2,1,0,87,86,1,0,0,0,87,88,1,0,0,0,88,
        89,1,0,0,0,89,90,5,0,0,1,90,1,1,0,0,0,91,97,3,4,2,0,92,97,3,6,3,
        0,93,97,3,82,41,0,94,97,3,84,42,0,95,97,3,78,39,0,96,91,1,0,0,0,
        96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,100,1,
        0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,3,1,0,0,0,100,98,1,0,0,0,101,
        103,5,13,0,0,102,104,5,64,0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,
        105,1,0,0,0,105,106,5,30,0,0,106,107,3,2,1,0,107,108,5,31,0,0,108,
        5,1,0,0,0,109,110,3,8,4,0,110,116,5,64,0,0,111,113,5,24,0,0,112,
        114,3,16,8,0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,
        117,3,10,5,0,116,111,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,
        119,5,30,0,0,119,120,3,14,7,0,120,122,5,31,0,0,121,123,5,25,0,0,
        122,121,1,0,0,0,122,123,1,0,0,0,123,7,1,0,0,0,124,125,7,0,0,0,125,
        9,1,0,0,0,126,131,3,12,6,0,127,128,5,26,0,0,128,130,3,12,6,0,129,
        127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,
        11,1,0,0,0,133,131,1,0,0,0,134,136,3,16,8,0,135,134,1,0,0,0,135,
        136,1,0,0,0,136,137,1,0,0,0,137,138,5,64,0,0,138,13,1,0,0,0,139,
        140,3,16,8,0,140,141,5,24,0,0,141,144,1,0,0,0,142,144,3,18,9,0,143,
        139,1,0,0,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,
        146,1,0,0,0,146,15,1,0,0,0,147,145,1,0,0,0,148,149,7,1,0,0,149,17,
        1,0,0,0,150,161,3,20,10,0,151,161,3,22,11,0,152,161,3,24,12,0,153,
        161,3,26,13,0,154,161,3,32,16,0,155,161,3,54,27,0,156,161,3,56,28,
        0,157,161,3,58,29,0,158,161,3,68,34,0,159,161,3,70,35,0,160,150,
        1,0,0,0,160,151,1,0,0,0,160,152,1,0,0,0,160,153,1,0,0,0,160,154,
        1,0,0,0,160,155,1,0,0,0,160,156,1,0,0,0,160,157,1,0,0,0,160,158,
        1,0,0,0,160,159,1,0,0,0,161,163,1,0,0,0,162,164,5,25,0,0,163,162,
        1,0,0,0,163,164,1,0,0,0,164,19,1,0,0,0,165,168,5,7,0,0,166,169,3,
        32,16,0,167,169,3,54,27,0,168,166,1,0,0,0,168,167,1,0,0,0,169,21,
        1,0,0,0,170,173,5,6,0,0,171,174,3,32,16,0,172,174,3,54,27,0,173,
        171,1,0,0,0,173,172,1,0,0,0,174,23,1,0,0,0,175,178,5,11,0,0,176,
        179,5,64,0,0,177,179,3,32,16,0,178,176,1,0,0,0,178,177,1,0,0,0,179,
        25,1,0,0,0,180,181,5,12,0,0,181,182,5,42,0,0,182,183,3,28,14,0,183,
        187,5,43,0,0,184,188,3,6,3,0,185,188,3,32,16,0,186,188,3,54,27,0,
        187,184,1,0,0,0,187,185,1,0,0,0,187,186,1,0,0,0,188,27,1,0,0,0,189,
        194,3,30,15,0,190,191,5,26,0,0,191,193,3,30,15,0,192,190,1,0,0,0,
        193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,29,1,0,0,0,196,
        194,1,0,0,0,197,198,7,2,0,0,198,199,5,64,0,0,199,31,1,0,0,0,200,
        202,7,3,0,0,201,200,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,
        204,1,0,0,0,204,206,1,0,0,0,205,203,1,0,0,0,206,207,3,34,17,0,207,
        208,3,42,21,0,208,210,5,32,0,0,209,211,3,48,24,0,210,209,1,0,0,0,
        210,211,1,0,0,0,211,212,1,0,0,0,212,216,5,33,0,0,213,215,7,4,0,0,
        214,213,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,
        217,33,1,0,0,0,218,216,1,0,0,0,219,221,7,5,0,0,220,219,1,0,0,0,221,
        224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,225,1,0,0,0,224,
        222,1,0,0,0,225,226,3,36,18,0,226,35,1,0,0,0,227,229,7,6,0,0,228,
        227,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,231,
        233,1,0,0,0,232,230,1,0,0,0,233,238,7,7,0,0,234,235,5,42,0,0,235,
        236,3,38,19,0,236,237,5,43,0,0,237,239,1,0,0,0,238,234,1,0,0,0,238,
        239,1,0,0,0,239,243,1,0,0,0,240,242,7,8,0,0,241,240,1,0,0,0,242,
        245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,37,1,0,0,0,245,243,
        1,0,0,0,246,251,3,40,20,0,247,248,5,26,0,0,248,250,3,40,20,0,249,
        247,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,252,
        39,1,0,0,0,253,251,1,0,0,0,254,259,3,36,18,0,255,259,5,60,0,0,256,
        259,5,64,0,0,257,259,5,65,0,0,258,254,1,0,0,0,258,255,1,0,0,0,258,
        256,1,0,0,0,258,257,1,0,0,0,259,41,1,0,0,0,260,263,5,64,0,0,261,
        263,3,44,22,0,262,260,1,0,0,0,262,261,1,0,0,0,263,43,1,0,0,0,264,
        265,5,72,0,0,265,266,3,46,23,0,266,45,1,0,0,0,267,296,5,36,0,0,268,
        296,5,37,0,0,269,296,5,38,0,0,270,296,5,39,0,0,271,296,5,40,0,0,
        272,296,5,41,0,0,273,296,5,42,0,0,274,296,5,43,0,0,275,296,5,44,
        0,0,276,296,5,45,0,0,277,296,5,46,0,0,278,296,5,47,0,0,279,296,5,
        48,0,0,280,296,5,49,0,0,281,296,5,50,0,0,282,296,5,51,0,0,283,296,
        5,52,0,0,284,296,5,53,0,0,285,296,5,54,0,0,286,296,5,55,0,0,287,
        296,5,56,0,0,288,296,5,57,0,0,289,296,5,58,0,0,290,296,5,59,0,0,
        291,292,5,32,0,0,292,296,5,33,0,0,293,294,5,34,0,0,294,296,5,35,
        0,0,295,267,1,0,0,0,295,268,1,0,0,0,295,269,1,0,0,0,295,270,1,0,
        0,0,295,271,1,0,0,0,295,272,1,0,0,0,295,273,1,0,0,0,295,274,1,0,
        0,0,295,275,1,0,0,0,295,276,1,0,0,0,295,277,1,0,0,0,295,278,1,0,
        0,0,295,279,1,0,0,0,295,280,1,0,0,0,295,281,1,0,0,0,295,282,1,0,
        0,0,295,283,1,0,0,0,295,284,1,0,0,0,295,285,1,0,0,0,295,286,1,0,
        0,0,295,287,1,0,0,0,295,288,1,0,0,0,295,289,1,0,0,0,295,290,1,0,
        0,0,295,291,1,0,0,0,295,293,1,0,0,0,296,47,1,0,0,0,297,302,3,50,
        25,0,298,299,5,26,0,0,299,301,3,50,25,0,300,298,1,0,0,0,301,304,
        1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,49,1,0,0,0,304,302,1,
        0,0,0,305,307,7,6,0,0,306,305,1,0,0,0,307,310,1,0,0,0,308,306,1,
        0,0,0,308,309,1,0,0,0,309,311,1,0,0,0,310,308,1,0,0,0,311,313,3,
        36,18,0,312,314,5,64,0,0,313,312,1,0,0,0,313,314,1,0,0,0,314,317,
        1,0,0,0,315,316,5,36,0,0,316,318,3,52,26,0,317,315,1,0,0,0,317,318,
        1,0,0,0,318,51,1,0,0,0,319,320,7,9,0,0,320,53,1,0,0,0,321,323,7,
        10,0,0,322,321,1,0,0,0,323,326,1,0,0,0,324,322,1,0,0,0,324,325,1,
        0,0,0,325,327,1,0,0,0,326,324,1,0,0,0,327,328,3,36,18,0,328,331,
        5,64,0,0,329,330,5,36,0,0,330,332,3,52,26,0,331,329,1,0,0,0,331,
        332,1,0,0,0,332,55,1,0,0,0,333,334,5,64,0,0,334,336,5,32,0,0,335,
        337,3,48,24,0,336,335,1,0,0,0,336,337,1,0,0,0,337,338,1,0,0,0,338,
        341,5,33,0,0,339,340,5,24,0,0,340,342,3,60,30,0,341,339,1,0,0,0,
        341,342,1,0,0,0,342,347,1,0,0,0,343,344,5,30,0,0,344,345,3,74,37,
        0,345,346,5,31,0,0,346,348,1,0,0,0,347,343,1,0,0,0,347,348,1,0,0,
        0,348,57,1,0,0,0,349,350,5,58,0,0,350,351,5,64,0,0,351,352,5,32,
        0,0,352,357,5,33,0,0,353,354,5,30,0,0,354,355,3,76,38,0,355,356,
        5,31,0,0,356,358,1,0,0,0,357,353,1,0,0,0,357,358,1,0,0,0,358,59,
        1,0,0,0,359,364,3,62,31,0,360,361,5,26,0,0,361,363,3,62,31,0,362,
        360,1,0,0,0,363,366,1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,
        61,1,0,0,0,366,364,1,0,0,0,367,368,5,64,0,0,368,370,5,32,0,0,369,
        371,3,64,32,0,370,369,1,0,0,0,370,371,1,0,0,0,371,372,1,0,0,0,372,
        373,5,33,0,0,373,63,1,0,0,0,374,379,3,66,33,0,375,376,5,26,0,0,376,
        378,3,66,33,0,377,375,1,0,0,0,378,381,1,0,0,0,379,377,1,0,0,0,379,
        380,1,0,0,0,380,65,1,0,0,0,381,379,1,0,0,0,382,383,7,9,0,0,383,67,
        1,0,0,0,384,386,7,11,0,0,385,384,1,0,0,0,386,389,1,0,0,0,387,385,
        1,0,0,0,387,388,1,0,0,0,388,390,1,0,0,0,389,387,1,0,0,0,390,391,
        3,34,17,0,391,392,3,42,21,0,392,394,5,32,0,0,393,395,3,48,24,0,394,
        393,1,0,0,0,394,395,1,0,0,0,395,396,1,0,0,0,396,400,5,33,0,0,397,
        399,7,4,0,0,398,397,1,0,0,0,399,402,1,0,0,0,400,398,1,0,0,0,400,
        401,1,0,0,0,401,403,1,0,0,0,402,400,1,0,0,0,403,404,5,30,0,0,404,
        405,3,72,36,0,405,406,5,31,0,0,406,69,1,0,0,0,407,409,7,11,0,0,408,
        407,1,0,0,0,409,412,1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,
        413,1,0,0,0,412,410,1,0,0,0,413,414,3,34,17,0,414,415,3,42,21,0,
        415,417,5,32,0,0,416,418,3,48,24,0,417,416,1,0,0,0,417,418,1,0,0,
        0,418,419,1,0,0,0,419,423,5,33,0,0,420,422,7,4,0,0,421,420,1,0,0,
        0,422,425,1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,426,1,0,0,
        0,425,423,1,0,0,0,426,427,5,30,0,0,427,428,3,72,36,0,428,429,5,31,
        0,0,429,71,1,0,0,0,430,432,7,12,0,0,431,430,1,0,0,0,432,435,1,0,
        0,0,433,431,1,0,0,0,433,434,1,0,0,0,434,73,1,0,0,0,435,433,1,0,0,
        0,436,438,7,12,0,0,437,436,1,0,0,0,438,441,1,0,0,0,439,437,1,0,0,
        0,439,440,1,0,0,0,440,75,1,0,0,0,441,439,1,0,0,0,442,444,7,12,0,
        0,443,442,1,0,0,0,444,447,1,0,0,0,445,443,1,0,0,0,445,446,1,0,0,
        0,446,77,1,0,0,0,447,445,1,0,0,0,448,449,3,34,17,0,449,450,5,64,
        0,0,450,452,5,32,0,0,451,453,3,48,24,0,452,451,1,0,0,0,452,453,1,
        0,0,0,453,454,1,0,0,0,454,455,5,33,0,0,455,456,5,30,0,0,456,457,
        3,80,40,0,457,458,5,31,0,0,458,79,1,0,0,0,459,461,7,12,0,0,460,459,
        1,0,0,0,461,464,1,0,0,0,462,460,1,0,0,0,462,463,1,0,0,0,463,81,1,
        0,0,0,464,462,1,0,0,0,465,469,5,14,0,0,466,470,5,64,0,0,467,468,
        5,13,0,0,468,470,5,64,0,0,469,466,1,0,0,0,469,467,1,0,0,0,470,471,
        1,0,0,0,471,472,5,25,0,0,472,83,1,0,0,0,473,474,5,69,0,0,474,85,
        1,0,0,0,54,87,96,98,103,113,116,122,131,135,143,145,160,163,168,
        173,178,187,194,203,210,216,222,230,238,243,251,258,262,295,302,
        308,313,317,324,331,336,341,347,357,364,370,379,387,394,400,410,
        417,423,433,439,445,452,462,469
    ]

class CppParser ( Parser ):

    grammarFileName = "CppParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'struct'", "'public'", "'private'", 
                     "'protected'", "'virtual'", "'static'", "'const'", 
                     "'volatile'", "'inline'", "'friend'", "'template'", 
                     "'namespace'", "'using'", "'typedef'", "'enum'", "'union'", 
                     "'override'", "'explicit'", "'extern'", "'mutable'", 
                     "'register'", "'auto'", "':'", "';'", "','", "'.'", 
                     "'->'", "'::'", "'{'", "'}'", "'('", "')'", "'['", 
                     "']'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
                     "'!'", "'&'", "'|'", "'^'", "'<<'", "'>>'", "'++'", 
                     "'--'", "'~'", "'?'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "STRUCT", "PUBLIC", "PRIVATE", 
                      "PROTECTED", "VIRTUAL", "STATIC", "CONST", "VOLATILE", 
                      "INLINE", "FRIEND", "TEMPLATE", "NAMESPACE", "USING", 
                      "TYPEDEF", "ENUM", "UNION", "OVERRIDE", "EXPLICIT", 
                      "EXTERN", "MUTABLE", "REGISTER", "AUTO", "COLON", 
                      "SEMICOLON", "COMMA", "DOT", "ARROW", "SCOPE", "LBRACE", 
                      "RBRACE", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
                      "ASSIGN", "PLUS", "MINUS", "MULT", "DIV", "MOD", "LT", 
                      "GT", "LE", "GE", "EQ", "NE", "AND", "OR", "NOT", 
                      "BITAND", "BITOR", "XOR", "LSHIFT", "RSHIFT", "INC", 
                      "DEC", "TILDE", "QUESTION", "INTEGER_LITERAL", "FLOATING_LITERAL", 
                      "CHARACTER_LITERAL", "STRING_LITERAL", "IDENTIFIER", 
                      "QUALIFIED_NAME", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "PREPROCESSOR", "OTHER", "TYPENAME", "OPERATOR" ]

    RULE_compilationUnit = 0
    RULE_translationUnit = 1
    RULE_namespaceDefinition = 2
    RULE_classDefinition = 3
    RULE_classKey = 4
    RULE_classInheritanceList = 5
    RULE_classInheritance = 6
    RULE_classBody = 7
    RULE_accessSpecifier = 8
    RULE_memberDeclaration = 9
    RULE_staticDeclaration = 10
    RULE_virtualDeclaration = 11
    RULE_friendDeclaration = 12
    RULE_templateDeclaration = 13
    RULE_templateParameterList = 14
    RULE_templateParameter = 15
    RULE_memberFunction = 16
    RULE_returnType = 17
    RULE_typeSpecifier = 18
    RULE_templateArgumentList = 19
    RULE_templateArgument = 20
    RULE_functionName = 21
    RULE_operatorName = 22
    RULE_operatorSymbol = 23
    RULE_parameterList = 24
    RULE_parameter = 25
    RULE_defaultValue = 26
    RULE_memberVariable = 27
    RULE_constructor = 28
    RULE_destructor = 29
    RULE_memberInitializerList = 30
    RULE_memberInitializer = 31
    RULE_argumentList = 32
    RULE_argument = 33
    RULE_inlineMethod = 34
    RULE_methodWithBody = 35
    RULE_methodBody = 36
    RULE_constructorBody = 37
    RULE_destructorBody = 38
    RULE_functionDefinition = 39
    RULE_functionBody = 40
    RULE_usingDeclaration = 41
    RULE_preprocessorDirective = 42

    ruleNames =  [ "compilationUnit", "translationUnit", "namespaceDefinition", 
                   "classDefinition", "classKey", "classInheritanceList", 
                   "classInheritance", "classBody", "accessSpecifier", "memberDeclaration", 
                   "staticDeclaration", "virtualDeclaration", "friendDeclaration", 
                   "templateDeclaration", "templateParameterList", "templateParameter", 
                   "memberFunction", "returnType", "typeSpecifier", "templateArgumentList", 
                   "templateArgument", "functionName", "operatorName", "operatorSymbol", 
                   "parameterList", "parameter", "defaultValue", "memberVariable", 
                   "constructor", "destructor", "memberInitializerList", 
                   "memberInitializer", "argumentList", "argument", "inlineMethod", 
                   "methodWithBody", "methodBody", "constructorBody", "destructorBody", 
                   "functionDefinition", "functionBody", "usingDeclaration", 
                   "preprocessorDirective" ]

    EOF = Token.EOF
    CLASS=1
    STRUCT=2
    PUBLIC=3
    PRIVATE=4
    PROTECTED=5
    VIRTUAL=6
    STATIC=7
    CONST=8
    VOLATILE=9
    INLINE=10
    FRIEND=11
    TEMPLATE=12
    NAMESPACE=13
    USING=14
    TYPEDEF=15
    ENUM=16
    UNION=17
    OVERRIDE=18
    EXPLICIT=19
    EXTERN=20
    MUTABLE=21
    REGISTER=22
    AUTO=23
    COLON=24
    SEMICOLON=25
    COMMA=26
    DOT=27
    ARROW=28
    SCOPE=29
    LBRACE=30
    RBRACE=31
    LPAREN=32
    RPAREN=33
    LBRACKET=34
    RBRACKET=35
    ASSIGN=36
    PLUS=37
    MINUS=38
    MULT=39
    DIV=40
    MOD=41
    LT=42
    GT=43
    LE=44
    GE=45
    EQ=46
    NE=47
    AND=48
    OR=49
    NOT=50
    BITAND=51
    BITOR=52
    XOR=53
    LSHIFT=54
    RSHIFT=55
    INC=56
    DEC=57
    TILDE=58
    QUESTION=59
    INTEGER_LITERAL=60
    FLOATING_LITERAL=61
    CHARACTER_LITERAL=62
    STRING_LITERAL=63
    IDENTIFIER=64
    QUALIFIED_NAME=65
    WS=66
    LINE_COMMENT=67
    BLOCK_COMMENT=68
    PREPROCESSOR=69
    OTHER=70
    TYPENAME=71
    OPERATOR=72

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CppParser.EOF, 0)

        def translationUnit(self):
            return self.getTypedRuleContext(CppParser.TranslationUnitContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = CppParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 86
                self.translationUnit()


            self.state = 89
            self.match(CppParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespaceDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.NamespaceDefinitionContext)
            else:
                return self.getTypedRuleContext(CppParser.NamespaceDefinitionContext,i)


        def classDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.ClassDefinitionContext)
            else:
                return self.getTypedRuleContext(CppParser.ClassDefinitionContext,i)


        def usingDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.UsingDeclarationContext)
            else:
                return self.getTypedRuleContext(CppParser.UsingDeclarationContext,i)


        def preprocessorDirective(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.PreprocessorDirectiveContext)
            else:
                return self.getTypedRuleContext(CppParser.PreprocessorDirectiveContext,i)


        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(CppParser.FunctionDefinitionContext,i)


        def getRuleIndex(self):
            return CppParser.RULE_translationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslationUnit" ):
                listener.enterTranslationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslationUnit" ):
                listener.exitTranslationUnit(self)




    def translationUnit(self):

        localctx = CppParser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 25478) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 35) != 0):
                self.state = 96
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 91
                    self.namespaceDefinition()
                    pass
                elif token in [1, 2]:
                    self.state = 92
                    self.classDefinition()
                    pass
                elif token in [14]:
                    self.state = 93
                    self.usingDeclaration()
                    pass
                elif token in [69]:
                    self.state = 94
                    self.preprocessorDirective()
                    pass
                elif token in [7, 8, 9, 64, 65]:
                    self.state = 95
                    self.functionDefinition()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMESPACE(self):
            return self.getToken(CppParser.NAMESPACE, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def translationUnit(self):
            return self.getTypedRuleContext(CppParser.TranslationUnitContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CppParser.RULE_namespaceDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaceDefinition" ):
                listener.enterNamespaceDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaceDefinition" ):
                listener.exitNamespaceDefinition(self)




    def namespaceDefinition(self):

        localctx = CppParser.NamespaceDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespaceDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(CppParser.NAMESPACE)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 102
                self.match(CppParser.IDENTIFIER)


            self.state = 105
            self.match(CppParser.LBRACE)
            self.state = 106
            self.translationUnit()
            self.state = 107
            self.match(CppParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classKey(self):
            return self.getTypedRuleContext(CppParser.ClassKeyContext,0)


        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def classBody(self):
            return self.getTypedRuleContext(CppParser.ClassBodyContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def COLON(self):
            return self.getToken(CppParser.COLON, 0)

        def classInheritanceList(self):
            return self.getTypedRuleContext(CppParser.ClassInheritanceListContext,0)


        def SEMICOLON(self):
            return self.getToken(CppParser.SEMICOLON, 0)

        def accessSpecifier(self):
            return self.getTypedRuleContext(CppParser.AccessSpecifierContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_classDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDefinition" ):
                listener.enterClassDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDefinition" ):
                listener.exitClassDefinition(self)




    def classDefinition(self):

        localctx = CppParser.ClassDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.classKey()
            self.state = 110
            self.match(CppParser.IDENTIFIER)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 111
                self.match(CppParser.COLON)
                self.state = 113
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 112
                    self.accessSpecifier()


                self.state = 115
                self.classInheritanceList()


            self.state = 118
            self.match(CppParser.LBRACE)
            self.state = 119
            self.classBody()
            self.state = 120
            self.match(CppParser.RBRACE)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 121
                self.match(CppParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CppParser.CLASS, 0)

        def STRUCT(self):
            return self.getToken(CppParser.STRUCT, 0)

        def getRuleIndex(self):
            return CppParser.RULE_classKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassKey" ):
                listener.enterClassKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassKey" ):
                listener.exitClassKey(self)




    def classKey(self):

        localctx = CppParser.ClassKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classKey)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassInheritanceListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classInheritance(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.ClassInheritanceContext)
            else:
                return self.getTypedRuleContext(CppParser.ClassInheritanceContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_classInheritanceList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassInheritanceList" ):
                listener.enterClassInheritanceList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassInheritanceList" ):
                listener.exitClassInheritanceList(self)




    def classInheritanceList(self):

        localctx = CppParser.ClassInheritanceListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classInheritanceList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.classInheritance()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 127
                self.match(CppParser.COMMA)
                self.state = 128
                self.classInheritance()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassInheritanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def accessSpecifier(self):
            return self.getTypedRuleContext(CppParser.AccessSpecifierContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_classInheritance

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassInheritance" ):
                listener.enterClassInheritance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassInheritance" ):
                listener.exitClassInheritance(self)




    def classInheritance(self):

        localctx = CppParser.ClassInheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_classInheritance)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                self.state = 134
                self.accessSpecifier()


            self.state = 137
            self.match(CppParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessSpecifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.AccessSpecifierContext)
            else:
                return self.getTypedRuleContext(CppParser.AccessSpecifierContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COLON)
            else:
                return self.getToken(CppParser.COLON, i)

        def memberDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.MemberDeclarationContext)
            else:
                return self.getTypedRuleContext(CppParser.MemberDeclarationContext,i)


        def getRuleIndex(self):
            return CppParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)




    def classBody(self):

        localctx = CppParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & 6953557824662078463) != 0):
                self.state = 143
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 4, 5]:
                    self.state = 139
                    self.accessSpecifier()
                    self.state = 140
                    self.match(CppParser.COLON)
                    pass
                elif token in [6, 7, 8, 9, 10, 11, 12, 19, 20, 21, 22, 23, 58, 64, 65]:
                    self.state = 142
                    self.memberDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccessSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(CppParser.PUBLIC, 0)

        def PRIVATE(self):
            return self.getToken(CppParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(CppParser.PROTECTED, 0)

        def getRuleIndex(self):
            return CppParser.RULE_accessSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccessSpecifier" ):
                listener.enterAccessSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccessSpecifier" ):
                listener.exitAccessSpecifier(self)




    def accessSpecifier(self):

        localctx = CppParser.AccessSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_accessSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staticDeclaration(self):
            return self.getTypedRuleContext(CppParser.StaticDeclarationContext,0)


        def virtualDeclaration(self):
            return self.getTypedRuleContext(CppParser.VirtualDeclarationContext,0)


        def friendDeclaration(self):
            return self.getTypedRuleContext(CppParser.FriendDeclarationContext,0)


        def templateDeclaration(self):
            return self.getTypedRuleContext(CppParser.TemplateDeclarationContext,0)


        def memberFunction(self):
            return self.getTypedRuleContext(CppParser.MemberFunctionContext,0)


        def memberVariable(self):
            return self.getTypedRuleContext(CppParser.MemberVariableContext,0)


        def constructor(self):
            return self.getTypedRuleContext(CppParser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(CppParser.DestructorContext,0)


        def inlineMethod(self):
            return self.getTypedRuleContext(CppParser.InlineMethodContext,0)


        def methodWithBody(self):
            return self.getTypedRuleContext(CppParser.MethodWithBodyContext,0)


        def SEMICOLON(self):
            return self.getToken(CppParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return CppParser.RULE_memberDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberDeclaration" ):
                listener.enterMemberDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberDeclaration" ):
                listener.exitMemberDeclaration(self)




    def memberDeclaration(self):

        localctx = CppParser.MemberDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_memberDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 150
                self.staticDeclaration()
                pass

            elif la_ == 2:
                self.state = 151
                self.virtualDeclaration()
                pass

            elif la_ == 3:
                self.state = 152
                self.friendDeclaration()
                pass

            elif la_ == 4:
                self.state = 153
                self.templateDeclaration()
                pass

            elif la_ == 5:
                self.state = 154
                self.memberFunction()
                pass

            elif la_ == 6:
                self.state = 155
                self.memberVariable()
                pass

            elif la_ == 7:
                self.state = 156
                self.constructor()
                pass

            elif la_ == 8:
                self.state = 157
                self.destructor()
                pass

            elif la_ == 9:
                self.state = 158
                self.inlineMethod()
                pass

            elif la_ == 10:
                self.state = 159
                self.methodWithBody()
                pass


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 162
                self.match(CppParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(CppParser.STATIC, 0)

        def memberFunction(self):
            return self.getTypedRuleContext(CppParser.MemberFunctionContext,0)


        def memberVariable(self):
            return self.getTypedRuleContext(CppParser.MemberVariableContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_staticDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticDeclaration" ):
                listener.enterStaticDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticDeclaration" ):
                listener.exitStaticDeclaration(self)




    def staticDeclaration(self):

        localctx = CppParser.StaticDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_staticDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(CppParser.STATIC)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 166
                self.memberFunction()
                pass

            elif la_ == 2:
                self.state = 167
                self.memberVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VirtualDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIRTUAL(self):
            return self.getToken(CppParser.VIRTUAL, 0)

        def memberFunction(self):
            return self.getTypedRuleContext(CppParser.MemberFunctionContext,0)


        def memberVariable(self):
            return self.getTypedRuleContext(CppParser.MemberVariableContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_virtualDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVirtualDeclaration" ):
                listener.enterVirtualDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVirtualDeclaration" ):
                listener.exitVirtualDeclaration(self)




    def virtualDeclaration(self):

        localctx = CppParser.VirtualDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_virtualDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(CppParser.VIRTUAL)
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 171
                self.memberFunction()
                pass

            elif la_ == 2:
                self.state = 172
                self.memberVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FriendDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FRIEND(self):
            return self.getToken(CppParser.FRIEND, 0)

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def memberFunction(self):
            return self.getTypedRuleContext(CppParser.MemberFunctionContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_friendDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFriendDeclaration" ):
                listener.enterFriendDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFriendDeclaration" ):
                listener.exitFriendDeclaration(self)




    def friendDeclaration(self):

        localctx = CppParser.FriendDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_friendDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(CppParser.FRIEND)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(CppParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 177
                self.memberFunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMPLATE(self):
            return self.getToken(CppParser.TEMPLATE, 0)

        def LT(self):
            return self.getToken(CppParser.LT, 0)

        def templateParameterList(self):
            return self.getTypedRuleContext(CppParser.TemplateParameterListContext,0)


        def GT(self):
            return self.getToken(CppParser.GT, 0)

        def classDefinition(self):
            return self.getTypedRuleContext(CppParser.ClassDefinitionContext,0)


        def memberFunction(self):
            return self.getTypedRuleContext(CppParser.MemberFunctionContext,0)


        def memberVariable(self):
            return self.getTypedRuleContext(CppParser.MemberVariableContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_templateDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateDeclaration" ):
                listener.enterTemplateDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateDeclaration" ):
                listener.exitTemplateDeclaration(self)




    def templateDeclaration(self):

        localctx = CppParser.TemplateDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_templateDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(CppParser.TEMPLATE)
            self.state = 181
            self.match(CppParser.LT)
            self.state = 182
            self.templateParameterList()
            self.state = 183
            self.match(CppParser.GT)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 184
                self.classDefinition()
                pass

            elif la_ == 2:
                self.state = 185
                self.memberFunction()
                pass

            elif la_ == 3:
                self.state = 186
                self.memberVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def templateParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.TemplateParameterContext)
            else:
                return self.getTypedRuleContext(CppParser.TemplateParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_templateParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateParameterList" ):
                listener.enterTemplateParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateParameterList" ):
                listener.exitTemplateParameterList(self)




    def templateParameterList(self):

        localctx = CppParser.TemplateParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_templateParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.templateParameter()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 190
                self.match(CppParser.COMMA)
                self.state = 191
                self.templateParameter()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def CLASS(self):
            return self.getToken(CppParser.CLASS, 0)

        def TYPENAME(self):
            return self.getToken(CppParser.TYPENAME, 0)

        def getRuleIndex(self):
            return CppParser.RULE_templateParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateParameter" ):
                listener.enterTemplateParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateParameter" ):
                listener.exitTemplateParameter(self)




    def templateParameter(self):

        localctx = CppParser.TemplateParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_templateParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not(_la==1 or _la==71):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 198
            self.match(CppParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(CppParser.ReturnTypeContext,0)


        def functionName(self):
            return self.getTypedRuleContext(CppParser.FunctionNameContext,0)


        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CppParser.ParameterListContext,0)


        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.CONST)
            else:
                return self.getToken(CppParser.CONST, i)

        def VOLATILE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VOLATILE)
            else:
                return self.getToken(CppParser.VOLATILE, i)

        def INLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INLINE)
            else:
                return self.getToken(CppParser.INLINE, i)

        def EXPLICIT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.EXPLICIT)
            else:
                return self.getToken(CppParser.EXPLICIT, i)

        def EXTERN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.EXTERN)
            else:
                return self.getToken(CppParser.EXTERN, i)

        def MUTABLE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MUTABLE)
            else:
                return self.getToken(CppParser.MUTABLE, i)

        def REGISTER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.REGISTER)
            else:
                return self.getToken(CppParser.REGISTER, i)

        def AUTO(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.AUTO)
            else:
                return self.getToken(CppParser.AUTO, i)

        def OVERRIDE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OVERRIDE)
            else:
                return self.getToken(CppParser.OVERRIDE, i)

        def getRuleIndex(self):
            return CppParser.RULE_memberFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberFunction" ):
                listener.enterMemberFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberFunction" ):
                listener.exitMemberFunction(self)




    def memberFunction(self):

        localctx = CppParser.MemberFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_memberFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 200
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16254720) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

            self.state = 206
            self.returnType()
            self.state = 207
            self.functionName()
            self.state = 208
            self.match(CppParser.LPAREN)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 216172782113783811) != 0):
                self.state = 209
                self.parameterList()


            self.state = 212
            self.match(CppParser.RPAREN)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 213
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 262912) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CppParser.TypeSpecifierContext,0)


        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.CONST)
            else:
                return self.getToken(CppParser.CONST, i)

        def VOLATILE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VOLATILE)
            else:
                return self.getToken(CppParser.VOLATILE, i)

        def STATIC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STATIC)
            else:
                return self.getToken(CppParser.STATIC, i)

        def getRuleIndex(self):
            return CppParser.RULE_returnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnType" ):
                listener.enterReturnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnType" ):
                listener.exitReturnType(self)




    def returnType(self):

        localctx = CppParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 219
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 225
            self.typeSpecifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def QUALIFIED_NAME(self):
            return self.getToken(CppParser.QUALIFIED_NAME, 0)

        def LT(self):
            return self.getToken(CppParser.LT, 0)

        def templateArgumentList(self):
            return self.getTypedRuleContext(CppParser.TemplateArgumentListContext,0)


        def GT(self):
            return self.getToken(CppParser.GT, 0)

        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.CONST)
            else:
                return self.getToken(CppParser.CONST, i)

        def VOLATILE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VOLATILE)
            else:
                return self.getToken(CppParser.VOLATILE, i)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MULT)
            else:
                return self.getToken(CppParser.MULT, i)

        def BITAND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITAND)
            else:
                return self.getToken(CppParser.BITAND, i)

        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITOR)
            else:
                return self.getToken(CppParser.BITOR, i)

        def getRuleIndex(self):
            return CppParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)




    def typeSpecifier(self):

        localctx = CppParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 233
            _la = self._input.LA(1)
            if not(_la==64 or _la==65):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 234
                self.match(CppParser.LT)
                self.state = 235
                self.templateArgumentList()
                self.state = 236
                self.match(CppParser.GT)


            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6755949196869632) != 0):
                self.state = 240
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6755949196869632) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def templateArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.TemplateArgumentContext)
            else:
                return self.getTypedRuleContext(CppParser.TemplateArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_templateArgumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateArgumentList" ):
                listener.enterTemplateArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateArgumentList" ):
                listener.exitTemplateArgumentList(self)




    def templateArgumentList(self):

        localctx = CppParser.TemplateArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_templateArgumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.templateArgument()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 247
                self.match(CppParser.COMMA)
                self.state = 248
                self.templateArgument()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CppParser.TypeSpecifierContext,0)


        def INTEGER_LITERAL(self):
            return self.getToken(CppParser.INTEGER_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def QUALIFIED_NAME(self):
            return self.getToken(CppParser.QUALIFIED_NAME, 0)

        def getRuleIndex(self):
            return CppParser.RULE_templateArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateArgument" ):
                listener.enterTemplateArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateArgument" ):
                listener.exitTemplateArgument(self)




    def templateArgument(self):

        localctx = CppParser.TemplateArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_templateArgument)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.typeSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(CppParser.INTEGER_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.match(CppParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 257
                self.match(CppParser.QUALIFIED_NAME)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def operatorName(self):
            return self.getTypedRuleContext(CppParser.OperatorNameContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_functionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionName" ):
                listener.enterFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionName" ):
                listener.exitFunctionName(self)




    def functionName(self):

        localctx = CppParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionName)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(CppParser.IDENTIFIER)
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.operatorName()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(CppParser.OPERATOR, 0)

        def operatorSymbol(self):
            return self.getTypedRuleContext(CppParser.OperatorSymbolContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_operatorName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorName" ):
                listener.enterOperatorName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorName" ):
                listener.exitOperatorName(self)




    def operatorName(self):

        localctx = CppParser.OperatorNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operatorName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(CppParser.OPERATOR)
            self.state = 265
            self.operatorSymbol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorSymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(CppParser.ASSIGN, 0)

        def PLUS(self):
            return self.getToken(CppParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CppParser.MINUS, 0)

        def MULT(self):
            return self.getToken(CppParser.MULT, 0)

        def DIV(self):
            return self.getToken(CppParser.DIV, 0)

        def MOD(self):
            return self.getToken(CppParser.MOD, 0)

        def LT(self):
            return self.getToken(CppParser.LT, 0)

        def GT(self):
            return self.getToken(CppParser.GT, 0)

        def LE(self):
            return self.getToken(CppParser.LE, 0)

        def GE(self):
            return self.getToken(CppParser.GE, 0)

        def EQ(self):
            return self.getToken(CppParser.EQ, 0)

        def NE(self):
            return self.getToken(CppParser.NE, 0)

        def AND(self):
            return self.getToken(CppParser.AND, 0)

        def OR(self):
            return self.getToken(CppParser.OR, 0)

        def NOT(self):
            return self.getToken(CppParser.NOT, 0)

        def BITAND(self):
            return self.getToken(CppParser.BITAND, 0)

        def BITOR(self):
            return self.getToken(CppParser.BITOR, 0)

        def XOR(self):
            return self.getToken(CppParser.XOR, 0)

        def LSHIFT(self):
            return self.getToken(CppParser.LSHIFT, 0)

        def RSHIFT(self):
            return self.getToken(CppParser.RSHIFT, 0)

        def INC(self):
            return self.getToken(CppParser.INC, 0)

        def DEC(self):
            return self.getToken(CppParser.DEC, 0)

        def TILDE(self):
            return self.getToken(CppParser.TILDE, 0)

        def QUESTION(self):
            return self.getToken(CppParser.QUESTION, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def LBRACKET(self):
            return self.getToken(CppParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(CppParser.RBRACKET, 0)

        def getRuleIndex(self):
            return CppParser.RULE_operatorSymbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperatorSymbol" ):
                listener.enterOperatorSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperatorSymbol" ):
                listener.exitOperatorSymbol(self)




    def operatorSymbol(self):

        localctx = CppParser.OperatorSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_operatorSymbol)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(CppParser.ASSIGN)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(CppParser.PLUS)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(CppParser.MINUS)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 270
                self.match(CppParser.MULT)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 5)
                self.state = 271
                self.match(CppParser.DIV)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 6)
                self.state = 272
                self.match(CppParser.MOD)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 7)
                self.state = 273
                self.match(CppParser.LT)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 8)
                self.state = 274
                self.match(CppParser.GT)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 9)
                self.state = 275
                self.match(CppParser.LE)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 10)
                self.state = 276
                self.match(CppParser.GE)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 11)
                self.state = 277
                self.match(CppParser.EQ)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 12)
                self.state = 278
                self.match(CppParser.NE)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 13)
                self.state = 279
                self.match(CppParser.AND)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 14)
                self.state = 280
                self.match(CppParser.OR)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 15)
                self.state = 281
                self.match(CppParser.NOT)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 16)
                self.state = 282
                self.match(CppParser.BITAND)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 17)
                self.state = 283
                self.match(CppParser.BITOR)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 18)
                self.state = 284
                self.match(CppParser.XOR)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 19)
                self.state = 285
                self.match(CppParser.LSHIFT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 20)
                self.state = 286
                self.match(CppParser.RSHIFT)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 21)
                self.state = 287
                self.match(CppParser.INC)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 22)
                self.state = 288
                self.match(CppParser.DEC)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 23)
                self.state = 289
                self.match(CppParser.TILDE)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 24)
                self.state = 290
                self.match(CppParser.QUESTION)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 25)
                self.state = 291
                self.match(CppParser.LPAREN)
                self.state = 292
                self.match(CppParser.RPAREN)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 26)
                self.state = 293
                self.match(CppParser.LBRACKET)
                self.state = 294
                self.match(CppParser.RBRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.ParameterContext)
            else:
                return self.getTypedRuleContext(CppParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = CppParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.parameter()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 298
                self.match(CppParser.COMMA)
                self.state = 299
                self.parameter()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CppParser.TypeSpecifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(CppParser.ASSIGN, 0)

        def defaultValue(self):
            return self.getTypedRuleContext(CppParser.DefaultValueContext,0)


        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.CONST)
            else:
                return self.getToken(CppParser.CONST, i)

        def VOLATILE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VOLATILE)
            else:
                return self.getToken(CppParser.VOLATILE, i)

        def getRuleIndex(self):
            return CppParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = CppParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 305
                    _la = self._input.LA(1)
                    if not(_la==8 or _la==9):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 311
            self.typeSpecifier()
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 312
                self.match(CppParser.IDENTIFIER)


            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 315
                self.match(CppParser.ASSIGN)
                self.state = 316
                self.defaultValue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(CppParser.INTEGER_LITERAL, 0)

        def FLOATING_LITERAL(self):
            return self.getToken(CppParser.FLOATING_LITERAL, 0)

        def CHARACTER_LITERAL(self):
            return self.getToken(CppParser.CHARACTER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(CppParser.STRING_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def QUALIFIED_NAME(self):
            return self.getToken(CppParser.QUALIFIED_NAME, 0)

        def getRuleIndex(self):
            return CppParser.RULE_defaultValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultValue" ):
                listener.enterDefaultValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultValue" ):
                listener.exitDefaultValue(self)




    def defaultValue(self):

        localctx = CppParser.DefaultValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_defaultValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            _la = self._input.LA(1)
            if not(((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & 63) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CppParser.TypeSpecifierContext,0)


        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(CppParser.ASSIGN, 0)

        def defaultValue(self):
            return self.getTypedRuleContext(CppParser.DefaultValueContext,0)


        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.CONST)
            else:
                return self.getToken(CppParser.CONST, i)

        def VOLATILE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VOLATILE)
            else:
                return self.getToken(CppParser.VOLATILE, i)

        def STATIC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STATIC)
            else:
                return self.getToken(CppParser.STATIC, i)

        def MUTABLE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MUTABLE)
            else:
                return self.getToken(CppParser.MUTABLE, i)

        def REGISTER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.REGISTER)
            else:
                return self.getToken(CppParser.REGISTER, i)

        def AUTO(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.AUTO)
            else:
                return self.getToken(CppParser.AUTO, i)

        def getRuleIndex(self):
            return CppParser.RULE_memberVariable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberVariable" ):
                listener.enterMemberVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberVariable" ):
                listener.exitMemberVariable(self)




    def memberVariable(self):

        localctx = CppParser.MemberVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_memberVariable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 321
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680960) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 327
            self.typeSpecifier()
            self.state = 328
            self.match(CppParser.IDENTIFIER)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 329
                self.match(CppParser.ASSIGN)
                self.state = 330
                self.defaultValue()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CppParser.ParameterListContext,0)


        def COLON(self):
            return self.getToken(CppParser.COLON, 0)

        def memberInitializerList(self):
            return self.getTypedRuleContext(CppParser.MemberInitializerListContext,0)


        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def constructorBody(self):
            return self.getTypedRuleContext(CppParser.ConstructorBodyContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def getRuleIndex(self):
            return CppParser.RULE_constructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor" ):
                listener.enterConstructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor" ):
                listener.exitConstructor(self)




    def constructor(self):

        localctx = CppParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(CppParser.IDENTIFIER)
            self.state = 334
            self.match(CppParser.LPAREN)
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 216172782113783811) != 0):
                self.state = 335
                self.parameterList()


            self.state = 338
            self.match(CppParser.RPAREN)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 339
                self.match(CppParser.COLON)
                self.state = 340
                self.memberInitializerList()


            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 343
                self.match(CppParser.LBRACE)
                self.state = 344
                self.constructorBody()
                self.state = 345
                self.match(CppParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TILDE(self):
            return self.getToken(CppParser.TILDE, 0)

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def destructorBody(self):
            return self.getTypedRuleContext(CppParser.DestructorBodyContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def getRuleIndex(self):
            return CppParser.RULE_destructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestructor" ):
                listener.enterDestructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestructor" ):
                listener.exitDestructor(self)




    def destructor(self):

        localctx = CppParser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_destructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(CppParser.TILDE)
            self.state = 350
            self.match(CppParser.IDENTIFIER)
            self.state = 351
            self.match(CppParser.LPAREN)
            self.state = 352
            self.match(CppParser.RPAREN)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 353
                self.match(CppParser.LBRACE)
                self.state = 354
                self.destructorBody()
                self.state = 355
                self.match(CppParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberInitializerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberInitializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.MemberInitializerContext)
            else:
                return self.getTypedRuleContext(CppParser.MemberInitializerContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_memberInitializerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberInitializerList" ):
                listener.enterMemberInitializerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberInitializerList" ):
                listener.exitMemberInitializerList(self)




    def memberInitializerList(self):

        localctx = CppParser.MemberInitializerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_memberInitializerList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.memberInitializer()
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 360
                self.match(CppParser.COMMA)
                self.state = 361
                self.memberInitializer()
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberInitializerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(CppParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_memberInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberInitializer" ):
                listener.enterMemberInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberInitializer" ):
                listener.exitMemberInitializer(self)




    def memberInitializer(self):

        localctx = CppParser.MemberInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_memberInitializer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(CppParser.IDENTIFIER)
            self.state = 368
            self.match(CppParser.LPAREN)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & 63) != 0):
                self.state = 369
                self.argumentList()


            self.state = 372
            self.match(CppParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CppParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = CppParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.argument()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 375
                self.match(CppParser.COMMA)
                self.state = 376
                self.argument()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(CppParser.INTEGER_LITERAL, 0)

        def FLOATING_LITERAL(self):
            return self.getToken(CppParser.FLOATING_LITERAL, 0)

        def CHARACTER_LITERAL(self):
            return self.getToken(CppParser.CHARACTER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(CppParser.STRING_LITERAL, 0)

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def QUALIFIED_NAME(self):
            return self.getToken(CppParser.QUALIFIED_NAME, 0)

        def getRuleIndex(self):
            return CppParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CppParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            _la = self._input.LA(1)
            if not(((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & 63) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InlineMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(CppParser.ReturnTypeContext,0)


        def functionName(self):
            return self.getTypedRuleContext(CppParser.FunctionNameContext,0)


        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def methodBody(self):
            return self.getTypedRuleContext(CppParser.MethodBodyContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CppParser.ParameterListContext,0)


        def VIRTUAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VIRTUAL)
            else:
                return self.getToken(CppParser.VIRTUAL, i)

        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.CONST)
            else:
                return self.getToken(CppParser.CONST, i)

        def VOLATILE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VOLATILE)
            else:
                return self.getToken(CppParser.VOLATILE, i)

        def INLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INLINE)
            else:
                return self.getToken(CppParser.INLINE, i)

        def STATIC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STATIC)
            else:
                return self.getToken(CppParser.STATIC, i)

        def OVERRIDE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OVERRIDE)
            else:
                return self.getToken(CppParser.OVERRIDE, i)

        def getRuleIndex(self):
            return CppParser.RULE_inlineMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInlineMethod" ):
                listener.enterInlineMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInlineMethod" ):
                listener.exitInlineMethod(self)




    def inlineMethod(self):

        localctx = CppParser.InlineMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_inlineMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 384
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 390
            self.returnType()
            self.state = 391
            self.functionName()
            self.state = 392
            self.match(CppParser.LPAREN)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 216172782113783811) != 0):
                self.state = 393
                self.parameterList()


            self.state = 396
            self.match(CppParser.RPAREN)
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262912) != 0):
                self.state = 397
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 262912) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 403
            self.match(CppParser.LBRACE)
            self.state = 404
            self.methodBody()
            self.state = 405
            self.match(CppParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodWithBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(CppParser.ReturnTypeContext,0)


        def functionName(self):
            return self.getTypedRuleContext(CppParser.FunctionNameContext,0)


        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def methodBody(self):
            return self.getTypedRuleContext(CppParser.MethodBodyContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CppParser.ParameterListContext,0)


        def VIRTUAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VIRTUAL)
            else:
                return self.getToken(CppParser.VIRTUAL, i)

        def CONST(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.CONST)
            else:
                return self.getToken(CppParser.CONST, i)

        def VOLATILE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.VOLATILE)
            else:
                return self.getToken(CppParser.VOLATILE, i)

        def INLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INLINE)
            else:
                return self.getToken(CppParser.INLINE, i)

        def STATIC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STATIC)
            else:
                return self.getToken(CppParser.STATIC, i)

        def OVERRIDE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OVERRIDE)
            else:
                return self.getToken(CppParser.OVERRIDE, i)

        def getRuleIndex(self):
            return CppParser.RULE_methodWithBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodWithBody" ):
                listener.enterMethodWithBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodWithBody" ):
                listener.exitMethodWithBody(self)




    def methodWithBody(self):

        localctx = CppParser.MethodWithBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_methodWithBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 407
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

            self.state = 413
            self.returnType()
            self.state = 414
            self.functionName()
            self.state = 415
            self.match(CppParser.LPAREN)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 216172782113783811) != 0):
                self.state = 416
                self.parameterList()


            self.state = 419
            self.match(CppParser.RPAREN)
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 262912) != 0):
                self.state = 420
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 262912) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 426
            self.match(CppParser.LBRACE)
            self.state = 427
            self.methodBody()
            self.state = 428
            self.match(CppParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OTHER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OTHER)
            else:
                return self.getToken(CppParser.OTHER, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.IDENTIFIER)
            else:
                return self.getToken(CppParser.IDENTIFIER, i)

        def QUALIFIED_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUALIFIED_NAME)
            else:
                return self.getToken(CppParser.QUALIFIED_NAME, i)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STRING_LITERAL)
            else:
                return self.getToken(CppParser.STRING_LITERAL, i)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INTEGER_LITERAL)
            else:
                return self.getToken(CppParser.INTEGER_LITERAL, i)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACE)
            else:
                return self.getToken(CppParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACE)
            else:
                return self.getToken(CppParser.RBRACE, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LPAREN)
            else:
                return self.getToken(CppParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RPAREN)
            else:
                return self.getToken(CppParser.RPAREN, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SEMICOLON)
            else:
                return self.getToken(CppParser.SEMICOLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DOT)
            else:
                return self.getToken(CppParser.DOT, i)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ARROW)
            else:
                return self.getToken(CppParser.ARROW, i)

        def SCOPE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SCOPE)
            else:
                return self.getToken(CppParser.SCOPE, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ASSIGN)
            else:
                return self.getToken(CppParser.ASSIGN, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.PLUS)
            else:
                return self.getToken(CppParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MINUS)
            else:
                return self.getToken(CppParser.MINUS, i)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MULT)
            else:
                return self.getToken(CppParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DIV)
            else:
                return self.getToken(CppParser.DIV, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LT)
            else:
                return self.getToken(CppParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GT)
            else:
                return self.getToken(CppParser.GT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LE)
            else:
                return self.getToken(CppParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GE)
            else:
                return self.getToken(CppParser.GE, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.EQ)
            else:
                return self.getToken(CppParser.EQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NE)
            else:
                return self.getToken(CppParser.NE, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.AND)
            else:
                return self.getToken(CppParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OR)
            else:
                return self.getToken(CppParser.OR, i)

        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NOT)
            else:
                return self.getToken(CppParser.NOT, i)

        def BITAND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITAND)
            else:
                return self.getToken(CppParser.BITAND, i)

        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITOR)
            else:
                return self.getToken(CppParser.BITOR, i)

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.XOR)
            else:
                return self.getToken(CppParser.XOR, i)

        def LSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LSHIFT)
            else:
                return self.getToken(CppParser.LSHIFT, i)

        def RSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RSHIFT)
            else:
                return self.getToken(CppParser.RSHIFT, i)

        def INC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INC)
            else:
                return self.getToken(CppParser.INC, i)

        def DEC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DEC)
            else:
                return self.getToken(CppParser.DEC, i)

        def TILDE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.TILDE)
            else:
                return self.getToken(CppParser.TILDE, i)

        def QUESTION(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUESTION)
            else:
                return self.getToken(CppParser.QUESTION, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COLON)
            else:
                return self.getToken(CppParser.COLON, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACKET)
            else:
                return self.getToken(CppParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACKET)
            else:
                return self.getToken(CppParser.RBRACKET, i)

        def getRuleIndex(self):
            return CppParser.RULE_methodBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodBody" ):
                listener.enterMethodBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodBody" ):
                listener.exitMethodBody(self)




    def methodBody(self):

        localctx = CppParser.MethodBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_methodBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 430
                    _la = self._input.LA(1)
                    if not(((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & 74354473697279) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 435
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OTHER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OTHER)
            else:
                return self.getToken(CppParser.OTHER, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.IDENTIFIER)
            else:
                return self.getToken(CppParser.IDENTIFIER, i)

        def QUALIFIED_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUALIFIED_NAME)
            else:
                return self.getToken(CppParser.QUALIFIED_NAME, i)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STRING_LITERAL)
            else:
                return self.getToken(CppParser.STRING_LITERAL, i)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INTEGER_LITERAL)
            else:
                return self.getToken(CppParser.INTEGER_LITERAL, i)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACE)
            else:
                return self.getToken(CppParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACE)
            else:
                return self.getToken(CppParser.RBRACE, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LPAREN)
            else:
                return self.getToken(CppParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RPAREN)
            else:
                return self.getToken(CppParser.RPAREN, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SEMICOLON)
            else:
                return self.getToken(CppParser.SEMICOLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DOT)
            else:
                return self.getToken(CppParser.DOT, i)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ARROW)
            else:
                return self.getToken(CppParser.ARROW, i)

        def SCOPE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SCOPE)
            else:
                return self.getToken(CppParser.SCOPE, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ASSIGN)
            else:
                return self.getToken(CppParser.ASSIGN, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.PLUS)
            else:
                return self.getToken(CppParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MINUS)
            else:
                return self.getToken(CppParser.MINUS, i)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MULT)
            else:
                return self.getToken(CppParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DIV)
            else:
                return self.getToken(CppParser.DIV, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LT)
            else:
                return self.getToken(CppParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GT)
            else:
                return self.getToken(CppParser.GT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LE)
            else:
                return self.getToken(CppParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GE)
            else:
                return self.getToken(CppParser.GE, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.EQ)
            else:
                return self.getToken(CppParser.EQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NE)
            else:
                return self.getToken(CppParser.NE, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.AND)
            else:
                return self.getToken(CppParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OR)
            else:
                return self.getToken(CppParser.OR, i)

        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NOT)
            else:
                return self.getToken(CppParser.NOT, i)

        def BITAND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITAND)
            else:
                return self.getToken(CppParser.BITAND, i)

        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITOR)
            else:
                return self.getToken(CppParser.BITOR, i)

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.XOR)
            else:
                return self.getToken(CppParser.XOR, i)

        def LSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LSHIFT)
            else:
                return self.getToken(CppParser.LSHIFT, i)

        def RSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RSHIFT)
            else:
                return self.getToken(CppParser.RSHIFT, i)

        def INC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INC)
            else:
                return self.getToken(CppParser.INC, i)

        def DEC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DEC)
            else:
                return self.getToken(CppParser.DEC, i)

        def TILDE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.TILDE)
            else:
                return self.getToken(CppParser.TILDE, i)

        def QUESTION(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUESTION)
            else:
                return self.getToken(CppParser.QUESTION, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COLON)
            else:
                return self.getToken(CppParser.COLON, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACKET)
            else:
                return self.getToken(CppParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACKET)
            else:
                return self.getToken(CppParser.RBRACKET, i)

        def getRuleIndex(self):
            return CppParser.RULE_constructorBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructorBody" ):
                listener.enterConstructorBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructorBody" ):
                listener.exitConstructorBody(self)




    def constructorBody(self):

        localctx = CppParser.ConstructorBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_constructorBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 436
                    _la = self._input.LA(1)
                    if not(((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & 74354473697279) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 441
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OTHER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OTHER)
            else:
                return self.getToken(CppParser.OTHER, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.IDENTIFIER)
            else:
                return self.getToken(CppParser.IDENTIFIER, i)

        def QUALIFIED_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUALIFIED_NAME)
            else:
                return self.getToken(CppParser.QUALIFIED_NAME, i)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STRING_LITERAL)
            else:
                return self.getToken(CppParser.STRING_LITERAL, i)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INTEGER_LITERAL)
            else:
                return self.getToken(CppParser.INTEGER_LITERAL, i)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACE)
            else:
                return self.getToken(CppParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACE)
            else:
                return self.getToken(CppParser.RBRACE, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LPAREN)
            else:
                return self.getToken(CppParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RPAREN)
            else:
                return self.getToken(CppParser.RPAREN, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SEMICOLON)
            else:
                return self.getToken(CppParser.SEMICOLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DOT)
            else:
                return self.getToken(CppParser.DOT, i)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ARROW)
            else:
                return self.getToken(CppParser.ARROW, i)

        def SCOPE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SCOPE)
            else:
                return self.getToken(CppParser.SCOPE, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ASSIGN)
            else:
                return self.getToken(CppParser.ASSIGN, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.PLUS)
            else:
                return self.getToken(CppParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MINUS)
            else:
                return self.getToken(CppParser.MINUS, i)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MULT)
            else:
                return self.getToken(CppParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DIV)
            else:
                return self.getToken(CppParser.DIV, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LT)
            else:
                return self.getToken(CppParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GT)
            else:
                return self.getToken(CppParser.GT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LE)
            else:
                return self.getToken(CppParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GE)
            else:
                return self.getToken(CppParser.GE, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.EQ)
            else:
                return self.getToken(CppParser.EQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NE)
            else:
                return self.getToken(CppParser.NE, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.AND)
            else:
                return self.getToken(CppParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OR)
            else:
                return self.getToken(CppParser.OR, i)

        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NOT)
            else:
                return self.getToken(CppParser.NOT, i)

        def BITAND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITAND)
            else:
                return self.getToken(CppParser.BITAND, i)

        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITOR)
            else:
                return self.getToken(CppParser.BITOR, i)

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.XOR)
            else:
                return self.getToken(CppParser.XOR, i)

        def LSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LSHIFT)
            else:
                return self.getToken(CppParser.LSHIFT, i)

        def RSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RSHIFT)
            else:
                return self.getToken(CppParser.RSHIFT, i)

        def INC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INC)
            else:
                return self.getToken(CppParser.INC, i)

        def DEC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DEC)
            else:
                return self.getToken(CppParser.DEC, i)

        def TILDE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.TILDE)
            else:
                return self.getToken(CppParser.TILDE, i)

        def QUESTION(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUESTION)
            else:
                return self.getToken(CppParser.QUESTION, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COLON)
            else:
                return self.getToken(CppParser.COLON, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACKET)
            else:
                return self.getToken(CppParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACKET)
            else:
                return self.getToken(CppParser.RBRACKET, i)

        def getRuleIndex(self):
            return CppParser.RULE_destructorBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestructorBody" ):
                listener.enterDestructorBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestructorBody" ):
                listener.exitDestructorBody(self)




    def destructorBody(self):

        localctx = CppParser.DestructorBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_destructorBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 442
                    _la = self._input.LA(1)
                    if not(((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & 74354473697279) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 447
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(CppParser.ReturnTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def functionBody(self):
            return self.getTypedRuleContext(CppParser.FunctionBodyContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CppParser.ParameterListContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)




    def functionDefinition(self):

        localctx = CppParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.returnType()
            self.state = 449
            self.match(CppParser.IDENTIFIER)
            self.state = 450
            self.match(CppParser.LPAREN)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 216172782113783811) != 0):
                self.state = 451
                self.parameterList()


            self.state = 454
            self.match(CppParser.RPAREN)
            self.state = 455
            self.match(CppParser.LBRACE)
            self.state = 456
            self.functionBody()
            self.state = 457
            self.match(CppParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OTHER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OTHER)
            else:
                return self.getToken(CppParser.OTHER, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.IDENTIFIER)
            else:
                return self.getToken(CppParser.IDENTIFIER, i)

        def QUALIFIED_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUALIFIED_NAME)
            else:
                return self.getToken(CppParser.QUALIFIED_NAME, i)

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.STRING_LITERAL)
            else:
                return self.getToken(CppParser.STRING_LITERAL, i)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INTEGER_LITERAL)
            else:
                return self.getToken(CppParser.INTEGER_LITERAL, i)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACE)
            else:
                return self.getToken(CppParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACE)
            else:
                return self.getToken(CppParser.RBRACE, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LPAREN)
            else:
                return self.getToken(CppParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RPAREN)
            else:
                return self.getToken(CppParser.RPAREN, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SEMICOLON)
            else:
                return self.getToken(CppParser.SEMICOLON, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DOT)
            else:
                return self.getToken(CppParser.DOT, i)

        def ARROW(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ARROW)
            else:
                return self.getToken(CppParser.ARROW, i)

        def SCOPE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.SCOPE)
            else:
                return self.getToken(CppParser.SCOPE, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ASSIGN)
            else:
                return self.getToken(CppParser.ASSIGN, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.PLUS)
            else:
                return self.getToken(CppParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MINUS)
            else:
                return self.getToken(CppParser.MINUS, i)

        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.MULT)
            else:
                return self.getToken(CppParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DIV)
            else:
                return self.getToken(CppParser.DIV, i)

        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LT)
            else:
                return self.getToken(CppParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GT)
            else:
                return self.getToken(CppParser.GT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LE)
            else:
                return self.getToken(CppParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.GE)
            else:
                return self.getToken(CppParser.GE, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.EQ)
            else:
                return self.getToken(CppParser.EQ, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NE)
            else:
                return self.getToken(CppParser.NE, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.AND)
            else:
                return self.getToken(CppParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.OR)
            else:
                return self.getToken(CppParser.OR, i)

        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.NOT)
            else:
                return self.getToken(CppParser.NOT, i)

        def BITAND(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITAND)
            else:
                return self.getToken(CppParser.BITAND, i)

        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.BITOR)
            else:
                return self.getToken(CppParser.BITOR, i)

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.XOR)
            else:
                return self.getToken(CppParser.XOR, i)

        def LSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LSHIFT)
            else:
                return self.getToken(CppParser.LSHIFT, i)

        def RSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RSHIFT)
            else:
                return self.getToken(CppParser.RSHIFT, i)

        def INC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.INC)
            else:
                return self.getToken(CppParser.INC, i)

        def DEC(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.DEC)
            else:
                return self.getToken(CppParser.DEC, i)

        def TILDE(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.TILDE)
            else:
                return self.getToken(CppParser.TILDE, i)

        def QUESTION(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.QUESTION)
            else:
                return self.getToken(CppParser.QUESTION, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COLON)
            else:
                return self.getToken(CppParser.COLON, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.LBRACKET)
            else:
                return self.getToken(CppParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.RBRACKET)
            else:
                return self.getToken(CppParser.RBRACKET, i)

        def getRuleIndex(self):
            return CppParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)




    def functionBody(self):

        localctx = CppParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 459
                    _la = self._input.LA(1)
                    if not(((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & 74354473697279) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsingDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USING(self):
            return self.getToken(CppParser.USING, 0)

        def SEMICOLON(self):
            return self.getToken(CppParser.SEMICOLON, 0)

        def IDENTIFIER(self):
            return self.getToken(CppParser.IDENTIFIER, 0)

        def NAMESPACE(self):
            return self.getToken(CppParser.NAMESPACE, 0)

        def getRuleIndex(self):
            return CppParser.RULE_usingDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsingDeclaration" ):
                listener.enterUsingDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsingDeclaration" ):
                listener.exitUsingDeclaration(self)




    def usingDeclaration(self):

        localctx = CppParser.UsingDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_usingDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.match(CppParser.USING)
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [64]:
                self.state = 466
                self.match(CppParser.IDENTIFIER)
                pass
            elif token in [13]:
                self.state = 467
                self.match(CppParser.NAMESPACE)
                self.state = 468
                self.match(CppParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 471
            self.match(CppParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreprocessorDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREPROCESSOR(self):
            return self.getToken(CppParser.PREPROCESSOR, 0)

        def getRuleIndex(self):
            return CppParser.RULE_preprocessorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorDirective" ):
                listener.enterPreprocessorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorDirective" ):
                listener.exitPreprocessorDirective(self)




    def preprocessorDirective(self):

        localctx = CppParser.PreprocessorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_preprocessorDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(CppParser.PREPROCESSOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





