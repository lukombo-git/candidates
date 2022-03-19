from http.client import responses
from django.http import response
from flask import Blueprint, jsonify, request,flash,redirect
from flask.helpers import make_response
from models import db, Candidates
from models import *
from flask import Flask, flash, request, redirect
import json
import os

candidate_blueprint=Blueprint('candidates_api_routes',__name__,url_prefix='/api/candidates')

#createing a new candidate
@candidate_blueprint.route('/create', methods=['GET','POST'])
def create_candidates():
    if request.method == 'POST':
        try:
            candidate = Candidates()
            candidate.nome_completo = request.form["nome_completo"]
            candidate.data_nascimento = request.form["data_nascimento"]
            candidate.natural_de = request.form["natural_de"]
            candidate.genero = request.form["genero"]
            candidate.n_bilhete = request.form["n_bilhete"]
            candidate.provincia_residencia = request.form["provincia_residencia"]
            candidate.telemovel_principal = request.form["telemovel_principal"]
            candidate.email = request.form["email"]
            candidate.habilitacoes_academica = request.form["habilitacoes_academica"]
            candidate.instituicao=request.form["instituicao"]
            candidate.curso = request.form["curso"]
            candidate.ano_conclusao = request.form["ano_conclusao"]
            candidate.media_final = request.form["media_final"]
            candidate.area_candidatura = request.form["area_candidatura"]
            candidate.ano_experiencia_area = request.form["ano_experiencia_area"]
            candidate.disponibilidade = request.form["disponibilidade"]
            candidate.nivel_ingles = request.form["nivel_ingles"]
            candidate.curriculum = request.form["curriculum"]
            db.session.commit()
            db.session.add(candidate)
            db.session.commit() 
            
            response ={'message':'Candidato Criado com sucesso!','result':candidate.serialize()}         

        except Exception as e:
            print(str(e))
            response = {'message':'Erro ao criar o candidato','result':candidate.id_candidato} 
    return jsonify(response)

#updating candidate
@candidate_blueprint.route('/update_cand/<id_candidato>', methods=['PUT'])
def candidate_update_form(id_candidato):
    candidate = Candidates.query.get(id_candidato)
    try:
        candidate.nome_completo = request.form["nome_completo"]
        candidate.genero = request.form["genero"]
        candidate.instituicao=request.form["instituicao"]
        candidate.curso = request.form["curso"]
        candidate.nivel_ingles = request.form["nivel_ingles"]
        candidate.provincia_residencia = request.form["provincia_residencia"]
        db.session.commit()
        db.session.add(candidate)
        db.session.commit() 
        response ={'message':'Candidato Atualizado com sucesso com sucesso!','result':candidate.serialize()}         
    except Exception as e:
        print(str(e))
        response = {'message':'Erro ao criar o candidato','result':candidate.id_candidato} 
    return jsonify(response)

#deleting candidate
@candidate_blueprint.route('/delete/<id_candidato>', methods=['DELETE'])
def candidate_delete(id_candidato):
    try:
        candidate = Candidates.query.get(id_candidato)
        db.session.delete(candidate)
        db.session.commit()
        response ={'message':'Candidato(a) eliminad0(a) com sucesso!','result':candidate.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message':'Candidato não existe.'}
    return jsonify(response)

#getting all candidates
@candidate_blueprint.route('/all', methods=['GET'])
def get_all_candidates():
    all_candidates = Candidates.query.all()
    result = [candidate.serialize() for candidate in all_candidates]
    response = {'message':'Returning all candidates','result': result}
    return jsonify(response)

#getting 10 candidates
@candidate_blueprint.route('/10_candidates', methods=['GET'])
def get_10_candidates():
    all_candidates = Candidates.query.limit(10).all()
    result = [candidate.serialize() for candidate in all_candidates]
    response = {'message':'Returning all candidates','result': result}
    return jsonify(response)

#get candidate by id
@candidate_blueprint.route('/<int:id_candidato>', methods=['GET'])
def candidates_id(id_candidato):
    candidate = Candidates.query.filter_by(id_candidato=id_candidato).first()
    if candidate:
        return jsonify({"result":candidate.serialize()}), 200
    return jsonify({"result":"Candidato não existe"}), 404


#count how much candidate is there
@candidate_blueprint.route('/count_candidates', methods=['GET'])
def cont_candidates():
    total_candidato = Candidates.query.count()
    response = {'message':'Returning all candidates','result': total_candidato}
    return jsonify(response)

#get candidate by id
@candidate_blueprint.route('/<nome_completo>', methods=['GET'])
def candidates_nome(nome_completo):
    candidate = Candidates.query.filter_by(nome_completo=nome_completo).first()
    if candidate:
        return jsonify({"result":candidate.serialize()}), 200
    return jsonify({"result":"Candidato não existe"}), 404

