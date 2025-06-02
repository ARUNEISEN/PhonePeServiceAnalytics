import os
import pandas as pd
import json

class AggregatedData:

    def getAggregatedInsuranceData(self):
         path = "./data/data/aggregated/insurance/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
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

                    for dt in f['data']['transactionData']:
                        name = dt['name']
                        tran_count = dt['paymentInstruments'][0]['count']
                        tran_amount = dt['paymentInstruments'][0]['amount']
                        column['Transaction_type'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))

         agg_insurance_data = pd.DataFrame(column)
         return agg_insurance_data

    def getAggregatedTransactionData(self):
         path = "./data/data/aggregated/transaction/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
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

                    for dt in f['data']['transactionData']:
                        name = dt['name']
                        tran_count = dt['paymentInstruments'][0]['count']
                        tran_amount = dt['paymentInstruments'][0]['amount']
                        column['Transaction_type'].append(name)
                        column['Transaction_count'].append(tran_count)
                        column['Transaction_amount'].append(tran_amount)
                        column['State'].append(state)
                        column['Year'].append(year)
                        column['Quarter'].append(int(quarter.strip('.json')))

         agg_insurance_data = pd.DataFrame(column)
         return agg_insurance_data

    def getAggregatedUserData(self):
         path = "./data/data/aggregated/user/country/india/state/"
         agg_state_list = os.listdir(path)         
         column = {'State':[], 'Year':[], 'Quarter':[], 'Brand':[], 'User_count':[], 'User_Percentage':[]}
         
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
                    if f['data'].get('usersByDevice') is not None:
                        for dt in f['data']['usersByDevice']:
                            name = dt['brand']
                            user_count = dt['count']
                            user_percent = dt['percentage']
                            column['Brand'].append(name)
                            column['User_count'].append(user_count)
                            column['User_Percentage'].append(user_percent)
                            column['State'].append(state)
                            column['Year'].append(year)
                            column['Quarter'].append(int(quarter.strip('.json')))
                    else:
                        print("User by device is None")

         agg_insurance_data = pd.DataFrame(column)
         return agg_insurance_data
    
ad = AggregatedData()
ad.getAggregatedUserData()
ad.getAggregatedInsuranceData()
ad.getAggregatedTransactionData()

