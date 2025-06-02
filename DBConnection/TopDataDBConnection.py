import pandas as pd
from sqlalchemy import create_engine
import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from DataExtractionFromRepo.TopTableData import TopData
from DataExtractionFromRepo.AggregatedTableData import AggregatedData
from DataExtractionFromRepo.MapTableData import MapData
class TopDataDBConnection:
    def __init__(self):
        self.topdata = TopData()
        self.aggregatedata = AggregatedData()
        self.mapdata = MapData()
    def moveDFToDB(self):
        engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/Phonepe_analysis')
        df = self.topdata.getTopInsuranceData()
        table_name = 'Top_insurance'
        if df is not None and not df.empty:
             df.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
            print("DataFrame is None or Empty so skipping DB insertion.")
        df1 = self.topdata.getTopTransactionData()
        table_name = 'Top_Transaction'
        if df1 is not None and not df1.empty:
             df1.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
            print("DataFrame is None or Empty so skipping DB insertion.")
        df2 = self.topdata.getTopUserData()
        table_name = 'Top_User'
        if df2 is not None and not df2.empty:
             df2.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
            print("DataFrame is None or Empty so skipping DB insertion.")

    def moveaggregatedDFToDB(self):
        engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/Phonepe_analysis')
        df = self.aggregatedata.getAggregatedInsuranceData()
        table_name = 'Aggregated_insurance' 
        if df is not None and not df.empty:
             df.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
            print("DataFrame is None or Empty so skipping DB insertion.")
       
        df1 = self.aggregatedata.getAggregatedTransactionData()
        table_name = 'Aggregated_transaction'
        if df1 is not None and not df1.empty:
             df1.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
            print("DataFrame is None or Empty so skipping DB insertion.")

        df3 = self.aggregatedata.getAggregatedUserData()
        table_name = 'Aggregated_user'
        if df3 is not None and not df3.empty:
             df3.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
             print("DataFrame is None or Empty so skipping DB insertion.")

    def moveMapDFToDB(self):
        engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/Phonepe_analysis')
        df = self.mapdata.getMapInsuranceData()
        table_name = 'Map_insurance'
        if df is not None and not df.empty:
             df.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
             print("DataFrame is None or Empty so skipping DB insertion.")
        df1 = self.mapdata.getMapTransactionData()
        table_name = 'Map_map'
        if df1 is not None and not df1.empty:
             df1.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
             print("DataFrame is None or Empty so skipping DB insertion.")
        df2 = self.mapdata.getMapUserData()
        table_name = 'Map_user'
        if df2 is not None and not df2.empty:
             df2.to_sql(table_name, engine , if_exists='replace', index = False)
             print(f'{table_name} Table created succesfully in the Phonepe_analysis Database')
        else:
             print("DataFrame is None or Empty so skipping DB insertion.")
    
tdbc = TopDataDBConnection()
tdbc.moveDFToDB()
tdbc.moveaggregatedDFToDB()
tdbc.moveMapDFToDB()
