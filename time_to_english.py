# Time to English
# You are given an integer representing the number of minutes that have elapsed since midnight. You
# should return a string representing the current time, in traditional spoken convention. Use numerals,
# except specifically the following words – midnight, noon, past, til, half, quarter. Examples: if given 30​,
# return "half past midnight"​. If given 75​, return "quarter past 1 am"​. If given 710​, return
# "10 til noon"​. If given 1000​, return "20 til 5 pm"​.

    #return will be an f-string f"{minutes} {pt} {hours} {meridiem(am/pm)} "

def time_in_eng(total_time):
    if total_time >= 1440:
        total_time = total_time % 1440
    hours = total_time // 60
    minutes = total_time % 60
    meridiem = False 
    if minutes > 30:
        hours += 1
        pt = "til"
        minutes = 60 - minutes
    else:
        pt = "past"
    if hours == 0 or hours == 24:
        hours = "midnight"
    elif hours == 12:
        hours = "noon"
    elif hours < 12:
        meridiem = "am"
    else:
        hours -= 12
        meridiem = "pm"
    if minutes == 0:
        if not meridiem:
            return f"{hours}"
        else:
            return f"{hours} {meridiem}"
    if minutes == 15:
        minutes = "quarter"
    if minutes == 30:
        minutes = "half"
    if not meridiem:
        return f"{minutes} {pt} {hours}"
    else:
        return f"{minutes} {pt} {hours} {meridiem}"
    
print(time_in_eng(1200))
#8 pm
print(time_in_eng(1220))
#20 past 8 pm
print(time_in_eng(1240))
#20 til 9 pm
print(time_in_eng(435))
#quarter past 7 am
print(time_in_eng(0))
#midnight
print(time_in_eng(720))
#noon
print(time_in_eng(735))
# quarter past noon
print(time_in_eng(750))
# half past noon
print(time_in_eng(705))
#quarter til noon
print(time_in_eng(1425))
#quarter til midnight
print(time_in_eng(710))
#10 til noon


