# Answer sheet for medium questions section in the data str and alg worksheet
# by Prith (STEM ambassador)

#Medium questions


def xify(s):
    print('X'*len(s))

xify('theString123') #=> 'XXXXXXXXXXXX'
xify('134897')       #=> 'XXXXXX'
xify('i')            #=> 'X'


def palindrome(s):
    if s == s[::-1]:
        print('True')

palindrome('racecar') #=> True
palindrome('maddam')  #=> True
palindrome('laptop')  #=> False



def letterdict(s):
    s = [i for i in s]
    d2 = {}
    for i in s:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    print(d2)
letterdict('bamboozle')         #=> {'b':2, 'a':1, 'm':1, 'o':2, 'z':1, 'l':1, 'e':1}
letterdict('microsoftoffice')  #=> {'m':1, 'i':2, 'c':2, 'r':1, 'o':3, 'f':3, 't':1, 'e':1}


def shift(s,n):
    print(str(s[n:] + s[:n]))
    
shift('shiftingby3',3) #=> ftingby3shi
shift('abcdefgh',5) #=> fghabcde



import random

def passwordgen():
    length = random.randint(8,15)
    symbols = ['!', '£', '$', '%', '&', '*', '? ', '#']
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    all_list = letters + numbers + symbols
    p = "".join(random.sample(all_list,length))
    print(p)

passwordgen()
