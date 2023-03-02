patterned_words = []

import re
# wordlist = "/home/jrouquie/archives/collected-docs/dico.txt"
wordlist = "/usr/share/dict/words"

with open(wordlist) as infile:
    dico = infile.readlines()

# convention vowel = dash / consonnant = dot. Too constrained.
#dot_regexp  = "[^aeiouy]"
#dash_regexp =  "[aeiouy]"

dash_regexp = "[bdfghjklpqtyBDFGHJKLPQTY]"
dot_regexp  = "[aceimnorsuvwxz]"

# dot_regexp = "[abdegopq]" # letters with a hole
# dash_regexp = "[cfhijklmnrstuvwxyz]"

with open("morse.txt") as infile:
    for line in infile:
        letter = line[0]
        code = line[2:-1]
        print(letter, code, "  ", end='')
        apo = "'*"
        # code_regexp = apo.join(code) .replace('.', dot_regexp)  .replace('-', dash_regexp)
        code_regexp = code.replace('.', dot_regexp)  .replace('-', dash_regexp)
        # rexexp = re.compile('^' + letter.lower() + apo + code_regexp + "\n",  re.IGNORECASE)
        # rexexp = re.compile('^' + letter.lower() + code_regexp ,  re.IGNORECASE)
        rexexp = re.compile('^' + code_regexp + "\n") # ,  re.IGNORECASE
        words_current_letter = []
        for word in dico:
            if rexexp.match(word):
                words_current_letter.append(word.strip())
        patterned_words.append(words_current_letter)
