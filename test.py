import pandas
from random import randint
data = pandas.read_csv("./data/french_words.csv")

words_collection= data.to_dict()
index = randint(0,100)
print(words_collection["French"][index])
print(words_collection["English"][index])

# words_collection.

# print(data["English"])