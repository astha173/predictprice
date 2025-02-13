import json
import pickle
import numpy as np
__locations=None
__data_columns=None
__model=None

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    vector = np.zeros(len(__data_columns))
    vector[0] = sqft
    vector[1] = bath
    vector[2] = bhk
    if loc_index >=0:
        vector[loc_index] = 1
    return round(__model.predict([vector])[0],2)

def get_location():
    return __locations

def load_saved_artifects():
    global __locations, __data_columns, __model
    with open("./artifects/columns.json","r") as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]
    with open("./artifects/house_prediction_model.pickle",'rb') as f:
        __model=pickle.load(f)

if __name__=="__main__":
    load_saved_artifects()
    print(get_location())
    print(get_estimated_price('1st Phase JP Nagar',500,1,1))

