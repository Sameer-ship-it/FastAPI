from fastapi import FastAPI, Path,  HTTPException, Query
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

@app.get('/sort')
def sort_patient(sort_by: str = Query(..., description='sort on the basis of height, wieht or bmi'), order: str = Query('asc' , description='sort in asc or desc order')):

    valid_fields = ['height', 'weight' , 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, details= 'Invalid field selct from {valid_fields}')
    
    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code=400 , details = 'Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sort_by(data.values() , key = lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


