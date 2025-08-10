# ARRAYS IN PYTHON ARE CALLED LISTS

arr= [1,2,3]
print(arr)

#can be used as stacks
arr.append(6)
arr.append(7)
print(arr) #[1, 2, 3, 6, 7]

arr.pop()
print(arr) #[1, 2, 3, 6]

arr.insert(1,56)
print(arr)    # [1, 2, 3, 56, 6]

# arr[index] = x(num to be replaced with)
arr[3] = 0  # [1, 56, 2, 0, 6]
arr[0]= 99  # [99, 56, 2, 0, 6]
print(arr)

print("initializing arr of size n with the default value of 1")
n=5
arr =[1]*n
print (arr)
print(len(arr))

print("indexing of array is diff -num is not out of bound its the form the last value")
arr = [7,5,1,4,3]
print(arr[1]) # 5 
print(arr[-1]) # 3
print(arr[-5])#7
print(arr[0]) #7

print("Sublist")
arr=[76,97,53,43,85]
print(arr[0:5])


nums = [1,2,3,4,5]

print("with INDEX")
for i in nums:
    print(i)
    
    print("without INDEX")
    nums=[11,22,33,55,66]
    for i in nums:
        print(nums)
        
        print("INDEX & VALUE")
        for i, n in enumerate(nums):
            print(i,n)
            
            print("looping through multiple arr simultaneously")
            nums1 = [8,5,3]
            nums2 = [4,6,7]
            for n1,n2 in zip(nums1, nums2):
                print(n1,n2)
                
                nums1.reverse()
                print(nums1)
                
                print("Array sorting in ascending order")
                arr1 = [7,2,6,1,4]
                arr1.sort()
                print(arr1)
                
                print("Array sorting in reverse/descending  order")
                arr1.sort(reverse=True)
                print(arr1)
                
                arr2 = ["boss","alice","Bose","doe"]
                arr2.sort()
                print(arr2)
                
                print("Sort by string length")
                arr2.sort(key = lambda x: len(x))
                print(arr2)
                
                print("list comprehension")
                arr3 = [i for i in range(5)] 
                print(arr3) #[0, 1, 2, 3, 4]
                
                arr3 = [i*i for i in range(5)] # [0, 1, 4, 9, 16] 
                print(arr3)
                
                print("2D Lists")
                arr = [[1] * 2 for i in range (3)]
                print(arr)
                
                print("Strings")
                s = "abcd"
                print(s[0:3]) # abc
                
                s += "efg"
                print(s) #abcdefg
                
                print(s[2:5]) #cde
                
                print(int("123") + int("123")) # 246
                print(str(123) + str(123)) # 123123
                
                print("In rare case we need the ASCII value")
                print(ord("a"))
                print(ord("k"))
                
                print("combining list of string with an empty string")
                strings = ["ab", "cd", "ef"]
                print("-".join(strings)) # ab-cd-ef
                
from collections import deque
queue = deque()
queue.append(6)
queue.append(8)
queue.append(9)
queue.append(9)
print(queue) # deque([6, 8, 9, 9])

queue.popleft()
print(queue, "popped left") #deque([8, 9])

queue.appendleft(1)
print(queue,"append at left")# deque([1, 8, 9])

queue.pop()
print(queue) #deque([1, 8])


print("Hashset")
mySet = set()

mySet.add(1)
mySet.add(2)
mySet.add(2)
mySet.add(7)
print(mySet)
print(len(mySet))

print("for finding out weather the elem is present")
print(1 in mySet)#True
print(2 in mySet)#True
print(3 in mySet) #False

mySet.remove(7)
print(7 in mySet)
print(mySet) #{1, 2}

print("lists to set")
print(set([1,2,3]))

print("Set comprehension")
mySet = { i for i in range(5)}
print(mySet)

map = {}
map["alice"] = 88
map["bob"] = 77
map["bob"] = 77
map[13] ="komal"
print(map["alice"]) # 88
print(map) # {'alice': 88, 'bob': 77, 13: 'komal'}
print(len(map)) # 3
print("bob" in map) #True
map.pop("alice")
print(map) #{'bob': 77, 13: 'komal'}

print("Dict comprehension")
map = { i: 2*i for i in range(5)}
print(map)

print("Looping through the maps")
map ={"alice": 88, "bob": 77}

for okey in map:
    print(okey, map[okey]) # alice 88 bob 77
    
for k, val in map.items():
        print(k, val) #  alice 88 bob 77
        
for v in map.values():
            print(v) # 88 77
            
for inkey in map.keys():
                print(inkey) # alice bob
                
                tup = (1, 2, 3)
                print(tup)
                print(tup[0]) # 1
                print(tup[1])# 2
                print(tup[-1])#3
                 #  tup[0] = 0 --> cant modify 
                print("Tuples can be used as key for hash map/set")
                map = {(1,2):3}
                print(map[(1,2)])
                
                sets = set()
                sets.add((1,2))
                print((1,2) in sets)
                
                #lists cant be keys becoz its not hashable
                
                import heapq
                
                print("heaps")
                minHeap = []
                heapq.heappush(minHeap,8)
                heapq.heappush(minHeap,1)
                heapq.heappush(minHeap,3)
                heapq.heappush(minHeap,4)
                print(minHeap) #[1, 4, 3, 8]
                print(minHeap[0]) #  1 will always give u the smallest
                print(minHeap[1]) #  4 can be anything after smallest 
                print(minHeap[2]) #  3
                
                print("popping")
                print("length",len(minHeap)) # 4
                while len(minHeap):
                    print(heapq.heappop(minHeap)) #While there is something inside, keep popping 1 3 4 8
                    #heapq.heappop(minHeap) shows (returns) the element it just removed (popped) from the heap, NOT what’s left inside the heap.
                 
                 # NO Max heap by default, to use it multiply by -1 during push & pop
                 
maxH =[]
heapq.heappush(maxH, -3)
heapq.heappush(maxH, -7)
heapq.heappush(maxH, -5)
heapq.heappush(maxH, -4)
print(maxH)
            
print("popping the max elem")
print(-1*maxH[0]) 
            
while(len(maxH)):
                print(-1*heapq.heappop(maxH))
                
                print("Suppose the arr is given already then we heapify")
                arr = [2, 1,8, 4,5 ]
                heapq.heapify(arr)
                print(arr) # [1, 2, 8, 4, 5]
                while(arr):
                    print(heapq.heappop(arr)) # 1 2 4 5 8

print("Functions")
def myFun(n,m):
    return n*m
print(myFun(2,5))   

print ("nested functions")
def outer(a,b):
    c = "c"    
    def inner():
        return a+b+c
    return inner()
print(outer("a", "b")) #abc 

def double(nums, val):
    for i in range(len(nums)):
        nums[i] *= val
nums = [1,2]
val = 3
double(nums, val)
print(nums)

class MyClass:
    def __init__(self, nums):
        self.nums =nums
        self.size = len(nums)
        
    def getlength(self):
            return self.size
        
    def getDoubleLength(self):
            return 2*self.getlength()
        
arr = MyClass ([1,2,3,4,5])
print(arr.getlength()) #5
print(arr.getDoubleLength()) # 10
print(arr.nums) # [1, 2, 3, 4, 5]
print(arr.size) # 5
         
            
            
             
        
                





                
                
                
                   



