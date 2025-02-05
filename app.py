# Import relevant libraries
from fastapi import FastAPI

# Instantiate routing object
app = FastAPI()

# Data containing names, occupations and addresses
data = [
  {
    "name": "John Doe",
    "occupation": "Software Engineer",
    "address": "123 Main St"
  },
  {
    "name": "Jane Smith",
    "occupation": "Data Scientist",
    "address": "456 Elm St"
  },
  {
    "name": "Michael Johnson",
    "occupation": "Web Developer",
    "address": "789 Oak St"
  },
  {
    "name": "Emily Brown",
    "occupation": "UX Designer",
    "address": "101 Maple Ave"
  },
  {
    "name": "David Lee",
    "occupation": "Product Manager",
    "address": "202 Pine St"
  },
  {
    "name": "Sarah Taylor",
    "occupation": "Marketing Specialist",
    "address": "303 Cedar St"
  },
  {
    "name": "Chris Evans",
    "occupation": "Graphic Designer",
    "address": "404 Walnut St"
  },
  {
    "name": "Jessica White",
    "occupation": "Financial Analyst",
    "address": "505 Birch St"
  },
  {
    "name": "Matthew Miller",
    "occupation": "Systems Administrator",
    "address": "606 Spruce St"
  },
  {
    "name": "Amanda Martinez",
    "occupation": "HR Coordinator",
    "address": "707 Chestnut St"
  }
]

# Route to get all names 
@app.get("/name")
def get_names():
    return {"names": [person["name"] for person in data]}

# Route to get all occupations
@app.get("/occupation")
def get_occupation():
    return {"occupations": [person["occupation"] for person in data]}

# Route to get all addressess
@app.get("/address")
def get_address():
    return {"addressess": [person["address"] for person in data]}