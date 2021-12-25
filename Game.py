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