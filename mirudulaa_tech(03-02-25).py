#1
d1={'Joe': 70, 'Nick': 95, 'Moni': 85, 'Nisha': 50}
high_marks=sorted(d1.items(), key= lambda x: x[1])
print(f"Students mark in ascending order: {high_marks}")
low_marks=sorted(d1.items(), key= lambda x: x[1], reverse=True)
print(f"Students mark in descending order: {low_marks}")
top_3=sorted(d1.items(), key= lambda x: x[1], reverse=True)[:3]
print(f"Top 3 marks: {top_3}")
alpha_order=sorted(d1.items(), key= lambda x: x[0])
print(f"Alphabetical order: {alpha_order}")

#2
print(f"\n")
d2={'Joe': 10, 'Nick': 5, 'Moni': 8, 'Nisha': 7}
high_score=sorted(d2.items(), key= lambda x: x[1])
print(f"Player's scores in ascending order: {high_score}")
low_scores=sorted(d2.items(), key= lambda x: x[1], reverse=True)
print(f"Player's scores in descending order: {low_scores}")
top_3=sorted(d2.items(), key= lambda x: x[1], reverse=True)[:3]
print(f"Top 3 player's: {top_3}")
alpha_order=sorted(d2.items(), key= lambda x: x[0])
print(f"Alphabetical order: {alpha_order}")
