# Telephone Words
# On older telephones, the keypad associates letters with each numeral. Given a seven-digit telephone
# number, return an array of all possible strings that equate to that phone number. For reference, here is
# the mapping: [2:ABC; 3:DEF; 4:GHI; 5:JKL; 6:MNO; 7:PQRS; 8:TUV; 9:WXYZ]​ – for
# completeness, map 1 to I​ and zero to O​. As an example, given the phone number 6937130 you should
# return an array of 1296 different strings, including “mydrifo” and “oyesido”.

phone_map = { 1: "I", 2:"ABC", 3:'DEF', 4:'GHI', 5:'JKL', 6:'MNO', 7:'PQRS', 8:'TUV', 9:'WXYZ', 0: "O" }

def tel_words(num):
    my_list = []
    if num < 10:
        for i in range(len(phone_map[num])):
            my_list.append(phone_map[num][i])
        return my_list
    num = str(num)
    digit = int(num[0])
    num = int(num[1:])
    for subsection in tel_words(num):
        for i in range(len(phone_map[digit])):
            my_list.append(phone_map[digit][i] + subsection)
    return my_list

print(tel_words(6937130))
print(len(tel_words(6937130)))
res = tel_words(6937130)
print(res.__contains__("MYDRIFO"))
print(res.__contains__("OYESIDO"))
# 432
# True
# True


# I got a different length but mine is the expected length by my math: 6,3 and 3 each have 3 options, 9 and 7 have 4 and 1 and 0 each have only 1 option
# so the total variations are 3^3 * 4^2 * 1^2 = 432 this value *3 would = 1296 but I dont know where the last *3 multiplier would be coming from 