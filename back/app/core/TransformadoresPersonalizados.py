from sklearn.base import BaseEstimator, TransformerMixin

import re
import unicodedata
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import pandas as pd



class TildeCorrector(BaseEstimator, TransformerMixin):
    def __init__(self, columna):
        self.columna = columna
        self.replacements = {
            'Ã±': 'ñ',
            'Ã³': 'ó',
            'Ãº': 'ú',
            'Ã©': 'é',
            'Ã¡': 'á',
            'Ã­': 'í'
        }
        

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        if self.columna in X.columns:
            X[self.columna] = X[self.columna].astype(str).apply(self._correct_tildes)
        return X

    def _correct_tildes(self, text):
        for malformado, correcto in self.replacements.items():
            text = text.replace(malformado, correcto)
        return text
    



class TextCleaner(BaseEstimator, TransformerMixin):
    def __init__(self, columna, language='spanish'):
        self.columna = columna
        self.language = language
        self.stop_words = set(stopwords.words(language))
        self.stemmer = SnowballStemmer(language)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        if self.columna in X.columns:
            X[self.columna] = X[self.columna].astype(str).apply(self._clean_text)
        return X

    def _clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        text = unicodedata.normalize('NFKD', text)
        text = ''.join([c for c in text if not unicodedata.combining(c)])
        word_tokens = word_tokenize(text)
        filtered_words = [word for word in word_tokens if word not in self.stop_words]
        stems = [self.stemmer.stem(word) for word in filtered_words]
        return ' '.join(stems)