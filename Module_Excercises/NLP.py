import nltk
from nltk import word_tokenize
text = word_tokenize("I enjoy biking on the trails")
output = nltk.pos_tag(text)
print(output)

#Skill Drill
import nltk
from nltk import word_tokenize
text = word_tokenize("Go ahead and run this code with a sentence of your choice.")
output = nltk.pos_tag(text)
print(output)

#Start from 16.6.1