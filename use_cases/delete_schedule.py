from models.schedule import Schedule
from logger import logger

def delete_schedules(clinic_to_delete,date_to_delete,time_to_delete,cpf_to_delete,session):
    
    logger.warning(f"Deletando agendamento Clinica '{clinic_to_delete}', Date '{date_to_delete}', Time '{time_to_delete}', CPF '{cpf_to_delete}'")
    try:
        # fazendo a busca
        schedule = session.query(Schedule).filter(Schedule.schedule_date == date_to_delete).filter(Schedule.schedule_time == time_to_delete)\
                   .filter(Schedule.clinic == clinic_to_delete).filter(Schedule.cpf == cpf_to_delete).delete()
        session.commit()
        if not schedule:
            # se não há produtos cadastrados
            logger.warning("Agendamento não encontrado")
            return {"mensagem": "Agendamento não encontrado"}, 204
        else:
            logger.debug(f"%d rodutos econtrados" % len(schedule))
            # retorna a representação de produto
            return {"agendamento deletado": f"Clinica:'{clinic_to_delete}' Dia: '{date_to_delete}' Horario: '{time_to_delete}' CPF: '{cpf_to_delete}'"}, 200
        
    except Exception as e:
        error_msg = "Não foi possível excluir o item :/"
        logger.warning(f"Erro ao remover agendamento Clinica:'{clinic_to_delete}' Dia: '{date_to_delete}' Horario: '{time_to_delete}' CPF: '{cpf_to_delete}', {error_msg}")
        return {"msg":"Não foi possível excluir o item :/"}, 400