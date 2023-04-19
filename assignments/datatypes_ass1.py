# creates a list of all words in a text
text = "CR7 is a great footballer. CR7 plays football and has great fan following. CR7 is 35 years old. CR7 is a good boy."

# text = input("Enter a paragraph or a passage. ")
text = text.lower()
listofwords = text.split()

#need to remove unwanted signs, symbols in a text
list_updated = []
for items in listofwords:
     newitem = items.strip(".?(),:;'[]/-")
     list_updated.append(newitem)
print(list_updated)

#Create a dictionary that maps each unique word to the number of times it appears in the text
mydict = {}
for item in list_updated:
     c = list_updated.count(item)
     mydict[item] = c
print("Created a dictionary with unique words and their occurence in the text:")
print(mydict)

#create a set of unique words in a set
setofwords = set(list_updated)
print("This is the set of the unique words in the text.")
print(setofwords)

#grouping unique words in the text
words_sorted = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
mydict_sorted = dict(words_sorted)
# print(mydict_sorted)

print("Top 5 most repeated words in the text are: ")
count = 1
for key,value in mydict_sorted.items():
     print(key,value)
     if (count==5):
          break
     count += 1

