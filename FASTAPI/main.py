from fastapi import FastAPI,Path
from pydantic import BaseModel
import json

class Patient(BaseModel):
   id:int
   Name: str
   height: float
   mob_no: int
   blood_group: str
   weight: float

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
@app.get("/contact")
def contact():
 return {"message": "contact_no are 1234455"}
@app.get("/patients_get")
def patient():
 with open("patient.json", "r") as file:
   patients = json.load(file)
 return patients
 
@app.get("/patients/{id}")
def get_patient(id: int = Path(..., description = "need patient id ", example = 101)):
    with open("patient.json", "r") as file:
        patients = json.load(file)

    for patient in patients:
        if patient["id"] == id:
            return patient
        

    return {"message": "Patient not found"}
@app.post("/add")
def add_patient(patient:Patient):
    with open("patient.json", "r") as file:

        patients = json.load(file)

    patients.append(patient.model_dump())

    with open("patient.json", "w") as file:

        json.dump(patients, file, indent=4)

    return {

        "message": "Patient added successfully",

        "patient": patient}
        
   

