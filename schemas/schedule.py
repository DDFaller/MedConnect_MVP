
from pydantic import BaseModel
from typing import Optional, List
from models.schedule import Schedule

class ScheduleSchema(BaseModel):
    """ 
    Define como um novo produto a ser inserido deve ser representado
    """
    doctor_crm: str = "Dr. Frederico"
    patient: str = "Fulano"
    schedule_date: str = "2023-11-08"
    schedule_time: str = "18:05:00"
    healthcare: str = "Unimed"
    clinic: str = "Visconde"
    clinic_id: str = "-1"
    contact: str = ""
    cpf: str = ""
    schedule_status = ""

class DeleteScheduleSchema(BaseModel):
    """ 
    Define como um produto a ser excluido deve ser representado
    """
    doctor: str = "Dr. Frederico"
    patient: str = "Fulano"
    schedule_date: str = "2023-11-08"
    schedule_time: str = "18:05:00"
    clinic: str = "Visconde"


class ListagemSchedulesSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    produtos:List[ScheduleSchema]

def apresenta_agendamentos(schedules: Schedule):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """

    result = []
    for schedule in schedules:
        result.append(apresenta_agendamento(schedule))

    return {"agendamentos":result}


def apresenta_agendamento(schedule: Schedule):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "Doutor": schedule.doctor_crm,
        "CPF": schedule.cpf,
        "Paciente": schedule.patient,
        "Plano": schedule.healthcare,
        "Consultorio": schedule.clinic,
        "Dia":str(schedule.schedule_date),
        "Horario": str(schedule.schedule_time),
        "Status": str(schedule.schedule_status),
        "Contato": schedule.contact
    }

def apresenta_clinicas(clinics):
    result = []
    for clinic in clinics:
        result.append(clinic[0])
    return {"consultorios":result}