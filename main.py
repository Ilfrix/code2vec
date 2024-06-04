import ast
import os
from math import log10
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib


def prepare():
    dictionary = []  # dicts by files
    words = dict()  # one dict with sum words(yes or no in that file)
    path = "./train_vec"
    files = os.listdir(path)
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
        open_file = f'{path}/{file}'
        with open(open_file) as f:
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



def classify(vector, model=None):
    if model is None:
        model = joblib.load('logistic_regression_model.pkl')
    pred = model.predict(vector)
    return pred


def code2vec(path='./data'):
    file = open("log_train.txt", 'w')
    files = os.listdir(path)
    log_file = open("log_data.txt", 'w')
    
    with open('./result_vec.txt', 'r') as f:
        dictionary = f.read()
    result_dict = defaultdict(int, ast.literal_eval(dictionary))
    for file in files:
        s = ""
        open_file = path + '/' + file
        
        with open(open_file, 'r', encoding='utf8') as f:
            for line in f:
                s += str(line)
        s = s.split('\"\n\"')

        s[0] = s[0][6:]
        s[-1] = s[-1][:-2]
        value_error = 0
        value = 0
        d = defaultdict(int)
        for prog in s:
            value += 1
            try:
                k = ast.parse(prog)
            except SyntaxError:
                value_error += 1
                # print(f"In file {file} syntax error! \n#####{prog}###")
                continue
            for node in ast.walk(k):
                d[type(node).__name__] += 1
            vec = []
            for word in result_dict:
                vec.append(d[word] * result_dict[word])
            print(file, file=log_file)
            print(*vec, file=log_file)
        print(file)
        print(value_error, value, value_error/value)
            
    log_file.close()


def train():
    X = []
    Y = []
    with open("log_data.txt", 'r') as f:
        s = f.readline()
        while s:
            if (s[:5] == "task-"):
                name = int(s[5:7])
                Y.append(name)
            else:
                arr = list(map(float, s.split()))
                X.append(arr)
            s = f.readline()
            
        
    print(len(X)) # вектора
    print(len(Y)) # Ответы

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Масштабирование данных
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Создание и обучение модели логистической регрессии
    model = LogisticRegression(multi_class='auto', max_iter=1000)
    model.fit(X_train, y_train)

    # Оценка точности модели на тестовом наборе
    accuracy = model.score(X_test, y_test)
    print("Точность модели:", accuracy)
    joblib.dump(model, 'logistic_regression_model.pkl')
    return model



def main():
    # dic, word, count = prepare()
    # result_file = open("result_vec.txt", 'w')
    # result_dict = process(dic, word, count)
    # print(result_dict, file=result_file)
    # result_file.close()
    # print(result_dict)
    # print(code2vec()) # apply
    # code2vec()
    # train()
    # classify(vector)


if __name__ == '__main__':
    main()
