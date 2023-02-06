def permutations(s):
    if len(s) == 1:
        return [s] # return it as a list
    
    perms = permutations(s[1:]) # recursive call that gets all possible permutations
    char = s[0]
    result = []
    
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:]) # puts character in every possible position
            #bc -> abc, bac, bca 
    return result
    
        
s = input('Enter a string: ')
print(permutations(s))