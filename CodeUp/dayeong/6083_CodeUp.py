r, g, b = map(int, input().split())
count = 0
for i in range(0, r) :
    for j in range(0, g) :
        for k in range(0, b) :
            count += 1
            print(str(i) + " " + str(j) + " " + str(k))
            
print(count)
