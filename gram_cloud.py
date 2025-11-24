import nltk
import string
# set up some prereqs
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud

# parse the text.txt file
try:

    with open('text.txt', 'r') as infile:
        content = infile.read()

except FileExistsError as fee:
    m = f"Error reading file: {fee}"
    print("Error: {m}")
    exit(1)

except FileNotFoundError as fnf:
    m = f"Error reading file: {fnf}"
    print("Error: {m}")
    exit(1)

except PermissionError as pe:
    m = f"Error reading file: {pe}"
    print("Error: {m}")
    exit(1)

except Exception as e:
    m = f"Error reading file: {e}"
    print("Error: {m}")
    exit(1)

finally:

    if infile:

        infile.close()

    else:

        raise ValueError(f"text.txt is not a file")

# bucket of words it into a collection for counting
punc = set(string.punctuation)
stop_words = set(stopwords.words('english'))
words = word_tokenize(content.lower()) # Convert to lowercase for consistent counting
filt_words = [w for w in words if w not in stop_words]
cleaned_words = [c for c in filt_words if c not in punc]

word_counts = Counter(cleaned_words)
bigrams_list = list(ngrams(cleaned_words, 2))
bigram_counts = Counter(bigrams_list)
trigrams_list = list(ngrams(cleaned_words, 3))
trigram_counts = Counter(trigrams_list)

# print(word_counts)
# print(bigram_counts)
# print(trigram_counts)

wc = WordCloud(width=600, height=300, max_words=30, background_color='#202020').generate(content)
wc.to_file('wordcloud_words.png')
