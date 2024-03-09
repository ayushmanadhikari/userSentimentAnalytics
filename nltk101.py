from nltk import tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk import WordNetLemmatizer
from nltk import pos_tag

#tokenizers split any string into tokens(words) which can be used for further analysis
#2 types of tokenizers are displayed below... whitespacetokenizer and treebanktokenzier

string1 = "this is some random string, that we are going to tokenize adsjkfn 435kjn 324."
ws_tok = tokenize.WhitespaceTokenizer()
token_list = ws_tok.tokenize(string1)
print(token_list)


#treebank tokenizer
tb_tokenizer = tokenize.TreebankWordTokenizer()
token_list = tb_tokenizer.tokenize(string1)
print(token_list)


#stemming is normalizing your text.. thus it reduces the information from your text
#stem is the base form of a word 
#affix is the additional detail attached to the word... interpreted... stem('interpret').. affix('ed')
#so stemming is removing the additional parts by leaving only the core word/ base
#Stemming is an essential preprocessing step in nlp as it helps in filtering data redundancies, leading to better machine learning training by converting variations of words into a consistent format

#porterstemmer ... less agresive 
porter = PorterStemmer()
porter_tokens = [porter.stem(token) for token in token_list]
print(porter_tokens)


#lancasterstemmer... for aggressive
lanc = LancasterStemmer()
token_list = [lanc.stem(token) for token in token_list ]
print(token_list)




#similar to stemming, lemmatization is another normalization technique with the goal of reducing the variance of your text
#The main difference is that instead of cutting the word into suffixes, it tries to get to the root of the word, commonly called lemma
#it takes pos(part of speech) tag as an input to give the exact root we are looking for
#good thing is we can extract pos tag from the text  and use it with lementizer
lementizer = WordNetLemmatizer()
lemments_list = [lementizer.lemmatize(token) for token in token_list]
print(lemments_list)


#this returns the part of speech tag from token list
pos_tags = pos_tag(lemments_list)
print(pos_tags)