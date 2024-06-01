'''lst=[
    {"NAME": "Laptop","Price": 36000},
    {"NAME": "Desktop","Price": 25000},
    {"NAME": "iPAD","Price": 56000},
    {"NAME": "SmartPhone","Price": 12000}
]
srt=sorted(lst,key=lambda x: x["Price"])
print(srt)'''
lst = [
    {"NAME": "Laptop", "Price": 36000},
    {"NAME": "Desktop", "Price": 25000},
    {"NAME": "iPAD", "Price": 56000},
    {"NAME": "SmartPhone", "Price": 12000}
]

# Custom sorting algorithm using lambda function
def custom_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (lambda x: x["Price"])(lst[j]) > (lambda x: x["Price"])(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Sorting the list using custom_sort function
custom_sort(lst)
print(lst)
