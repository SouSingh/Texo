from transformers import pipeline
from translate import Translator


classifier = pipeline('sentiment-analysis')

class Sentitweeten():

    def __init__(self):
        self.classifier = pipeline('sentiment-analysis')

    def Tweet_analy(self, text):
         result = classifier(text)
         result1 = result[0]
         return { 'Label' : result1['label'],
                   'Score' : result1['score']}



class Sentitweethn():

    def __init__(self):
        self.classifier = pipeline('sentiment-analysis')

    def score(self, text):
         result = classifier(text)
         result1 = result[0]
         return result1

    def convertlanguage(self, word):
        translator = Translator(from_lang='hindi', to_lang='english')
        translation = translator.translate(word)
        return translation

    def Tweet_anal(self, text):
        translator = Translator(from_lang='hindi', to_lang='english')
        translation = translator.translate(text)
        result = self.classifier(translation)
        result1 = result[0]
        return { 'Label' : result1['label'],
                   'Score' : result1['score']}

class Sentitweetsp():

    def __init__(self):
        self.classifier = pipeline('sentiment-analysis')

    def score(self, text):
         result = classifier(text)
         result1 = result[0]
         return result1

    def convertlanguage(self, word):
        translator = Translator(from_lang='spanish', to_lang='english')
        translation = translator.translate(word)
        return translation

    def Tweet_anal(self, text):
        translator = Translator(from_lang='spanish', to_lang='english')
        translation = translator.translate(text)
        result = self.classifier(translation)
        result1 = result[0]
        return { 'Label' : result1['label'],
                   'Score' : result1['score']}

class Sentitweetgn():

    def __init__(self):
        self.classifier = pipeline('sentiment-analysis')

    def score(self, text):
         result = classifier(text)
         result1 = result[0]
         return result1

    def convertlanguage(self, word):
        translator = Translator(from_lang='german', to_lang='english')
        translation = translator.translate(word)
        return translation

    def Tweet_anal(self, text):
        translator = Translator(from_lang='german', to_lang='english')
        translation = translator.translate(text)
        result = self.classifier(translation)
        result1 = result[0]
        return { 'Label' : result1['label'],
                   'Score' : result1['score']}

class Sentitweetkn():

    def __init__(self):
        self.classifier = pipeline('sentiment-analysis')

    def score(self, text):
         result = classifier(text)
         result1 = result[0]
         return result1

    def convertlanguage(self, word):
        translator = Translator(from_lang='korean', to_lang='english')
        translation = translator.translate(word)
        return translation

    def Tweet_anal(self, text):
        translator = Translator(from_lang='korean', to_lang='english')
        translation = translator.translate(text)
        result = self.classifier(translation)
        result1 = result[0]
        return { 'Label' : result1['label'],
                   'Score' : result1['score']}