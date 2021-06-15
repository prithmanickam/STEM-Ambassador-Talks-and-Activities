# Answer sheet for hard questions section in the data str and alg worksheet
# by Prith (STEM ambassador)


#Hard questions

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
