'''6. Insurance Engagement Analysis
Scenario:
PhonePe aims to analyze insurance transactions across various states and districts to understand the uptake of
insurance services among users. This analysis will provide insights into user behavior, market demand, and potential
areas for growth in insurance offerings.
'''

import pandas as pd
import psycopg2 as psg

class InsuranceEngagementAnalysis:
    def __init__(self):
        self.connection = psg.connect(
            host="localhost",
            database="Phonepe_analysis",
            user="postgres",
            password="root"
        )
        self.cursor = self.connection.cursor()

    def getTotalTransactionsByState(self):
        query = '''select "State", sum("Transaction_count") as "Total_Transactions"
                    from "Map_insurance"
                    Group by "State"
                    order by "Total_Transactions" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_Users'])
        return df
    

    def getTotalTransactionsByQuarterly(self):
        query = '''select 
                             "Year", "Quarter",
                              sum("Transaction_count") as "Total_Transactions"
                        from "Map_insurance"
                        Group by  "Year", "Quarter"
                        order by  "Year", "Quarter"'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ["Year", "Quarter",'Total_Transactions'])
        return df
    
    def geTotalTransactionsByYearly(self):
        query = '''select 
                        "Year",
                        sum("Transaction_count") as "Total_Transactions"
                        from "Map_insurance"
                        Group by  "Year"
                        order by "Total_Transactions" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ["Year",'Total_Users'])
        return df

    def getTotalAmountByState(self):
        query = '''select 
                        "State", 
                        ROUND(sum("Transaction_amount")::NUMERIC,2) as "Total_Amount"
                    from "Map_insurance"
                    Group by "State"
                    order by "Total_Amount" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_Amount'])
        return df

    def getAverageAmountPerTransactionByState(self):
        query = '''select 
                        "State",
                        sum("Transaction_count") as "Total_Transactions",
                        round(sum("Transaction_amount")::NUMERIC,2) as "Total_Amount",
                        round(1.0 * sum("Transaction_amount")::NUMERIC/NULLIF(sum("Transaction_count"),0)::NUMERIC,2) as "Average_Amount"
                    from "Map_insurance"
                    group by "State"
                    order by "Average_Amount" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns =['State', 'Total_Transactions','Total_Amount','Average_Amount'])
        return df

    #Year-over-Year growth of registered users by state
    def getTotalTransactionsByYearly(self):
        query = '''select 
                             "State", "Year",
                              sum("Transaction_count") as "Total_Transactions"
                        from "Map_insurance"
                        Group by  "State", "Year"
                        order by  "State", "Year"'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State',"Year",'Total_Transactions'])
        return df

    #Region-wise average app opens per user (engagement metric)
    def getAverageAmountPerTransactionByRegion(self):
        query = '''select 
                        "Region_name",
                        sum("Transaction_count") as "Total_Transactions",
                        round(sum("Transaction_amount")::NUMERIC,2) as "Total_Amount",
                        round(1.0 * sum("Transaction_amount")::NUMERIC/NULLIF(sum("Transaction_count"),0)::NUMERIC,2) as "Average_Amount"
                    from "Map_insurance"
                    group by "Region_name"
                    order by "Average_Amount" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns =['Region_name', 'Total_Transactions','Total_Amount','Average_Amount'])
        return df
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

iea = InsuranceEngagementAnalysis()
iea.getAverageAmountPerTransactionByRegion()
iea.close_connection