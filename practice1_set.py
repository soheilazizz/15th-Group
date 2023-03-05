mytext = "Python is an interpreted object oriented high level programming language with dynamic semantics " \
         "Its high level built in data structures combined with dynamic typing and dynamic binding " \
         "make it very attractive for Rapid Application Development as well as for use as a scripting " \
         "or glue language to connect existing components together Python simple easy to learn syntax" \
         " emphasizes readability and therefore reduces the cost of program maintenance Python supports " \
         "modules and packages which encourages program modularity and code reuse" \
         "The Python interpreter and the extensive standard library are available in source or binary form without " \
         "charge " \
         "for all major platforms, and can be freely distributed"
mytext = mytext.lower() #غیر حساس شدن به حروف بزرگ و کوچک
textlist = mytext.split(" ") # ساخت لیست از متن
textset = set(textlist) # ساخت مجموعه از متن جهت شمارش کلمات منحصر بفرد
#  a) total number of words
print(f'total numer of words :{len(textlist)}')
#  b) total number of unique words
print(f'total numer of unique words :{len(textset)}')
#  c) total number of 'to be' occurrences
#  d) number of each 'to be' words

counlist = []
rwordlist =[]
rwordset = set()
for word in textlist:
    i = textlist.count(word)
    if i > 1:
        counlist.append(i)  # make a list for number of "to be" occurrence
        rwordlist.append(word)  # make a list for "to be" occurrence
        rwordset.add(word)  # make a set for "to be" occurrence to calculate total number
repeated_word_dictionary = {k:v for k,v in zip(rwordlist,counlist)} # make a dictionary
#  c) total number of 'to be' occurrences
print(f"total number of 'to be' occurrences:{len(rwordset)}")
#  d) number of each 'to be' words
print(f"number of each 'to be' words:{repeated_word_dictionary}")

# print(rwordlist) # چطور شد فهمید باید ورد را یونیک کند!!!!؟



