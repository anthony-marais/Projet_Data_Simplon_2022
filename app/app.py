import streamlit as st
import pandas as pd
import os, sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
import time
import plotly.express as px

def create_connection():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(BASE_DIR, ".env"))
    sys.path.append(BASE_DIR)
    url = os.environ["DATABASE_URL"]
    engine = create_engine(url)
    return engine


connection = create_connection()



def Get_Data(connection):
    request = """ SELECT "User"."Email Address", "User"."FirstName", "User"."LastName", "Job_Title"."Job Title", "State"."State" , "City"."City" , "Street"."Street", "Street_Number"."Number"
    FROM "User" 
    JOIN "Job_Title" ON "User"."ID_Job_Title" = "Job_Title"."ID_Job_Title" 
    JOIN "State" ON "User"."ID_State" = "State"."ID_State"
    JOIN "City" ON "User"."ID_City" = "City"."ID_City"
    JOIN "Street" ON "User"."ID_Street" = "Street"."ID_Street"
    JOIN "Street_Number" ON "User"."ID_Street_Number" = "Street_Number"."ID_Street_Number"
    """
    data = pd.read_sql_query(request, connection)
    data[["Mail", "Domain_Name"]] = data["Email Address"].str.split("@", 1, expand=True)
    data = data.drop(["Email Address"], axis=1)
    return data

df = Get_Data(connection)



st.title("Datavisualisation d'un jeux de données")  # Titre de l'application
st.sidebar.title("Datavisualisation d'un jeux de données")
st.markdown(
    "Cette application permet d'afficher les données pour mettre en évidence plusieurs critères"
)
st.sidebar.markdown(
    "Cette application permet d'afficher les données pour mettre en évidence plusieurs critères"
)


with st.spinner(text="In progress"):
    time.sleep(1)
    


st.sidebar.header("Select what to display")

select = st.sidebar.selectbox(
    "Share",
    ["Dataframe","Diagramm"],
    key="1",
)


if select == "Dataframe":
    st.dataframe(df)

    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="large_df.csv",
        mime="text/csv",
    )

if select == "Diagramm":
    
    value = df["Job Title"].value_counts()

    fig = px.pie(df, values=value, names = 'Job Title', hover_name='State')

	

	# this function adds labels to the pie chart
	# for more information on this chart, visit: https://plotly.com/python/pie-charts/
    fig.update_traces(textposition='inside', textinfo='percent+label')

	# after creating the chart, we display it on the app's screen using this command
    st.write(fig)



st.success("Done")
st.button("Re-run")
