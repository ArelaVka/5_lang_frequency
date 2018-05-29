import re
import sys
import os
import collections


def load_data(file_path):
    try:
        with open(file_path, 'r') as opened_file:
            return opened_file.read()
    except ValueError:
        return None


def get_most_frequent_words(text, count_of_words):
    words = re.findall(r'\w+', text.lower())
    most_freq_words = collections.Counter(words).most_common(count_of_words)
    return most_freq_words


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        path_to_file = sys.argv[1]
        words_to_print = 10
        print ('Ten most frequent words: ',
               get_most_frequent_words(load_data(path_to_file), words_to_print))
    else:
        sys.exit('You forget enter path or file does not exist')
