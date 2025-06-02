import os
import pandas as pd
import json

class MapData:

    def getMapInsuranceData(self):
         path = "./data/data/map/insurance/hover/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Region_name':[], 'Transaction_count':[], 'Transaction_amount':[]}
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

                    for dt in f['data']['hoverDataList']:
                        name = dt['name']
                        tran_count = dt['metric'][0]['count']
                        tran_amount = dt['metric'][0]['amount']
                        column['Region_name'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))

         map_insurance_data = pd.DataFrame(column)
         return map_insurance_data

    def getMapTransactionData(self):
         path = "./data/data/map/transaction/hover/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Region_name':[], 'Transaction_count':[], 'Transaction_amount':[]}
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

                    for dt in f['data']['hoverDataList']:
                        name = dt['name']
                        tran_count = dt['metric'][0]['count']
                        tran_amount = dt['metric'][0]['amount']
                        column['Region_name'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))

         map_transaction_data = pd.DataFrame(column)
         return map_transaction_data

    def getMapUserData(self):
         path = "./data/data/map/user/hover/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Region_name':[], 'Registered_Users_count':[], 'App_opens':[]}
         
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

                    for region, dt in f['data']['hoverData'].items():
                        user_count = dt['registeredUsers']
                        user_percent = dt['appOpens']
                        column['Region_name'].append(region)
                        column['Registered_Users_count'].append(user_count)
                        column['App_opens'].append(user_percent)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))

         agg_insurance_data = pd.DataFrame(column)
         return agg_insurance_data

md = MapData()
md.getMapUserData()
md.getMapInsuranceData()
md.getMapTransactionData()

