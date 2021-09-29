import nltk, math, string, random
from nltk.corpus import stopwords as StopWords

class Cleaner:
    symbols= ['\n', '~', ':', "'", "''", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', '&', '<', '`', '``', '}', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    def __init__(self):
        self.better_stop_words= self.getStopWords()
    
    def getStopWords(self, lang= None, symbols=True)->list:
        if(lang== None): lang= "english"
        sw= StopWords.words(lang)
        sw+= [w.capitalize() for w in sw]
        if(symbols):
            sw+= ['\n', '~', ':', "'", "''", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '``', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
        return sw

    def tokenize_to_sentences(self, data)->list:
        """tokenizes given data in sentences"""
        return nltk.sent_tokenize(data)

    def tokenize_to_words(self, data:str)->list:
        """tokenizes given data in words"""
        return nltk.word_tokenize(data)

    def stopClean(self, data):
        """sentences:list= list of sentences, sentence:list= list of words i.e. it is an element of sentences"""
        data= "".join([x.lower() for x in data if x not in Cleaner.symbols])
        data= "".join([x for x in data if not x.isdigit()])
        sentences= self.tokenize_to_sentences(data)
        for i, s in enumerate(sentences):
            word_s= self.tokenize_to_words(s)
            word_s= [w.lower() for w in word_s if w not in self.better_stop_words]
            sentences[i]= word_s
        
        for i, s in enumerate(sentences):
            tag_word_s= nltk.pos_tag(s)
            sentences[i]= [tw[0] for tw in tag_word_s if tw[1] in ["NN", "NNS", "NNP", "NNPS"]]
        return sentences
    
    def clean(self, data):
        data= "".join([x for x in data if x not in Cleaner.symbols])
        sentences= self.tokenize_to_sentences(data)
        for i, s in enumerate(sentences):
            word_s= self.tokenize_to_words(s)
            word_s= [w for w in word_s if w not in [".", ","]]
            sentences[i]= word_s
        return sentences

    def printClean(self, data):
        cleaned_data= self.clean(data)
        for i, s in enumerate(cleaned_data):
            cleaned_data[i]= " ".join(s)
            cleaned_data[i]+= "."
        return cleaned_data

class Document:
    def __init__(self, text):
        self.raw_text= text
        self.doc_cleaner= Cleaner()
        self.cleanDocument()

    def cleanDocument(self):
        self.stop_sentences= self.doc_cleaner.stopClean(self.raw_text)
        self.cleaned_sentences = self.doc_cleaner.clean(self.raw_text)
        self.print_sentences = self.doc_cleaner.printClean(self.raw_text)

    def getstopSentences(self):
        return self.stop_sentences

    def getCleanedSentences(self):
        return self.cleaned_sentences

    def getPrintSentences(self):
        return self.print_sentences

class QuestionGenerator:
    def __init__(self, doc):
        self.document= doc

# TF-IDF
    def tf(self, words, len_words)->dict:
        tf_score= {}
        for each_word in words:
            tf_score[each_word]= tf_score.get(each_word, 0)+ 1
        # Dividing each element of dict by total_no_of_words
        tf_score.update((x, y/len_words) for x, y in tf_score.items())
        return tf_score

    def idf(self, words, sentences, len_sentences)->dict:
        idf_score = {}
        
        def check_in_sentence(word, sentences): # check occurence of a word in all sentences
            final= [word in s for s in sentences]
            return final.count(True)
        
        for each_word in words:
            if each_word in idf_score:
                idf_score[each_word] += check_in_sentence(each_word, sentences)
            else:
                idf_score[each_word] = 1
        # Performing a log and divide
        idf_score.update((x, math.log(len_sentences)/y) for x, y in idf_score.items())
        return idf_score

    def tf_idf(self, stop_sentences)->dict:
        # Gather list of all sentences and all words
        no_of_sentences= len(stop_sentences)
        words= [] # list of all words
        for s in stop_sentences:
            words.extend(s)
        no_of_words= len(words)
        # Calculate TF
        tf_score= self.tf(words, no_of_words) # Term Frequency
        # Calculate IDF
        idf_score= self.idf(words, stop_sentences, no_of_sentences) # Inverse Document Frequency
        # Calculate TF-IDF
        tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
        # Sort tf_idf_scores
        tf_idf_score= dict(sorted(tf_idf_score.items(), key=lambda elem: elem[1], reverse = True)) 
        return tf_idf_score

    def get_candidates(self, sentences, extracted_words)->dict:
        q_can= {}
        for s_id, s in enumerate(sentences):
            ans_words= [w for w in s if w.lower() in extracted_words] # list of words from the sentence that can be answer
            for aw in ans_words:
                for indx in [i for i,v in enumerate(s) if v==aw]: # find and replace ans_word with '_____'
                    sent_copy= [w.lower() for w in s]
                    sent_copy[indx]= "_____"
                    q_can[(s_id, aw)]= " ". join(sent_copy)
        return q_can

    def MakeQuestions(self)->dict:
        stop_sentences= self.document.getstopSentences()
        cleaned_sentences= self.document.getCleanedSentences()
        tf_idf_score= self.tf_idf(stop_sentences)
        question_candidates= self.get_candidates(cleaned_sentences, tf_idf_score)
        questions_marked= {}
        random_sent_order= [n for n in range(len(cleaned_sentences))]
        random.shuffle(random_sent_order)
        for i in random_sent_order:
            selected= False
            ith_questions= []
            for k in question_candidates:
                if(selected): break
                if(k[0]== i):
                    ith_questions.append(k)
            rand_indx= random.choice(ith_questions)
            questions_marked[rand_indx]= question_candidates[rand_indx]

        # question_candidates= {tuple(sentence_id, answer): dash_question}
        return questions_marked