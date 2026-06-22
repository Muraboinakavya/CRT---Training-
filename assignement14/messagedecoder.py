arr = int(input("Enter the string :"))
freq ={}
for i in arr:
    if i in freq:
        freq[i] +=1
    else:
         freq[i] =1
print(freq)
if(freq != freq[i]):
      freq.pop(freq[i])
else:
         print("yes")
         