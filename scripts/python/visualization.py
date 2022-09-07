from ast import Try
import pandas as pd
import json
import plotly
import plotly.express as px
import sys
import os
sys.path.append('../../data')
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Graph One
df1 =pd.read_csv('../../data/financialSummary.csv')
spent_data= df1.drop([2,3,5,6,10], axis=0)
spent_data['PAID OUT']= spent_data['PAID OUT'].str.replace(',', '').astype(float)
spent_data.sort_values(by='PAID OUT', ascending=True,inplace= True)

fig1 = px.bar(spent_data,x= 'TRANSACTION TYPE', y='PAID OUT',color= 'TRANSACTION TYPE', title='SPENDING SUMMARY')
fig1.write_image("../../visualization/application/static/images/fig1.png")


# Graph two
earnings_data= df1.drop([0,4,7,8,9,10], axis=0)
earnings_data['PAID OUT']= earnings_data['PAID OUT'].str.replace(',', '').astype(float)
earnings_data.sort_values(by='PAID IN', ascending=True,inplace= True)

fig2 = px.bar(earnings_data,x= 'TRANSACTION TYPE', y='PAID IN',color= 'TRANSACTION TYPE',  title='EARNINGS SUMMARY')
fig2.write_image("../../visualization/application/static/images/fig2.png")


# Graph three
df2= pd.read_csv("../../data/TransactionData.csv")
df2['Completion Time']=pd.to_datetime(df2['Completion Time'])
transaction_period= df2.sort_values(by='Completion Time',ascending=True)
transaction_period= transaction_period.groupby(transaction_period['Completion Time'].dt.strftime('%Y-%m')).max()
transaction_period["Month"] = pd.to_datetime(transaction_period['Completion Time'], format='%b', errors='coerce').dt.month

fig3 = px.line(transaction_period,x= 'Month', y='Paid in',  title='MONTHLY EARNINGS SUMMARY')
fig3.write_image("../../visualization/application/static/images/fig3.png")



# Graph four

fig4 = px.line(transaction_period,x= 'Month', y='Withdrawn',  title='MONTHLY SPENDING SUMMARY')
fig4.write_image("../../visualization/application/static/images/fig4.png")

logger.info("images successfully saved")