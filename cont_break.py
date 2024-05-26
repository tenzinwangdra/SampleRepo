num=10
for i in range(1,num):
    if i==3:
        print("Skipping 3 in the inner loop")
        continue
        
    if i==7:
        print("Reached 7, breaking the outer loop")
        break
    print(i)
    i=i+1

    