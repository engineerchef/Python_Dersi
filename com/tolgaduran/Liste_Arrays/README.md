~~~~Lists
    Python Collections (Arrays)
        1. List
            * ordered
            * changeable
            * dublicate
        2. Tuple
            * ordered
            * unchangebale
            * duplicate
        3. Set
            * unordered
            * unindexed
            * no duplicate
        4. Dictionary
            * unordered
            * changeable
            * indexed
            * no duplicate

1. List Array Methods
Python has a set of built-in methods that you can use on lists.

Method      Description

append()    Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()    Removes the item with the specified value
reverse()   Reverses the order of the list
sort()	    Sorts the list

2. Tuple Array Methods
Python has two built-in methods that you can use on tuples.

Method  Description

count() Returns the number of times a specified value occurs in a tuple
index() Searches the tuple for a specified value and returns the position of where it was found

3. Set Array Methods
Python has a set of built-in methods that you can use on sets.

Method	                        Description

add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two or more sets
difference_update()             Removes the items in this set that are also included in another, specified set
discard()                       Remove the specified item
intersection()	                Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()                      Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()                        Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()                        Update the set with the union of this set and others

4. Dictionary Array Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()      Returns a dictionary with the specified keys and values
get()	        Returns the value of the specified key
items()	        Returns a list containing the a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()       Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()        Updates the dictionary with the specified key-value pairs
values()        Returns a list of all the values in the dictionary