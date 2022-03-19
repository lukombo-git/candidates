import requests
from .import CURRICULUM_API_URL

class CurriculumClient:
    @staticmethod
    def get_curriculums():
        response = requests.get(CURRICULUM_API_URL+'/api/curriculums/all')
        return response.json()

    
    @staticmethod
    def get_candidate(slug):
        response = requests.get(CURRICULUM_API_URL+'/api/curriculums/'+slug)
        return response.json()
    
    @staticmethod
    def create_curriculum(id_candidato,habilidades,vaga_pontuacao):
        curriculum= None
        payload = {
            'id_candidato':id_candidato.data,
            'habilidades':habilidades.data,
            'vaga_pontuacao':vaga_pontuacao.data,
        }
        url = CURRICULUM_API_URL +'/api/curriculum/create'
        response = requests.request("POST", url=url, data=payload)
        if response:
            curriculum = response.json()
        return curriculum
