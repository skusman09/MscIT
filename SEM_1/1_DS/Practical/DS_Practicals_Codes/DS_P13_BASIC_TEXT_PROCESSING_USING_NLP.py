# DS_P13_BASIC_TEXT_PROCESSING_USING_NLP

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
Txt = "Good Day Mr. Vermeulen, \
how are you doing today?\
The weather is great, and Data Science is awesome.\
You are doing well!"
print (Txt, '\n')
print('Identify sentences')
print(sent_tokenize (Txt), '\n')
print('Identify Word')
print (word_tokenize (Txt))