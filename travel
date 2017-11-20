import os
import osa

current_dir = os.path.dirname(os.path.abspath(__file__))
currencies = os.path.join(current_dir, os.path.abspath("currencies.txt"))

cl = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")


def parsing_file(file_path):
    travel_list = [s.strip().split(":") for s in open(file_path)]
    travel_dict = {}
    for l in travel_list:
        travel_dict[l[0]] = l[1].strip().split(" ")
    return travel_dict


def get_result_in_rub(currency_dict):
    result_in_rub_dict = {}
    for k, v in currency_dict.items():
        v = cl.service.ConvertToNum(fromCurrency= v[1], toCurrency="rub", amount=float(v[0]), rounding="true")
        result_in_rub_dict[k] = v
    return result_in_rub_dict


def get_average(target_dict, count):
    return round(sum(target_dict.values()), count)


def print_average_sum(file_name):
    print(get_average(get_result_in_rub(parsing_file(file_name)), 0))


print_average_sum(currencies)