input = int(input("Enter maximum number of stars (even number): "))

l1 = (list(range(2,input + 1,2)))
l1.reverse()

j = 0
for i in l1:
    print(" "*j,"*"*i," "*j)
    j += 1

l2 = (list(range(2,input + 1,2)))
j -= 1
for i in l2:
    print(" "*j, "*"*i, " "*j)
    j -= 1


