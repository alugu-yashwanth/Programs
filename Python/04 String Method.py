a="!!!!Hello!!!!!!!!!!!"
print(len(a),"\n")
print(a.upper(),"\n")
print(a.lower(),"\n")
print(a.rstrip("!"),"\n")
# strip the trailing characteers in a string which are after the string
print(a.replace("Hello", "Yashu"),"\n")
b="i am trying different string methods"
print(b.split(" "),"\n")
# converts a string into list 
print(b.capitalize(),"\n")
# converts first letter capital
print(b.center(50),"\n")
# adds pre space on to string to bring it to center
print(b.count("e"),"\n")
# count no of times the character has been occured
print(b.endswith("vsdvsdvsvsvsvsfv"),"\n")
# check for the given value end with gives in boolean
print(b.endswith("ing",5,11),"\n")
# check for value between indexes

c= "he is a very a good of the night man of the vampire rised in good sunny "
print(c.find("very"),"\n")
# to find a character in the string 
print(c.find("yashwanth"),"\n")
# for not finding give the value of -1
# print(c.index("yashwanth"),"\n")
# does same work as find but if occurence of chareacter is not found it gives a Error

d="yfweiuwvonwwiwe12454r3nndvsvjv43nsvnsfvnnsv"
print(d.isalnum(),"\n")
# from A-Z and a-z and 0-9
d="yashwanthfifvsnvjnvnven"
print(d.isalpha(),"\n")
# from A-Z ad a-z 
print(d.islower(),"\n")
# tells if a string is lower or not
print(d.isprintable(),"\n")
# tells if the given string is printable or not and always escape characters are not prntable
print(d.isspace(),'\n')
# returns true when a string has white spaces

e="he is a king of forest but dont know anything so very poor"
print(e.istitle(),'\n')
# tells if each word in a string has first letter as capital or not
print(e.isupper(),'\n')
# tells if each word in a string is in upper case or not
print(e.startswith('he'),'\n')
# gives true if a string starts with given string
print(e.swapcase(),'\n')
# swap case fro each character in a string 
print(e.title(),'\n')
# converts a f=given string into title case which is when each wordhas first letter as capital