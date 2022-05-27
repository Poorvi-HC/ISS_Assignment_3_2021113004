flag = int(input("Sort in Ascending/Descending order: 1 for ascending, 0 for descending : "))
print("Enter 10 strings:")

l1 = []
for i in range(10):
    l1.append(input())
print("**********")
l1.sort()

if (flag == 1):
    for i in l1:
        print(i)

else:
    l1.reverse()
    for i in l1:
        print(i)
    
new = input("Input another string to be integrated in the list: ")
l1.append(new)

print("**********")
l1.sort()

if (flag == 1):
    for i in l1:
        print(i)

else:
    l1.reverse()
    for i in l1:
        print(i)

