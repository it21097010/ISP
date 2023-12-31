import tensorflow as tf
import pickle
import os

def __load_model_and_vectorizer():
    model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), "models/model_cnn.h5"))
    vectorizer = pickle.load(open(os.path.join(os.path.dirname(__file__), "models/vectorizer_cnn"), 'rb'))
    
    return model, vectorizer

def __clean_data(input_val):
    replacem = {
        '\n': '',
        '%20': ' ',
        '=': ' = ',
        '((': ' (( ',
        '))': ' )) ',
        '(': ' ( ',
        ')': ' ) ',
        '1 ': 'numeric ',
        ' 1': ' numeric',
        "'1 ": "'numeric ",
        " 1'": " numeric'",
        '1,': 'numeric,',
        ' 2 ': ' numeric ',
        ' 3 ': ' numeric ',
        ' 3--': ' numeric--',
        ' 4 ': ' numeric ',
        ' 5 ': ' numeric ',
        ' 6 ': ' numeric ',
        ' 7 ': ' numeric ',
        ' 8 ': ' numeric ',
        '1234': ' numeric ',
        '22': ' numeric ',
        ' 200 ': ' numeric ',
        '23 ': ' numeric ',
        '"1': '"numeric',
        '1"': '"numeric',
        '7659': 'numeric',
        ' 37 ': ' numeric ',
        ' 45 ': ' numeric '
    }

    for key, value in replacem.items():
        input_val = input_val.replace(key, value)

    return input_val

def predict(input_val):
    model, vectorizer = __load_model_and_vectorizer()
    
    input_val = __clean_data(input_val)
    
    input_val = [input_val]
    input_val = vectorizer.transform(input_val).toarray()
    input_val.shape = (1, 64, 64, 1)
    
    result = model.predict(input_val)

    if result > 0.5:
        #Then it seems like Malicious SQL query
        return 1
    else:
        #Then it seems like safe
        return 0
    
    