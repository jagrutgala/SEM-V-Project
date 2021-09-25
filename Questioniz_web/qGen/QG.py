import nltk, math, string
from nltk.corpus import stopwords as StopWords
from nltk.util import skipgrams as skipGram


class QuestionsGenerator:
    def __init__(self, qa_sentences):
        self.qa_sentences= qa_sentences
        
