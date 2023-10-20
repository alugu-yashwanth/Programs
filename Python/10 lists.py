# l=[19,"Yashu",27,'Vaishu']
# # a list can contain many data types
# print(l)

# # now indexex for list
# l2=[19,44,89,32,99,28]
# print(l2[3])
# print(l2[-4])
# # is similar as 
# print(l2[len(l2)-4])

# if(27 in l2):
#     print("present in list")
# else:
#     print("not present in the list")

# # using range for indexing in lists
# names=["cat","bat","doggy","cow","fish","goldy","mokey","special"]
# print(names[0:])
# # syntax for range is nameofthelist[start:end:difference between iteration]
# print(names[0::2])

# # using list comprehension means creating a list out of existing list
# # by applying a condition on it

nouns=["cat","bat","rat","mat","fit","hit","chair","table","happy","love","angry","mad","sad","grief","gratitude","lion","mamal","human","eye"]
letter_3noun=[i for i in nouns if(len(i)<4)]
print(letter_3noun)
