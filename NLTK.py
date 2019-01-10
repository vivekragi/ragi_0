from nltk.tokenize import sent_tokenize,word_tokenize
lol = "hi, i am Mr . Vivek , The weather is great and python is awesome "
# print(sent_tokenize(lol))
# print(word_tokenize(lol))
for i in word_tokenize(lol):
	print(i)