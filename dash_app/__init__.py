import yfinance as yf
import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dash_table

import plotly.io as poi

poi.renderers.default = 'browser'

# global_Styles
CHARTS_TEMPLATE = go.layout.Template(
    layout=dict(
        font=dict(family='Century Gothic')
    )
)

tickers = [
    'CL=F',
    'GC=F'
]  # CL - данные по нефти, #GC данные по золоту \\ все это к баксу
####Раздел где формируются датасет и на основе него ричуется график для OIL_GOLD
new_column = []
for memos in tickers:
    ticker = yf.Ticker(memos)
    dxx = ticker.history(period='max')['Close']
    dxx.name = memos
    new_column += [dxx]
df_clgc = pd.concat(new_column, axis=1)
df_clgc['CL/GC'] = df_clgc['CL=F'] / df_clgc['GC=F']
column_gc = df_clgc['CL/GC']
# print(column)
fig_clgc = px.line(df_clgc, y="CL/GC", title='Oil / GoldOZ')  # формирование графика
fig_clgc.update_layout(template=CHARTS_TEMPLATE)
# раздел, где формируется дата и график на нефть к баксу
data_closedprice_oil_usd = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd = px.line(data_closedprice_oil_usd, y="Close", title='Oil / USD')
fig_oil_usd.update_layout(template=CHARTS_TEMPLATE)
####Раздел где формируются датасет и на основе него ричуется график для GAS_GOLD
empresas = [
    'NG=F',
    'GC=F'
]  # NG - данные по натуральному газу, #GC данные по золоту \\ все это к баксу

recolector = []
for nemo in empresas:
    ticker = yf.Ticker(nemo)
    dx = ticker.history(period='max')['Close']
    dx.name = nemo
    recolector += [dx]
df_clgc = pd.concat(recolector, axis=1)
df_clgc['NG/GC'] = df_clgc['NG=F'] / df_clgc['GC=F']

fig = px.line(df_clgc, y="NG/GC", title='Natural Gas / GoldOZ')  # формирование графика
fig.update_layout(template=CHARTS_TEMPLATE)

####Раздел где формируются датасет и на основе него ричуется график для GAS_USD

gas_usd = 'NG=F'
data_closedprice_gas_usd = yf.Ticker(gas_usd).history(period='max')['Close']
# print(data_closedprice_gas_usd)
fig_gas_usd = px.line(data_closedprice_gas_usd, y="Close", title='Natural Gas / USD')
fig_gas_usd.update_layout(template=CHARTS_TEMPLATE)
#####Раздел где формируется дата и график для рсходов в USD


food = pd.read_csv("food1.csv")

# Create a Plotly chart
food_plotly = px.line(food, x="DATE", y="Expenditures", title='Expenditures/USD')
food_plotly.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для рсходов в GOLD

food_gold = pd.read_csv("food1.csv")
food_gold_plotly_1 = px.line(food_gold, x="DATE", y="Ratio_gd", title='Expenditures/GoldOZ')
food_gold_plotly_1.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для нефти бакса

data_closedprice_oil_usd = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd = px.line(data_closedprice_oil_usd, y="Close", title='Oil / USD')
fig_oil_usd.update_layout(template=CHARTS_TEMPLATE)

####Раздел, где формируется дата и графики относительно стоимости биткоина
tickers_for_btc = [
    'CL=F',
    'BTC=F'
]  # CL - данные по нефти, #GC данные по bitcoin \\ все это к баксу

new_column_btc = []
for memos_btc in tickers_for_btc:
    ticker = yf.Ticker(memos_btc)
    dxx_btc = ticker.history(period='max')['Close']
    dxx_btc.name = memos_btc
    new_column_btc += [dxx_btc]
df_cl_btc = pd.concat(new_column_btc, axis=1)
df_cl_btc['CL/BTC'] = df_cl_btc['CL=F'] / df_cl_btc['BTC=F']
column_btc = df_cl_btc['CL/BTC']

fig_cl_btc = px.line(df_cl_btc, y="CL/BTC", title='Oil/BTC')  # формирование графика
fig_cl_btc.update_layout(template=CHARTS_TEMPLATE)

# раздел, где формируется дата и график на нефть к баксу
data_closedprice_oil_usd_btc = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd_btc = px.line(data_closedprice_oil_usd_btc, y="Close", title='Oil / USD')
fig_oil_usd_btc.update_layout(template=CHARTS_TEMPLATE)

####Раздел где формируются датасет и на основе него ричуется график для GAS_GOLD
empresas_btc = [
    'NG=F',
    'BTC=F'
]  # NG - данные по натуральному газу, #BTC-USD данные по bitcoin \\ все это к баксу

recolector_btc = []
for nemo_btc in empresas_btc:
    ticker = yf.Ticker(nemo_btc)
    dx = ticker.history(period='max')['Close']
    dx.name = nemo_btc
    recolector_btc += [dx]
df_cl_btc = pd.concat(recolector_btc, axis=1)
df_cl_btc['NG/BTC'] = df_cl_btc['NG=F'] / df_cl_btc['BTC=F']

fig_btc = px.line(df_cl_btc, y="NG/BTC", title='Natural Gas / BTC')  # формирование графика
fig_btc.update_layout(template=CHARTS_TEMPLATE)

####Раздел где формируются датасет и на основе него ричуется график для GAS_USD

gas_usd = 'NG=F'
data_closedprice_gas_usd = yf.Ticker(gas_usd).history(period='max')['Close']
# print(data_closedprice_gas_usd)
fig_gas_usd = px.line(data_closedprice_gas_usd, y="Close", title='Natural Gas / USD')
fig_gas_usd.update_layout(template=CHARTS_TEMPLATE)
#####Раздел где формируется дата и график для рсходов в USD

food = pd.read_csv("food1.csv")
food_plotly_usd_2 = px.line(food, x="DATE", y="Expenditures", title='Expenditures/USD')
food_plotly_usd_2.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для рсходов в GOLD

food_btc = pd.read_csv("food1.csv")
food_btc_plotly = px.line(food_btc, x="DATE", y="Ratio_BTC", log_y=True, title='Expenditures/BTC')
food_btc_plotly.update_layout(template=CHARTS_TEMPLATE)

#####Раздел где формируется дата и график для нефти бакса

data_closedprice_oil_usd_btc = yf.Ticker('CL=F').history(period='max')['Close']
fig_oil_usd_btc = px.line(data_closedprice_oil_usd_btc, y="Close", title='Oil / USD')
fig_oil_usd_btc.update_layout(template=CHARTS_TEMPLATE)
#####Раздел где объединяются даты нефти и золота и формируется новая графа ratioOilvsGold

empresas_btc = [
    'NG=F',
    'BTC=F'
]
####Раздел где формируется график и подготавливается дата для history gold price
h_gold = pd.read_csv("GoldpriceData.csv")
h_gold_plotly = px.line(h_gold, x="date", y="price", title='History GoldOZ/USD')
h_gold_plotly.update_layout(template=CHARTS_TEMPLATE)
####Раздел где формируется график и подгатавливается дата для history inflation rate
h_inflation_rate = pd.read_csv("CPIrate.csv")
h_inflation_rate_plotly = px.bar(h_inflation_rate, x="DATE", y="InflRate")
h_inflation_rate_plotly.update_layout(template=CHARTS_TEMPLATE)

####TableContent
df_infl_rate_p_3 = pd.read_csv("inflation_rate_period3.csv")

####TabsContent
tab1_gold = [
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=food_plotly),
            html.P('''Данный график показывает общие среднегодовые расходы американца (включая траты на ипотеку, 
            здравоохранение, крупные траты, повседневные траты и тд). Общий тренд графика говорит о том, что с каждым 
            годом среднегодовые расходы американца в долларах растут.''')
        ],width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=food_gold_plotly_1),
            html.P('''Данный график, как и соседний, показывает общие среднегодовые расходы американца, но уже по 
            отношению не к доллару, а к одной тройской унции золота(включая траты на ипотеку, здравоохранение, 
            крупные траты, повседневные траты и тд). То есть на графике отражено то, сколько унций золота требуется 
            американцу в год, чтобы покрыть личные расходы. Общий тренд графика говорит о том, что с каждым годом 
            среднегодовые расходы американца в золоте падают.''')
        ],width={'size': 6})

    ]),

    dbc.Row([

        dbc.Col([
            dcc.Graph(figure=fig),
            html.P('''График выше отражает соотношение унций золота к одному лоту газа. Иными словами график 
            показывает то, сколько унций было необходимо в каждый момент времени, чтобы купить 1 лот газа по биржевой 
            цене.''')
        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=fig_gas_usd),
            html.P(
                '''График Natural Gas/USD в реальном времени показывает стоимость за 1 лот газа на бирже в долларах.''')
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig_clgc),
            html.P('''Данный график показывает динамику стоимости одного барреля нефти в унциях золота.''')
        ]),
        dbc.Col([
            dcc.Graph(figure=fig_oil_usd),
            html.P('''На графике Oil/USD отражена стоимость барреля нефти в долларах США .''')
        ])

    ]),
]

tab2_bitcoin = [
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=food_btc_plotly),
            html.P('''Данный график, как и соседний, показывает общие среднегодовые расходы американца, но уже по 
            отношению не к доллару, а к bitcoin (включая траты на ипотеку, здравоохранение, крупные траты, 
            повседневные траты и тд). То есть на графике отражено то, сколько монет bitcoin требуется американцу в 
            год, чтобы покрыть личные расходы. Общий тренд графика говорит о том, что с каждым годом среднегодовые 
            расходы американца в золоте падают.''')

        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=food_plotly_usd_2),
            html.P('''Данный график показывает общие среднегодовые расходы американца (включая траты на ипотеку, здравоохранение, 
            крупные траты, повседневные траты и тд). Общий тренд графика говорит о том, что с каждым годом среднегодовые расходы американца в долларах растут.''')
        ],
            width={'size': 6})
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig_cl_btc),
            html.P('''Oil/BTC отображает динамику стоимости барреля нефти в bitcoin.''')
        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=fig_oil_usd_btc),
            html.P('''Oil/USD отображает динамику стоимости барреля нефти в долларах США.''')
        ],
            width={'size': 6}),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig_btc),
            html.P(
                '''Данный график показывает стоимость газа (одного биржевого лота фьючерса на газ) в bitcoin. То есть 
                шкала Y показывает колличество необходимых монет bitcoin.''')
        ],
            width={'size': 6}),
        dbc.Col([
            dcc.Graph(figure=fig_gas_usd),
            html.P(
                '''Данный график показывает стоимость газа (одного биржевого лота фьючерса на газ) в долларах США.''')
        ],
            width={'size': 6})
    ]),
]

tab4_inflation = [

    dbc.Row([
        dcc.Graph(figure=h_gold_plotly),
        html.P('''На графике отображена динамика стоимости золота в долларах США.Примечательно то, что до отмены 
        Бреттон-Вудской системы в ~1976 году цена на золото практически не изменялась. Факт малой подвижности цены 
        золота связан с инфляций, данные по которой приведены на графике ниже.''')
    ]),
    dbc.Row([
        dcc.Graph(figure=h_inflation_rate_plotly),
        html.P('''Далее приводятся данные для Великобритании по причине того, что у Банка Англии есть в открытом доступе данные по инфляции с 1210 года.
        Для периода классического золотого стандарта, который продлился до 1944 года характерны взаимопогашающиеся колебания инфляции.
        Это означает, что если  инфляция за год "X" составила +2.3%, то в следующий год "Y" будет дефляция на уровне 2.3%. Поскольку на инфляцию влияет множество внешних факторов, то
        допустимы незначительные отклонения, однако, как будет видно из таблицы ниже период золотого стандарта прошел с околонулевыми значениями инфляции.
        При этом в это время активно развивалось и сельское хозяйство и промышленность.''')
    ]),
    dbc.Row([
        dash_table.DataTable(df_infl_rate_p_3.to_dict('records'),
                             columns=[{"name": i, "id": i}
                                      for i in df_infl_rate_p_3.columns],
                             style_data={'width': '30px'}),
        html.P('''В таблице представлены три периода и указана средняя инфляция в процентах годовых для каждого из 
        периодов. Перед Бреттон-Вудом можно выделить еще один период под называнием: "золотослитковый стандарт", 
        но он продлился недолго с 1925 по 1944 год, однако главной проблемой этой системы была неконтроллируемая 
        возможность эмиссии (печати) новых денег, которые не были обеспечены золотом, что в конечном итоге привело к 
        краху британского фунта, как резервной валюты. На смену пришла резервная система с долларом США, который был 
        обеспечен золотом и мог конвертироваться в него до 1971 года. Из всех монетарных систем, стабильнее всего 
        показала себя система классического золотого стандарта. В США с 1837 по 1862 год частные банки могли иметь 
        свои банкноты, которые обязаны были держать обеспечение под выданные бумажные деньги''')
    ])

]
tab3_about = [
    dbc.Row([html.P('''Проект создан, чтобы каждый мог наглядно увидеть выгоду если бы были частные деньги 
    обеспеченные активами, как пример золотом или криптовалютой. Я склонен считать, что криптовалюта может являться 
    альтернативой фиатным деньгам (деньги без обеспечения, на сегодняшний день обеспечением не пользуются, 
    начиная с 1971 года), по скольку не возможно нарушить темп эмиссии (иначе говоря создания нового объема монет), 
    а также на производство монеты и обработку транзакций затрачиваются вполне реальные ресурсы (главным образом 
    электроэнергия), также криптовалютные майнеры осуществляют инвестиции в оборудование, помещения для его 
    размещения и инфраструктуру для коммутации asic/gpu, чтобы присоединения к вычислениям. Проект не является 
    завершенным и будет дорабатываться.'''),
             html.P('''Для того, чтобы наглядно продемонстрировать абсурд сегодняшних денег цены на нефть, газ, 
             а также средний объем годовых расходов американца были приведены к золоту и bitcoin. В большинстве 
             примеров видно удешевление стоимости сырья или объема расходов. Иными словами для потребителей зачастую 
             услуги и товары год от года дешевели бы или оставались на прежнем уровне.'''),
             html.P('''В конечном итоге, если отталкиваться от истории золотого стандарта, инфляция могла бы 
             вернуться к около нулевым значениям. Накопления бы не обесценивались, предприниматели могли бы исключить 
             риски девальвации или инфляции от чрезмерной эмиссии денежных средств. Банки смогли бы держать 
             стабильный уровень кредитно-депозитных ставок, это позволит по выданным кредитам получать поток денежных 
             средств, которые по сути имеют ту же покупательную способность, что и в момент выдачи кредита. И у 
             потребителей и у производителей такая система могла вызывать большое доверие и как следствие полученные 
             доходы население могло бы инвестировать в экономику.'''),
             html.P('''Мы живем в эпоху высоких технологий и вместе с классическим золотым стандартом появляются 
             криптовалюты. На мой взгляд наиболее полезным, с экономической точки зрения, является семейство 
             алгоритмов на PoW (Proof of Work) или доказательство работы. Для эмиссии монет, которая ограничена 
             программным кодом и не может быть изменена, как я и писал ранее, можно рассчитать затраты и финансовую 
             выгоду от инвестиций в оборудование для майнинга. Как и в случае с золотом для майнинга криптовалют 
             можно рассчитать свой All-in Sustaining Cost (AISC), таким образом для Bitcoin при заданных расходах на 
             аренду, инвестиции в оборудование, ремонт, затраты на электричество и тд, можно оценить целесообразность 
             майнинга и инвестиций в него.''')]),
             html.P('''С золотом похожая ситуация, если его в обороте становится много, то оно теряет ценность и в 
             какой то момент времени золотодобытчики не смогут из выручки покрывать расходы. Тогда объем добычи может 
             сократиться, таким образом ценность золота может возрасти и золотодобытчики вновь смогут добывать металл 
             в нужных рынку объемах.''')
]
####Раздел со стилем
'''LAYOUT'''


def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, external_stylesheets=[dbc.themes.BOOTSTRAP], name="Dashboard", url_base_pathname="/dash/")
    dash_app.layout = html.Div([
        dbc.Row([
            dbc.Col(
                html.Img(src=dash_app.get_asset_url('images/icon.png'),
                         style={'width': '50px', 'marginLeft': '40px'}),
                width={'size': 1}
            ),
            dbc.Col(html.H2('Dashboard from Awaking project'),
                    width={'size': 7}),
            dbc.Col(html.Div([html.A('Back to home', href='/home')]),
                    width={'size': 4})],
            className='app-header'),
        html.Div([
            # Body
            # Tabs
            dbc.Tabs([
                dbc.Tab(tab1_gold, label='*/Gold'),
                dbc.Tab(tab2_bitcoin, label='*/Bitcoin'),
                dbc.Tab(tab4_inflation, label='Inflation'),
                dbc.Tab(tab3_about, label='About Project')
            ])

        ],
            style={'marginLeft': '90px',
                   'marginRight': '90px',
                   'marginTop': '20px'}, )
    ])
    return dash_app

