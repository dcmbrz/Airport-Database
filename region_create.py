def RegionCode(event, connection) -> list:
    """This function returns a list of all columns in a row of values
    given an inputted region's region code."""

    Code = connection.execute(f"SELECT * FROM region WHERE region_code = '{event.region_code()}'")
    region_code = Code.fetchall()
    return region_code
def RegionLocalCode(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
        given an inputted region's local code."""

    LocalCode = connection.execute(f"SELECT * FROM region WHERE local_code = '{event.local_code()}'")
    local_code = LocalCode.fetchall()
    return local_code

def RegionName(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
        given an inputted region's name."""

    Name = connection.execute(f"SELECT * FROM region WHERE name = '{event.region_code()}'")
    Name = Name.fetchall()
    return Name

def RegionAndLocalCode(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted region's region and local code."""

    RegionAndLocal = connection.execute(f"SELECT * FROM region WHERE region_code = '{event.region_code()}' AND local_code = '{event.local_code()}'")
    Code = RegionAndLocal.fetchall()
    return Code

def RegionCodeAndName(event, connection) -> list: #start*****
    """Function that returns a list of all columns in a row of values
            given an inputted region's name and region code."""

    R_CodeAndName = connection.execute(f"SELECT * FROM region WHERE name = '{event.name()}' AND region_code = '{event.region_code()}'")
    CodeAndName = R_CodeAndName.fetchall()
    return CodeAndName

def RegionNameAndLocalCode(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted region's name and local code."""

    LocalCodeAndName = connection.execute(f"SELECT * FROM region WHERE name = '{event.name()}' AND local_code = '{event.region_code()}'")
    LocalAndName = LocalCodeAndName.fetchall()
    return LocalAndName

def ThreeRegions(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted region's name, region code, and local code."""

    GivenThree = connection.execute(f"SELECT * FROM region WHERE region_code = '{event.region_code()}' AND local_code = '{event.local_code()}' AND name = '{event.name()}'")
    Three = GivenThree.fetchall()
    return Three

def RegionList(event, connection) -> list:
    """Function that returns a list of all columns in a row of values
            given an inputted region's id."""

    region_ids = connection.execute(f"SELECT * FROM region WHERE region_id = '{event.region_id()}'")
    row = region_ids.fetchall()
    return row

def RegionCodes(connection) -> list:
    """Function that returns a list of all the region codes in the region database."""

    region_codes = connection.execute(f"SELECT region_code FROM region")
    Region_Codes = region_codes.fetchall()
    c = [country for Co in Region_Codes for country in Co]
    return c

def StartRegionSearch(event, data):
    """Function that checks the given input and returns a list of the
    columns of a row of values given certain inputs."""

    if event.name() is None and (event.local_code() is None):
        continent = RegionCode(event, data)
        return continent
    elif event.name() is None and (event.region_code() is None):
        continent = RegionLocalCode(event, data)
        return continent
    elif event.local_code() is None and (event.region_code() is None):
        continent = RegionName(event, data)
        return continent
    elif event.name() is None:
        continent = RegionAndLocalCode(event, data)
        return continent
    elif event.local_code() is None:
        continent = RegionCodeAndName(event, data)
        return continent
    elif event.region_code() is None:
        continent = RegionNameAndLocalCode(event, data)
        return continent
    else:
        continent = ThreeRegions(event, data)
        return continent

def LoadRegion(event, data):
    """Function that returns a list of all columns in a row of values
            given an inputted region's id."""
    return RegionList(event, data)

def SaveNewRegion(event, data):
    """Function that checks the given inputs of A newly created region and
    creates a new region id for every new country and returns a list of all
    inputted values and its id."""

    if event.region().region_code in RegionCodes(data):
        x = "This code is already in the database"
        return x
    elif type(event.region().region_code) != str:
        x = "This code is not a string"
        return x
    elif event.region().local_code == "":
        x = "Enter a region Code"
        return x
    elif type(event.region().local_code) != str:
        x = "This code is not a string"
        return x
    elif event.region().name == "":
        x = "Enter a name"
        return x
    elif type(event.region().name) != str:
        x = "Must be string"
        return x

    elif event.region().continent_id is None:
        x = "Enter an id"
        return x
    elif type(event.region().continent_id) != int:
        x = "continent id must be an integer"
        return x

    elif type(event.region().country_id) != int:
        x = "country id must be an integer"
        return x

    elif event.region().country_id is None:
        x = "enter an id"
        return x

    elif event.region().wikipedia_link is not None and type(event.region().wikipedia_link) != str:
        x = "link must be a string"
        return x

    elif event.region().keywords is not None and type(event.region().keywords) != str:
        x = "must be a string"
        return x

    else:
        region_id = 0
        ids = data.execute(f"SELECT region_id FROM region")
        Ids = ids.fetchall()
        i = [i_d for Id in Ids for i_d in Id]
        for n in i:
            if region_id in i:
                region_id = n
                region_id += 1
        return[region_id,event.region().region_code,event.region().local_code,event.region().name,event.region().continent_id,event.region().country_id, event.region().wikipedia_link,event.region().keywords]

def SaveRegion(event, data):
    """Function that checks the given inputs of An edited created region and
        updates the region given the new inputs. If there are no changes the
        region stays the same."""

    region_ids = data.execute(f"SELECT * FROM region WHERE region_id = '{event.region().region_id}'")
    row = region_ids.fetchall()
    if row[0][1] != event.region().region_code:
        if event.region().region_code in RegionCodes(data):
            x = "This code is already in the database"
            return x
    elif type(event.region().region_code) != str:
        x = "This code is not a string"
        return x
    elif event.region().local_code == "":
        x = "Enter a region Code"
        return x
    elif type(event.region().local_code) != str:
        x = "This code is not a string"
        return x
    elif event.region().name == "":
        x = "Enter a name"
        return x
    elif type(event.region().name) != str:
        x = "Must be string"
        return x

    elif event.region().continent_id is None:
        x = "Enter an id"
        return x
    elif type(event.region().continent_id) != int:
        x = "continent id must be an integer"
        return x

    elif type(event.region().country_id) != int:
        x = "country id must be an integer"
        return x

    elif event.region().country_id is None:
        x = "enter an id"
        return x

    elif event.region().wikipedia_link is not None and type(event.region().wikipedia_link) != str:
        x = "link must be a string"
        return x

    elif event.region().keywords is not None and type(event.region().keywords) != str:
        x = "must be a string"
        return x

    else:
        return [event.region().region_id, event.region().region_code,event.region().local_code,event.region().name,event.region().continent_id,event.region().country_id, event.region().wikipedia_link,event.region().keywords]