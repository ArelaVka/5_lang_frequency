import re


def load_data(file_path):
    try:
        with open(file_path, 'r') as opened_file:
            return opened_file.read()
    except ValueError:
        return False


def get_most_frequent_words(input_text):
    words = re.findall(r'\w+', input_text.lower())
    print(words)
    #Counter(words).most_common(5)
    #clear_list_data = input_text.replace('.', '').replace(',', '').split()
    #for word in clear_list_data:
    #print('Слово (', word, ') встречается ', clear_list_data.count(word), ' раз(а).')

if __name__ == '__main__':
    path_to_file = 'test1.txt'
    if load_data(path_to_file):
        get_most_frequent_words(load_data(path_to_file))
    else:
        print('No such file')
