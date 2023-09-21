
from pydantic import BaseModel
from typing import List
from models.clinic import Clinic 

class ClinicSchema(BaseModel):
  id: int = -1
  name: str = "Dr. Frederico"
  address: str = "Nascimento Silva"

class ListClinicSchema(BaseModel):
    doctors:List[ClinicSchema]

def show_clinics(clinics: Clinic):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for clinic in clinics:
        result.append(show_clinic(clinic))

    return {"clinics":result}

def show_clinic(clinic: Clinic):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": clinic.id,
        "Nome": clinic.name,
        "Address": clinic.address
    }
