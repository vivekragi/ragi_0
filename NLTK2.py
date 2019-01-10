from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
lol = "this is an example showing off stopwords filteration"
stop_words = set(stopwords.words("english"))
words = word_tokenize(lol)
filtered_sentence = []

for w in words :
	if w not in stop_words:
		filtered_sentence.append(w)

print(filtered_sentence)