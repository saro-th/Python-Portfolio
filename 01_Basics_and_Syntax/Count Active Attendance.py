"""
Script to iterate through an attendance dictionary and count how many students are marked present (1).
"""

attendance = {
    "Elna": 1,
    "Alex": 0,
    "Sam": 1,
    "John": 1
}
count = 0
for students in attendance:
    if attendance[students] == 1:
         count += 1
print(count)