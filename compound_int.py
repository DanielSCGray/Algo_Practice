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

cmp2(700, .14, 15)
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


# cmp2(800, .14, 15, 20, (1, 5))
