import matplotlib.pyplot as plt

#Collect the data
data = [] # empty list
print("Enter Pokeman data:")
print("Day 1: ", end="")
day1 = int(input())
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())

# put the data in a list
data = [day1, day2, day3]

# TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot([1, 2, 3], data)
plt.title("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()
