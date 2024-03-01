def compounder(starting_amt, interest_rate, years, contributions_or_withdrawls=0, cw_start=0):
    total = starting_amt
    cw = -66
    for i in range(1,years+1):
        opening_amt = total
        gain = round((total * interest_rate),3)
        total += gain
        if i > cw_start:
            cw = contributions_or_withdrawls
        total += cw
        total = round(total,3)
        print(f"Year {i} start: {opening_amt} gain: {gain} c/w: {cw} year end: {total} ")
    return

# compounder(800, .08, 10, -10)

# compounder(3250, .08, 20, -166, 5)
# compounder(800, .08, 9, 33)
# compounder(4000, .08, 20, -100)

def cmp2(starting_amt, interest_rate, years, cw=0, cw_timeframe: tuple = None):
    total = starting_amt
    for i in range(1, years+1):
        opening_amt = total
        if cw_timeframe != None:
            if i in range(cw_timeframe[0], cw_timeframe[1]+1):
                total += cw
                print(f"Year {i}, c/w of {cw}")
        gain = round((total * interest_rate),3)
        total += gain
        total = round(total,3)
        print(f"Year {i} start: {opening_amt} gain: {gain} year end: {total} ")
    return

# cmp2(800, .14, 15)
# Year 1 start: 800 gain: 112.0 year end: 912.0 
# Year 2 start: 912.0 gain: 127.68 year end: 1039.68
# Year 3 start: 1039.68 gain: 145.555 year end: 1185.235
# Year 4 start: 1185.235 gain: 165.933 year end: 1351.168
# Year 5 start: 1351.168 gain: 189.164 year end: 1540.332
# Year 6 start: 1540.332 gain: 215.646 year end: 1755.978
# Year 7 start: 1755.978 gain: 245.837 year end: 2001.815
# Year 8 start: 2001.815 gain: 280.254 year end: 2282.069
# Year 9 start: 2282.069 gain: 319.49 year end: 2601.559
# Year 10 start: 2601.559 gain: 364.218 year end: 2965.777
# Year 11 start: 2965.777 gain: 415.209 year end: 3380.986
# Year 12 start: 3380.986 gain: 473.338 year end: 3854.324
# Year 13 start: 3854.324 gain: 539.605 year end: 4393.929
# Year 14 start: 4393.929 gain: 615.15 year end: 5009.079
# Year 15 start: 5009.079 gain: 701.271 year end: 5710.35

# cmp2(700, .14, 15)
# Year 1 start: 700 gain: 98.0 year end: 798.0 
# Year 2 start: 798.0 gain: 111.72 year end: 909.72
# Year 3 start: 909.72 gain: 127.361 year end: 1037.081
# Year 4 start: 1037.081 gain: 145.191 year end: 1182.272
# Year 5 start: 1182.272 gain: 165.518 year end: 1347.79
# Year 6 start: 1347.79 gain: 188.691 year end: 1536.481
# Year 7 start: 1536.481 gain: 215.107 year end: 1751.588
# Year 8 start: 1751.588 gain: 245.222 year end: 1996.81
# Year 9 start: 1996.81 gain: 279.553 year end: 2276.363
# Year 10 start: 2276.363 gain: 318.691 year end: 2595.054
# Year 11 start: 2595.054 gain: 363.308 year end: 2958.362
# Year 12 start: 2958.362 gain: 414.171 year end: 3372.533
# Year 13 start: 3372.533 gain: 472.155 year end: 3844.688
# Year 14 start: 3844.688 gain: 538.256 year end: 4382.944
# Year 15 start: 4382.944 gain: 613.612 year end: 4996.556


# cmp2(3750000, .07, 20)

# adding 1% int adds 2.5 mil by the end of 20 years. look into more exposure to market to push it up that 1 % while maintaining conservative base.

cmp2(700, .145, 20)

# Year 1 start: 700 gain: 101.5 year end: 801.5 
# Year 2 start: 801.5 gain: 116.217 year end: 917.717 
# Year 3 start: 917.717 gain: 133.069 year end: 1050.786 
# Year 4 start: 1050.786 gain: 152.364 year end: 1203.15 
# Year 5 start: 1203.15 gain: 174.457 year end: 1377.607 
# Year 6 start: 1377.607 gain: 199.753 year end: 1577.36 
# Year 7 start: 1577.36 gain: 228.717 year end: 1806.077 
# Year 8 start: 1806.077 gain: 261.881 year end: 2067.958 
# Year 9 start: 2067.958 gain: 299.854 year end: 2367.812 
# Year 10 start: 2367.812 gain: 343.333 year end: 2711.145 
# Year 11 start: 2711.145 gain: 393.116 year end: 3104.261 
# Year 12 start: 3104.261 gain: 450.118 year end: 3554.379
# Year 13 start: 3554.379 gain: 515.385 year end: 4069.764
# Year 14 start: 4069.764 gain: 590.116 year end: 4659.88
# Year 15 start: 4659.88 gain: 675.683 year end: 5335.563
# Year 16 start: 5335.563 gain: 773.657 year end: 6109.22
# Year 17 start: 6109.22 gain: 885.837 year end: 6995.057
# Year 18 start: 6995.057 gain: 1014.283 year end: 8009.34
# Year 19 start: 8009.34 gain: 1161.354 year end: 9170.694
# Year 20 start: 9170.694 gain: 1329.751 year end: 10500.445