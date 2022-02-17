list = ["Bob", "Rolf", "Anne"]
tupple = ("Bob", "Rolf", "Anne")
set = {"Bob", "Rolf", "Anne"}

# Access individual items in lists and tuples using the index.

print(list[0])
print(tupple[0])
# print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.

list[0] = "Smith"
# t[0] = "Smith"  # This gives an error because tuples are "immutable".

print(list)
print(tupple)

# Add to a list by using `.append`

list.append("Jen")
print(list)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`

set.add("Jen")
print(set)

# Sets can't have the same element twice.

set.add("Bob")
print(set)
