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
        top_words = get_most_frequent_words(
            load_data(path_to_file), words_to_print)
        place_in_rating = 1
        for every_word in top_words:
            print('{0} - place is word "{1}" (count-{2})'.format(
                i, every_word[0], every_word[1]))
            place_in_rating += 1
    else:
        sys.exit('You forget enter path or file does not exist')
