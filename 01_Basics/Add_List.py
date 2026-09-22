#Append Items
ashish = ["Smart", "handsome" , "good looking", "Intelligent" ,"Kind"]
ashish.append("Motivated")
print(ashish)

#Insert Items
ashish = ["Smart", "handsome" , "good looking", "Intelligent" ,"Kind"]
ashish.insert(3,"Motivated")
print(ashish)


#Extend List
ashish = ["Smart", "handsome" ]
objective = ["good looking", "Intelligent" ,"Kind"]
ashish.extend(objective)
print(ashish)

#Add Any Iterable
ashish = ["Smart", "handsome" ]
objective = ("good looking", "Intelligent" ,"Kind")
ashish.extend(objective)
print(ashish)