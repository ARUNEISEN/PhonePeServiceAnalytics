'''1. Decoding Transaction Dynamics on PhonePe scenario
PhonePe, a leading digital payments platform, has recently identified significant variations in transaction behavior across states,
 quarters, and payment categories. While some regions and transaction types demonstrate consistent growth, others show stagnation or decline.
   The leadership team seeks a deeper understanding of these patterns to drive targeted business strategies.
'''
import pandas as pd
import psycopg2 as psg

class TransactionDynamics:

    def __init__(self):
        self.connection = psg.connect(
            host="localhost",
            database="Phonepe_analysis",
            user="postgres",
            password="root"
        )
        self.cursor = self.connection.cursor()

    def getTotalTransactionsByState(self):
        query = '''SELECT "State", SUM("Transaction_count") AS Total_transactions
                   FROM "Aggregated_transaction"
                   GROUP BY "State"
                   ORDER BY total_transactions DESC;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()             
        df = pd.DataFrame(rows, columns=["State", "Total_transactions"])
        return df
    
    def getTotalAmountByState(self):
        query = '''SELECT "State", ROUND(SUM("Transaction_amount")::NUMERIC,2) AS "Total_Amount"
                    FROM "Aggregated_transaction"
                    GROUP BY "State"
                    ORDER BY "Total_Amount" DESC;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()             
        df = pd.DataFrame(rows, columns=["State", "Total_Amount"])
        return df
    
    def getTotalTransactionsByYearAndQuarter(self):
        query = '''SELECT "Year", "Quarter", SUM("Transaction_count") AS "Total_Transactions"
                    FROM "Aggregated_transaction"
                    GROUP BY "Year", "Quarter"
                    ORDER BY "Year", "Quarter"'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=["Year", "Quarter", "Total_Transactions"])
        return df

    def getTotalTransactionsByTransationType(self):
        query = '''SELECT "Transaction_type", SUM("Transaction_count") AS "Total_transactions"
                    FROM "Aggregated_transaction"
                    GROUP BY "Transaction_type"
                    ORDER BY "Total_transactions" DESC;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Transaction_type',"Total_Transactions"])
        return df
    
    def getTotalAmountByTransationType(self):
        query = '''SELECT "Transaction_type",ROUND(SUM("Transaction_amount")::NUMERIC,2) AS "Total_Amount"
                    FROM "Aggregated_transaction"
                    GROUP BY "Transaction_type"
                    ORDER BY "Total_Amount" DESC;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Transaction_type',"Total_Transactions"])
        return df
    
    def getTopFiveStatesByTotalTransactions(self):
        query = '''SELECT "State",SUM("Transaction_count") AS "Total_transactions",
                ROUND(SUM("Transaction_amount")::NUMERIC, 2) AS "Total_Amount"
                FROM "Aggregated_transaction"
                GROUP BY "State"
                ORDER BY "Total_transactions" DESC
                LIMIT 5;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=['State', 'Total_Transactions','Total_Amount'])
        return df

    def getTopFiveStatesByTotalAmount(self):
        query = '''SELECT "State",SUM("Transaction_count") AS "Total_transactions",
                ROUND(SUM("Transaction_amount")::NUMERIC, 2) AS "Total_Amount"
                FROM "Aggregated_transaction"
                GROUP BY "State"
                ORDER BY "Total_Amount" DESC
                LIMIT 5;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=['State', 'Total_Transactions','Total_Amount'])
        return df

    def getTransactionTypeByPercantage(self):
        query = '''SELECT "Transaction_type",
                            SUM("Transaction_count") AS "Total_Transacions",
                            ROUND(100.0 * SUM("Transaction_count") / 
                            (SELECT SUM("Transaction_count") FROM "Aggregated_transaction"), 2) AS "Percentage_share"
                    FROM "Aggregated_transaction"
                    GROUP BY "Transaction_type"
                    ORDER BY "Percentage_share" DESC;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=['Transaction_Type', 'Total_Transactions','Percentage_share'])
        return df

    def getTransactionsPercantageByState(self):
        query = '''SELECT "State", SUM("Transaction_count") AS "Total_Transacions",
                   ROUND(100.0 * SUM("Transaction_count") / 
                         (SELECT SUM("Transaction_count") FROM "Aggregated_transaction"), 2) AS "Percentage_share"
                    FROM "Aggregated_transaction"
                    GROUP BY "State"
                    ORDER BY "Percentage_share" DESC;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=['State', 'Total_Transactions','Percentage_share'])
        return df


    def close_connection(self):
        self.cursor.close()
        self.connection.close()

td = TransactionDynamics()
td.getTransactionTypeByPercantage()
td.close_connection
    