from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, render_template,request
from urllib.parse import unquote
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.exc import IntegrityError


from flask_cors import CORS
from logger import logger
from schemas import *
from models import *

from use_cases import \
    add_doctor, \
    add_schedule,\
    get_schedule_by_doctor_clinic,\
    get_schedules, \
    get_doctors,\
    get_clinics_by_doctor,\
    delete_schedules,\
    delete_doctor

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
agendamento_tag = Tag(name="Produto", description="Adição, visualização e remoção de agendamentos à base")
comentario_tag = Tag(name="Comentario", description="Adição de um comentário à um produtos cadastrado na base")



@app.route('/')
def home():
    return render_template("home.html"), 200


@app.post('/agendamento', tags=[agendamento_tag],
          responses={"200": ScheduleSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_schedule(form: ScheduleSchema):
    """Adiciona um novo Agendamento à base

    Retorna uma representação dos agendamentos.
    """
    session = Session()
    return add_schedule(form,session)
    
@app.post('/doutor', tags=[agendamento_tag],
          responses={"200": ScheduleSchema,"409": ErrorSchema, "400": ErrorSchema})
def post_doctor(form: DoctorSchema):
    """Adiciona um novo Produto à base de dados

    Retorna os doutores cadastrados na base.
    """
    session = Session()
    response = add_doctor(form,session)
    session.close()
    return response

@app.get('/encontrar_agendamentos', tags=[agendamento_tag],
         responses={"200": ListagemSchedulesSchema})
def schedule_by_doctor_and_clinic():
    """Faz a busca por todos os agendamentos cadastrados

    Retorna uma listagem dos agendamentos.
    """
    doctor_crm = request.args.get("doctor_crm")
    clinic = request.args.get("clinic")
    session = Session()
    response = get_schedule_by_doctor_clinic(doctor_crm,clinic,session)
    session.close()
    return response


@app.get('/agendamentos', tags=[agendamento_tag],
         responses={"200": ListagemSchedulesSchema})
def schedules():
    """Faz a busca por todos os agendamentos cadastrados

    Retorna uma representação da listagem dos agendamentos.
    """
    session = Session()
    response = get_schedules(session)
    session.close()
    return response

@app.get('/doutores',tags = [agendamento_tag],
         responses={'200':ListDoctorSchema})
def all_doctors():
    """Faz a busca por todos os Doutores cadastrados

    Retorna uma representação no formato de uma listagem.
    """
    session = Session()
    response = get_doctors(session)
    session.close()
    return response

@app.get('/consultorios',tags = [agendamento_tag],
         responses={'200':ListDoctorSchema})
def clinics_of_doctor():
    """Faz a busca por todos os consultórios onde um médico faz atendimento

    Retorna uma representação no formato de uma listagem.
    """
    doctor_crm = request.args.get("doctor_crm")
    session = Session()
    response = get_clinics_by_doctor(doctor_crm,session)
    session.close()
    return response

@app.route('/agendamento', methods=['DELETE'])
def remove_a_schedule():
    """Deleta um agendamento da base

     Retorna 1 caso tenha deletado apenas um agendamento conforme esperado
    """
    clinic_to_delete = request.args.get("clinic")
    date_to_delete = request.args.get("date")
    time_to_delete = request.args.get("time")
    cpf_to_delete = request.args.get("cpf")
    session = Session()
    response = delete_schedules(clinic_to_delete,date_to_delete,time_to_delete,cpf_to_delete,session)
    session.close()
    return response


@app.route('/doutor', methods=['DELETE'])
def remove_doctor():
    """Remove um médico da base

    Retorna 1 caso tenha deletado apenas um médico conforme esperado
    """
    doctor_crm = request.args.get("doctor_crm")
    session = session()
    response = delete_doctor(doctor_crm,session)
    session.close()
    return response