import ast
import os
from math import log10
from collections import defaultdict
from sklearn.linear_model import LogisticRegression


def prepare():
    dictionary = []  # dicts by files
    words = dict()  # one dict with sum words(yes or no in that file)
    files = os.listdir(".")
    file_value = 0
    log_file = open("log.txt", 'w')
    files_name = []

    # get information
    for file in files:
        if file[-2:] != 'py':
            continue
        files_name.append(file)
        file_value += 1
        s = ""
        with open(file) as f:
            for line in f:
                s += str(line)
            k = ast.parse(s)
            d = dict()

            for node in ast.walk(k):
                if type(node).__name__ in d:
                    d[type(node).__name__] += 1
                else:
                    d[type(node).__name__] = 1
            dictionary.append(d)
            for current_word in list(d.keys()):
                if current_word in words:
                    words[current_word] += 1
                else:
                    words[current_word] = 1

    print(file_value, file=log_file)
    print(files_name, file=log_file)
    print(dictionary, file=log_file, end="\n\n")
    print(words, file=log_file, end="\n\n")

    log_file.close()
    return dictionary, words, file_value


def average_dicts(dicts):
    result = defaultdict(list)

    for d in dicts:
        for key, value in d.items():
            result[key].append(value)
    return {key: sum(values) / len(values) for key, values in result.items()}


def process(dictionary, words, file_value):
    vector = []
    for i in range(len(dictionary)):
        vector.append(dict())
        r = 0
        for word in dictionary[i]:
            r += dictionary[i][word]
        for word in dictionary[i]:
            vector[i][word] = (dictionary[i][word] / r) * \
                (log10((file_value + 1) / (words[word] + 1)) + 1)

    result = []
    norm = 0
    for i in range(len(vector)):
        for word in dictionary[i]:
            norm += vector[i][word] ** 2

    norm = norm ** 0.5
    for i in range(len(vector)):
        result.append(dict())
        for word in dictionary[i]:
            result[i][word] = vector[i][word] / norm
    result_file = open("result.txt", 'w')
    print(result, file=result_file)
    result_file.close()

    result_dict = average_dicts(result)
    return result_dict


def code2vec():
    dictionary = defaultdict()
    words = dict()
    path = "./test"
    files = os.listdir(path)
    file_value = 0
    log_file = open("log_test.txt", 'w')
    print("test", file=log_file)
    print("files:", files, file=log_file)

    with open('result_vec.txt', 'r') as f:
        dictionary = f.read()
    result_dict = defaultdict(int, ast.literal_eval(dictionary))

    # get information
    for file in files:
        if file[-2:] != 'py':
            continue

        file_value += 1
        s = ""
        open_file = path + '/' + file
        with open(open_file) as f:
            for line in f:
                s += str(line)
            k = ast.parse(s)
            d = defaultdict(int)

            for node in ast.walk(k):
                d[type(node).__name__] += 1

    result_vec = []
    for word in result_dict:
        result_vec.append(d[word] * result_dict[word])

    print(result_vec, file=log_file, end='\n\n')
    log_file.close()
    return result_vec


def classify(vector, model=None):
    if model is None:
        model = LogisticRegression(random_state=42)


def train():
    data = []
    with open("result_vec.txt", 'r') as f:
        data = f.read()
    model = LogisticRegression(multi_class="multinomial")
    model.fit()

    return model


def main():
    dic, word, count = prepare()
    result_file = open("result_vec.txt", 'w')
    print(process(dic, word, count), file=result_file)
    result_file.close()
    print(code2vec())


if __name__ == '__main__':
    main()
