from collections import UserString
import os, sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from app.utils import (
    format_job_title,
    format_state,
    format_city,
    format_street,
    format_street_number,
    format_fk_city,
    format_fk_state,
    format_fk_street,
    format_fk_street_number,
    format_fk_job_title,
    format_user,
)


from app.models import Job_Title, User, State, City, Street, Street_Number


def insert_db(connection):
    """Insère les données nécessaire à l'utilisation de l'application"""
    # On récupère les données du fichier CSV dans un dataframe
    data = pd.read_csv("./data/data.csv")

    data[["FirstName", "LastName"]] = data["FirstName LastName"].str.split(
        " ", 1, expand=True
    )
    data[["Street", "Number"]] = data["adress"].str.split(", ", 1, expand=True)
    data.drop(columns=["FirstName LastName", "adress"], inplace=True)

    job_title = format_job_title(data)
    state = format_state(data)
    city = format_city(data)
    street = format_street(data)
    street_number = format_street_number(data)
    fk_job_title = format_fk_job_title(data, job_title)
    fk_state = format_fk_state(data, state)
    fk_city = format_fk_city(data, city)
    fk_street = format_fk_street(data, street)
    fk_street_number = format_fk_street_number(data, street_number)
    user = format_user(
        data, fk_job_title, fk_state, fk_city, fk_street, fk_street_number
    )

    # On format les données (int64 pour les champs) afin de les préparer à l'insertion
    # On insère les données dans la table House
    Job_Title.insert_job_title_from_pd(connection, job_title)
    State.insert_state_from_pd(connection, state)
    City.insert_city_from_pd(connection, city)
    Street.insert_street_from_pd(connection, street)
    Street_Number.insert_street_number_from_pd(connection, street_number)
    User.insert_user_from_pd(connection, user)
    print("Données insérées dans la BDD")
