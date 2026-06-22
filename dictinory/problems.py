#TASK1: FREQUENCY OF THE WORDS in string:
# text = "apple bananna pineapple strawberry bananna apple"
# words =text.split()
# dict ={}
# for word in words:
#     if word in dict:
#         dict[word] +=1
#     else:
#         dict[word] = 1
# print(dict)
#TASK2:CREATE A DICT WITH EMPLOYE DETAILE NOE ADD BRANCH AND PHONE NUMBER AT A TIME FETCH ALL THE KEY AND VALUES USING LOOP
'''#MAKE SURE TO COPY BEFORE DELETING ANY PAIR AND POP THE LAST LAST ADDED PAIR
employe ={
    "name" :"kavya",
    "age"  : 10

}
employe.update({"branch":"cse","phone" : 8331957436})
b = employe.copy()
print(b)
print(employe.popitem())
'''
#TASK3: GROUP ANAGRAM:
# text = ["eat","tea","tan","ate","tan","nat","bat"]
# groups = {}

# for word in text:
#     key="".join(sorted(word))

#     if key in groups:
#         groups[key].append(word)
#     else:
#         groups[key]=[word]

# print(list(groups.values()))
#TASK: TOP K FREQUENT ELEMENTS:
n = [1,1,1,2,2,3]
k = int(input())
dict ={}
for i in n:
    if i in dict:
        dict[i] +=1
    else:
         dict[i] = 1
print(dict)
#sort by dict descending
result = sorted(dict,key=dict.get,reverse=True)
print(result[:k])
     

