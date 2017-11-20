import os
import osa
from currencies import get_average, parsing_file


current_dir = os.path.dirname(os.path.abspath(__file__))
travel= os.path.join(current_dir, os.path.abspath("travel.txt"))

cl = osa.Client("http://www.webservicex.net/length.asmx?WSDL")


def get_result_in_km(miles_dict):
    result_in_km_dict = {}
    for k, v in miles_dict.items():
        if v[1] == "mi":
            v = cl.service.ChangeLengthUnit(LengthValue=float(v[0].replace(',','')), fromLengthUnit="Miles", toLengthUnit="Kilometers")
            result_in_km_dict[k] = v
    return result_in_km_dict


def print_average_sum(file_name):
    print(get_average(get_result_in_km(parsing_file(file_name)), 2))


print_average_sum(travel)


