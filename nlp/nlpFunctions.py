# -*- coding: utf-8 -*-
__author__ = 'SMIDA AMINE'

"""
This class contain all the  functions that allow us  to  manipulate the text
Those  functions  are the basic of the NLP  programme
the Functions are :
    1-senTenceSegm(text)  Segment the Text in to sentences
"""

from nltk.corpus import stopwords
from nltk import *
from nltk.util import ngrams


class NlpFunc():






    ## Simple function return List of Sentens
    ##return list of sentences
    def senTenceSegm(self,text):
        #remove punction    ,re.UNICODE
        text=" ".join(re.findall(r"\w+",text))
        sent_detector = data.load('tokenizers/punkt/english.pickle')
        return  sent_detector.tokenize(text)




    ## Tokennize the text(list of sentences)
    ##return list of words
    def tokennisation(self,listSentences):

        listWord=[]
        for sentece in listSentences:
            for word in word_tokenize(sentece):
                listWord.append(word)
        return listWord




    ##Lower Case the words
    def lowerCaseAll(self,listWord):

        listWordLower=[]
        for word in listWord:
            listWordLower.append(word.lower())

        return listWordLower


    ##Stop word removal
    def removeStopWord(self,listWord):
        listWordNonStoW=[]
        for word in listWord:
            ##french
            if word not in stopwords.words('english'):
                listWordNonStoW.append(word)


        return listWordNonStoW

    ##tagging (POS)
    def tagging(self,listtWord):
        wordsTag=[]
        temp=" ".join(listtWord)
        print pos_tag(listtWord)
        for word in listtWord:
            wordsTag.append(pos_tag(word))
        #unigram_tagger = nltk.UnigramTaggerkkd
        return wordsTag

    ##Stemmer
    def stemer(self,listWord):
        tempList=[]
        ##french
        stemer=stem.SnowballStemmer('english')
        for word in listWord:
            tempList.append(stemer.stem(word))

        return  tempList



    def replaNumber(self,list):

        text=" ".join(list)
        text=re.sub(r'\d+',"[NUM]",text)
        return text.split()



    def ngrammeGenerat(self,listWord,nb):
        trigrams = ngrams(listWord, nb)

        listNgram=[]
        for grams in trigrams:
            listNgram.append(grams)

            print grams

        return listNgram



    def processText(self,text,nb):
        sentences=self.senTenceSegm(text)
        #print sentences
        tokens= self.tokennisation(sentences)
        #print "Tokens :",tokens
        listlower=self.lowerCaseAll(tokens)
        #print "Lower:",listlower
        listNoStop=self.removeStopWord(listlower)

        listSter=self.stemer(listNoStop)

        #print"sttemed",listSter

        listReplaceNum=self.replaNumber(listSter)
        #print "replace Number",listReplaceNum

        return  self.ngrammeGenerat(listReplaceNum,nb)

        #print plagiaFunc.jaccardSimilarity(listReplaceNum,listReplaceNum,len(listReplaceNum),len(listReplaceNum))

