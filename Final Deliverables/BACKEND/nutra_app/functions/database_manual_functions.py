import os,time
from django.http import HttpResponse
from datetime import datetime

from nutra.settings import BASE_DIR
from nutra_app.models import FoodNutrientConversionFactor


source_file = os.path.join(BASE_DIR,'files/downloads/DataFile/food.csv')
destination_file = os.path.join(BASE_DIR,'files/uploads/foods.csv')



def write_Food_data_csv(request):

    source_file = os.path.join(BASE_DIR,'files/downloads/DataFile/food.csv')
    destination_file = os.path.join(BASE_DIR,'files/uploads/foods.csv')

    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","fdc_id","food_class","data_type","description","food_category_id","publication_date","scientific_name","food_key","is_having_nutrient_id","created_at","updated_at","updated_by"\n'
            destination.write(header)
            max_size = 30000


            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    fdc_id = data[0][1:]
                    is_having_nutrient_id = 0
                    if FoodNutrientConversionFactor.objects.filter(fdc_id=fdc_id):
                        is_having_nutrient_id = 1 
                    if data[3] == '':
                        data[3] = 0
                    new_row = f'{count},{data[0][1:]},"",{data[1]},"{data[2]}",{data[3]},"{data[4][:-2]}","","","{is_having_nutrient_id}","{datetime.now()}","{datetime.now()}",""\n'
                    destination.write(new_row)
                    print(count)

                if count == max_size:
                    print(f'The max_size is increased from {max_size} to {max_size+30000}')
                    max_size += 30000 
                    time.sleep(20)

    return HttpResponse('Successfully written the data in csv format')





def write_FoodCalorieConversionFactor_data_csv(source_file,destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","food_nutrient_conversion_factor_id","protein_value","fat_value","carbohydrate_value","calories","created_at","updated_at","updated_by"\n'
            destination.write(header)

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    if data[1] == '':
                        data[1] = 0
                    if data[2] == '':
                        data[2] = 0
                    if data[3][:-2] == '':
                        data_new = 0
                        calorie = float(data[1])*4+float(data[2])*9+float(data_new)*4
                    else:
                        calorie = float(data[1])*4+float(data[2])*9+float(data[3][:-2])*4
                    new_row = f'"{count}","{data[0][1:]}","{data[1]}","{data[2]}","{data[3][:-2]}","{calorie:.2f}","{datetime.now()}","{datetime.now()}",""\n'
                    destination.write(new_row)
                    print(count)


    
def write_FoodCategory_data_csv(source_file,destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","code","description","created_at","updated_at","updated_by"\n'
            destination.write(header)

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    new_row = f'"{data[0][1:]}","{data[1]}","{data[2][:-2]}","{datetime.now()}","{datetime.now()}",""\n'
                    destination.write(new_row)


def update_FoodNutrientConversionFactor_data_csv(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","food_nutrient_conversion_factor_id","fdc_id","created_at","updated_at","updated_by"\n'
            print(header)
            destination.write(header)

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    new_row = f'"{count}","{data[0][1:]}","{data[1][:-2]}","{datetime.now()}","{datetime.now()}",""\n'
                    print(new_row)
                    destination.write(new_row)





def write_FoodProtienConversionFactor_data_csv(source_file,destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","food_nutrient_conversion_factor_id","value","created_at","updated_at","updated_by"\n'
            destination.write(header)

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    new_row = f'"{count}","{data[0][1:]}","{data[1][:-2]}","{datetime.now()}","{datetime.now()}",""\n'
                    destination.write(new_row)


def write_FoodUpdateLogEntry_data_csv(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","fdc_id","description","last_updated","created_at","updated_at","updated_by"\n'
            destination.write(header)
            max_size = 100000

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    new_row = f'"{count}","{data[0][1:]}","{data[1]}","{data[2][:-2]}","{datetime.now()}","{datetime.now()}",""\n'
                    print(count)
                    destination.write(new_row)
                
                if count == max_size:
                    print(f'max_size is increased form {count} to {count+100000}')
                    max_size += 100000
                    print('System going to sleep for 30 seconds')
                    time.sleep(30)


def update_MeasureUnit_data_csv(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","measure_unit_id","name","abbreviation","created_at","updated_at","updated_by"\n'
            destination.write(header)
            print(header)

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    new_row = f'"{count}","{data[0][1:]}","{data[1][:-2]}","","{datetime.now()}","{datetime.now()}",""\n'
                    print(new_row)
                    destination.write(new_row)


def update_Nutrient_data_csv(source_file, destination_file):
    with open(source_file,'r') as source:
        with open(destination_file,'w') as destination:
            header = '"id","nutrient_id","name","unit_name","nutrient_nbr","rank","created_at","updated_at","updated_by"\n'
            print(header)
            destination.write(header)

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    new_row = f'"{count}","{data[0][1:]}","{data[1]}","{data[2]}","{data[3]}","{data[4][:-2]}","{datetime.now()}","{datetime.now()}",""\n'
                    destination.write(new_row)
                    print(new_row)



def update_NutrientIncomingName_data_csv(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            header = '"id","nutrient_incoming_name_id","name","nutrient_id","created_at","updated_at","updated_by"\n'
            print(header)
            destination.write(header)

            for count,rows in enumerate(source):
                if count > 0:
                    data = rows.split('","')
                    new_row = f'"{count}","{data[0][1:]}","{data[1]}","{data[2][:-2]}","{datetime.now()}","{datetime.now()}",""\n'
                    destination.write(new_row)
                    print(new_row)





if __name__ == '__main__':
    source_file = 'files/downloads/DataFile/food_calorie_conversion_factor.csv'
    destination_file = 'files/uploads/food_calorie_conversion_factor.csv'
    write_FoodCalorieConversionFactor_data_csv(source_file,destination_file)
    source_file = 'files/downloads/DataFile/food_category.csv'
    destination_file = 'files/uploads/food_category.csv'
    write_FoodCategory_data_csv(source_file, destination_file)
    source_file = 'files/downloads/DataFile/food_nutrient_conversion_factor.csv'
    destination_file = 'files/uploads/food_nutrient_conversion_factor.csv'
    update_FoodNutrientConversionFactor_data_csv(source_file, destination_file)
    source_file = 'files/downloads/DataFile/food_protein_conversion_factor.csv'
    destination_file = 'files/uploads/food_protein_conversion_factor.csv'
    write_FoodProtienConversionFactor_data_csv(source_file, destination_file)
    source_file = 'files/downloads/DataFile/food_update_log_entry.csv'
    destination_file = 'files/uploads/food_update_log_entry.csv'
    write_FoodUpdateLogEntry_data_csv(source_file, destination_file)
    source_file = 'files/downloads/DataFile/measure_unit.csv'
    destination_file = 'files/uploads/measure_unit.csv'
    update_MeasureUnit_data_csv(source_file, destination_file)
    source_file = 'files/downloads/DataFile/nutrient.csv'
    destination_file = 'files/uploads/nutrient.csv'
    update_Nutrient_data_csv(source_file, destination_file)
    source_file = 'files/downloads/DataFile/nutrient_incoming_name.csv'
    destination_file = 'files/uploads/nutrient_incoming_name.csv'
    update_NutrientIncomingName_data_csv(source_file, destination_file)
