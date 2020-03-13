import itertools

def permute(inputlist):
    templist = list(itertools.permutations(inputlist))
    resultlist = [list(l) for l in templist]
    return resultlist
