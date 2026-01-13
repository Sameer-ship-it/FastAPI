from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

#importing the ml model

with open('model.pkl' , 'rb') as f:
    model = pickle.load(f)

app = FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


#Creating  Pydandic Model To Validate Data
class UserInput(BaseModel):

    age: Annotated[int, Field(..., gt =0, lt = 120, description = 'Age of the User')]
    weight: Annotated[float, Field(..., gt =0,  description = 'Weight of the User')]
    height: Annotated[float, Field(..., gt =0, lt = 2.5, description = 'Hieght of the User')]
    income_lpa: Annotated[float, Field(..., gt =0, description = 'Annual Salary of the User')]
    smoker: Annotated[bool, Field(..., description = ' Is the User Smoker')]
    city: Annotated[str, Field(...,description = 'The City of the User Belongs To')]
    occupation: Annotated[Literal['retired', 'freelancer', 'Student', 'government_job',
        'buisness_owner', 'unemployed', 'private_job'], Field(..., description = 'Description of the User')]

@computed_field
@property
def bmi(self) -> float:
    return self.weight(self.height**2)

@computed_field
@property
def lifestyle_risk(self) -> str:
    if self.smoker and self.bmi > 30:
        return "high"
    elif self.smoker or self.bmi > 27:
        return "medium"
    else:
        return "low"
    
@computed_field
@property
def age_group(self) -> str:
    if self.age < 25:
        return "young"
    elif self.age < 45:
        return "adult"
    elif self.age < 60:
        return "middle_aged"
    return "senior"

@computed_field
@property
def city_tier(self) -> int:
    if self.city in tier_1_cities:
        return 1
    elif self.city in tier_2_cities:
        return 2
    else:
        return 3
    

