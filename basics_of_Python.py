
# looping form i=0 to i=4
for i in range(5):
    print(i)
    print('next line')
    
    #looping from i=5 to i=2
    for i in range(5,1,-1):
        print(i)
        
        print(5/2) # 2.5
        print(5//2) #2
        print(-3/2) #-1.5
        print(-3//2) # -2
        print(int(-3/2)) #-1 tries giving close to zero
        print(int(-3//2)) #2
        
        print(10%3)
        print(-10%3)
        import math
        print(math.fmod(-10, 3))
        print(math.floor(3/2)) # prints 1 because it rounds down
        print(math.ceil(3/2)) # prints 2 because it rounds up
        
        print(math.sqrt(2))
        print(math.pow(2,3))
        print(math.pow(2,200))
        print(math.pow(2,200) < float("inf")) #true
        print(math.pow(2,200) < float("inf")) #false
        
        