import json

from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


def write_to_json(path: str, records: list[dict]):
    """
    Writes list of dictionaries to json
    :param path: Path to a file
    :param records: List of dictionaries
    :return:
    """
    print(path)
    with open(path, "w") as output_file:
        print(json.dumps(records, indent=4), file=output_file)


def write_to_xml(path: str, records: list[dict]):
    """
    Writes list of dictionaries to xml
    :param path: Path to a file
    :param records: List of dictionaries
    :return:
    """
    with open(path, "w") as output_file:
        print(_parse_list_of_dict_to_xml(records), file=output_file)


def _parse_list_of_dict_to_xml(records: list[dict]):
    """
    Transforms list of dictionaries to xml
    :param records: List of dictionaries
    :return: xml str
    """
    xml_list = []
    for record in records:
        xml_list.append(dicttoxml(record, root=False, attr_type=False))

    xml = '<?xml version="1.0" encoding="UTF-8" ?> <root>'
    for record in xml_list:
        xml += '<item>' + record.decode('utf-8') + '</item>'
    xml += '</root>'

    return parseString(xml).toprettyxml()
