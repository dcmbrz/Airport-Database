def ContinentIds(connection) -> list:
    """Function that returns a list of continent ids from the continent
    database."""

    ids = connection.execute(f"SELECT continent_id FROM continent")
    Ids = ids.fetchall()
    n = [na for Na in Ids for na in Na]
    return n

def CountryCode(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
        given an inputted country code."""

    Country_Code = connection.execute(f"SELECT * FROM country WHERE country_code = '{event.country_code()}'")
    Code = Country_Code.fetchall()
    return Code


def CountryName(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted country's name."""

    Country_Name = connection.execute(f"SELECT * FROM country WHERE name = '{event.name()}'")
    Name = Country_Name.fetchall()
    return Name


def CountryNameAndCode(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted region's name and country code."""

    Name_and_Code = connection.execute(f"SELECT * FROM country WHERE country_code = '{event.country_code()}' AND name = '{event.name()}'")
    Both = Name_and_Code.fetchall()
    return Both


def ListOfCountries(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
               given an inputted country's id."""

    country_ids = connection.execute( f"SELECT * FROM country WHERE country_id = '{event.country_id()}'")
    row = country_ids.fetchall()
    return row


def CountryCodes(connection) -> list:
    """Function that returns a list of all the country codes in the country database."""

    country_codes = connection.execute(f"SELECT country_code FROM country")
    Country_Codes = country_codes.fetchall()
    c = [country for Co in Country_Codes for country in Co]
    return c


def StartCountrySearch(event, data) -> list:
    """Function that checks the given input and returns a list of the
        columns of a row of values given certain inputs."""

    if event.country_code() is None:
        country = CountryName(event, data)
        return country
    elif event.name() is None:
        country = CountryCode(event, data)
        return country
    else:
        country = CountryNameAndCode(event, data)
        return country


def LoadCountry(event, data) -> list:
    """Function that returns a list of all columns in a row of values
                given an inputted country's id."""

    return ListOfCountries(event, data)


def SaveNewCountry(event, data):
    """Function that checks the given inputs of A newly created country and
        creates a new country id for every new country the returns a list of all
        inputted values and its id."""

    if event.country().country_code in CountryCodes(data):
        x = "This code is already in the database"
        return x

    elif type(event.country().country_code) != str:
        x = "Must be string"
        return x

    elif event.country().country_code == "":
        x = "Enter a country code"
        return x

    elif type(event.country().name) != str:
        x = "Must be string"
        return x

    elif event.country().name == "":
        x = "Enter a country name"
        return x

    elif event.country().continent_id is None:
        x = "id can not be null"
        return x

    elif type(event.country().continent_id) != int:
        x = "continent id must be an integer"
        return x

    elif event.country().continent_id not in ContinentIds(data):
        x = "continent does not exist"
        return x

    elif event.country().wikipedia_link == "":
        x = "Enter a link"
        return x

    elif type(event.country().wikipedia_link) != str:
        x = "Enter a valid link"
        return x

    elif event.country().keywords is not None and (type(event.country().keywords) != str):
        x = "Enter a valid keyword"
        return x

    else:
        country_id = 0
        ids = data.execute(f"SELECT country_id FROM country")
        Ids = ids.fetchall()
        i = [i_d for Id in Ids for i_d in Id]
        for n in i:
            if country_id in i:
                country_id = n
                country_id += 1
        return [country_id, event.country().country_code, event.country().name, event.country().continent_id, event.country().wikipedia_link, event.country().keywords]

def SaveCountry(event, data):
    """Function that checks the given inputs of An edited created country and
            updates the country given the new inputs. If there are no changes the
            country stays the same."""

    region_ids = data.execute(f"SELECT * FROM country WHERE country_id = '{event.country().country_id}'")
    row = region_ids.fetchall()
    if row[0][1] != event.country().country_code:
        if event.country().country_code in CountryCodes(data):
            x = "This code is already in the database"
            return x

    elif type(event.country().country_code) != str:
        x = "Must be string"
        return x

    elif event.country().country_code == "":
        x = "Enter a country code"
        return x

    elif type(event.country().name) != str:
        x = "Must be string"
        return x

    elif event.country().name == "":
        x = "Enter a country name"
        return x

    elif event.country().continent_id is None:
        x = "id can not be null"
        return x

    elif type(event.country().continent_id) != int:
        x = "continent id must be an integer"
        return x

    elif event.country().continent_id not in ContinentIds(data):
        x = "continent does not exist"
        return x

    elif event.country().wikipedia_link == "":
        x = "Enter a link"
        return x

    elif type(event.country().wikipedia_link) != str:
        x = "Enter a valid link"
        return x

    elif event.country().keywords is not None and (type(event.country().keywords) != str):
        x = "Enter a valid keyword"
        return x

    else:
        return [event.country().country_id, event.country().country_code, event.country().name, event.country().continent_id, event.country().wikipedia_link, event.country().keywords]