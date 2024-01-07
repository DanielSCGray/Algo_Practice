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
compounder(4000, .08, 20, -100)