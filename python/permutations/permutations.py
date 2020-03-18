class Permutation:
    resultlist = list()
    intlist = list()
    def __init__(self,intlist):
        self.resultlist = []
        self.intlist = intlist

def swap(i,j,intlist):
    temp = intlist[i]
    intlist[i] = intlist[j]
    intlist[j] = temp
    return intlist

def CreatePermutation(i,n,intlist,resultlist):
    if i == n:
        resultlist.extend(intlist)
    else:
        for j in range(i,n):
            swap(i,j,intlist)
            CreatePermutation(i+1,n,intlist,resultlist)
            swap(i,j,intlist)
    return resultlist

def CreatePermutationNestedList(intlist,resultlist):
    templist = list()
    perlist = CreatePermutation(0,len(intlist),intlist,resultlist)
    persize = len(intlist)
    n = int(len(perlist))
    i = 0
    while i<len(perlist):
        templist.append(perlist[i:i+3])
        i+=3

    if intlist[0]<intlist[1]:
        templist=sorted(templist, reverse=False)
    elif intlist[0]>intlist[1]:
        templist=sorted(templist, reverse=True)
    return(templist)

def permute(intlist):
    permutation = Permutation(intlist)
    return CreatePermutationNestedList(permutation.intlist,permutation.resultlist)

resultlist = []
