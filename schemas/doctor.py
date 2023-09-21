from pydantic import BaseModel
from typing import List
from models.doctor import Doctor 

class DoctorSchema(BaseModel):
  name: str = "Dr. Frederico"
  speciality: str = "Cardiologista"
  crm: str = "0000"

class ListDoctorSchema(BaseModel):
    doctors:List[DoctorSchema]

def apresenta_doutores(doctors: Doctor):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for doctor in doctors:
        result.append(apresenta_doutor(doctor))

    return {"doutores":result}



def apresenta_doutor(doctor: Doctor):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "Doutor": doctor.name,
        "Especialidade": doctor.speciality,
        "CRM": doctor.crm
    }

