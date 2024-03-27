def solution(L, x):
    if x not in L :
        return [-1]
    else : 
        return [i for i, v in enumerate(L) if v == x]
