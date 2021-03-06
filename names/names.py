import time

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements


'''
The ORIGINAL runtime of the TWO FOR LOOPS would be: O(n^2) 
The NEW runtime with a ONE FOR LOOP and IF statement would be: O(n)

[ORIGINAL] ===> 8.507248640060425 seconds
[NEW]      ===> 1.2948925495147705 seconds
[STRETCH]  ===> 0.008977413177490234 seconds
'''
# ===== STRETCH SOLUTION =====
# names_1 = set(names_1)
# names_2 = set(names_2)
# ===== STRETCH SOLUTION =====

for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.