#!/usr/bin/env python
# coding: utf-8

# ## Blockchain
# 
# Março, 2022
# 
# - Carolina Barbosa
# - Cícero Thiago
# - Caio Emmanuel
# - Luís Filipe Loureiro
# - Yuri
# 

# In[1]:


from utils import *


# In[2]:


# Ex1

print('''
01. Uma instituição financeira paga juros simples de 9% a.a. Aplicando hoje R$1.000.000,00, o Montante ao final de cinco anos será de
''')

valor_inicial = 1000000.00 # R$
taxa_juros = 9 # % a.a.
tempo = 5 # anos

retorno, montante = calcula_retorno(valor_inicial, taxa_juros, tempo)

print(f'Aplicando hoje R$1.000.000,00, o Montante ao final de cinco anos será de R${round(montante, 2)}')
print_retorno(valor_inicial, taxa_juros, tempo)
print('\n\n')


# In[3]:


# Ex2

print('''
02. Uma instituição financeira paga taxa de juros simples de 2% a.m. A quantia a ser aplicada para que se obtenham R$ 100.000,00 em 2anos deve ser de
''')

montante = 100000.00 # R$
taxa_juros = 2 # % a.m,.
tempo = 24 # meses = 2 anos

valor_inicial = calcula_inverso_retorno(montante, taxa_juros, tempo)

print(f'A quantia a ser aplicada para que se obtenham R$100.000,00 em 2 anos deve ser de R${round(valor_inicial, 2)}')
print('\n\n')


# In[4]:


# Ex3

print('''
03. Um investidor aplica a quantia de R$ 50.000,00 por 4 dias, no regime de juros simples a uma taxa de 3% a.m. Os rendimentos auferidos no período serão de
''')

valor_inicial = 50000.00 # R$
taxa_juros_inicial = 3 # % a.m.
tempo = 4 # dias

taxa_juros_final = converter_juros(taxa_juros_inicial, 29, interno=False)

retorno, montante = calcula_retorno(valor_inicial, taxa_juros_final, tempo)

print(f'Os rendimentos auferidos no período serão de R${round(retorno, 2)}')
print('\n\n')


# In[5]:


# Ex4

print('''
04. Uma pessoa toma um empréstimo de RS 25.000,00, por 5 meses, com pagamento no final. O custo da operação é de 10% a.m. O montante do empréstimo no final.(j simples e j compostos) será de
''')

valor_inicial = 25000.00 # R$
taxa_juros = 10 # % a.m.
tempo = 5 # meses

retorno_simples, montante_simples = calcula_retorno(valor_inicial, taxa_juros, tempo)
retorno_composto, montante_composto = calcula_retorno(valor_inicial, taxa_juros, tempo, regime='composto')

print(f'O montante do empréstimo no final(simples e compostos) será de R${round(montante_simples, 2)} e R${round(montante_composto, 2)}, respectivamente')
print('Regime simples:')
print_retorno(valor_inicial, taxa_juros, tempo)
print('Regime composto:')
print_retorno(valor_inicial, taxa_juros, tempo, regime='composto')
print('\n\n')


# In[6]:


# Ex5

print('''
05. Um capital inicial de R$ 60.000,00 é investido por 81 dias. No regime de juros compostos, às taxa de 1.2% a.m. O valor de resgate bruto será de
''')

valor_inicial = 60000.00 # R$
taxa_juros_inicial = 1.2 # % a.m.
tempo = 81 # dias

taxa_juros_final = converter_juros(taxa_juros_inicial, 30, interno=False)

retorno, montante = calcula_retorno(valor_inicial, taxa_juros_final, tempo, regime='composto')

print(f'O valor de resgate bruto será de R${round(montante, 2)}')
print('\n\n')


# In[7]:


# Ex6

print('''
06. Uma aplicação de RS 40.000,00 gera um montante de R$ 86.730,00, em 95 dias, regime de juros compostos.A taxa efetiva mensal da operação é de
''')

valor_inicial = 40000.00 # R$
montante = 86730.00 # R$
tempo = 95 # dias

taxa_juros_diaria = calcula_taxa_juros(valor_inicial, montante, tempo, regime='composto')
taxa_juros_mensal = converter_juros(taxa_juros_diaria, 30)

print(f'A taxa efetiva mensal da operação é de {round(taxa_juros_mensal, 2)}% a.m.')
print('\n\n')


# In[8]:


# Ex7

print('''
07. A taxa trimestral proporcional à taxa de 21% a.a. é
''')

taxa_juros_anual = 21 # % a.a.
taxa_juros_trimestral = converter_juros(taxa_juros_anual, 4, regime='simples', interno=False)

print(f'A taxa trimestral proporcional à taxa de 21% a.a. é {round(taxa_juros_trimestral, 2)}% a.t.')
print('\n\n')


# In[9]:


# Ex8

print('''
08. A taxa mensal proporcional à taxa de 36% a.a. é 
''')

taxa_juros_anual = 36 # % a.a.
taxa_juros_mensal = converter_juros(taxa_juros_anual, 12, regime='simples', interno=False)

print(f'A taxa mensal proporcional à taxa de 36% a.a. é {round(taxa_juros_mensal, 2)}% a.m.')
print('\n\n')


# In[10]:


# Ex9

print('''
09. A taxa diária equivalente “a taxa de 4% a.m”. é
''')

taxa_juros_mensal = 4 # % a.m.
taxa_juros_diaria = converter_juros(taxa_juros_mensal, 30, interno=False)

print(f'A taxa diária equivalente à taxa de 4% a.m. é {round(taxa_juros_diaria, 4)}% a.d.')
print('\n\n')


# In[11]:


# Ex10

print('''
10. A  taxa por dia útil equivalente à taxa de 1.5% a.m. (21 dias úteis) é
''')

taxa_juros_mensal = 1.5 # % a.m.
taxa_juros_diaria = converter_juros(taxa_juros_mensal, 21, interno=False)

print(f'A taxa por dia útil equivalente à taxa de 1.5% a.m. (21 dias úteis) é {round(taxa_juros_diaria, 5)}% a.d.')
print('\n\n')


# In[12]:


# Ex11

print('''
11. Uma pessoa investe R$ 50.000,00 no mercado financeiro por três meses, obtendo as seguintes rentabilidades efetivas mensais: primeiro mês  5%, segundo mês 8% e no terceiro  mês  10%,  o montante de resgate será de
''')

valor_inicial = 50000.00 # R$
taxas_tempo_map = { # taxa (% a.m.) : tempo de investimento sobre a taxa (mês)
    5: 1,
    8: 1,
    10: 1
}

montante = valor_inicial
for taxa, tempo in taxas_tempo_map.items():
    retorno, montante = calcula_retorno(montante, taxa, tempo, regime='composto')

print(f'O montante de resgate será de R${round(montante, 2)}')
print('\n\n')


# In[13]:


# Ex12

print('''
12. Uma operação interbancária com principal de RS1. 000.000,00 é realizada por 5 dias úteis. As taxas over ano da operação são as seguintes: 15,25% a.a., 15,30% a.a., 15,40% a.a., 15,45% a.a., 15,50% a.a. O montante da operação será de
''')

valor_inicial = 1000000.00 # R$
taxas_tempo_map = { # taxa (% a.a.) : tempo de investimento sobre a taxa (dia)
    15.25: 1,
    15.30: 1,
    15.40: 1,
    15.45: 1,
    15.50: 1
}

montante = valor_inicial
for taxa, tempo in taxas_tempo_map.items():
    taxa_juros_diaria = converter_juros(taxa, 252, interno=False)
    retorno, montante = calcula_retorno(montante, taxa_juros_diaria, tempo, regime='composto')

print(f'O montante de resgate será de R${round(montante, 2)}')
print('\n\n')


# In[14]:


# Ex13, Ex14, Ex15

print('''
QUESTÕES N.º 13, N.º 14 e N.º 15.

Um indivíduo aplicou no mercado financeiro no início de janeiro de 200X a quantia de R$ 500.000,00 e resgatou, no final de abril do mesmo ano, o valor de R$ 1.200.000,00.
As taxas de inflação mensal do período. Foram: JAN 16,51%, FEV 17,96%, MAR 16,01%, ABR 19,28%.
''')

valor_inicial = 500000.00 # R$
montante = 1200000.00 # R$
inflacao_tempo_map = { # inflação (% a.m.) : tempo de investimento sobre a taxa (mês)
    16.51: 1,
    17.96: 1,
    16.01: 1,
    19.28: 1
}

print('\n')


# In[15]:


# Ex13

print('''
13. A taxa da operação no período  foi de:
''')

performance = ((montante / valor_inicial) - 1) * 100

print(f'A taxa da operação no período foi de {round(performance, 2)}%')
print('\n\n')


# In[16]:


# Ex14

print('''
14. A taxa de inflação acumulada foi de:
''')

inflacao_acumulada = 1
for taxa, tempo in inflacao_tempo_map.items():
    _, inflacao_acumulada = calcula_retorno(inflacao_acumulada, taxa, tempo, regime='composto')
    
inflacao_acumulada -= 1
inflacao_acumulada *= 100

print(f'A taxa de inflação acumulada foi de {round(inflacao_acumulada, 2)}%')
print('\n\n')


# In[17]:


# Ex15

print('''
15. A taxa real de retorno (período) foi de:
''')

taxa_real = calcula_taxa_real(performance, inflacao_acumulada)

print(f'A taxa real de retorno (período) foi de {round(taxa_real, 2)}%')
print('\n\n')


# In[18]:


# Ex16, Ex17

print('''
QUESTÕES N.º 16 e N.º 17.

Apresenta-se a seguinte operação para nossa avaliação: Aplicar R$ 1.000.000, por 42 dias com duas alternativas.
''')

valor_inicial = 1000000.00 # R$
tempo = 42 # dias

print('\n')


# In[19]:


# Ex16

print('''
16. O montante da operação, considerando-se juros de 14% a.a. (juros simples, base 365) será de
''')

taxa_juros_anual = 14 # % a.a.
taxa_juros_diaria = converter_juros(taxa_juros_anual, 365, regime='simples', interno=False)

retorno, montante = calcula_retorno(valor_inicial, taxa_juros_diaria, tempo)

print(f'O montante da operação será de R${round(montante, 2)}')
print('\n\n')


# In[20]:


# Ex17

print('''
17. O montante da operação, considerando-se juros de 16% a.a., (juros compostos, base 360) será de
''')

taxa_juros_anual = 16 # % a.a.
taxa_juros_diaria = converter_juros(taxa_juros_anual, 360, interno=False)

retorno, montante = calcula_retorno(valor_inicial, taxa_juros_diaria, tempo, regime='composto')

print(f'O montante da operação será de R${round(montante, 2)}')
print('\n\n')


# In[21]:


# Ex18, Ex19, Ex20

print('''
QUESTÕES N.º 18, N.º 19 e N.º 20.

Uma duplicata de R$ 18.000,00 foi descontada num banco dois meses antes do vencimento, a uma taxa de desconto de 2,5% a.m.
''')

valor_duplicata = 18000 # R$
tempo_passado = 2 # meses
taxa_desconto = 2.5 # % a.m.

print('\n')


# In[22]:


# Ex18

print('''
18. O desconto foi de
''')

desconto = valor_duplicata * (taxa_desconto * tempo_passado) / 100

print(f'O desconto foi de R${round(desconto, 2)}')
print('\n\n')


# In[23]:


# Ex19

print('''
19. O valor descontado dessa operação foi de
''')

valor_operacao = valor_duplicata - desconto

print(f'O valor descontado dessa operação foi de R${round(valor_operacao, 2)}')
print('\n\n')


# In[24]:


# Ex20

print('''
20. A  taxa efetiva da operação foi de
''')

taxa_efetiva = desconto / valor_operacao * 100

print(f'A taxa efetiva da operação foi de {round(taxa_efetiva, 2)}%')
print('\n\n')


# EOF
