import itertools
class Game():
    def bit_game(alice,bob,alice_1):
        list = ["H"]
        if(alice == 1): #Alice will makes her move 
            list = ["T"]
        else:
            list = ["H"]
    
        if(bob == 1 and list[0] == "H"):  #Bob makes his move
            list = ['T']
        elif(bob == 1 and list[0] == "T"):
            list = ['H']
    
        if(alice_1 == 1 and list[0] == 'T'):  #Alice makes her move
            list = ['H']
        elif(alice_1 == 1 and list[0] == 'H'):
            list = ['T']
        
        result = 0
        
        if(list[0] =='H'):
            result = 0
            print("Alice won the game")
        else:
            result = 1
            print("Bob won the game")
        print("state after measurement is",result)
        print()
        return list
    def All_Possibility():
        counter = 0
        j= 0
        for i in itertools.product([0,1],repeat=3):
            j = j+1
            #a = i[0]
            #b = i[1]
            #c = i[2]
            print("case",j)
            print("choice", i)
            a = Game.bit_game(i[0],i[1],i[2])
            if (a[0] == "H"):
                counter = counter +1
        print("Alice won" , counter)
        print("Bob Won",8 - counter )
    def result(counts):
        print()
        a = []
        a = list(counts.items())
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        
        if (a[0][0] == '00'):
            c1 = a[0][1]
            print("Both have cooperated --> (00)",c1,"Times")
            print()
        elif (a[0][0] == '01'):
            c1 = a[0][1]
            print("Alice defected and bob cooperated --> (01)",c1,"Times")
            print()
        
        elif (a[0][0] == '10'):
            c1 = a[0][1]
            print("Bob defected and alice cooperated --> (10)",c1,"Times")
            print()
        
        elif (a[0][0] == '11'):
            c1 = a[0][1]
            print("Both Defected --> (11)",c1,"Times")
            print()
    

        try:
            a[1][0]
        except (ValueError, IndexError): 
            v = False
        else: 
            v = True

        if(v == True):    
            if (a[1][0] == '00'):
                c2 = a[1][1]
                print("Both have cooperated --> (00)",c2,"Times")
                print()
            elif (a[1][0] == '01'):
                c2 = a[1][1]
                print("Alice defected and bob cooperated --> (01)",c2,"Times")
                print()
            elif (a[1][0] == '10'):
                c2 = a[1][1]
                print("Bob defected and alice cooperated --> (10)",c2,"Times")
                print()
            elif (a[1][0] == '11'):
                c2 = a[1][1]
                print("Both Defected --> (11)",c2,"Times")
                print()
        try: 
            a[2][0]
        except (ValueError, IndexError): 
            v = False
        else: 
            v = True

        if(v == True): 
            if (a[2][0] == '00'):
                c3 = a[2][1]
                print("Both have cooperated --> (00)",c3,"Times")
                print()
            elif (a[2][0] == '01'):
                c3 = a[2][1]
                print("Alice defected and bob cooperated -->(01)",c3,"Times")
            
                print()
            elif (a[2][0] == '10'):
                c3 = a[2][1]
                print("Bob defected and alice cooperated --> (10)",c3,"Times")
            
                print()
            elif (a[2][0] == '11'):
                c3 = a[2][1]
                print("Both Defected --> (11)",c3,"Times")
           
                print()
        try:
            a[3][0]
        except (ValueError, IndexError): 
            v = False
        else: 
            v = True

        if(v == True):    
            if (a[3][0] == '00'):
                c4 = a[3][1]
                print("Both have cooperated --> (00)",c4,"Times")
            
                print()
            elif (a[3][0] == '01'):
                c4 = a[3][1]
                print("Alice defected and bob cooperated --> (01)",c4,"Times")
            
                print()
            elif (a[3][0] == '10'):
                c4 = a[3][1]
                print("Bob defected and alice cooperated --> (10)",c4,"Times")
            
                print()
            elif (a[3][0] == '11'):
                c4 = a[3][1]
                print("Both Defected --> (11)",c4,"Times")
                print()
                
    def minority_game(s):
        a = s[0] + s[1] + s[2] + s[3] 
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        
        if(a == 1): 
            if(s[0] == 1 and s[1] == 0 and s[2] == 0 and s[3] == 0):
                print("player 1 wins the game",s)
                p1 = 1
            if(s[0] == 0 and s[1] == 1 and s[2] == 0 and s[3] == 0):
                print("player 2 wins the game",s)
                p2 = 1
            if(s[0] == 0 and s[1] == 0 and s[2] == 1 and s[3] == 0):
                print("player 3 wins the game",s)
                p3 = 1
            if(s[0] == 0 and s[1] == 0 and s[2] == 0 and s[3] == 1):
                print("player 4 wins the game",s)
                p4 = 1
        elif(a == 2):
            print("No player wins the game",s)
        elif(a == 3):
            if(s[0] == 1 and s[1] == 1 and s[2] == 1 and s[3] == 0):
                print("player 4 wins the game",s)
                p4 = 1
            if(s[0] == 1and s[1] == 0 and s[2] == 1 and s[3] == 1):
                print("player 2 wins the game",s)
                p2 = 1
            if(s[0] == 1 and s[1] == 1 and s[2] == 0 and s[3] == 1):
                print("player 3 wins the game",s)
                p3 = 1
            if(s[0] == 0 and s[1] == 1 and s[2] == 1 and s[3] == 1):
                print("player 1 wins the game",s)
                p1 = 1
        elif(a == 4):
            if(s[0] == 1 and s[1] == 1 and s[2] == 1 and s[3] == 1):
                print("No player wins the game",s)
        elif(a == 0):
            if(s[0] == 0 and s[1] == 0 and s[2] == 0 and s[3] == 0):
                print("No player wins the game",s)
        else:
            print("Error wrong choice",s)
        return p1,p2,p3,p4
    def All_possibility_minority_game():
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        counter = 0
        for i in itertools.product([0,1],repeat=4):
            a = Game.minority_game(i)
            print()
            if (a[0] == 1):
                p1 = p1 +1
            elif(a[1] == 1):
                p2 = p2+1
            elif(a[2] == 1):
                p3 = p3+1
            elif(a[3] == 1):
                p4 = p4+1
            counter = counter + 1
        print("player 1 wins",p1,"times")
        print("player 2 wins",p2,"times")
        print("player 3 wins",p3,"times")
        print("player 4 wins",p4,"times")
        print("Total possible conditions = ",counter)
    def result_minority_game(counts):
        print()
        r = []
        r = list(counts.items())
        if(r[0][0] == '1000'or r[0][0] == '0111'):
            print("player 1 wins --->",r[0][1],"times")
        
        elif(r[0][0] == '0100'or r[0][0] == '1011'):
            print("player 2 wins --->",r[0][1],"times")
        
        elif(r[0][0] == '0010'or r[0][0] =='1101'):
            print("player 3 wins --->",r[0][1],"times")
        
        elif(r[0][0] == '0001'or r[0][0] == '1110'):
            print("player 4 wins --->",r[0][1],"times")
    
    
        if(r[1][0] == '1000'or r[1][0] == '0111'):
            print("player 1 wins --->",r[1][1],"times")
        
        elif(r[1][0] == '0100'or r[1][0] == '1011'):
            print("player 2 wins --->",r[1][1],"times")
        
        elif(r[1][0] == '0010'or r[1][0] =='1101'):
            print("player 3 wins --->",r[1][1],"times")
        
        elif(r[1][0] == '0001'or r[1][0] == '1110'):
            print("player 4 wins --->",r[1][1],"times")
            
    
        if(r[2][0] == '1000'or r[2][0] == '0111'):
            print("player 1 wins --->",r[2][1],"times")
        
        elif(r[2][0] == '0100'or r[2][0] == '1011'):
            print("player 2 wins --->",r[2][1],"times")
        
        elif(r[2][0] == '0010'or r[2][0] =='1101'):
            print("player 3 wins --->",r[2][1],"times")
        
        elif(r[2][0] == '0001'or r[2][0] == '1110'):
            print("player 4 wins --->",r[0][1],"times")
    
        if(r[3][0] == '1000'or r[3][0] == '0111'):
            print("player 1 wins --->",r[3][1],"times")
        
        elif(r[3][0] == '0100'or r[3][0] == '1011'):
            print("player 2 wins --->",r[3][1],"times")  
            
        elif(r[3][0] == '0010'or r[3][0] =='1101'):
            print("player 3 wins --->",r[3][1],"times")
        
        elif(r[3][0] == '0001'or r[3][0] == '1110'):
            print("player 4 wins --->",r[3][1],"times")

        