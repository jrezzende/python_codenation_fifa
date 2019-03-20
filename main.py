import csv
from itertools import islice
from collections import Counter

# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():
    with open('data.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        return len(set([row['nationality'] for row in reader]))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    with open('data.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        return len(set([row['club'] for row in reader]))

# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    with open('data.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        return [row['full_name'] for row in islice(reader, 20)]
    
# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    with open('data.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        wages = [ (row['full_name'], float(row['eur_wage'])) for row in reader ]
        wages = sorted(wages, reverse=True, key=lambda row: row[1])[:10]    
        return [ tup[0] for tup in wages ]

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    with open('data.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        ages = [ (row['full_name'], row['age']) for row in reader ]
        ages = sorted(ages, reverse=True, key=lambda row: row[1])[:10]
        return [ tup[0] for tup in ages]

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    with open('data.csv', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        
        total_ages = [ row['age'] for row in reader ]
        return { int(k): int(v) for k, v in Counter(total_ages).items() }
