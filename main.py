total = 0

print("enter marks obtained in all 6 subjects-")
for i in range(6):
    score = float(input())
    total +=score

average = total/6
print(f"average marks-{average}")