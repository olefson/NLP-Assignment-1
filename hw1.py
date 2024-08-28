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
		r'(\w+) was (\w+)',
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
            hypernym, hyponym = match
            if hypernym in NPs and hyponym in NPs:
                hypernyms.add((hypernym, hyponym))
    # create a list of Hearst Patterns where order is hyponym -> hypernym
    patterns2 = [
		r'(\w+)[, ] such as ([\w\s]+)[, ](and|or)?[\w\s]', 
		r'(\w+) such as (\w+)',
		r'(\w+)[, ](\w+)',
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

# TEST CODE START (COMMENT OR DELETE UPON SUBMISSION)

# Test set 1
# NPs = ['dogs', 'cats', 'mammals', 'living things']
# s = "All mammals, such as dogs and cats, eat to survive. Mammals are living things, aren't they?"
# problem1(NPs, s)

# Test set 2
# NPs = ['animals', 'dogs', 'cats']
# s = "Some animals, including cats, are considered. But it is NOT true that dogs are animals; I refuse to accept it."
# problem1(NPs, s)

# Test set 3
# NPs = ['hemingway', 'bibliophile', 'author', 'william faulkner', 'mark twain']
# s = "Hemingway was an author of many classics. But also, Hemingway was a bibliophile, having read the works of every other famous American author, such as William Faulkner and Mark Twain."
# problem1(NPs, s)

# TEST CODE END

# PROBLEM 2
def problem2(s1, s2):
    pass
	