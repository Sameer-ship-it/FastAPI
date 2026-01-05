from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json


app = FastAPI()   #created an object

@app.get("/")     #get here is used to fetch somthing from the server , post is used to post somthing in the server
def greet():
    return {'messege':"Patient Management System API "}

@app.get('/about')
def about():
    return {'messege' :'A Fully Functional API Management System To Manage Patient Records  ' }


@app.get('/view', response_model=None)
def view():
    data = load_data()
    return data


#saving new data
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data,  f)


# Fetching Patient Data
@app.get('/patient/{patient_id}', response_model=None)
def view_patient(patient_id: str):
    #load all the pateints
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    else:
        return {'Error : Patient Not Found'} 
    

@app.get('/sort', response_model=None)
def sort_patient(sort_by: str = Query(..., description='sort on the basis of height, wieht or bmi'),order: str = Query('asc' , description='sort in asc or desc order')):

    valid_fields = ['height', 'weight' , 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field selct from {valid_fields}')
    
    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code=400 , detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key = lambda x: x.get(sort_by, 0),
        reverse = sort_order
    )

    return sorted_data



class Patient(BaseModel):

    id: Annotated[str, Field(..., description = 'Id of the patient', examples=['P001'])] 
    name: Annotated[str, Field(..., description = 'Name of the patient')] 
    city : Annotated[str, Field(..., description = 'Where the patient Lives')] 
    age: Annotated[int, Field(..., gt=0 , lt=120, description = 'Age of the patient', examples=120)] 
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')] 
    height: Annotated[float, Field(...,gt = 0, description='Height of the patient in meters')] 
    weight : Annotated[float, Field(...,gt = 0, description='Weight of the patient Kgs')] 

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        
        elif self.bmi < 25:
            return 'Normal'
        
        elif self.bmi < 30:
            return 'Obese'
        
        else:
            return 'Extremely Obese'

def load_data():
    try:
        with open('patients.json' , 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}


@app.post('/create')
def create_patient(patient: Patient):

    #load exisiting data
    data = load_data()

    #check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient Already Exists')

    #new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    #save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content = {'messege': ' Patient created succcessfully'})
