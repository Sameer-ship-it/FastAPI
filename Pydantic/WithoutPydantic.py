def insert_patient_data(name: str, age: int):

    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative")
        else:
            print(name)
            print(age)
            print('Inserted into database')

    else:
        raise TypeError('Incorect Format Used')