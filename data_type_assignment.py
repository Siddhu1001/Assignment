# Python Solutions (1–18)

# 1. Add two lists index-wise
list1 = ["M", "na", "i", "Ra"]
list2 = ["y", "me", "s", "hul"]
result = [[list1[i], list2[i]] for i in range(len(list1))]
print("1:", result)

# 2. Add 7000 after 6000
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print("2:", list1)

# 3. Candy items mapping
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]
print("3:")
for i in range(len(candy_list)):
    print(f"{candy_list[i]}-{no_of_items[i]}")

# 4. Running sum
list1 = [1,2,3,4,5,6]
result = []
total = 0
for num in list1:
    total += num
    result.append(total)
print("4:", result)

# 5. Sum of greater elements + itself
lst = [2,4,6,10,1]
result = []
for i in range(len(lst)):
    total = 0
    for j in range(len(lst)):
        if lst[j] >= lst[i]:
            total += lst[j]
    result.append(total)
print("5:", result)

# 6. Common unique sorted elements
num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
print("6:", sorted(list(set(num1) & set(num2))))

# 7. Sort by product of digits
lst = ['1ac21', '23fg', '456', '098d','1','kls']
def product(s):
    prod = 1
    found = False
    for ch in s:
        if ch.isdigit():
            prod *= int(ch)
            found = True
    return prod if found else 1
print("7:", sorted(lst, key=product))

# 8. Max of each row
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("8:", [max(row) for row in matrix])

# 9. Student shortlist (example)
records = [
    ("Manohar","B.Tech","Python","2022"),
    ("Ponian","B.Sc.","C++","2020")
]
req = ("Python","B.Tech","2022")
print("9:")
found = False
for rec in records:
    if (rec[2], rec[1], rec[3]) == req:
        print(rec)
        found = True
if not found:
    print("No such candidate")

# 10. Common elements in 3 lists
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
print("10:", list(set(ar1) & set(ar2) & set(ar3)))

# 11. Unique vowels count
s = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
vowels = set([ch for ch in s if ch in "aeiouAEIOU"])
print("11:", len(vowels))

# 12. Intersection using list comprehension
lst1 = [15, 9, 10, 56, 23, 78, 5, 4]
lst2 = [9, 4, 5, 36, 47, 26, 10]
print("12:", [x for x in lst1 if x in lst2])

# 13. List of tuples → dictionary
lst = [("akash", 10), ("gaurav", 12), ("anand", 14)]
result = {}
for key, val in lst:
    result[key] = [val]
print("13:", result)

# 14. Unique elements list
def unique_list(lst):
    return list(set(lst))
print("14:", unique_list([1,2,3,3,3,4,5]))

# 15. Even numbers
lst = [1,2,3,4,5,6,7,8,9]
print("15:", [x for x in lst if x % 2 == 0])

# 16. Perfect number
def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
print("16:", is_perfect(6))

# 17. Merge dictionaries
def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result
print("17:", merge_dicts({1:10},{2:20},{3:30}))

# 18. Histogram (bin size 10)
lst = [13,42,15,37,22,39,41,50]
hist = {}
for num in lst:
    low = (num//10)*10 + 1
    high = low + 9
    key = f"{low}-{high}"
    hist[key] = hist.get(key, 0) + 1
print("18:", hist)
