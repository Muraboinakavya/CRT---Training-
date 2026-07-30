n = input()
num = int(input())
count =0
days={
    "Monday":1,
    "Tuesday":2,
    "wednesday":3,
    "Thursday":4,
    "friday":5,
    "saturday":6,
    "sunday":7
}
value = days[n]

for i in range(1,num+1):
    current_day = (value + i-1) % 7
    if(current_day == 0):
        count +=1
print(count)

