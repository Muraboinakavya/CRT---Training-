 #clap = list(map(int,input().split()))
# the above line means 
# list--->[10,20]
# input--->user(string)
# split--->1020--->"10","20"
# int---->10,20
#clap = int(input("Enter the number of claps"))
#clap = list(map(int,input().split()))
N = int(input())
claps =input().split()
total =0
for num in range(N):
    total = total + int(claps[i])
    avg = (total)//2
print("Total : ",total)
#avg = (total)//2
print("Average :",avg)