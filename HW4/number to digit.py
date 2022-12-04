# Вычислить число c заданной точностью d
# Пример: 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = 0.001

def rounding(innumber, d):
    number = str(d)
    len_innumber = len(str(round(innumber)))
    preci = abs(number.find('.') - len(number)) - 1
    result = ''
    string_innumber = str(innumber)
    for i in range(len_innumber + 1 + preci):
        result += string_innumber[i]
    print(result)

rounding(math.pi, d)
