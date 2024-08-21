# Dice sum probability calculator
# Författare: oscar wolfbrandt
# Datum:21/08/2024

"""
def main():
    user_input = input().split(" ")

if __name__ == "__main__":
    main()
"""
import random  

#takes input of dice 
d1 = input("Sidor tärning 1:")
d2 = input("sidor tärning 2:")
list = []
high = []
pre = 0

#makes list with all ressults 
for x in range(1,int(d1)+1):
    for y in range(1,int(d2)+1):
        list.append(x+y)

#counts the most common output 
for p in range(1,int(d1)+int(d2)):
    new = list.count(p)
    if new > pre:
        high.clear()
        high.append(p)
    elif new == pre:
        high.append(p)
    pre = list.count(p)



print(high)



