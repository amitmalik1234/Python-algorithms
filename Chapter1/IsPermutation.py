## Determine weather or not one string is permutation of another.abs

def checkPerputation( s1,  s2):
    if len(s1) != len(s2):
        return False
    chars={}
    for i in range(len(s1)):
        if s1[i] not in chars:
            chars[str(s1[i])]=1
        else:
            chars[str(s1[i])] = int(chars[str(s1[i])]) +1
            if int(chars[str(s1[i])]) == 0:
                chars.pop(str(s1[i]))

        if s2[i] not in chars:
            chars[str(s2[i])] =-1
        else:
            chars[str(s2[i])] = int(chars[str(s2[i])]) - 1 
            if int(chars[str(s2[i])]) == 0:
                chars.pop(str(s2[i]))
                

    if chars == None:
        return True
    
            
  
if __name__ == "__main__":
    print(str(checkPerputation('abcd', 'bacd')))
