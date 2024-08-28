"""
Jason Olefson
8/28/24
Assignment 1

§ Must work in Python 3.8+ without any special libraries (besides those that are in all default Python installations, e.g.,
sys, os, re, etc.), unless listed below

§ Submit a file hw1.py with no outputting code (print or any similar statements) at any level. This file should contain the
top-level functions:

§ problem1(NPs, S), where:
§ NPs: A list of strings [np1, np2, ...] where each string is a lowercase noun phrase. You may assume that no
noun phrase in this list is a substring of another.

§ S: A string which contains arbitrary text and symbols.
§ Using regular expressions, find all hypernyms in S which link only noun phrases in NPs. Use only the Hearst
patterns in the previous slide.

§ Noun phrases may appear capitalized in S.

§ Noun phrases in NP will not have the indefinite article (a, an), but it may appear in the string S. In such
cases, extract the hypernym relationship. For example, if “dog” and “mammal” appear in NP, but S
contains ‘a dog is a mammal’, then extract (‘mammal’, ‘dog’).

§ Return: A set() containing each hypernym as a tuple of strings (x,y), where x is a hypernym of y in S, and
both x and y appear exactly as they appeared in NPs.



§ problem2(s1, s2), where:
§ s1, s2: Two strings

§ Return: a single integer which is the Levenshtein edit distance from s1 to s2. You may not use any libraries
that implement the edit distance algorithm for you (you may use them for testing your code, but remove
them from the submitted version). Plagiarized code will receive an instant ‘0’.

"""

import re # import RegEx module


""" 
PROBLEM 1
Outline:
1. Use RegEx to search for occurrences of Hearst patterns
2. For each occurence, check if the noun phrases involved in pattern are in Nps
3. If match is found and both x and y are oin Nps, add pair to hypernyms set
4. Return hypernyms set
"""


def problem1(NPs, s):
    hypernyms = set() # create an empty set to store hypernyms
    s_lower = s.lower() # convert the string to lowercase
    # create a list of Hearst Patterns where order is hypernym -> hyponym
    patterns1 = [
		r'(\w+) is (\w+)',
		r'(\w+) is a type of (\w+)',
		r'(\w+) is a kind of (\w+)',
		r'(\w+) was an? (\w+)', # was an? is used to match 'was a' or 'was an'
		r'(\w+) was a type of (\w+)',
		r'(\w+) was a kind of (\w+)',
		r'(\w+) are ([\w\s]+)',
		r'(\w+) are a type of (\w+)',
		r'(\w+) is a (\w+)',
		r'(\w+) are a kind of (\w+)',
	]
    for pattern in patterns1: # iterate through each type 1 pattern
        matches = re.findall(pattern, s_lower)
        for match in matches:
            hyponym, hypernym = match
            if hypernym in NPs and hyponym in NPs:
                hypernyms.add((hypernym, hyponym))
    # create a list of Hearst Patterns where order is hyponym -> hypernym
    patterns2 = [
        r'(\w+)[, ] such as ([\w\s]+)(,? (and|or)?[\w\s]+)?', # such as pattern with optional and/or /commas
		r'(\w+) such as (\w+)',
		r'(\w+)[, ] including (\w+)',
		r'(\w+)[, ](\w+)',
		r'(\w+)[, ](\w+)'
	]
    for pattern in patterns2:
        matches = re.findall(pattern, s_lower)
        for match in matches:
            hypernym = match[0]
            hyponym_string = match[1].strip()
            
            for np in NPs:
                if np in hyponym_string and hypernym in NPs:
                    hypernyms.add((hypernym, np))
    # DELETE THE LINE BELOW BEFORE SUBMISSION
    # print(hypernyms)
    return hypernyms

# P1 TEST CODE START (COMMENT OR DELETE UPON SUBMISSION)

# P1 Test set 1
# NPs = ['dogs', 'cats', 'mammals', 'living things']
# s = "All mammals, such as dogs and cats, eat to survive. Mammals are living things, aren't they?"
# problem1(NPs, s)

# P1 Test set 2
# NPs = ['animals', 'dogs', 'cats']
# s = "Some animals, including cats, are considered. But it is NOT true that dogs are animals; I refuse to accept it."
# problem1(NPs, s)

# P1 Test set 3
# NPs = ['hemingway', 'bibliophile', 'author', 'william faulkner', 'mark twain']
# s = "Hemingway was an author of many classics. But also, Hemingway was a bibliophile, having read the works of every other famous American author, such as William Faulkner and Mark Twain."
# problem1(NPs, s)

# P1 TEST CODE END


# PROBLEM 2
def problem2(s1, s2):
    Lmatrix = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] # create an  L-matrix of 0s with dimensions len(s1) + 1 x len(s2) + 1
    for i in range(len(Lmatrix)):
        Lmatrix[i][0] = i
    for i in range(len(Lmatrix[0])):
        Lmatrix[0][i] = i

    for i in range(1, len(Lmatrix)): # iterate through the rows
        for j in range(1, len(Lmatrix[0])): # iterate through the columns
            if s1[i - 1] == s2[j-1]: # if the characters are the same
                Lmatrix[i][j] = Lmatrix[i - 1][j - 1]
            else:
                Lmatrix[i][j] = min(
                    Lmatrix[i][j-1]+1, # insert (penalty of 1)
                    Lmatrix[i-1][j-1]+2, # replace (penalty of 2)
                    Lmatrix[i-1][j]+1)  # delete (penalty of 1)
    # DELETE THE LINE BELOW BEFORE SUBMISSION
    print(Lmatrix[-1][-1])
    return Lmatrix[-1][-1] # return the last element of the last row of the L-matrix (bottom right)


# P2 TEST CODE START (COMMENT OR DELETE UPON SUBMISSION)

# P2 Test set 1
# s1 = "abc"
# s2 = "abbc"
# problem2(s1, s2)
# Should return 1

# P2 Test set 2
# s1 = "rjkl;34lkj 34 .!@#\n"
# s2 = "®jkl;34lK j 34 .!@#\n\t"
# problem2(s1, s2)
# Should return 6

# P2 Test set 3
# s1 = """Don't let your dreams be dreams\nYesterday you said tomorrow\nSo just do it\nMake your dreams come true\nJust do it"""
# s2 = """Some people dream of success\nWhile you're gonna wake up and work hard at it\nNothing is impossible"""
# problem2(s1, s2)
# Should return 126

# P2 TEST CODE END