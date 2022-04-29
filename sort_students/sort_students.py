# MY CODE
def sort_a_list(a_list):
    return sorted(a_list)


def sort_by_mark(my_class):
    # dic = {}
    li = []
    for tup in my_class:
        li.append(tup)       
    
    # tuple = sorted(dic.items(), reverse=True) 
    # for i in tuple:
    #     print(i)
    return sorted(li, reverse=True)

def test(li):
    return li[1]
def sort_by_name(my_class):
    li = []
    for i in my_class:
        li.append(i)

    return sorted(li, key=test, reverse=False)


# Uncomment the following lines as needed
# if you want to test your implementation a bit:

# print(sort_a_list([3, 2, 1]))  # should print [1, 2, 3]
# my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]
# # print(sort_by_mark(my_class))  #should print []
# print(sort_by_name(my_class))


# SOMEONE ELSES
#!/usr/bin/env python3

def sort_a_list(a_list):
    return sorted(a_list, reverse=True)
    
def sort_by_mark(my_class):
    return sort_a_list(my_class)
    
def sort_by_name(my_class):
    return sorted(my_class, key=lambda x: x[1])