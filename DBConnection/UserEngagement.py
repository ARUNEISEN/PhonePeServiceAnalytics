'''5. User Engagement and Growth Strategy
Scenario
PhonePe seeks to enhance its market position by analyzing user engagement across different states and districts.
With a significant number of registered users and app opens, understanding user behavior can provide
valuable insights for strategic decision-making and growth opportunities.
'''

import pandas as pd
import psycopg2 as psg

class UserEngagement:
    def __init__(self):
        self.connection = psg.connect(
            host="localhost",
            database="Phonepe_analysis",
            user="postgres",
            password="root"
        )
        self.cursor = self.connection.cursor()
#1. Which states have the highest and lowest number of registered users?
    def getTotalRegisteredUsersByState(self):
        query = '''select "State", sum("Registered_Users_count") as "Total_Users"
                    from "Map_user"
                    Group by "State"
                    order by "Total_Users" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_Users'])
        return df
    

    #2. What is the trend of user growth over time (yearly/quarterly)?
    def getRegisteredUsersByQuarterly(self):
        query = '''select 
                             "Year", "Quarter",
                              sum("Registered_Users_count") as "Total_Users"
                        from "Map_user"
                        Group by  "Year", "Quarter"
                        order by  "Year", "Quarter"'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ["Year", "Quarter",'Total_Users'])
        return df
    
    def getRegisteredUsersByYearly(self):
        query = '''select 
                        "Year",
                        sum("Registered_Users_count") as "Total_Users"
                        from "Map_user"
                        Group by  "Year"
                        order by "Total_Users" '''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ["Year",'Total_Users'])
        return df

#getRegisteredUsersByYearly
    def getTotalAppOpensByState(self):
        query = '''select "State", sum("App_opens") as "Total_App_opens"
                    from "Map_user"
                    Group by "State"
                    order by "Total_App_opens" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State', 'Total_App_opens'])
        return df
    #State-wise average app opens per user (engagement metric)
    def getAverageAppOpensByState(self):
        query = '''select 
                        "State",
                        sum("Registered_Users_count") as "Total_Users",
                        sum("App_opens") as "Total_App_Opens",
                        round(1.0 * sum("App_opens")/NULLIF(sum("Registered_Users_count"),0),2) as "Average_App_Opens"
                    from "Map_user"
                    group by "State"
                    order by "Average_App_Opens" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns =['State', 'Total_Users','Total_App_opens','Average_App_Opens'])
        return df

    #Year-over-Year growth of registered users by state
    def getRegisteredUsersByQuarterlyStateLevel(self):
        query = '''select 
                             "State", "Year",
                              sum("Registered_Users_count") as "Total_Users"
                        from "Map_user"
                        Group by  "State", "Year"
                        order by  "State", "Year"'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns = ['State',"Year",'Total_Users'])
        return df

    #Region-wise average app opens per user (engagement metric)
    def getAverageAppOpensByRegion(self):
        query = '''select 
                        "Region_name",
                        sum("Registered_Users_count") as "Total_Users",
                        sum("App_opens") as "Total_App_Opens",
                        round(1.0 * sum("App_opens")/NULLIF(sum("Registered_Users_count"),0),2) as "Average_App_Opens"
                    from "Map_user"
                    group by "Region_name"
                    order by "Average_App_Opens" desc'''
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns =['Region_name', 'Total_Users','Total_App_opens','Average_App_Opens'])
        return df
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

ue = UserEngagement()
ue.getAverageAppOpensByRegion()
ue.close_connection