import os
import osa

cl = osa.Client("http://www.webservicex.net/ConvertTemperature.asmx?WSDL")

current_dir = os.path.dirname(os.path.abspath(__file__))
temps = os.path.join(current_dir, os.path.abspath("temps.txt"))
travel = os.path.join(current_dir, os.path.abspath("travel.txt"))


def parsing_temps(file_path):
    temps_list = [s.strip().split(" ") for s in open(file_path)]

    temps_dict = {}
    for l in temps_list:
        temps_dict[l[0]] = l[1]
    return temps_dict


def average_temp(temp_dict):
    result_list = []
    for k, v in temp_dict.items():
        if v == "F":
            result_list.append(int(cl.service.ConvertTemp(Temperature=k, FromUnit="degreeFahrenheit", ToUnit="degreeCelsius")))
        elif v == "C":
            result_list.append(
                int(cl.service.ConvertTemp(Temperature=k, FromUnit="degreeCelsius", ToUnit="degreeFahrenheit")))

    return sum(result_list)/len(result_list)


def print_aver_temp(file_path):
    print(average_temp(parsing_temps(file_path)))

print_aver_temp(temps)