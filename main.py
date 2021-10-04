# Projeto de portfólio com da base de dados da House Rocket
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# 1 - Questões de negócio.
    # 1 - Quais os imóveis que a House Rocket deveria comprar e por qual preço?
    # 2 - Uma vez comprado, qual o melhor momento para vendê-los e por qual preço?


# 2 - Entendimento do negócio
    # 1 - Produto final (Email, planilha, Modelo de ML...)
    #     2 Relatórios:
    #         - Relatório com as sugestões de compra de imóveis por um valor recomendado.
    #         - Relatório com as sugestões de venda de uma imóvel por um valor recomendado.

    # 2 - Ferramentas 
    #     Python
    #     VS Code
    #     Jupyter Notebook
        

# 3 - Processo (Quais os passos necessários para alcançar meu objetivo)

    # 1 - Quais são os imóveis que a House Rocket deveria comprar?
        # - Coleta de dados (no Kaggle)
def get_data(path):
    data = pd.read_csv(path)
    return data

# Data Overview
def show_data(data):
    st.title('Data overview')
    st.write(data.head())

        # - Agrupar os dados por região (zipcode)
        # - Dentro da cada região, eu vou encontrar a mediana do preço dos imóveis.
        # - Vou sugerir que os imóveis que estão abaixo do preço mediano de dada região se que estjam em voas condições, sejam comprados.
        
        # - Exemplo 
        #     Imóvel Cod | Região  | Preço do Imóvel | Preço da Mediana | Condições | Status
        #        103131  | 3021346 | R$ 451201       | R$ 251354        | 3         | Não Compra
        #        103131  | 3021346 | R$ 151201       | R$ 251354        | 3         | Compra
        #        103131  | 3021346 | R$ 151201       | R$ 251354        | 1         | Não Compra

    # 2 - Uma vez comprado, qual o melhor momento para vender e por qual preço?
        # - Plano 01:
        #     - Agrupar os dados por região (zipcode) e sazonalidade (Summer , winter)
        #     - Dentro de cada região e sazonalidade, eu calcular a mediana de preço.
        #     - Condições de venda:
        #         1 - Se o preço da compra for maior que a mediana da região + sazonalidade
        #             O preço da venda será igual ao preço da compra + 10%
        #         2 - Se o preço da compra for menor que a mediana da região + sazonalidade
        #             O preço da venda será igual ao preço da compra + 30%

        # - Exemplo 
        #     Imóvel Cod | Região  | Temporada  | Preço da compra | Preço da Mediana | Preço da venda    | Lucro 
        #        103131  | 3021346 | Summer     |  R$ 451201      | R$ 251354        |  R$ 451201 + 10%  | ?
        #        103131  | 3021346 | Winter     |  R$ 151201      | R$ 251354        |  R$ 151201 + 30%  | ?
        #        103131  | 3021346 | Winter     |  R$ 151201      | R$ 251354        |  R$ 151201 + 30%  | ?


# Limpeza de dados
    # - Eliminar outliers
    # - Gerar colunas necessárias
    # - Formatar colunas (tipo de dados)

# EDA (Exploratory Data Analysis)
    # Objetivos:
    #     1 - Descobrir insights para o time de negócio
    #     2 - Explorar os dados para identificar o impacto das atributos nos algoritmos de ML
    
    # O que são insights?
    #     - Insights são descobertas, atraves das dados, que são inesperadas para o time de negócio.
    #     - Insights precisa ser acionavel, caso contrário será apenas uma curiosidade

    #     Exemplos:
    #         - Durante o período de Natal vende-se mais casas do que na páscoa (Descoberta)
    #         - Casas com porão são maiores que casas sem porão (Não acionável)
    
    # Hipóteses:
    #     É interassante que as hipóteses sejam formuladas após conhecer os atributos dos imóveis.
    #     Toda Hipótese de negócio precisa ter três características:
    #         1 - precisa ser uma afirmação
    #         2 - precisa ser uma comparação entre duas variáveis
    #         3 - precisa ter um valor definido

    #     H1 - Imóveis que possuem vista para água são 20% mais caros, na média.
    #     H2 - Imóveis com data de construção menor que 1950, são 50% mais baratos, na média
    #     H3 - Imóveis com porão são 40% mais caros, na media
    #     H4 - O crescimento do preço YoY é de 10%
    #     H5 - Imóveis com mais de um banheiro são 15% mais caros
    #     H6 - Imóveis próximos da água e sem vista para a água são 20% mais baratos, na média.
    #     H7 - Imóveis térreos são 20% mais caros, na média
    #     H8 - O preço do imóvel aumenta com o aumenta da área de estar.
    #     H9 - Imóveis muito recentes, construção depois de 2010, são 30% mais caros.
    #     H10 - Imóveis com maior área externa são mais 10% mais caros.

# Modelagem da dados


# ML(Machine learning)


# Avaliação de performanca dos algoritmos de ML


# Publicação do modelo

if __name__ == '__main__':
    path = 'dataset/kc_house_data.csv'
    show_data(get_data(path))


