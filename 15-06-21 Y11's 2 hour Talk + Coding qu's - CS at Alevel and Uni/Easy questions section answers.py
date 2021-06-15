# Answer sheet for easy questions section in the data str and alg worksheet
# by Prith (STEM ambassador)


#Easy questions

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

