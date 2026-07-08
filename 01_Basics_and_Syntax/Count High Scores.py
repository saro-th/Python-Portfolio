"""
Script to iterate through a scores dictionary and count how many individuals scored 100 or higher.
"""

scores = {
    "Elna": 120,
    "Alex": 85,
    "Sam": 150,
    "John": 95
}
count = 0
for grade in scores:
    if scores[grade] >= 100:
       count += 1
print(count)