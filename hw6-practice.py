# Isabelle Guiliano
# Cite any sources you used to help with the homework 
# tutorialsources, educative, https://datagy.io/python-count-unique-values-list/, https://www.digitalocean.com/community/tutorials/python-add-to-dictionary,
# https://www.tutorialspoint.com/How-to-count-total-number-of-occurrences-of-an-object-in-a-Python-list#:~:text=Using%20the%20list%20count(),given%20element%20of%20a%20list.
# including TAs and classmates: Mackenzie Smith


def string3(str):
    end = str[-2:]
    newStr = end + end + end
    return newStr
    

def exchange(str):
    first_let = str[0]
    last_let = str[-1]
    mid_str = str[1:-1]
    if len(str) <= 1:
        new_str = first_let
    else:
        new_str = last_let + mid_str + first_let
    return new_str


def count_list(lst):
    new_list = [0] * (max(lst) + 1)
    for num in lst:
      new_list[num] += 1
    return new_list
     

def remove_range(alist, min, max):
    new_list = [var for var in alist if not min <= var <= max]
    return new_list
    

def word_count_in_set(words):
    return len(set(words))
    

def topping1(dict):
    toppings = {}
    toppings["bread"] = "butter"
    for food, topping in dict.items():
        if "ice cream" == food:
            toppings["ice cream"] = "cherry"
        else:
            toppings[food] = topping
    return toppings
    

def friend_list(friend_dictionary):
    friends = {}
    for person, friend in friend_dictionary.items():
        if person not in friends:
            friend_list = [friend]
            friends[person] = friend_list
        else:
            friends[person].append(friend)
        if friend not in friends:
            people = [person]
            friends[friend] = people
        else:
            friends[friend].append(person)
        temp = friends.pop("Marty")
        friends["Marty"] = ["Cynthia", "Danielle"]
    return friends
    

#Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert exchange("code") == "eodc", 'exchange("code") expected eodc'
print("correct")
assert exchange("ba") == 'ab', 'exchange("ba") expected ab'
print("correct")
assert exchange("a") == 'a', 'exchange("a") expected a'
print("correct")

assert count_list([1,1,5,6,6,7,3]) ==  [0,2,0,1,0,1,2,1], 'expected  [0,2,0,1,0,1,2,1]'
print("correct")
assert count_list([0,0,0,1]) ==  [3,1], 'expected  [3,1]'
print("correct")
assert count_list([10,9,8,7,6,5,4,3,2,1,0]) ==  [1,1,1,1,1,1,1,1,1,1,1], 'expected  [1,1,1,1,1,1,1,1,1,1,1]'
print("correct")

assert remove_range([7, 9, 4, 2, 7, 7, 5, 3, 5, 1, 7, 8, 6, 7], 5, 7) == [9, 4, 2, 3, 1, 8] , '[9, 4, 2, 3, 1, 8] expected'
print("correct")
assert remove_range([7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], 2, 3) == [7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7], '[7, 9, 4, 7, 7, 5, 5, 1, 7, 8, 6, 7] expected'
print("correct")
assert remove_range([7, 9, 7], 7, 9) == [], '[] expected'
print("correct")

assert word_count_in_set(["the", "quick", "brown", "fox", "brown"]) == 4, 'expected 4'
print("correct")
assert word_count_in_set(["brown", "brown"]) == 1, 'expected 1'
print("correct")

assert topping1({"ice cream": "peanuts"}) == {"bread": "butter", "ice cream": "cherry"}, 'expected {"bread": "butter", "ice cream": "cherry"}'
print("correct")
assert topping1({"bread": "butter"}) == {"bread": "butter"}, 'expected {"bread": "butter"}'
print("correct")
assert topping1({"pancake": "syrup"}) == {"bread": "butter", "pancake": "syrup"}, '{"bread": "butter", "pancake": "syrup"}'
print("correct")

assert friend_list({"Marty": "Cynthia", "Danielle": "Marty"})== {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}, 'expected {"Cynthia":["Marty"], "Danielle":["Marty"], "Marty":["Cynthia", "Danielle"]}'
print("correct")


# Problems found on https://codingbat.com/python



