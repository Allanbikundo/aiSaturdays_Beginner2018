import random 

#initializing lists
ourList = list()
belowFive = list()

count = 0


while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    #if statement to check if element is larger than five
    if ourList[count-1] < 5:
        belowFive.append(ourList[count-1])       
    
#print lists    
print(ourList)
print(belowFive)
