# Answer sheet for data structure and algorithm questions
# by Prith (STEM ambassador)

# parameters are s for string, l for list, d for dictionary
# note: there can be many ways to code the solution

#example questions


def reverseStrInList(l):
    result = []
    for i in l:
        result.append(i[::-1])
    # could use a list comprehension:  result = [i[::-1] for i in l]
    print(result)
    
reverseStrInList(['Hello','World','How','Are','You','?'])
reverseStrInList(['going','to','town','now'])


def selectionDict(d):
    list1 = []
    for k,v in d.items(): #k is key, v is value
        if v > 30:
            list1.append(k)
    print(list1)

selectionDict({'Alex':10, 'Ben':27, 'Chris':41, 'Don':39}) 
selectionDict({'apple':20, 'banana':4, 'cherry':36})       



#easy questions

def duplicates(l):
    x = []
    dup = []
    for i in l:
        if i in x:
            dup.append(i)
        else:
            x.append(i)
    print(dup)

duplicates(['b', 'y', 'i', 'i', 'a', 'y'])  #=> ['i', 'y']
duplicates(['4', '4', '5', 'j', '5', 'j'])  #=> ['4', '5', 'j']



def strReverse(s):
    print(s[::-1])
    
strReverse('hello world') #=> 'dlrow olleh'
strReverse('racecar')     #=> 'racecar'
strReverse('email')       #=> 'liame'

def passwordCheck(s):
    symbols = ['!', '£', '$', '%', '&', '*', '? ', '#']
    upper = False
    lower = False
    symbol = False
    length = True
    if len(s) >=8:
        length = True
    for i in s:
        if i == i.upper():
            upper = True
        if i == i.lower():
            lower = True
        if i in symbols:
            symbol = True
    if upper == True and lower == True and symbol == True and length == True: #or simply- if upper and lower and symbol:
        print('True')
    else:
        print('False')
        print('for the string: ' + str(s))
        print('upper is ' + str(upper))
        print('lower is ' + str(lower))
        print('symbol is ' + str(symbol))
        print('length is ' + str(length))
        
    #could also use isupper() islower() isdigit()
    
#passwordCheck('Password1!')
#passwordCheck('password')


def endCheck(s):
    x = False
    endings = ['ed', 'ing', 'ion', 'ly', 'ies']
    for i in endings:
        if s.endswith(i):
            x = True
    print(str(x))

endCheck('jumping') #=> True
endCheck('joly')         #=> True
endCheck('faught')    #=> False

#question 5 (easy questions)
colours = ['red', 'black', 'orange', 'yellow', 'blue', 'cyan', 'green', 'purple']
print(colours[0])
print(colours[-1])
print(colours[4])
print(colours[::2])


#medium questions

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
shift('abcdefgh',5)    #=> fghabcde



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


#hard questions

def playerLevel(n):
    
    lvl = 0
    lvls = [1,2,3,4,5,6,7,8,9]
    xpcap = [10,20,40,100,200,500,1000,2500,5000]
    
    for i in range(len(xpcap)):
        if sum(xpcap[:i+1]) > n:
            lvl = lvls[i]
            curxp =  n - sum(xpcap[:i])
            endxp = xpcap[i]
            print('lvl:'+str(lvl)+' xp:' + str(curxp) + '/' + str(endxp))
            break
        
playerLevel(60)   #=> lvl:3 xp:30/40
playerLevel(282)  #=> lvl:5 xp:112/200
playerLevel(1250) #=> lvl:7 xp:380/1000
playerLevel(2222) #=> lvl:8 xp:352/2500


def panel(r,c,n):
    for i in range(r):
        print(str(n) * c)
        
panel(2,3,1)
panel(4,3,5)


