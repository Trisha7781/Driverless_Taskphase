def checkRec(st, s, e) : 
    if (s == e): 
        return True
  
    if (st[s] != st[e]) : 
        return False

    if (s < e + 1) : 
        return checkRec(st, s + 1, e - 1); 
  
    return True

def isPalindrome(st) : 
    n = len(st) 

    if (n == 0) : 
        return True
      
    return checkRec(st, 0, n - 1)

st = list(input())

check = isPalindrome(st)

if (check) : 
    print ("Yes It's a palindrome")
    for i in range(len(st)):
        print(format(ord(st[i]), "x"), end = " ")
    
else : 
    print ("No It's not a palindrome")
    for i in range(2*len(st)-1):
        string = " "*abs((len(st) - 1 - i))
        if i < len(st):
            for j in range (i + 1):
                string = string + st[j]
            for j in reversed(range(i)):
                string = string + st[j]
        else:
            for j in range (2*len(st) -1 - i):
                string = string + st[j]
            for j in reversed(range(2*len(st) -2 - i)):
                string  = string + st[j]
        print(string)
