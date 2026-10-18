"""
Dicionário de Variáveis e Metadados da PNS 2019
Definições canônicas para o estudo epidemiológico de Doenças Cardiovasculares.
"""

# Mapeamento do nome no CSV original da PNS 2019 para o nome canônico do projeto
CSV_TO_CANONICAL = {
    'P006': 'P006',
    'P00620': 'P00620',
    'P00901': 'P00901',
    'P01101': 'P01101',
    'P013': 'P01301',    # No CSV bruto da PNS 2019 o código é P013
    'P015': 'P01501',    # No CSV bruto da PNS 2019 o código é P015
    'P018': 'P01801',    # No CSV bruto da PNS 2019 o código é P018
    'P02001': 'P02001',
    'P023': 'P023',
    'P02401': 'P02401',
    'P02501': 'P02501',
    'P02601': 'P02601',
    'P02602': 'P02602',
    'P00104': 'P00104',
    'P00404': 'P00404',
    'W00101': 'W00101',
    'W00201': 'W00201',
    'P050': 'P050',
    'P051': 'P05101',    # No CSV bruto da PNS 2019 o código é P051
    'P052': 'P052',
    'P053': 'P053',
    'P05401': 'P05401',
    'P05402': 'P05402',
    'P058': 'P058',
    'P05901': 'P05901',
    'P06701': 'P06701',
    'P068': 'P068',
    'M01001': 'M01001',
    'P027': 'P027',
    'P02801': 'P02801',
    'P029': 'P029',
    'P03201': 'P03201',
    'P034': 'P034',
    'P035': 'P035',
    'P036': 'P036',
    'P03701': 'P03701',
    'P039': 'P03901',    # No CSV bruto da PNS 2019 o código é P039
    'P040': 'P040',
    'P042': 'P042',
    'P04501': 'P04501',
    'P04502': 'P04502',
    'N001': 'N001',
    'N010': 'N010',
    'N016': 'N016',
    'Q06306': 'Q06306'
}

CANONICAL_TO_CSV = {v: k for k, v in CSV_TO_CANONICAL.items()}

# Lista ordenada das 44 variáveis preditoras
PREDICTOR_VARS = [
    'P006', 'P00620', 'P00901', 'P01101', 'P01301', 'P01501', 'P01801', 'P02001', 'P023', 'P02401', 'P02501', 'P02601', 'P02602',
    'P00104', 'P00404', 'W00101', 'W00201',
    'P050', 'P05101', 'P052', 'P053', 'P05401', 'P05402', 'P058', 'P05901', 'P06701', 'P068', 'M01001',
    'P027', 'P02801', 'P029', 'P03201',
    'P034', 'P035', 'P036', 'P03701', 'P03901', 'P040', 'P042', 'P04501', 'P04502',
    'N001', 'N010', 'N016'
]

TARGET_VAR = 'Q06306'
ALL_VARS = PREDICTOR_VARS + [TARGET_VAR]

# Metadados Descritivos (Domínio, Nome Descritivo, Tipo de Dado)
METADATA = {
    # Alimentação
    'P006': {'dominio': 'Alimentação', 'label': 'Dias/sem consome feijão', 'tipo': 'discreto'},
    'P00620': {'dominio': 'Alimentação', 'label': 'Tipo de feijão habitual', 'tipo': 'categorico'},
    'P00901': {'dominio': 'Alimentação', 'label': 'Dias/sem come alface/tomate/folhas', 'tipo': 'discreto'},
    'P01101': {'dominio': 'Alimentação', 'label': 'Dias/sem come legumes cozidos', 'tipo': 'discreto'},
    'P01301': {'dominio': 'Alimentação', 'label': 'Dias/sem come salada crua', 'tipo': 'discreto'},
    'P01501': {'dominio': 'Alimentação', 'label': 'Dias/sem legumes na comida', 'tipo': 'discreto'},
    'P01801': {'dominio': 'Alimentação', 'label': 'Dias/sem carne vermelha/frango', 'tipo': 'discreto'},
    'P02001': {'dominio': 'Alimentação', 'label': 'Dias/sem come peixe', 'tipo': 'discreto'},
    'P023': {'dominio': 'Alimentação', 'label': 'Dias/sem bebe suco natural', 'tipo': 'discreto'},
    'P02401': {'dominio': 'Alimentação', 'label': 'Adição de açúcar/adoçante no suco', 'tipo': 'categorico'},
    'P02501': {'dominio': 'Alimentação', 'label': 'Dias/sem bebe refrigerante/suco art.', 'tipo': 'discreto'},
    'P02601': {'dominio': 'Alimentação', 'label': 'Tipo de refrigerante habitual', 'tipo': 'categorico'},
    'P02602': {'dominio': 'Alimentação', 'label': 'Dias/sem come doces/guloseimas', 'tipo': 'discreto'},
    
    # Antropometria
    'P00104': {'dominio': 'Antropometria', 'label': 'Peso corporal informado (kg)', 'tipo': 'continuo'},
    'P00404': {'dominio': 'Antropometria', 'label': 'Altura informada (cm)', 'tipo': 'continuo'},
    'W00101': {'dominio': 'Antropometria', 'label': 'Perímetro da cintura (cm)', 'tipo': 'continuo'},
    'W00201': {'dominio': 'Antropometria', 'label': 'Perímetro do quadril (cm)', 'tipo': 'continuo'},
    
    # Tabagismo
    'P050': {'dominio': 'Tabagismo', 'label': 'Frequência atual uso de tabaco', 'tipo': 'categorico'},
    'P05101': {'dominio': 'Tabagismo', 'label': 'Fumo diário no passado', 'tipo': 'categorico'},
    'P052': {'dominio': 'Tabagismo', 'label': 'Cigarros/dia industrializados', 'tipo': 'categorico'},
    'P053': {'dominio': 'Tabagismo', 'label': 'Idade início fumo diário (anos)', 'tipo': 'continuo'},
    'P05401': {'dominio': 'Tabagismo', 'label': 'Uso cigarro palha/rolo', 'tipo': 'categorico'},
    'P05402': {'dominio': 'Tabagismo', 'label': 'Qtd cigarros palha/rolo/dia', 'tipo': 'continuo'},
    'P058': {'dominio': 'Tabagismo', 'label': 'Tentativa cessação tabágica 12m', 'tipo': 'categorico'},
    'P05901': {'dominio': 'Tabagismo', 'label': 'Tempo que parou de fumar (anos)', 'tipo': 'continuo'},
    'P06701': {'dominio': 'Tabagismo', 'label': 'Tabagismo passivo domiciliar', 'tipo': 'categorico'},
    'P068': {'dominio': 'Tabagismo', 'label': 'Tabagismo passivo no trabalho', 'tipo': 'categorico'},
    'M01001': {'dominio': 'Tabagismo', 'label': 'Exposição ocupacional a fumaça', 'tipo': 'categorico'},
    
    # Álcool
    'P027': {'dominio': 'Consumo de Álcool', 'label': 'Frequência consumo de álcool', 'tipo': 'categorico'},
    'P02801': {'dominio': 'Consumo de Álcool', 'label': 'Dias/sem consome bebida alcoólica', 'tipo': 'discreto'},
    'P029': {'dominio': 'Consumo de Álcool', 'label': 'Doses consumidas no dia típico', 'tipo': 'continuo'},
    'P03201': {'dominio': 'Consumo de Álcool', 'label': 'Consumo episódico pesado (binge)', 'tipo': 'categorico'},
    
    # Atividade Física
    'P034': {'dominio': 'Atividade Física', 'label': 'Esforço físico pesado no trabalho', 'tipo': 'categorico'},
    'P035': {'dominio': 'Atividade Física', 'label': 'Dias/sem esforço pesado trabalho', 'tipo': 'discreto'},
    'P036': {'dominio': 'Atividade Física', 'label': 'Deslocamento ativo trab/estudo', 'tipo': 'categorico'},
    'P03701': {'dominio': 'Atividade Física', 'label': 'Tempo deslocamento ativo (horas)', 'tipo': 'discreto'},
    'P03901': {'dominio': 'Atividade Física', 'label': 'Prática exercícios últimos 3m', 'tipo': 'categorico'},
    'P040': {'dominio': 'Atividade Física', 'label': 'Dias/sem prática de exercícios', 'tipo': 'categorico'},
    'P042': {'dominio': 'Atividade Física', 'label': 'Dias/sem caminhada/bike lazer', 'tipo': 'discreto'},
    'P04501': {'dominio': 'Atividade Física', 'label': 'Tempo diário assistindo TV', 'tipo': 'categorico'},
    'P04502': {'dominio': 'Atividade Física', 'label': 'Tempo diário computador/telas', 'tipo': 'categorico'},
    
    # Saúde Mental
    'N001': {'dominio': 'Saúde Mental', 'label': 'Autoavaliação estado de saúde', 'tipo': 'categorico'},
    'N010': {'dominio': 'Saúde Mental', 'label': 'Distúrbios/problemas de sono 2sem', 'tipo': 'categorico'},
    'N016': {'dominio': 'Saúde Mental', 'label': 'Sentimento tristeza/desânimo 2sem', 'tipo': 'categorico'},
    
    # Variável Alvo
    'Q06306': {'dominio': 'Target Clínico', 'label': 'Diagnóstico Doença do Coração', 'tipo': 'target'}
}

# Limites fisiológicos e biológicos para análise de sanidade (Etapa 2)
BIOLOGICAL_LIMITS = {
    'P00104': {'min': 30.0, 'max': 220.0, 'nome': 'Peso (kg)'},
    'P00404': {'min': 120.0, 'max': 220.0, 'nome': 'Altura (cm)'},
    'W00101': {'min': 40.0, 'max': 180.0, 'nome': 'Cintura (cm)'},
    'W00201': {'min': 50.0, 'max': 220.0, 'nome': 'Quadril (cm)'},
    'P053':   {'min': 5.0,  'max': 80.0,  'nome': 'Idade Início Fumo (anos)'},
    'P05402': {'min': 0.0,  'max': 100.0, 'nome': 'Qtd Outros Cigarros/dia'},
    'P05901': {'min': 0.0,  'max': 80.0,  'nome': 'Tempo Parou Fumar (anos)'},
    'P029':   {'min': 0.0,  'max': 50.0,  'nome': 'Doses Álcool/dia'},
    'P03701': {'min': 0.0,  'max': 720.0, 'nome': 'Tempo Deslocamento Ativo (min)'}
}
