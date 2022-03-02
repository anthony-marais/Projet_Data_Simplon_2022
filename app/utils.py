from os import pipe
import pandas as pd


def format_job_title(data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD
    Args:
        data (pd.DataFrame): dataframe provenant du fichier csv
    Returns:
        pd.DataFrame: Le dataframe converti
    """
    job_title = pd.DataFrame(columns=["Job Title"])
    job_title = pd.concat([job_title, data[["Job Title"]].drop_duplicates()])
    job_title = job_title.reset_index()
    job_title = job_title.drop(columns=["index"])
    job_title = job_title.reset_index()
    job_title = job_title.rename(columns={"index": "ID_Job_Title"})
    job_title.ID_Job_Title = job_title.ID_Job_Title + 1

    return job_title


def format_state(data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD
    Args:
        data (pd.DataFrame): dataframe provenant du fichier csv
    Returns:
        pd.DataFrame: Le dataframe converti
    """
    State = pd.DataFrame(columns=["State"])
    State = pd.concat([State, data[["State"]].drop_duplicates()])
    State = State.reset_index()
    State = State.drop(columns=["index"])
    State = State.reset_index()
    State = State.rename(columns={"index": "ID_State"})
    State.ID_State = State.ID_State + 1

    return State


def format_city(data: pd.DataFrame):

    City = pd.DataFrame(columns=["City"])
    City = pd.concat([City, data[["City"]].drop_duplicates()])
    City = City.reset_index()
    City = City.drop(columns=["index"])
    City = City.reset_index()
    City = City.rename(columns={"index": "ID_City"})
    City.ID_City = City.ID_City + 1

    return City


def format_street(data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD
    Args:
        ratings_data (pd.DataFrame): dataframe provenant du fichier csv
    Returns:
        pd.DataFrame: Le dataframe converti
    """
    Street = pd.DataFrame(columns=["Street"])
    Street = pd.concat([Street, data[["Street"]].drop_duplicates()])
    Street = Street.reset_index()
    Street = Street.rename(columns={"index": "ID_Street"})
    Street.ID_Street = Street.ID_Street + 1
    Street = Street.reset_index()
    Street = Street.drop(columns=["ID_Street"])
    Street = Street.rename(columns={"index": "ID_Street"})
    Street.ID_Street = Street.ID_Street + 1
    return Street


def format_street_number(data: pd.DataFrame):
    """Permet de formatter les champs du dataframe afin de les conformer au type de la BDD
    Args:
        to_read_data (pd.DataFrame): dataframe provenant du fichier csv
    Returns:
        pd.DataFrame: Le dataframe converti
    """
    Street_number = pd.DataFrame(columns=["Number"])
    Street_number = pd.concat([Street_number, data[["Number"]].drop_duplicates()])
    Street_number = Street_number.reset_index()
    Street_number = Street_number.rename(columns={"index": "ID_Street_Number"})
    Street_number.ID_Street_Number = Street_number.ID_Street_Number + 1
    return Street_number


def format_fk_job_title(data, job_title: pd.DataFrame):
    data_ID_job_title = pd.DataFrame(columns=["ID", "Job Title"])
    ID_job_title = data[["ID", "Job Title"]]
    data_ID_job_title = pd.concat([data_ID_job_title, ID_job_title])
    fk_job_title = data_ID_job_title
    fk_job_title = fk_job_title.merge(job_title)
    fk_job_title = fk_job_title.drop(columns=["Job Title"])
    fk_job_title = fk_job_title.sort_values(by=["ID"])
    return fk_job_title


def format_fk_state(data, state):
    data_ID_State = pd.DataFrame(columns=["ID", "State"])
    ID_State = data[["ID", "State"]]
    data_ID_State = pd.concat([data_ID_State, ID_State])
    fk_State = data_ID_State
    fk_State = fk_State.merge(state)
    fk_State = fk_State.drop(columns=["State"])
    fk_State = fk_State.sort_values(by=["ID"])

    return fk_State


def format_fk_city(data, city):
    data_ID_City = pd.DataFrame(columns=["ID", "City"])
    ID_City = data[["ID", "City"]]
    data_ID_City = pd.concat([data_ID_City, ID_City])
    fk_City = data_ID_City
    fk_City = fk_City.merge(city)
    fk_City = fk_City.drop(columns=["City"])
    fk_City = fk_City.sort_values(by=["ID"])

    return fk_City


def format_fk_street(data, street):
    data_ID_street = pd.DataFrame(columns=["ID", "Street"])
    ID_street = data[["ID", "Street"]]
    data_ID_street = pd.concat([data_ID_street, ID_street])
    fk_street = data_ID_street
    fk_street = fk_street.merge(street)
    fk_street = fk_street.drop(columns=["Street"])
    fk_street = fk_street.sort_values(by=["ID"])
    return fk_street


def format_fk_street_number(data, street_number):
    data_ID_street_number = pd.DataFrame(columns=["ID", "Number"])
    ID_street_number = data[["ID", "Number"]]
    data_ID_street_number = pd.concat([data_ID_street_number, ID_street_number])
    fk_street_number = data_ID_street_number
    fk_street_number = fk_street_number.merge(street_number)
    fk_street_number = fk_street_number.drop(columns=["Number"])
    fk_street_number = fk_street_number.sort_values(by=["ID"])
    return fk_street_number


def format_user(data, fk_job_title, fk_state, fk_city, fk_street, fk_street_number):
    user = data
    user = user.merge(fk_job_title)
    user = user.merge(fk_state)
    user = user.merge(fk_city)
    user = user.merge(fk_street)
    user = user.merge(fk_street_number)
    user = user.drop(columns=["Job Title", "State", "City", "Street", "Number"])
    return user
