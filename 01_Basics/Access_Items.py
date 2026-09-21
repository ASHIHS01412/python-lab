#List items are indexed and you can access them by referring to the index number
ashish = ["Smart", "handsome" , "good looking", "Intelligent" ,"Kind"]
print(ashish[1])

#Negative Indexing
print(ashish[-1])

#Range of Indexes
print(ashish[2:4])

#By leaving out the start value
print(ashish[:4])

#By leaving out the end value
print(ashish[2:])

#Range of Negative Indexes
print(ashish[-4:-1])

#Check if Item Exists
if "Kind" in ashish :
    print("Yes, 'Kind' is in the ashish")