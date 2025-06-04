'''3. Insurance Penetration and Growth Potential Analysis
Scenario:
PhonePe has ventured into the insurance domain, providing users with options to secure various policies.
With increasing transactions in this segment, the company seeks to analyze its growth trajectory and 
identify untapped opportunities for insurance adoption at the state level. This data will help prioritize
regions for marketing efforts and partnerships with insurers.
'''

import pandas as pd
import psycopg2 as psg

class InsurancePenetration:
    def __init__(self):
        self.connection = psg.connect(
            host="localhost",
            database="Phonepe_analysis",
            user="postgres",
            password="root"
        )
        self.cursor = self.connection.cursor()

    def getTotalTransactionsByState(self):
        query = '''select 
                        "State",
                        sum("Transaction_count") as "Total_Transactions"	
                    from "Aggregated_insurance"
                    group by "State"
                    order by "Total_Transactions" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_Transactions'])
        return df

    def getTotalAmountByState(self):
        query = '''select 
                        "State",
                         ROUND(sum("Transaction_amount")::NUMERIC,2) as "Total_Amount"	
                    from "Aggregated_insurance"
                    group by "State"
                    order by "Total_Amount" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_Amount'])
        return df

    def getTotalTransactionsByYear(self):
        query = '''select 
                        "Year",
                        sum("Transaction_count") as "Total_Transactions"	
                    from "Aggregated_insurance"
                    group by "Year"
                    order by "Total_Transactions" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_Transactions'])
        return df

    def getTotalAmountByYear(self):
        query = '''select 
                        "Year",
                         ROUND(sum("Transaction_amount")::NUMERIC,2) as "Total_Amount"	
                    from "Aggregated_insurance"
                    group by "Year"
                    order by "Total_Amount" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_Amount'])
        return df

#. How has insurance adoption grown over time (quarterly/yearly)?
    def getTotalTransactionsByQuarter(self):
        query = '''select 
                        "Year",
                        "Quarter",
                        sum("Transaction_count") as "Total_Transactions"	
                    from "Aggregated_insurance"
                    group by "Year", "Quarter"
                    order by "Year", "Quarter"'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Year','Quarter','Total_Transactions'])
        return df

    def getTotalAmountByQuarter(self):
        query = '''select 
                        "Year",
                        "Quarter",
                        ROUND(sum("Transaction_amount")::NUMERIC,2) as "Total_Amount"	
                    from "Aggregated_insurance"
                    group by "Year","Quarter"
                    order by "Year","Quarter"'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Year','Quarter','Total_Amount'])
        return df

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

ip = InsurancePenetration()
ip.getTotalTransactionsByQuarter()
ip.getTotalAmountByQuarter()
ip.close_connection