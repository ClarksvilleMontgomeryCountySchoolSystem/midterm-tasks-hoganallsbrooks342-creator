total_slices = medium + large + party_pizza_mini + large + medium
print(f"Total number of slices: {total_slices}")

people += 1
each_person_gets = total_slices / people
leftover_slices = total_slices // people
print(f"Each person gets: {each_person_gets}")
print(f"Leftover slices: {leftover_slices}")

people += 2
each_person_gets = total_slices / people
leftover_slices = total_slices // people
print(f"Each person gets: {total_slices}")
print(f" Leftover slices: {leftover_slices}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

total_slices += party_pizza_mini
people += 1
each_person_gets = total_slices / people
leftover_slices = total_slices // people
print(f"Each person gets: {total_slices}")
print(f"Leftover slices: {leftover_slices}")
