import pandas as pd

def read_urls_from_excel(file_path, sheet_name=0, column_name='URL'):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        urls = df[column_name].tolist()
        return urls
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")


    

def SPW():
    def count_syllables_for_text(r_p_w):
        syllable_count_dict = {}

        def count_syllables(word):
            if word.endswith("es") or word.endswith("ed"):
                return max(1, sum(word.count(vowel) for vowel in "aeiou") - word.count("e"))
            else:
                return max(1, sum(word.count(vowel) for vowel in "aeiou"))

        for word in r_p_w:
            syllables = count_syllables(word)
            syllable_count_dict[word] = syllables

        return syllable_count_dict

    syllable_counts = count_syllables_for_text(r_p_w)
    total_syl = sum(syllable_counts.values())

    total_syllables = total_syl / len(syllable_counts)
    print("total_syllables",total_syllables)

    def get_words_with_more_than_two_syllables(syllable_count_dict):
        words_with_more_than_two_syllables = []

        for word, syllable_count in syllable_count_dict.items():
            if syllable_count > 2:
                words_with_more_than_two_syllables.append(word)
        global complex_word_count
        complex_word_count = len(words_with_more_than_two_syllables)
        return complex_word_count

    complex_word_count = get_words_with_more_than_two_syllables(syllable_counts)

    print("complex_word count",r_p_w)
    print("complex_word_count",complex_word_count)
    print("total_syllables",total_syllables)
    return complex_word_count, total_syllables

# Example usage:


def pp():
  import re

  def count_personal_pronouns():
    # Define the regex pattern to match the personal pronouns
    pattern = r'\b(?:I|we|my|ours|us)\b'

    # Find all matches of the pattern in the text
    matches = re.findall(pattern, full_text2)


    # Count the total occurrences of personal pronouns
    pronoun_count = len(matches)
    print("pronoun_count",pronoun_count)
    return pronoun_count

  pronoun_count = count_personal_pronouns()
  return pronoun_count
  print("pronoun_count",pronoun_count)


import string
def AWL():

    # remove the punctuation



    def average_word_length():
        # Split the text into words


        # Calculate the total number of characters in all words
        total_characters = sum(len(word) for word in r_p_w)

        # Calculate the total number of words
        total_words = len(r_p_w)
        # Avoid division by zero
        if total_words == 0:
            return 0

        # Calculate the average word length
        avg_word_length = total_characters / total_words
        print('avg_word_length',avg_word_length)

        return avg_word_length

    # Example usage with your data
    avg_length = average_word_length()
    return avg_length


def AVG():


    def average_words_per_sentence(text):
        from nltk.tokenize import sent_tokenize
        # Tokenize sentences and words
        no_of_words = len(r_p_w)
        sentences = sent_tokenize(rejoined_text_flitered)
        no_of_sentences = len(sentences)

        # Remove stopwords and punctuation

        # Calculate the average number of words per sentence
        # Average Number of Words Per Sentence = the total number of words / the total number of sentences

        avg_words_per_sentence = no_of_words / no_of_sentences

        print("avg_words_per_sentence",avg_words_per_sentence)

        return avg_words_per_sentence

    # Example usage with your data in the variable full_text
    average_words_per_sentence_result = average_words_per_sentence(full_text)
    print(average_words_per_sentence_result)
    return average_words_per_sentence_result

#000

#poll
# AVG SENTENCE LENGTH
# PERCENTAGE OF COMPLEX WORDS
# FOG INDEX


def APF():
  import nltk
  from nltk.tokenize import sent_tokenize, word_tokenize

  def gunning_fox_index(text):
      # Tokenize sentences and words
      no_of_words = len(r_p_w)
      sentences = sent_tokenize(rejoined_text_flitered)
      no_of_sentences = len(sentences)

      # Calculate average sentence length

      avg_sentence_length = no_of_words/ no_of_sentences

      print()
      print("avg_sentence_length",avg_sentence_length)

      # Define function to check if a word is complex


      percentage_complex_words = complex_word_count /no_of_words


      # Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

      fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
      # Calculate percentage of complex words


      # Calculate Fog Index


      # kola2
      return avg_sentence_length,percentage_complex_words,fog_index

  # Example usage:
  readability_result = gunning_fox_index(full_text)
  return readability_result



## collecting stop words
def read_stopwords_from_files(stopword_files):
    all_stopwords_set = set()

    # Iterate over each file path
    for file_path in stopword_files:
        stopwords_set = set()
        with open(file_path, 'r', encoding='latin-1') as file:
            # Read stopwords from the file and add them to the set
            stopwords_set.update(file.read().splitlines())

        # Add stopwords from the current file to the set containing all stopwords
        all_stopwords_set.update(stopwords_set)

    return all_stopwords_set

# Example usage
stopword_files = ["files/StopWords/StopWords_Auditor.txt",
                  "files/StopWords/StopWords_Currencies.txt",
                  "files/StopWords/StopWords_DatesandNumbers.txt",
                  "files/StopWords/StopWords_Generic.txt",
                  "files/StopWords/StopWords_GenericLong.txt",
                  "files/StopWords/StopWords_Geographic.txt",
                  "files/StopWords/StopWords_Names.txt"]

# Create a set of all stopwords by reading from all files one by one
all_stopwords_set = read_stopwords_from_files(stopword_files)

# print(all_stopwords_set)


##removing stop words from full_text
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def remove_stopwords_from_text(full_text, stopwords_set):
    # Tokenize the text into words
    words = nltk.word_tokenize(full_text)

    # Remove stopwords
    filtered_words = [word for word in words if word not in stopwords_set]
    # Join the filtered words back into a string
    filtered_text = filtered_words

    return filtered_text

# Example usage

stopwords_set = all_stopwords_set
import pandas as pd

# Load existing data from the Excel file, if it exists
import pandas as pd

# Load existing data from the Excel file, if it exists
import pandas as pd
import os

def excel_save(positive_score, negative_score, polarity_score, subjective_score, avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count, total_syllables, pronoun_count, avg_word_length, assign_id):
    print("total_syllables ===>", total_syllables)
    
    # Define the data to be saved
    data = {'URL_ID': [assign_id],
            'URL': [url],  # Assuming url is defined somewhere
            'POSITIVE SCORE': [positive_score],
            'NEGATIVE SCORE': [negative_score],
            'POLARITY SCORE': [polarity_score],
            'SUBJECTIVITY SCORE': [subjective_score],
            'AVG SENTENCE LENGTH': [avg_sentence_length],
            'PERCENTAGE OF COMPLEX WORDS': [percentage_complex_words],
            'FOG INDEX': [fog_index],
            'AVG NUMBER OF WORDS PER SENTENCE': [avg_words_per_sentence],
            'COMPLEX WORD COUNT': [complex_word_count],
            'WORD COUNT': [word_count],
            'SYLLABLE PER WORD (Average over entire text)': [total_syllables],
            'Personal Pronouns': [pronoun_count],
            'AVG WORD LENGTH': [avg_word_length]}
    
    # Check if the file exists
    if os.path.exists('files/output_1/Output Data Structure.xlsx'):
        # Append data to existing Excel file
        df = pd.read_excel('files/output_1/Output Data Structure.xlsx')
        new_df = pd.DataFrame(data)
        df = pd.concat([df, new_df], ignore_index=True)
    else:
        # Create a new DataFrame
        df = pd.DataFrame(data)
    
    # Save the DataFrame to an Excel file
    df.to_excel('files/output_1/Output Data Structure.xlsx', index=False)

# Example usage
# You need to define variables like positive_score, negative_score, etc.



def clean_score(avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, total_syllables, pronoun_count, avg_word_length):

    print("complex_word_count ==>", complex_word_count)
    # Define create_custom_sentiment_dictionary function
    def create_custom_sentiment_dictionary():
        with open("files/MasterDictionary/positive-words.txt", "r", encoding="utf-8") as positive_file:
            positive_words = set(positive_file.read().splitlines())

        with open("files/MasterDictionary/negative-words.txt", "r", encoding="latin-1") as negative_file:
            negative_words = set(negative_file.read().splitlines())


        return positive_words, negative_words

    # Define calculate_sentiment_scores function
    def calculate_sentiment_scores(positive_words, negative_words):
        print(" calculate_sentiment_scores",full_text)

        positive_score = 0
        for word in full_text:
          if word.lower() in positive_words:
              positive_score += 1
        print("positive_score",positive_score)

        negative_score = 0
        for word_n in full_text:
          if word_n.lower() in negative_words:
              negative_score += 1
        print("negative_score",negative_score)

        total_words_after_cleaning = len(r_p_w)
        print(total_words_after_cleaning,"subjective_score2")
        # Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)

        polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

        # Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
        subjective_score = (positive_score + negative_score) / ((total_words_after_cleaning) + 0.000001)
        print(subjective_score)
        # Avoid division by zero

        def remove_stopwords_and_punctuation(tokens):
            import string
            import nltk
            nltk.download('stopwords')
            from nltk.corpus import stopwords
            stop_words = set(stopwords.words('english'))
            table = str.maketrans('', '', string.punctuation)
            cleaned_tokens = [token for token in tokens if token.lower() not in stop_words]
            cleaned_tokens = [token.translate(table) for token in cleaned_tokens]
            cleaned_tokens = [token for token in cleaned_tokens if token.strip()]
            word_count = len(cleaned_tokens)
            return word_count
        word_count = remove_stopwords_and_punctuation(full_text)


        return positive_score, negative_score, polarity_score, subjective_score, word_count

    # Example usage with your data in the variable full_text


    # Create custom sentiment dictionaries
    positive_words, negative_words = create_custom_sentiment_dictionary()

    # Calculate sentiment scores
    positive_score, negative_score, polarity_score, subjective_score, word_count = calculate_sentiment_scores(positive_words, negative_words)



    # Additional variables for demonstration


    print("subjective_score",subjective_score)

    # Additional function call for demonstration
    excel_save(positive_score, negative_score, polarity_score, subjective_score,avg_sentence_length, percentage_complex_words, fog_index,avg_words_per_sentence,complex_word_count,word_count,total_syllables, pronoun_count, avg_word_length, assign_id)


#ola

import requests
from bs4 import BeautifulSoup
import string
nltk.download('punkt')
def extract_data_from_url(url_2,classes_to_try, assign_id_2,title_selector='title'):

    global assign_id
    assign_id = assign_id_2


    global url 
    url = url_2
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title using specified selector (default is 'title')
        title_element = soup.select_one(title_selector)
        title = title_element.text.strip() if title_element else "Title not found"

        
        for class_name in classes_to_try:
            target_element = soup.find('div', class_=class_name)
            if target_element:
                break


        # Check if target_element is found after the second attempt
        if target_element:
            # Find all <p> tags within the target element
            p_tags = target_element.find_all('p')

            # Initialize an empty list to store text content
            all_text = []

            # Iterate over each <p> tag
            for tag in p_tags:
                # Extract text content and append to the list
                all_text.append(tag.get_text(separator=' ').strip())

            # Join all the text content into a single string with newline characters for separation
            text = '\n'.join(all_text)

        else:
           print("required element and text wasn't found")



        response.close()





        # Generate URL ID
        full_text = ""

        def concat(title, text):

            global full_text
            full_text = title + " " + text

            #full_text2 is particularly is used for Personal Pronouns in this program
            global full_text2
            full_text2 = full_text



            full_text = full_text.lower()

            #sentences for future use
            full_text_sen = full_text
            print("full_text sen",full_text)

            # for cleaning
            filtered_text = remove_stopwords_from_text(full_text, stopwords_set)
            global rejoined_text_flitered
            rejoined_text_flitered = ' '.join(filtered_text)

            full_text = filtered_text

            #this code is used for total number of word in entire program because it has removed punctuation
            # r_p_w removed punctuation words
            global r_p_w
            r_p_w = [word for word in full_text if word not in string.punctuation]

        concat(title, text)
        print("Title:", title)
        print("Text:", text)
        print()

        d = SPW()
        a = APF()
        b = AVG()
        print("b",b)
        print()

        # c = CWC()


        # the values are changed for below tmeprorarly
        e = pp()
        f = AWL()
        clean_score(*a,b,*d,e,f)



        return title, text  # Return extracted title and text
    else:
        print(f"Error: Unable to fetch data from the URL. Status code: {response.status_code} {url}")
        return "Title not found", "Text not found or class 'td-post-content' not found"


