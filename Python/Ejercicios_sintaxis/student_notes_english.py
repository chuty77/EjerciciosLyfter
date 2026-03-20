
n = int(input("Enter the QTY of notes: "))

total_sum = 0
approved = 0
disapproved = 0
approved_sum = 0
disapproved_sum = 0

for i in range(n):
    note = float(input(f"Enter the notes {i+1}: "))
    total_sum += note
    
    if note >= 70:
        approved += 1
        approved_sum += note
    else:
        disapproved += 1
        disapproved_sum += note

total_promedi = total_sum / n if n > 0 else 0
approved_sum = approved_sum / approved if approved > 0 else 0
disapprove_sum = disapproved_sum / disapproved if disapproved > 0 else 0


print(f"Approved notes: {approved}")
print(f"Disapproved notes: {disapproved}")
print(f"General average: {total_promedi:.2f}")
print(f"Approved average: {approved_sum:.2f}")
print(f"Disapproved average : {disapprove_sum:.2f}")
