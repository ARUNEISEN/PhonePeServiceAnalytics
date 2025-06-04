'''2. Device Dominance and User Engagement Analysis
Scenario
PhonePe aims to enhance user engagement and improve app performance by understanding user preferences across
 different device brands. The data reveals the number of registered users and app opens, segmented by device 
 brands, regions, and time periods. However, trends in device usage vary significantly across regions, and some
 devices are disproportionately underutilized despite high registration numbers
'''

import pandas as pd
import psycopg2 as psg

class DeviceDominance:
    def __init__(self):
        self.connection = psg.connect(
            host="localhost",
            database="Phonepe_analysis",
            user="postgres",
            password="root"
        )
        self.cursor = self.connection.cursor()

    def getTotalUserCountByBrand(self):
        query = '''SELECT "Brand", SUM("User_count") AS "TotalRegisteredUsers"
                   FROM "Aggregated_user"
                   GROUP BY "Brand"
                   ORDER BY "TotalRegisteredUsers" DESC '''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Brand', 'TotalRegisteredUsers'])
        return df

    def getTopTenBrandUsed(self):
        query = '''SELECT "Brand", SUM("User_count") AS "TotalRegisteredUsers"
                   FROM "Aggregated_user"
                   GROUP BY "Brand"
                   ORDER BY "TotalRegisteredUsers" DESC
                   LIMIT 10 '''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Brand', 'TotalRegisteredUsers'])
        return df

    def getTopThreeBrandsByState(self):
        query = '''WITH "BrandRanking" AS (
                        SELECT "State", "Brand",
                            AVG("User_count") AS "AverageUserCount",
                            ROW_NUMBER() OVER(PARTITION BY "State" ORDER BY AVG("User_count") DESC) AS "RankNo"
                        FROM "Aggregated_user"
                        GROUP BY  "State", "Brand"
                    )
                    SELECT "State","Brand","AverageUserCount"
                    FROM "BrandRanking"
                    WHERE "RankNo" <= 3
                    ORDER BY "State", "RankNo";'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State','Brand', 'AverageUserCount'])
        return df
    
    def getAvgUserPercentageByBrand(self):
        query = '''SELECT  "Brand",
                        AVG("User_Percentage") AS "AverageUserPercentage"
                    FROM  "Aggregated_user"
                    GROUP BY  "Brand"
                    ORDER BY  "AverageUserPercentage" DESC'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['Brand', 'AverageUserPercentage'])
        return df

    def getTotalUserCountByState(self):
        query = '''SELECT "State", SUM("User_count") AS "TotalRegisteredUsers"
                   FROM "Aggregated_user"
                   GROUP BY "State"
                   ORDER BY "TotalRegisteredUsers" DESC '''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'TotalRegisteredUsers'])
        return df

    def getTotalUserPercentageByState(self):
        query = '''SELECT "State", SUM("User_countU") AS "TotalRegisteredUsers"
                   FROM "Aggregated_user"
                   GROUP BY "State"
                   ORDER BY "TotalRegisteredUsers" DESC '''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'TotalRegisteredUsers'])
        return df

    def getUserPercentageByState(self):
        query = '''SELECT "State",
                        SUM("User_count") AS "Total_User",
                        ROUND(100.0 * SUM("User_count") / 
                        (SELECT SUM("User_count") FROM "Aggregated_user"), 2) AS "Percentage_share"
                    FROM "Aggregated_user"
                    GROUP BY "State"
                    ORDER BY "Percentage_share" DESC;'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_User','Percentage_share'])
        return df

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

dd = DeviceDominance()
dd.getUserPercentageByState()
dd.close_connection