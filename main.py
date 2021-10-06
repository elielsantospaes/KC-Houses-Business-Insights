# Projeto de portfólio com da base de dados da House Rocket
import pandas as pd
from pandas._config.config import set_option
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(layout = 'wide')


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
st.title('House Rocket Project')
st.write("The aim of the project is to define the best transactions opportunities within the House Rocket houses protifolium. ")
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    return data

# Data Overview
def show_data(data):
    st.header('Data Overview')
    st.write(data.head())

        # - Agrupar os dados por região (zipcode)
        # - Dentro da cada região, eu vou encontrar a mediana do preço dos imóveis.
        # - Vou sugerir que os imóveis que estão abaixo do preço mediano de dada região se que estejam em boas condições, sejam comprados.
        
        # - Exemplo 
        #     Imóvel Cod | Região  | Preço do Imóvel | Preço da Mediana | Condições | Status
        #        103131  | 3021346 | R$ 451201       | R$ 251354        | 3         | Não Compra
        #        103131  | 3021346 | R$ 151201       | R$ 251354        | 3         | Compra
        #        103131  | 3021346 | R$ 151201       | R$ 251354        | 1         | Não Compra
  

def mediam_price_per_condition(data):
    """
    mostra a mediana dos preços dos imóveis para cada uma das condições.
    """
    st.header('Median price per condition')
    st.write('As there are five different house conditions, it is important to know how the prices behaves deppends the houses conditions.')
    
    price_per_condition = data[['price', 'condition']].groupby('condition').median().reset_index()
    price_per_condition.columns=['condition', 'median_price']
    fig = px.line(price_per_condition, x = 'condition', y = 'median_price')
    st.plotly_chart(fig)

    st.write("As wee can see, the house's price increases with the increse of the house condition. So, the data will be grouped by region (zipcode) and condition.")


def median_price_per_condition_and_zipcode(data):
    data_zip = data[['price', 'condition', 'zipcode']].groupby(['condition', 'zipcode']).median().reset_index()
    data_zip.columns = ['condition', 'zipcode', 'median_price']
    return data_zip
    
def define_status(data, data_zip):
    st.header('Defining new features')
    st.write("Using the grouped data by condidiotn and regions, lets define two new features for the houses:")
    st.write(" - Status, that defines if a house should be bought")
    st.write(" - x% lower, that shows how much the house's price is lower the than median price for a given condition and region.")
    
    data['median_price'] = 0
    data['status'] = 'Buy'
    data['x% lower'] = 0
    
    for i in range(len(data_zip)):
       data.loc[(data['condition'] == data_zip.loc[i ,'condition']) & (data['zipcode'] == data_zip.loc[i, 'zipcode']), 'median_price'] = data_zip.loc[i, 'median_price']
       data.loc[(data['condition'] == data_zip.loc[i ,'condition']) & (data['price'] > data_zip.loc[i, 'median_price']) & (data['zipcode'] == data_zip.loc[i, 'zipcode']), 'status'] = 'Not Buy'
    
    data.loc[(data['price'] < data['median_price']), 'x% lower'] = 100*(1 - data['price']/data['median_price'])
    data['x% lower'] = data['x% lower'].astype(float)
    data.round({'x% lower': 2})
        
    st.header("New features over view.")
    st.write(data[['price','condition', 'median_price', 'status','x% lower']].head(10))
    

def best_opportunities(data):
    st.header('Mapping best opportunities.')
    st.write('Applying a filter in the data, takin only houses with status equal buy, lets see the distribution of opportunities, and how these opportunities are the best.')
    best = []
    for i in range(len(data)):
        if data.loc[i, 'x% lower'] > 0:
            best.append(data.loc[i, 'x% lower'])

    best_df = pd.DataFrame({'x% lower': best})
    

    c1, c2 = st.beta_columns((3,1))
    with c1:
        st.header('Distribution of opportunities')
        st.plotly_chart(px.histogram(best_df, x = 'x% lower', nbins = 60))

    with c2:
        st.header('Statistical description of opportunities')
        st.write(best_df.describe())

    st.write('By the chart and table we can conclude:')
    st.write('')
    st.write(" - There are 10678 houses with price lower than the median prices, in total")
    st.write(" - For these 10k houses, in average, the prices are about 20% lower than the median prices.")
    st.write(" - 25% of the houses are considered best opportunities, with prices equal or lower than 20% of the median prices.")
    st.write(" - 75% of the houses are with discount lower than 20% and can generate a higher number of profitable transaction.")
    st.write('')
    st.write('Based in the above conclusions, the data status will gain a new definition as follow:')
    st.write(" - If the discont is higher than 20% the status will be changed to Buy_SRP, that means Strongly Recommended Purchase")
    
    for i in range(len(data) - 20000): # In the production the 20000 must be deleted.
        if (data.loc[i, 'x% lower'] > 20):
            data.loc[i, 'status'] = 'Buy_SRP'
    
    st.header('Date overview with new definition')

    st.write(data[['price','condition', 'median_price', 'status','x% lower']].head(10))


def set_of_hypothesis(data):
    st.header('Set of Hypothesis')
    st.write('Now, lest check a set of hypothesis and see if there are specifics opportunities. All the hypothesis were formulated based on the house features. Regions caracteristics were not considered.')

# Hipóteses:
    #     É interassante que as hipóteses sejam formuladas após conhecer os atributos dos imóveis.
    #     Toda Hipótese de negócio precisa ter três características:
    #         1 - precisa ser uma afirmação
    #         2 - precisa ser uma comparação entre duas variáveis
    #         3 - precisa ter um valor definido

    #     H1 - Imóveis que possuem vista para água são 20% mais caros, na média.
    st.write('H1 - Houses with waterfront are, in average, 20% more expensive.')
    #     H2 - Imóveis com data de construção menor que 1950, são 50% mais baratos, na média
    st.write('H2 - Houses with year built lower than 1950 are, in average, 50% cheaper.')
    #     H3 - Imóveis com porão são 40% mais caros, na media
    st.write('H3 - Houses with basement are, in average, 40% more expensive.')
    #     H4 - O crescimento do preço YoY é de 10%
    st.write('H4 - The YoY price increase is 10%.')
    #     H5 - Imóveis com mais de um banheiro são 15% mais caros
    st.write('H5 - House that have more than one bathroom are, in average, 15% more expensive.')
    #     H6 - Imóveis próximos da água e sem vista para a água são 20% mais baratos, na média.
    st.write('H6 - houses near to water, but without waterfront, are, in average, 20% cheaper than houses with waterfront')
    #     H7 - Imóveis térreos são 20% mais caros, na média
    st.write('H7 - Houses with only one floor are, in average, 20% more expensive.')
    #     H8 - O preço do imóvel aumenta com o aumenta da área da sala de estar.
    st.write('H8 - Houses price increase with the increase of the area of livingroom.')
    #     H9 - Imóveis muito recentes, construção depois de 2010, são 30% mais caros.
    st.write('H9 - Houses with year built higher than 2010 are, in average, 30% more expensive.')
    #     H10 - Imóveis com maior área externa são mais 10% mais caros.
    st.write('H10 - Houses price increase with the increase of the lot area.')



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
    
    

# Modelagem da dados


# ML(Machine learning)


# Avaliação de performanca dos algoritmos de ML


# Publicação do modelo

if __name__ == '__main__':
    # Extraction
    path = 'dataset/kc_house_data.csv'
    data = get_data(path)
    show_data(data)

    # Transformation
    mediam_price_per_condition(data)

    data_zip = median_price_per_condition_and_zipcode(data)

    define_status(data, data_zip)

    best_opportunities(data)

    set_of_hypothesis(data)