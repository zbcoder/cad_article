from math import ceil
import json

def calculate_need_equipment(op_list, item_time, year_prog,
year_fond, adjaency_coef, teor_koef):
    need_equipment = []
    for i in range(len(op_list)):
        Ci_real = (float(item_time[i])*float(year_prog))/(60*float(adjaency_coef)*float(year_fond)*float(teor_koef))
        Ci_info = {}
        Ci_info.update({'practice': Ci_real, 'approximate': ceil(Ci_real)})
        need_equipment.append(Ci_info)
    return need_equipment


def calculate_json_obj(machine_dict, year_prog, year_fond, adjaency_coef, teor_koef):
    for machine in machine_dict:
        time_sum = sum(machine['time_values'])
        Ci_info = {}
        Ci_real = ((time_sum)*float(year_prog))/(60*float(adjaency_coef)*float(year_fond)*float(teor_koef))
        Ci_info.update({'practice': Ci_real, 'approximate': ceil(Ci_real)})
        machine.update({'Ci': Ci_info})

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    json_structure={}
    unique_numbers = set(numbers)

    for number in unique_numbers:
        json_structure = {'machine': number, 'time_values':[]}
        list_of_unique_numbers.append(json_structure)
    return list_of_unique_numbers

def append_value_in_dict(list, key, value):
    for json_struct in list:
        if(json_struct.get('machine') == key):
            json_struct['time_values'].append(float(value))
        #json_struct[key]['values'].append(value)


def calculate_koef(dict):
    counter = 0
    for elem in dict:
        koef = float(elem['Ci']['practice'])/float(elem['Ci']['approximate'])
        if koef>0.9:
            message = 'Корректировка ТП не требуется'
            koef_struct = {'Kload': koef, 'message': {'text': message,'color':'#7AE969'}, 'result': True}
        if koef<0.9:
            message = 'Требуется корректировка! Пожалуйста измените параметр Д или метод резания'
            koef_struct = {'Kload': koef,'message':{'text': message,'color':'#FC717B'}, 'result': False}
        elem.update(koef_struct) 


def check_result(dict):
    count = 0
    for elem in dict:
        if elem['result']==False:
            count += 1
        else:
            continue
    print(count)
    if count > 0:
        return False
    else: return True


def to_datatable(dict):
    lst = [['Модель', 'Значение']]
    for elem in dict:
        temp_list = []
        temp_list.append(elem['machine'])
        temp_list.append(elem['Kload'])
        print(temp_list)
        lst.append(temp_list)
    return lst