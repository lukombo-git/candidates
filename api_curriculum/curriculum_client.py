import requests
from flask import request
from .import CURRICULUM_API_URL

class CurriculumClient:
    @staticmethod
    def create_cand_curriculum(id_candidato,habilidades,vaga_pontuacao):
        curriculum= None
        payload = {
            'id_candidato':id_candidato,
            'habilidades':habilidades,
            'vaga_pontuacao':vaga_pontuacao,
        }
        url = CURRICULUM_API_URL +'/api/curriculums/create_curriculum'
        response = requests.request("POST", url=url, data=payload)
        if response:
            curriculum = response.json()
        return curriculum
