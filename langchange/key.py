import pandas as pd
import re

new_corpus = []
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def replace_Vconditional(char, replacement, word):
    return re.sub(r'(?<=[' + vowels + r'])' + char + r'(?=[' + vowels + r'])', replacement, word)

def replace_Cconditional(char, replacement, word):
    return re.sub(r'(?<=[' + consonants + r'])' + char + r'(?=[' + consonants + r'])', replacement, word)

def replace_CVconditional(char, replacement, word):
    return re.sub(r'(?<=[' + consonants + r'])' + char + r'(?=[' + vowels + r'])', replacement, word)

def replace_VCconditional(char, replacement, word):
    return re.sub(r'(?<=[' + vowels + r'])' + char + r'(?=[' + consonants + r'])', replacement, word)

new_corpus = ["" + w[1:] if w[0] in "*" else w for w in new_corpus]
#replace if it starts word
new_corpus = [w[:-1] + "" if w[-1] in "ɲ" else w for w in new_corpus]
#replace if it ends word

new_corpus = [w.replace("a", "b") for w in new_corpus]
#simple replace
new_corpus = [re.sub(r'(?<=c)a(?=b)', 'd', w) for w in new_corpus]
#replace given word char before and/or after
new_corpus = [w[0] + w[1:].replace("k", "g") for w in new_corpus]
#replace for all char except wod initial

new_corpus = [replace_Vconditional("b", "", w) for w in new_corpus]
#replace given V surrounds
new_corpus = [replace_Cconditional("b", "", w) for w in new_corpus]
#replace given C surrounds

new_corpus = [w[:-1] + "" if w[-1] in vowels else w for w in new_corpus]
#replace ending vowels
new_corpus = [w[:-1] + "" if w[-1] in consonants else w for w in new_corpus]
#replace ending consonants

new_corpus = [w[:-1] + "c" if w.endswith("a") and len(w) > 1 and 
              w[-2] == "b" else w for w in new_corpus]
# if word ends with a, replace with c, only if b right before
new_corpus = ["c" + w[1:] if w.startswith("a") and len(w) > 1 and 
              w[1] == "b" else w for w in new_corpus]
# if word starts with a, replace with c, only if b right after