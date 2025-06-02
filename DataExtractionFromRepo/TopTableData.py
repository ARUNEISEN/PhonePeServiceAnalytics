import os
import pandas as pd
import json

class TopData:

    def getTopInsuranceData(self):
         path = "./data/data/top/insurance/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Region_name':[], 'Region_Type':[], 'Transaction_count':[], 'Transaction_amount':[]}
         for state in agg_state_list:
            path_state = path + state + '/'
            agg_year = os.listdir(path_state)

            for year in agg_year:
                path_quarter = path_state + year +'/'
                agg_quarters = os.listdir(path_quarter)

                for quarter in agg_quarters:
                    file_path = path_quarter + quarter
                    file = open(file_path,'r')
                    f = json.load(file)

                    for dt in f['data']['districts']:
                        name = dt['entityName']
                        tran_count = dt['metric']['count']
                        tran_amount = dt['metric']['amount']
                        column['Region_name'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))
                        column['Region_Type'].append('District')
                    for dt in f['data']['pincodes']:
                        name = dt['entityName']
                        tran_count = dt['metric']['count']
                        tran_amount = dt['metric']['amount']
                        column['Region_name'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))
                        column['Region_Type'].append('pincodes')

         top_insurance_data = pd.DataFrame(column)
         return top_insurance_data

    def getTopTransactionData(self):
         path = "./data/data/top/transaction/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[],'Region_Type':[], 'Region_name':[],  'Transaction_count':[], 'Transaction_amount':[]}
         
         for state in agg_state_list:
            path_state = path + state + '/'
            agg_year = os.listdir(path_state)

            for year in agg_year:
                path_quarter = path_state + year +'/'
                agg_quarters = os.listdir(path_quarter)

                for quarter in agg_quarters:
                    file_path = path_quarter + quarter
                    file = open(file_path,'r')
                    f = json.load(file)

                    for dt in f['data']['districts']:
                        name = dt['entityName']
                        tran_count = dt['metric']['count']
                        tran_amount = dt['metric']['amount']
                        column['Region_name'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))
                        column['Region_Type'].append('District')
                    for dt in f['data']['pincodes']:
                        name = dt['entityName']
                        tran_count = dt['metric']['count']
                        tran_amount = dt['metric']['amount']
                        column['Region_name'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))
                        column['Region_Type'].append('pincodes')

         top_transaction_data = pd.DataFrame(column)
         return top_transaction_data

    def getTopUserData(self):
         path = "./data/data/top/user/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Region_Type':[], 'Region_name':[], 'Registered_Users_count':[]}
         
         for state in agg_state_list:
            path_state = path + state + '/'
            agg_year = os.listdir(path_state)

            for year in agg_year:
                path_quarter = path_state + year +'/'
                agg_quarters = os.listdir(path_quarter)

                for quarter in agg_quarters:
                    file_path = path_quarter + quarter
                    file = open(file_path,'r')
                    f = json.load(file)

                    for dt in f['data']['districts']:
                        name = dt['name']
                        tran_count = dt['registeredUsers']
                        column['Region_name'].append(name)
                        column['Registered_Users_count'].append(tran_count)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))
                        column['Region_Type'].append('District')
                    for dt in f['data']['pincodes']:
                        name = dt['name']
                        tran_count = dt['registeredUsers']
                        column['Region_name'].append(name)
                        column['Registered_Users_count'].append(tran_count)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))
                        column['Region_Type'].append('pincodes')

         top_insurance_data = pd.DataFrame(column)
         return top_insurance_data

td = TopData()
print(td.getTopInsuranceData())
# td.getTopTransactionData()
# td.getTopUserData()

