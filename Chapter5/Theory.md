**1.)**
emptyDict={}

---
**2.)**
dict= {'foo': 42}

---
**3.)**
Dictionary has key value pairs, unlike lists. While the order of items matters for determining whether two lists are the same, it does not matter in what order the key-value pairs are typed in a dictionary. Because dictionaries are not ordered, they can’t be sliced like lists.

---
**4.)**
As the key 'foo' doesn't exist in the given dictionary, it will give a KeyError message.

---
**5.)**
Both check for 'cat' in dictionary's keys.

---
**6.)**
'cat' in spam will check if 'cat' is a key in spam. 
'cat' in spam.values() checks if there's a value 'cat' corresponding to any key in the dictionary.

---
**7.)**
spam.setdefault('color', 'black')

---
**8.)**
We use pprint module to pretty print a dictionary's values. The function used is pprint.pprint(dcitionary_name).