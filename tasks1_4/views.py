from django.shortcuts import redirect, render
from .models import MachineDir, IndustrialConsts, IndustrialTypes
from django.core import serializers
import json
from .calculation import *
# Create your views here.

def start_page(request):
    mass = request.GET.get('mass')
    ic_name = request.GET.get('ic_name') 
    industrial_form = serializers.serialize('json', IndustrialTypes.objects.all())
    try:
        if ic_name and mass:
            ind_type = serializers.serialize('json', IndustrialTypes.objects.filter(it_id=ic_name))
            form_data = serializers.serialize('json', IndustrialConsts.objects.select_related('industrial_type').filter(min_mass__lte=mass, max_mass__gt=mass, industrial_type=ic_name))
        else:
            form_data = {}
            return render(request, context={'ind_form': json.loads(industrial_form)}, template_name='start-page.html')
    except Exception as e:
        print(e)
        form_data = {}
        return render(request, context={'ind_form': json.loads(industrial_form)}, template_name='start-page.html')  
    data = serializers.serialize('json', MachineDir.objects.all())
    return render(request=request, context={
        'machines': json.loads(data), 
        'description': json.loads(form_data), 
        'params':{'mass': mass, 'ind_type': json.loads(ind_type)}}, template_name='start-page.html')


def result(request):
    operation_list = request.POST.getlist('operation_number') # номер операции
    machine_list = request.POST.getlist('machine') # станок
    item_time_list = request.POST.getlist('item_time') # ti штучное время
    year_program = request.POST.get('year_program') # Д годовая программа
    year_fond = 1970 # request.GET.get('year_fond') #Фг годовой фонд
    adjaency_coef = 2 # request.GET.get('adjaency_coef') # Коэф сменности см
    teor_koef = 0.95 # request.GET.get('teor_koef') # теоритический коэфициент K
    clone_request = request.POST.dict()
    clone_request.update({'year_fond':year_fond, 'adjaency_coef': adjaency_coef, 'teor_koef': teor_koef})
    need_equipment_by_oper = calculate_need_equipment(operation_list, item_time_list, 
    year_program, year_fond, adjaency_coef, teor_koef)

    
    updated_data = get_unique_numbers(machine_list)
    print(range(len(operation_list)))
    for i in range(len(operation_list)):
        append_value_in_dict(updated_data, machine_list[i], item_time_list[i])
    
    calculate_json_obj(updated_data, year_program, 
    year_fond, adjaency_coef, teor_koef) # рассчет Ci По всем моделям, с дубликатами

    calculate_koef(updated_data)
    result = check_result(updated_data)
    dt = to_datatable(updated_data)
    print(dt)
    print('\n\n\n\n\n\n', updated_data, '\n\n\n\n\n\n' , updated_data)
    return render(request, template_name='result.html', context={'calc_results':updated_data, 'result': result,
    'graph_data': dt, 'stored_data': dict(request.POST), 'range': range(len(operation_list)), 'const_data': [year_fond, adjaency_coef, teor_koef]})