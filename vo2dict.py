import xmltodict
from pprint import pprint
import json


def read_voevent(xml_content, is_file=False):
    """
    Converts a VOEvent XML string to a Python dictionary.

    Parameters:
        xml_content (str): The VOEvent XML data as a string.
        is_file (bool): If True, xml_content is a file path.

    Returns:
        dict: A Python dictionary representation of the VOEvent.
    """
    if is_file:
        with open(xml_content, "r") as f:
            xml_content = f.read()
    # Parse the XML content using xmltodict
    voevent_dict = xmltodict.parse(xml_content)
    return clean_voevent(voevent_dict)


def coerce(val):
    """
    Turn our string representation of a value into a Python object.
    Priority is given to int, then float, then bool, then str.
    If an object is not a string, it is returned as is.

    Parameters:
    val (str): The string representation of a value.

    Returns:
    val (int, float, bool, str, obj): The Python object representation of a value.
    """
    # If the value is not a string, return it as is
    if not isinstance(val, str):
        return val

    # Try to convert the value to an int, then a float, then a bool
    try:
        return int(val)
    except:
        try:
            return float(val)
        except:
            if val.strip().lower() == "true":
                return True
            elif val.strip().lower() == "false":
                return False
            else:
                return val


def noat(val):
    """
    Remove the '@' symbol from a string if it exists.
    """
    if val.startswith("@"):
        return val[1:]
    return val


def clean_voevent(voevent):
    if "voe:VOEvent" in voevent:
        k = "voe:VOEvent"
    else:
        k = "VOEvent"
    return clean_dict(voevent[k])


def clean_dict(dirty):
    """
    Unpack a dict made by xlmtodict into a more readable format. This will
    remove all the @name and @value keys and replace them with the actual names
    and values.
    """
    new = dict()
    for k, v in dirty.items():
        name = noat(k)
        if name == "Param":
            new.update(group_params(v))
        elif name == "Group":
            new.update(group_groups(v))
        elif isinstance(v, dict):
            new[name] = clean_dict(v)
        elif isinstance(v, list):
            new[name] = clean_list(v)
        else:
            new[name] = coerce(v)
    return new


def clean_list(dirty):
    new = []
    for item in dirty:
        if isinstance(item, dict):
            new.append(clean_dict(item))
        elif isinstance(item, list):
            new.append(clean_list(item))
        else:
            new.append(coerce(item))
    return new


def group_params(params):
    new = dict()
    if not isinstance(params, list):
        params = [params]
    for p in params:
        name = p["@name"]
        new[name] = coerce(p["@value"])
        for k, v in p.items():
            if k not in ["@name", "@value"]:
                new[name + f"_{noat(k)}"] = coerce(v)
    return new


def group_groups(groups):
    new = dict()
    for p in groups:
        name = p["@name"]
        new[name] = group_params(p["Param"])
    return new


def test_SWIFT():
    fname = "notebooks/data/SWIFT_BAT_Lightcurve_new.xml"
    event = read_voevent(fname, is_file=True)
    pprint(event)
    return


def test_LVC():
    fname = "notebooks/data/LVC_real_preliminary_new.xml"
    event = read_voevent(fname, is_file=True)
    pprint(event)
    return


def test_all():
    from glob import glob

    print("file | result | note ")
    for fname in glob("output/*.xml"):
        try:
            if "classic" in fname:
                read_voevent(fname, is_file=True)
            else:
                with open(fname, "r") as f:
                    json.loads(f.read())
        except Exception as e:
            print(f"{fname} | fail | {e}")
        else:
            print(f"{fname} | pass | ")


if __name__ == "__main__":
    test_all()
