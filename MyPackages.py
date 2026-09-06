# Data Analysis
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Article Extraction
import yfinance as yf
import newsapi as napi

# html Webpage Extraction
import requests
from bs4 import BeautifulSoup

def web_text (url):
    headers = {"User-Agent": "Adam Lewis adamdlewis525@gmail.com"}

    response = requests.get(url, headers= headers)
    soup = BeautifulSoup(response.text, "html.parser")

    return soup

# Hypothesis Testing and Statistics
import scipy.stats as stats

# Binomial and Multinomial Linear Regression and Logistic Regression (supervised learning)
from statsmodels.api import OLS
from statsmodels.api import Logit
from statsmodels.api import MNLogit

# k-Means Cluster Analysis (unsupervised learning)
# NOTE: should use tf-idf instead of count vectorizer.
from sklearn.cluster import KMeans

# XGboost (regression and supervised learning classification)
import sklearn.model_selection as model_selection
import xgboost as xgb

# Converting large amounts of text to numbers
# Count Vectorizer counts word frequency
from sklearn.feature_extraction.text import CountVectorizer as count_vector
# TF-IDF counts and determins word importance
from sklearn.feature_extraction.text import TfidfVectorizer as tf_idf


# Sentiment Analysis #######################################################################
# FinBERT
from transformers import pipeline

def finbert (text):
    FinBert = pipeline(task= "text-classification", model= "ProsusAI/finbert")
    return FinBert(text, truncation=True, max_length=512)


# Topic Modeling ###########################################################################
# NOTE: Should use count vectorizer instead of tf-idf.
# Latent Dirichlet Allocation (Lda)
from sklearn.decomposition import LatentDirichletAllocation as lda


# Keyword Extraction #######################################################################
# NOTE: Do not use tf-idf or count vectorizer.
# KeyBERT
from keybert import KeyBERT


# Text Similarity ##########################################################################
# NOTE: should use tf-idf instead of count vectorizer.
# Cosine Similarity
from sklearn.metrics.pairwise import cosine_similarity

