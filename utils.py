def calcula_retorno(
        valor_inicial: float, 
        taxa_juros: float, 
        tempo: int, 
        regime: str = 'simples'
    ):
    
    taxa_juros /= 100

    if(regime == 'simples'):
        montante = valor_inicial * (1 + taxa_juros * tempo)
    if(regime == 'composto'):
        montante = valor_inicial * (1 + taxa_juros)**tempo

    retorno = montante - valor_inicial

    return retorno, montante


def calcula_inverso_retorno(
        montante_ou_retorno: float,
        taxa_juros: float,
        tempo: int,
        regime: str = 'simples',
        retorno: bool = False
    ):
    
    taxa_juros /= 100

    if(regime == 'simples'):
        valor_inicial = montante_ou_retorno / (taxa_juros * tempo) if retorno else montante_ou_retorno / (1 + taxa_juros * tempo)
    if(regime == 'composto'):
        valor_inicial = montante_ou_retorno / ((1 + taxa_juros)**tempo - 1) if retorno else montante_ou_retorno / (1 + taxa_juros)**tempo

    return valor_inicial


def print_retorno(
        valor_inicial: float,
        taxa_juros: float,
        tempo: int,
        regime: str = 'simples'
    ):

    table = [['Tempo', 'Valor investido'      , 'Taxa de Juros (%)' , 'Retorno', 'Montante'], 
             [0      , round(valor_inicial, 2), round(taxa_juros, 2),     0    , round(valor_inicial, 2)]]

    for i in range(1,tempo+1):
        retorno, montante = calcula_retorno(valor_inicial, taxa_juros, i, regime)
        table.append([i, 0, round(taxa_juros, 2), round(retorno, 2), round(montante, 2)])

    for row in table:
        print('| {:^5} | {:>15} | {:^17} | {:>11} | {:>11} |'.format(*row))


def converter_juros(
        taxa_juros_inicial: float,
        numero_periodos_uteis: int,
        regime: str = 'composto',
        interno: bool = True
    ):
    
    taxa_juros_final, _ = calcula_retorno(1, taxa_juros_inicial, numero_periodos_uteis, regime)
    
    if(regime == 'simples'):
        taxa_juros_final = taxa_juros_final if interno else taxa_juros_final / numero_periodos_uteis**2
    if(regime == 'composto'):
        taxa_juros_final = taxa_juros_final if interno else (taxa_juros_final + 1)**(1 / numero_periodos_uteis**2) - 1
        
    taxa_juros_final *= 100
    
    return taxa_juros_final


def calcula_taxa_juros(
        valor_inicial: float,
        montante_ou_retorno: float,
        tempo: int,
        regime: str = 'simples',
        retorno: bool = False
    ):
    
    if(regime == 'simples'):
        taxa_juros = (montante_ou_retorno / valor_inicial) / tempo if retorno else ((montante_ou_retorno - valor_inicial) / valor_inicial) / tempo
    if(regime == 'composto'):
        taxa_juros = ((montante_ou_retorno + valor_inicial) / valor_inicial)**(1/tempo) - 1 if retorno else (montante_ou_retorno / valor_inicial)**(1/tempo) - 1
        
    taxa_juros *= 100
    
    return taxa_juros