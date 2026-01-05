from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 chars',examples=['Sameer','Amit'])]
    email: EmailStr
    linkdin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    height: float
    married: Optional[bool] = None
    allergies: List[str] = Field(max_items=5)
    contact_details: Dict[str, str]


    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi



    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        # abc@hdfc.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a Valid domain')
        
        return value

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkdin_url)
    print(patient.age)
    print(patient.weight)
    print('BMI :', patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkdin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Updated')

patient_info = {
    'name': 'Nitish',
    'email': 'abc123@gmail.com',
    'linkdin_url': 'https://www.linkedin.com/in/abc/123',
    'height': 5.6,
    'age': 30,
    'weight': 56.7,
    'married': True,
    'allergies': ['dust', 'pollen'],
    'contact_details': {'Gmail': 'abc123@hdfc.com','Phone': '7623410911'}
}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)