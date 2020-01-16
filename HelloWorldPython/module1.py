student_names = ["James", "John", "Mark", "Paul", "Jesse", "Hannah", "Boaz", "Ruth", "Jesus"]

for name in student_names:
    if name == "Ruth":
        continue
        print("Found em! " + name)
    print("Currently testing " + name)

x = 0
while x <= 128:
    print ("x = {0}".format(x))
    x += 1
    pass

# Left off on for loops and Dictonaries (key value pairs)

student = {
"name": "Mark",
"student_id": 12,
"feedback": None
}

print(student["name"])

     