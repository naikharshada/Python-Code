import string, sys
def ispng(str1,alphabet=string.ascii_lowercase):
    alphabet=set(alphabet)
    return alphabet<=set(str1.lower())
print(ispng('the quick brown fox jumps over the lazy dog'))
print(ispng('the fox is very clever'))
