from fastapi import FastAPI  #Imported FastAPI class from fastapi
import json


app = FastAPI()   #created an object

def load_data():
    with open('Patients.json' , 'r') as f:
        data = json.load(f)

        return data



@app.get("/")     #get here is used to fetch somthing from the server , post is used to post somthing in the server

def greet():
    return {'messege':"Patient Management System API "}

@app.get('/about')

def about():
    return {'messege' :'A Fully Functional API Management System To Manage Patient Records  ' }

@app.get('/view')
def view():
    data = load_data()

    return data

# Fetching Patient Data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    #load all the pateints
    data = load_data()

    if patient_id in data:

        return data[patient_id]
    
    else:

        return {'Error : Patient Not Found'} 


