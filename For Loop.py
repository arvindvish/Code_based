
#1
exp= [1200,1582,2000,5545,6355]
# total= exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
total=0
for item in exp:
    total=total+item
print(total)

#2
for i in range(1,16):
    print(i)
    print(i*i)

#3

exp= [1200,1582,2000,5545,6355]
total=0
for i in range(len(exp)):
    print('month:',(i+1),'expense:',exp[i])
    total=total+exp[i]

print("Total expense is:",total)

#3

key_location="chair"
locations=["garage","living room","chair","closet"]
for i in locations:
    if i==key_location:
        print("key found in",i)
        break
    else:
        print("key is nott found in",i)

#4

for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)

#5

i=1
while i<=5:
    print(i)
    i=i+1