data = ["1,90", "2,50", "3,80", "2,80", "2,80","3,90", "1,45"]

students = {}

for entry in data:
    rno, marks = entry.split(",")
    totalmarks = students.get(rno,0)
    students[rno] = totalmarks + int(marks)

print(students)