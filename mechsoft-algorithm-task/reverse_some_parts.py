'''
You have a text that some of the words in reverse order.
The text also contains some words in the correct order, and they are wrapped in parenthesis.
Write a function fixes all of the words and,
remove the parenthesis that is used for marking the correct words.

Your function should return the same text defined in the constant CORRECT_ANSWER
'''

# Constants
INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
         ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
         "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
         "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
         "(and) nrae a egral enutrof (from) ).gnitirw")

CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

import re


def fix_text(mystr):
    # Function to reverse a word
    def reverse_word(word):
        return word[::-1]
    parts = re.split(r'(\s+|\(|\))', mystr)
    result = []
    inside_parentheses = False

    for part in parts:
        if part == '(':
            inside_parentheses = True
            result.append(part)
        elif part == ')':
            inside_parentheses = False
            result.append(part)
        elif inside_parentheses:
            result.append(part)
        elif part.strip() == '':
            result.append(part)
        else:
            result.append(reverse_word(part))

    final_text = ''.join(result)
    final_text = final_text.replace('(', '').replace(')', '')

    return final_text


# test
if __name__ == "__main__":
    INPUT = ("nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon "
             ",tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc "
             "noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif "
             "(American) srohtua (to) emoceb (an) lanoitanretni ytirbelec "
             "(and) nrae a egral enutrof (from) ).gnitirw")

    CORRECT_ANSWER = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

    result = fix_text(INPUT)
    print("Correct!" if result == CORRECT_ANSWER else "Sorry, it does not match with the correct answer.")
