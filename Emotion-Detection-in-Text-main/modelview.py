import pickle 
import os 

model_path=input("./models/emotion_classifier_pipe_lr.pkl")
with open(model_path, "rb") as model :
    load = pickle.load(model, encoding='utf-8')
    new_model_path = model_path.split('.pkl')[0] +'.txt'
    print("creating new file at : ", new_model_path)
    model_readable = open(new_model_path, 'rt')
    model_readable.write(load)
    print("writing model as readable : ", load)
model_readable.close()
model.close()