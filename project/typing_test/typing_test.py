""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"


def lines_from_file(path="data/words.txt"):
    f = open(path, 'r')
    list = []
    if not readable(f):
        return
    while tmp := readline(f):
        tmp = tmp.strip()
        list += [tmp]
    return list


def new_sample(path, i):
    f = open(path, 'r')
    if not readable(f):
        return
    for k in range(i + 1):
        tmp = readline(f).strip()
        if (k == i):
            return tmp


def analyze(sample_paragraph, typed_string, start_time, end_time):
    velocity = (len(typed_string) / 5) / (end_time - start_time) * 60
    sample = split(sample_paragraph)
    typed = split(typed_string)
    if len(typed) == 0:
        return [velocity, 0.0]
    length = min(len(sample), len(typed))
    correct = 0
    for i in range(length):
        if sample[i] == typed[i]:
            correct += 1
    return [velocity, correct / length * 100]


def pig_latin(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    words = split(string)
    res = ""
    for word in words:
        i = 0
        for i in range(len(word)):
            if word[i] in vowel:
                break
        if i == 0:
            tmp = word + "way"
        elif i == len(word) - 1:
            tmp = word + "ay"
        else:
            tmp = word[i:] + word[:i] + "ay"
        res += tmp + " "
    return strip(res)


def autocorrect(user_input, word_list, f):
    if user_input in word_list:
        return user_input
    res = 0
    comp = f(user_input, word_list[0])
    for i in range(1, len(word_list)):
        tmp = f(user_input, word_list[i])
        if comp <= tmp:
            continue
        else:
            comp = tmp
            res = i
    return word_list[res]


def swap_score(user_input, correct):
    # len_usr = len(user_input)
    # len_cor = len(correct)
    # r = min(len_usr,len_cor)
    # res = 0
    # for i in range(r):
    #     if correct[i] != user_input[i]:
    #         res += 1
    # return res
    if len(user_input) == 0 or len(correct) == 0:
        return 0
    if user_input[0] == correct[0]:
        return swap_score(user_input[1:], correct[1:])
    else:
        return 1 + swap_score(user_input[1:], correct[1:])


# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    '''
        if ______________:  # Fill in the condition
            # BEGIN Q6
            "*** YOUR CODE HERE ***"
            # END Q6
    
        elif ___________:  # Feel free to remove or add additional cases
            # BEGIN Q6
            "*** YOUR CODE HERE ***"
            # END Q6
    
        else:
            add_char = ______________  # Fill in these lines
            remove_char = ______________
            substitute_char = ______________
            # BEGIN Q6
            "*** YOUR CODE HERE ***"
            # END Q6
    '''
    if len(word1) == 0 and len(word2) == 0:
        return 0
    elif len(word1) != 0 and len(word2) == 0:
        return len(word1)
    elif len(word1) == 0 and len(word2) != 0:
        return len(word2)
    elif word1[0] == word2[0]:
        return score_function(word1[1:], word2[1:])

    return 1 + min(score_function(word1[1:], word2),
                   score_function(word1[1:], word2[1:]),
                   score_function(word1, word2[1:])
                   )


KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"


def score_function_accurate(word1, word2):
    if len(word1) == 0 and len(word2) == 0:
        return 0
    elif len(word1) != 0 and len(word2) == 0:
        return len(word1)
    elif len(word1) == 0 and len(word2) != 0:
        return len(word2)
    elif word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])

    return min((score_function_accurate(word1[1:], word2) + 1),  # delete
               (score_function_accurate(word1[1:], word2[1:]) + KEY_DISTANCES[word1[0], word2[0]]),  # substitute
               (score_function_accurate(word1, word2[1:]) + 1)  # insert
               )


record = {}


def score_function_final(word1, word2):
    tp1 = (word1, word2)
    tp2 = (word2, word1)
    if tp1 in record.keys():
        return record[tp1]
    elif tp2 in record.keys():
        return record[tp2]

    if len(word1) == 0 and len(word2) == 0:
        return 0
    elif len(word1) != 0 and len(word2) == 0:
        return len(word1)
    elif len(word1) == 0 and len(word2) != 0:
        return len(word2)
    elif word1[0] == word2[0]:
        res = score_function_final(word1[1:], word2[1:])
        record[tp1] = res
        return res

    res = min((score_function_final(word1[1:], word2) + 1),  # delete
              (score_function_final(word1[1:], word2[1:]) + KEY_DISTANCES[word1[0], word2[0]]),  # substitute
              (score_function_final(word1, word2[1:]) + 1)  # insert
              )
    record[tp1] = res
    return res


f = score_function_final
# END Q7-8
