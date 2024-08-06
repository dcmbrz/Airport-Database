def ContinentCode(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted continent code."""

    Con_Code = connection.execute(f"SELECT * FROM continent WHERE continent_code = '{event.continent_code()}'")
    Code = Con_Code.fetchall()
    return Code

def ContinentName(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted continent name."""

    Con_Name = connection.execute(f"SELECT * FROM continent WHERE name = '{event.name()}'")
    Name = Con_Name.fetchall()
    return Name

def ContinentNameAndCode(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted continent name and code."""

    Given_Both = connection.execute( f"SELECT * FROM continent WHERE continent_code = '{event.continent_code()}' AND name = '{event.name()}'")
    Both = Given_Both.fetchall()
    return Both

def ListOfContinents(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
                   given an inputted continent's id."""

    continent_ids = connection.execute(f"SELECT * FROM continent WHERE continent_id = '{event.continent_id()}'")
    row = continent_ids.fetchall()
    return row

def ContinentCodes(connection) -> list:
    """Function that returns a list of all the continent codes in the continent database."""

    con_codes = connection.execute(f"SELECT continent_code FROM continent")
    Codes = con_codes.fetchall()
    c = [co for Co in Codes for co in Co]
    return c

def StartContinentSearch(event, data) -> list:
    """Function that checks the given input and returns a list of the
            columns of a row of values given certain inputs."""

    if event.continent_code() is None:
        continent = ContinentName(event, data)
        return continent
    elif event.name() is None:
        continent = ContinentCode(event, data)
        return continent
    else:
        continent = ContinentNameAndCode(event, data)
        return continent

def LoadContinent(event, data) -> list:
    """Function that returns a list of all columns in a row of values
                    given an inputted continent's id."""

    return ListOfContinents(event, data)

def SaveNewContinent(event, data) -> list:
    """Function that checks the given inputs of A newly created continent and
            creates a new continent id for every new country the returns a list of all
            inputted values and its id."""

    if event.continent().continent_code in ContinentCodes(data):
        x = "This code is already in the database"
        return x
    elif type(event.continent().continent_code) != str:
        x = "This code is not a string"
        return x
    elif event.continent().continent_code == "":
        x = "Enter a Continent Code"
        return x
    elif type(event.continent().name) != str:
        x = "This name is not a string"
        return x
    elif event.continent().name == "":
        x = "Enter a Continent Name"
        return x
    else:
        unique_id = 1
        ids = data.execute(f"SELECT continent_id FROM continent")
        Ids = ids.fetchall()
        i = [i_d for Id in Ids for i_d in Id]
        for n in i:
            if unique_id in i:
                unique_id += 1
        return [unique_id, event.continent().continent_code, event.continent().name]

def SaveContinent(event, data):
    """Function that checks the given inputs of An edited created continent and
                updates the continent given the new inputs. If there are no changes the
                continent stays the same."""

    continent_ids = data.execute(f"SELECT * FROM continent WHERE continent_id = '{event.continent().continent_id}'")
    row = continent_ids.fetchall()
    if row[0][1] != event.continent().continent_code:
        if event.continent().continent_code in ContinentCodes(data):
            x = "This code is already in the database"
            return x
    elif type(event.continent().continent_code) != str:
        x = "This code is not a string"
        return x
    elif event.continent().continent_code == "":
        x = "Enter a Continent Code"
        return x
    elif type(event.continent().name) != str:
        x = "This name is not a string"
        return x
    elif event.continent().name == "":
        x = "Enter a Continent Name"
        return x
    else:
        return [event.continent().continent_id, event.continent().continent_code, event.continent().name]
