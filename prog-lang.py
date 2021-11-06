prog_lang = dict({1:"C programming language is one of the oldest and most popular languages as per the TIOBE index.", 2:"Java object-oriented and general use programming language that can create objects encompassing data and functions offering structure for applications and programs.", 3:"C++ is also a general-purpose programming language that has generic, object-oriented, and functional features along with low-level memory manipulation.",4:"JavaScript is the commonly-used programming language that is used to manage the behaviour of web pages.", 5:"Structured Query Language (SQL) is the programming language that is used to manipulate databases."})

list_order = [3, 2, 4, 1, 5] 

myDict = dict()
for key in list_order:
    myDict[key] = prog_lang[key]
    
print(myDict) 