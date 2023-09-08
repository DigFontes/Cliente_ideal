#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa do varejo e tem milhares de clientes diferentes.
# 
# Com o objetivo de aumentar o faturamento e o lucro da sua empresa, a diretoria quer conseguir identificar quem é o cliente ideal para seus produtos, baseado no histórico de compras dos clientes.
# 
# Para isso, ela fez um trabalho de classificar os clientes com uma nota de 1 a 100. Só que agora, sobrou para você conseguir, a partir dessa nota, descobrir qual o perfil de cliente ideal da empresa.
# 
# Qual a profissão? Qual a idade? Qual a faixa de renda? E todas as informações que você puder analisar para dizer qual o cliente ideal da empresa.
# 
# Base de Dados: https://drive.google.com/drive/folders/1XvNLDKVH7TUS8HdH4r0TkXL__MFpoc3e?usp=share_link

# In[51]:


# passo a passo 

# * Passo 1: Importar a base de dados:
import pandas as pd


# In[52]:


# * Passo 2: Visializar a base de dados: na base de dados identifiquei uma coluna com valores nulos,
            #usei o dropna para retirar da base e sort_values para ordenaros a base pela nota da maior para menor
# * Passo 3: Tratamento dos dados: conveti a coluna salário anual de object para numérico
tabela = pd.read_csv(
    r'C:\Users\Virtual Office\Python\Módulo 50 - Python aplicação no mercado de trabalho\Aula 2\Aula 2\clientes.csv',
    sep = ';',
    encoding = 'latin1'
)
tabela = tabela.drop('Unnamed: 8', axis = 1
                      ).sort_values(by = ['Nota (1-100)'], ascending=False
                                   )

tabela = tabela.dropna()

tabela['Salário Anual (R$)'] = pd.to_numeric(
    tabela['Salário Anual (R$)'], 
    errors = 'coerce'
)

    # - Entender as informações disponíveis na base de dados
display(tabela)
tabela.info()
display(tabela.describe())
    # - Identificar os poluidores dos dados


# In[62]:


# * Passo 4: Análise Inicial -> Entender as notas dos clientes
import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x =coluna , y ='Nota (1-100)', histfunc = 'avg', text_auto = True, )

    grafico.show()
# * Passo 5: Análise Completa -> Entender como cada característica do cliente impacta na nota


# In[ ]:


# Perfil ideal de cliente
    # - Consumidores acima de 10 anos
    # - Profissional do entreterimento e artistas 
    # - Famílias com até 7 membros
# Observações:  
        # * Obs.: Não há uma discrepância de nota entre os consumidores que fizeram a adesão no preço normal
            # ** com consumidores com aderiram no preço promocional;
        # * Obs.: Salário anual também não mostram qualquer discrepância;
        # * Obs.: Profissional advogados e da construção são detratores
        # * Obs.: Experiência de trabalho apesar da discrepância, não é possível inferir á uma raciocício lógico, já que 
            # ** já que profissionais com 17 anos de experiência tem uma média próxima da média geral.

