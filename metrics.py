import numpy as np
import pandas as pd

correct_answers = [
    {
        'Brand': '',
        'Model': 'S10',
        'Price': '',
        'Motor': '2.8',
        'Year': '03',
        'Odometer': '',
        'Fuel': 'diesel',
        'Gear': '',
        'Steering': '',
        'Color': 'branco',
        'Air-Conditioning': 'sim',
        'Optionals': 'completo',
     },

    {
        'Brand': '',
        'Model': 'ONIX LT',
        'Price': '38.990,00',
        'Motor': '1.4',
        'Year': '14',
        'Odometer': '',
        'Fuel': 'flex',
        'Gear': 'manual',
        'Steering': '',
        'Color': 'vermelha',
        'Air-Conditioning': '',
        'Optionals': '',
     },

    {
        'Brand': '',
        'Model': 'COBALT LTZ',
        'Price': '54.990,00',
        'Motor': '1.8',
        'Year': '16',
        'Odometer': '',
        'Fuel': 'flex',
        'Gear': 'manual',
        'Steering': '',
        'Color': 'marron',
        'Air-Conditioning': '',
        'Optionals': '',
     },

    {
        'Brand': '',
        'Model': 'ASTRA ADVANEGE',
        'Price': '',
        'Motor': '',
        'Year': '08',
        'Odometer': '',
        'Fuel': '',
        'Gear': '',
        'Steering': '',
        'Color': 'prata',
        'Air-Conditioning': 'sim',
        'Optionals': '4p, completo',
     },
    #   da a20 6 cil:  com comando 250s e escap. 6x2 cambio 5 marchas
    {
        'Brand': '',
        'Model': 'VERANEIO',
        'Price': '25.000,00',
        'Motor': '',
        'Year': '72',
        'Odometer': '',
        'Fuel': 'alcool',
        'Gear': '',
        'Steering': 'mecanica',
        'Color': '',
        'Air-Conditioning': '',
        'Optionals': '', # TODO Ver opcionais***
     },

    {
        'Brand': '',
        'Model': 'BLAZER',
        'Price': '24.500,00',
        'Motor': '4.3',
        'Year': '00',
        'Odometer': '',
        'Fuel': '',
        'Gear': '',
        'Steering': 'mecanica',
        'Color': 'azul',
        'Air-Conditioning': 'sim',
        'Optionals': 'v6, completa',
     },

    {
        'Brand': '',
        'Model': 'AGILE LTS',
        'Price': '35.990,00',
        'Motor': '1.4',
        'Year': '14',
        'Odometer': '',
        'Fuel': 'FLEX',
        'Gear': '',
        'Steering': '',
        'Color': 'branca',
        'Air-Conditioning': '',
        'Optionals': 'mecam',
     },

    {
        'Brand': '',
        'Model': 'CORSA CLASSIC',
        'Price': '19.500,00',
        'Motor': '',
        'Year': '08',
        'Odometer': '',
        'Fuel': '',
        'Gear': '',
        'Steering': '',
        'Color': 'preto',
        'Air-Conditioning': 'sim',
        'Optionals': 'spirit, competo',
     },

    {
        'Brand': '',
        'Model': 'CELTA SPIRIT',
        'Price': '',
        'Motor': '',
        'Year': '07',
        'Odometer': '',
        'Fuel': 'flex',
        'Gear': '',
        'Steering': '',
        'Color': 'preto',
        'Air-Conditioning': '',
        'Optionals': '4p',
     },

    {
        'Brand': '',
        'Model': 'PALIO',
        'Price': '20.490,00',
        'Motor': '1.0',
        'Year': '09',
        'Odometer': '110.900',
        'Fuel': 'flex',
        'Gear': '',
        'Steering': '',
        'Color': 'prata',
        'Air-Conditioning': 'sim',
        'Optionals': 'elx, 4portas, completo menos ac, otimo estado',
     },
]

def compute_metrics(templates):
    correctly_extracted_fields = pd.DataFrame()
    total_extracted_fields = pd.DataFrame()
    total_fields = pd.DataFrame()

    for loc, field in zip(range(0, len(templates[0])), templates[0]):
        correctly_extracted_fields.insert(loc=loc, column=field, value={})
        total_extracted_fields.insert(loc=loc, column=field, value={})
        total_fields.insert(loc=loc, column=field, value={})

    for template, correct_answer in zip(templates, correct_answers):
        tef = []
        tf = []
        cef = []
        for field in correct_answer.keys():
            tef.append(int(template[field] != ''))
            tf.append(int(correct_answer[field] != ''))
            cef.append(int(template[field] != '' and template[field] == correct_answer[field]))
        total_extracted_fields.loc[len(total_extracted_fields)] = tef
        total_fields.loc[len(total_extracted_fields)] = tf
        correctly_extracted_fields.loc[len(total_extracted_fields)] = cef

        total_extracted_fields.fillna(0)
        total_fields.fillna(0)
        correctly_extracted_fields.fillna(0)

    precision = correctly_extracted_fields.sum(axis=0)/total_extracted_fields.sum(axis=0)
    recall = correctly_extracted_fields.sum(axis=0)/total_fields.sum(axis=0)

    return precision, recall