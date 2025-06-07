import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import requests
import plotly.graph_objects as go


from DBConnection.TransactionDynamics import TransactionDynamics
from DBConnection.DeviceDominance import DeviceDominance
from DBConnection.InsurancePenetration import InsurancePenetration
from DBConnection.UserEngagement import UserEngagement
from DBConnection.InsuranceEngagementAnalysis import InsuranceEngagementAnalysis

st.set_page_config(page_title="Phonpe Pulse", layout="wide")

st.title("PhonePe Pulse Dashboard")

st.sidebar.header("PhonePe Analysis Sections")

selectRB = st.sidebar.radio(
    "Business Case Studies",
    options = 
    ["Home",
    "Transaction Dynamics",
    "Device Dominance",
    "Insurance Penetration",
    "User Engagement",
    "Insurance Engagement"
    ]
)

state_name_mapping = {
                "Andaman-&-Nicobar-Islands": "Andaman & Nicobar",
                "Andhra-Pradesh":"Andhra Pradesh",
                "Arunachal-Pradesh": "Arunanchal Pradesh",
                "Dadra-&-Nagar-Haveli-&-Daman-&-Diu":"Dadra and Nagar Haveli and Daman and Diu",
                "Himachal-Pradesh":"Himachal Pradesh",
                "Jammu-&-Kashmir":"Jammu & Kashmir",
                "Madhya-Pradesh":"Madhya Pradesh",
                "Tamil-Nadu":"Tamil Nadu",
                "Uttar-Pradesh":"Uttar Pradesh",
                "West-Bengal":"West Bengal"
                # Add more if needed based on your debug output
            }

@st.cache_data
def load_geojson():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    return requests.get(url).json()

if selectRB == "Home":
    select = st.radio(
    "Main Tabs",
    options = 
    ["PhonePe Transactions - Statewise Map",
    "Insurance Transactions - Statewise Map",
    "Registered Users - Statewise Map" ])
    if select == "PhonePe Transactions - Statewise Map":
        col1,col2= st.columns([3,1])
        with col1:
            df = TransactionDynamics().getTotalTransactionsByState()
            st.subheader("PhonePe Transactions - Statewise Map")
            df["State"] = df["State"].str.title().str.strip()

            # Load GeoJSON
            geojson_data = load_geojson()

            # Extract GeoJSON state names]

            # Show both for debugging
            

            df["State"] = df["State"].replace(state_name_mapping)

            fig = go.Figure(data=go.Choropleth(
                geojson=geojson_data,
                featureidkey='properties.ST_NM',
                locations=df['State'],
                z=df['Total_transactions'],
                zmin=0,
                zmax=df['Total_transactions'].max(),
                colorscale='sunsetdark',
                marker_line_color='white',
                colorbar_title="Total Transactions"
            ))

            fig.update_geos(
                visible=False,
                projection=dict(type='conic conformal'),
                lonaxis=dict(range=[68, 98]),
                lataxis=dict(range=[6, 38])
            )

            fig.update_layout(
                margin=dict(r=0, t=30, l=0, b=0),
                height=600,
                title="Total Transactions by State (India)"
            )

            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.dataframe(df)
    if select == "Insurance Transactions - Statewise Map":
        col1,col2= st.columns([3,1])
        with col1:
            df = InsurancePenetration().getTotalTransactionsByState()
            st.subheader("Insurance Transactions - Statewise Map")
            df["State"] = df["State"].str.title().str.strip()

            # Load GeoJSON
            geojson_data = load_geojson()

            df["State"] = df["State"].replace(state_name_mapping)

            fig = go.Figure(data=go.Choropleth(
                geojson=geojson_data,
                featureidkey='properties.ST_NM',
                locations=df['State'],
                z=df['Total_Transactions'],
                zmin=0,
                zmax=df['Total_Transactions'].max(),
                colorscale='aggrnyl',
                marker_line_color='white',
                colorbar_title="Total Transactions"
            ))

            fig.update_geos(
                visible=False,
                projection=dict(type='conic conformal'),
                lonaxis=dict(range=[68, 98]),
                lataxis=dict(range=[6, 38])
            )

            fig.update_layout(
                margin=dict(r=0, t=30, l=0, b=0),
                height=600,
                title="Total Insurance Transactions by State (India)"
            )

            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.dataframe(df)
    if select == "Registered Users - Statewise Map":
        col1,col2= st.columns([3,1])
        with col1:
            df = DeviceDominance().getTotalUserCountByState()
            st.subheader("Registered Users - Statewise Map")
            df["State"] = df["State"].str.title().str.strip()

            # Load GeoJSON
            geojson_data = load_geojson()

            df["State"] = df["State"].replace(state_name_mapping)

            fig = go.Figure(data=go.Choropleth(
                geojson=geojson_data,
                featureidkey='properties.ST_NM',
                locations=df['State'],
                z=df['TotalRegisteredUsers'],
                zmin=0,
                zmax=df['TotalRegisteredUsers'].max(),
                colorscale='tealrose',
                marker_line_color='white',
                colorbar_title="Total Transactions"
            ))

            fig.update_geos(
                visible=False,
                projection=dict(type='conic conformal'),
                lonaxis=dict(range=[68, 98]),
                lataxis=dict(range=[6, 38])
            )

            fig.update_layout(
                margin=dict(r=0, t=30, l=0, b=0),
                height=600,
                title="Total Registered Users by State (India)"
            )

            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.dataframe(df)


if selectRB == "Transaction Dynamics":

    col1,col2= st.columns([3,1])
    with col1:
        st.subheader("Decoding Transaction Dynamics on PhonePe")
        td = TransactionDynamics()
        if st.checkbox("Show total transactions By State level"):
            df = td.getTotalTransactionsByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Transactions By StateWise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_transactions"],color="red")
            ax.set_xlabel("Total_transactions")
            ax.set_ylabel("State")
            ax.set_title("Total Transactions VS State")
            ax.invert_yaxis()
            st.pyplot(fig)

        if st.checkbox("Show total Transaction Amount By State level"):
            df = td.getTotalAmountByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Amount By StateWise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Amount"],color="blue")
            ax.set_xlabel("Total_Amount")
            ax.set_ylabel("State")
            ax.set_title("Transactions_Amount VS State")
            ax.invert_yaxis()
            st.pyplot(fig)

        if st.checkbox("Show Total Transactions by Year-Quarter wise"):
            st.subheader("Total Transactions by Year-Quarter")
            df = td.getTransactionsPercantageByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

        if st.checkbox("Top states by Total Transactions"):
            df = td.getTopStatesByTotalTransactions()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Top states by Total Transactions")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Transactions"],color="blue")
            ax.set_xlabel("Total_Transactions")
            ax.set_ylabel("State")
            ax.set_title("Transactions VS State")
            ax.invert_yaxis()
            st.pyplot(fig)

        if st.checkbox("Top states by Total Amount"):
            df = td.getTopStatesByTotalAmount()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Top states by Total Amount")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Amount"],color="lightgreen")
            ax.set_xlabel("Total_Amount")
            ax.set_ylabel("State")
            ax.set_title("Amount VS State")
            ax.invert_yaxis()
            st.pyplot(fig)
        if st.checkbox("Percentage level contribution by Transaction Type"):
            df = td.getTransactionTypeByPercantage()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)
        
        if st.checkbox("Percentage level contribution by State"):
            df = td.getTransactionsPercantageByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

    with col2:
        if st.checkbox("Total Transactions vs Transaction Type"):
            df = td.getTotalTransactionsByTransationType()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Transactions per Transaction Type")
            fig,ax = plt.subplots()
            ax.pie(
                df["Total_Transactions"],
                labels = df["Transaction_type"],
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Pastel1.colors,
             )
            ax.set_title("Transactions vs TransactionType")
            ax.axis('equal')

            st.pyplot(fig)
        if st.checkbox("Total Amount vs Transaction Type"):
            df = td.getTotalAmountByTransationType()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Amount per Transaction Type")
            fig,ax = plt.subplots()
            ax.pie(
                df["Total_Amount"],
                labels = df["Transaction_type"],
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Pastel1.colors,
             )
            ax.set_title("Amount vs TransactionType")
            ax.axis('equal')
            st.pyplot(fig)
if selectRB == "Device Dominance":
    
    col1,col2= st.columns([3,1])
    with col1:
        st.subheader("Device Dominance and User Engagement Analysis")
        dd = DeviceDominance()
        if st.checkbox("Show total users By Brand wise"):
            df = dd.getTotalUserCountByBrand()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Users By Brand")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["Brand"],df["TotalRegisteredUsers"],color="red")
            ax.set_xlabel("Brand")
            ax.set_ylabel("TotalRegisteredUsers")
            ax.set_title("Total RegisteredUsers VS Brand")
            ax.invert_yaxis()
            st.pyplot(fig)

        if st.checkbox("Top level Brands used"):
            df = dd.getTopTenBrandUsed()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Top Brands By user")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["Brand"],df["TotalRegisteredUsers"],color="blue")
            ax.set_xlabel("Brand")
            ax.set_ylabel("TotalRegisteredUsers")
            ax.set_title("TotalRegisteredUsers VS Brand")
            ax.invert_yaxis()
            st.pyplot(fig)

        if st.checkbox("Show Top Three Brands By Each State"):
            st.subheader("Top Three Brands By Each State")
            df = dd.getTopThreeBrandsByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

        if st.checkbox("Average Users By Brand level"):
            df = dd.getAvgUserPercentageByBrand()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Average Users By Brand level")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["Brand"],df["AverageUserPercentage"],color="blue")
            ax.set_xlabel("AverageUserPercentage")
            ax.set_ylabel("Brand")
            ax.set_title("AverageUserPercentage VS State")
            ax.invert_yaxis()
            st.pyplot(fig)
        

        if st.checkbox("Total Registered User By State wise"):
            df = dd.getTotalUserCountByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total users By State wise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["TotalRegisteredUsers"],color="lightgreen")
            ax.set_xlabel("TotalRegisteredUsers")
            ax.set_ylabel("State")
            ax.set_title("Total RegisteredUsers VS State")
            ax.invert_yaxis()
            st.pyplot(fig)
        if st.checkbox("Average User Percentage By State level"):
            df = dd.getUserPercentageByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)    
if selectRB == "Insurance Penetration":
    col1,col2= st.columns([3,1])
    with col1:
        st.subheader("Insurance Penetration and Growth Potential Analysis")
        ip = InsurancePenetration()
        if st.checkbox("Show total Insurance transactions By State level"):
            df = ip.getTotalTransactionsByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Insurance Transactions By State Wise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Transactions"],color="red")
            ax.set_xlabel("Total_Transactions")
            ax.set_ylabel("State")
            ax.set_title("Total Transactions VS State")
            ax.invert_yaxis()
            st.pyplot(fig)
        if st.checkbox("Show total Insurance Amount By State level"):
            df = ip.getTotalAmountByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Insurance Amount By State Wise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Amount"],color="red")
            ax.set_xlabel("Total_Amount")
            ax.set_ylabel("State")
            ax.set_title("Total Amount VS State")
            ax.invert_yaxis()
            st.pyplot(fig)

        if st.checkbox("Show Insurance Transactions for Quarter"):
            df = ip.getTotalTransactionsByQuarter()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

        if st.checkbox("Show Insurance Amount for Quarter"):
            df = ip.getTotalAmountByQuarter()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

    with col2:
        if st.checkbox("Total Transactions vs Year"):
            df = ip.getTotalTransactionsByYear()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Insurance Transactions per Year")
            fig,ax = plt.subplots()
            ax.pie(
                df["Total_Transactions"],
                labels = df["Year"],
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Pastel1.colors,
             )
            ax.set_title("Total_Transactions vs Year")
            ax.axis('equal')

            st.pyplot(fig)

        if st.checkbox("Total Insurance Amount vs Year"):
            df = ip.getTotalAmountByYear()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Amount per Year")
            fig,ax = plt.subplots()
            ax.pie(
                df["Total_Amount"],
                labels = df["Year"],
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Pastel1.colors,
             )
            ax.set_title("Total Amount vs Year")
            ax.axis('equal')

            st.pyplot(fig)
if selectRB == "User Engagement":
    col1,col2= st.columns([3,1])
    with col1:
        st.subheader("User Engagement and Growth Strategy")
        ue = UserEngagement()
        if st.checkbox("Show total Registered Users By State level"):
            df = ue.getTotalRegisteredUsersByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Users By State Wise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Users"],color="red")
            ax.set_xlabel("Total_Users")
            ax.set_ylabel("State")
            ax.set_title("Total Users VS State")
            ax.invert_yaxis()
            st.pyplot(fig)
        if st.checkbox("Show total Registered Users ByYear-Quarter wise"):
            df = ue.getRegisteredUsersByQuarterly()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

        if st.checkbox("Show total Registered Users for Each State by Quarter wise"):
            df = ue.getRegisteredUsersByQuarterlyStateLevel()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

        if st.checkbox("Total Average App Opens By State Level"):
            df = ue.getAverageAppOpensByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)
                   
        
        if st.checkbox("Total Average App Opens By Region"):
            df = ue.getAverageAppOpensByRegion()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)
    
    with col2:
        if st.checkbox("Total Registered Users vs Year"):
            df = ue.getRegisteredUsersByYearly()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Users per Year")
            fig,ax = plt.subplots()
            ax.pie(
                df["Total_Users"],
                labels = df["Year"],
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Pastel1.colors,
             )
            ax.set_title("Total_Users vs Year")
            ax.axis('equal')

            st.pyplot(fig)

        if st.checkbox("Total App Opens By State Level"):
            df = ue.getTotalAppOpensByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)
if selectRB == "Insurance Engagement":
    col1,col2= st.columns([3,1])
    with col1:
        st.subheader("Insurance Engagement Analysis")
        iea = InsuranceEngagementAnalysis()
        if st.checkbox("Show total transactions By State level"):
            df = iea.getTotalTransactionsByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total Transactions By StateWise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Transactions"],color="lightgreen")
            ax.set_xlabel("Total_Transactions")
            ax.set_ylabel("State")
            ax.set_title("Total Transactions VS State")
            ax.invert_yaxis()
            st.pyplot(fig)
        if st.checkbox("Total Insurance Amount - State Level"):
            df = iea.getTotalAmountByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)
            st.subheader("Total Amount By StateWise")
            fig, ax = plt.subplots(figsize=(12,6))
            ax.barh(df["State"],df["Total_Amount"],color="lightgreen")
            ax.set_xlabel("Total_Amount")
            ax.set_ylabel("State")
            ax.set_title("Total Amount VS State")
            ax.invert_yaxis()
            st.pyplot(fig)

        if st.checkbox("Show total transactions By Quarterly"):
            df = iea.getTotalTransactionsByQuarterly()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)
            
        if st.checkbox("Total Average Insurance Amount per Transaction - State Level"):
            df = iea.getAverageAmountPerTransactionByState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

        if st.checkbox("Total Average Insurance Amount per Transaction - Region Level"):
            df = iea.getAverageAmountPerTransactionByRegion()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)   
         

        if st.checkbox("Total Insurance Transactions every Year State Level"):
            df = iea.getTotalTransactionsByYearlyForState()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

    with col2:
        if st.checkbox("Total Insurance transactions by every Year"):
            df = iea.getTotalTransactionsByYearly()
            if df.empty:
                st.warning("No Data available to display")
            st.dataframe(df)

            st.subheader("Total transactions per Year")
            fig,ax = plt.subplots()
            ax.pie(
                df["Total_Transactions"],
                labels = df["Year"],
                autopct='%1.1f%%',
                startangle=90,
                colors=plt.cm.Pastel1.colors,
             )
            ax.set_title("Total_Transactions vs Year")
            ax.axis('equal')

            st.pyplot(fig)

    

