# stringAnagrams
# Given a string, return an array where each element is a string representing a different anagram (a
# different sequence of the letters in that string). Example: if given "tar"​, return ["art", "atr",
# "rat", "rta", "tar", "tra"]​. For this challenge, you can use built-in string functions such as
# split()​.



def all_anagrams(string: str):
    if len(string) <= 1:
        return string
    my_list = []
    for variant in all_anagrams(string[1:]):
        for i in range(len(string)):
            my_list.append(variant[:i] + string[:1] + variant[i:])
    return my_list

print(all_anagrams("tar"))
#['tar', 'atr', 'art', 'tra', 'rta', 'rat']

print(all_anagrams("read"))
# ['read', 'erad', 'eard', 'eadr', 'raed', 'ared', 'aerd', 'aedr', 'rade', 'arde', 'adre', 'ader', 'reda', 'erda', 'edra', 'edar', 'rdea', 'drea', 'dera', 'dear', 'rdae', 'drae', 'dare', 'daer']