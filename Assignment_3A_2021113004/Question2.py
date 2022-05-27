list_of_dicts = []
num_of_inputs = int(input("Number of students: "))
for i in range(num_of_inputs):
    name = (input("Enter a name: "))
    roll = (input("Enter the roll number: "))
    Maths = float(input("Enter math marks: "))
    CSE_marks = float(input("Enter CSE marks: "))
    Sci = float(input("Enter science marks: "))
    list = [Maths,CSE_marks,Sci]
    tot = float(sum(list))
    dict = {"Name":name,
            "Roll-Number":roll,
            "Subjects":list,
            "Total": tot,
            "Rank": -1
            }
    list_of_dicts.append(dict)

def myFunc(e):
    return e["Total"]

list_of_dicts.sort(key=myFunc)
list_of_dicts.reverse()
idx = 0

print("Name -> Roll-Number")
for user in list_of_dicts:
    print(user["Name"], " -> " , user["Roll-Number"] )
    idx += 1
    user["Rank"] = idx

inp = str(input("Enter the name of the user whose data do you want to access: "))
for user in list_of_dicts:
    if (user["Name"] == inp):
        print("Name: ", user["Name"])
        print("Marks in Maths: ",user["Subjects"][0])
        print("Marks in CSE: ", user["Subjects"][1])
        print("Marks in Science: ", user["Subjects"][2])
        print("Mean: ",float(sum(user["Subjects"])/3))
        user["Subjects"].sort()
        print("Median: ",user["Subjects"][1])
        print("Rank: ",user["Rank"])


