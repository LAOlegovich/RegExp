from pprint import pprint

import csv,os, pandas,re


def input_data(file_name):
  with open(os.path.join(os.getcwd(),file_name), encoding= 'utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    return list(rows)

def parsing_data(contacts_list):
  pattern_fio = re.compile("[а-яёА-ЯЁ]+")
  pattern_phone = r"(\+7|8)?[\s-]*[\(]*(\d{3})[\)]*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*[(]?(доб\.)*\s*(\d*)[)]?"
  pattern_sub_phone = r"+7(\2)\3-\4-\5 \6\7"
  no_conflict_list = {}
  for id,val in enumerate(contacts_list):
    if id == 0 : 
      no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]] = contacts_list[id]
    find_str = val[0] +' '+ val[1] + ' ' + val[2]
    mass = pattern_fio.findall(find_str)
    len_mass = len(mass)
    contacts_list[id][0:len_mass] = mass
    contacts_list[id][5] = re.sub(pattern_phone,pattern_sub_phone, val[5]).rstrip()
    if contacts_list[id][0]+' '+contacts_list[id][1] not in no_conflict_list:
      no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]] = contacts_list[id]
    else:
      if no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][2] == "":
        no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][2] += contacts_list[id][2]
      if no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][3] == "":
        no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][3] += contacts_list[id][3]
      if no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][4] == "":
        no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][4] += contacts_list[id][4]  
      if no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][5] == "":
        no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][5] += contacts_list[id][5] 
      if no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][6] == "":
        no_conflict_list[contacts_list[id][0]+' '+contacts_list[id][1]][6] += contacts_list[id][6]                                                                   
  return [val for val in no_conflict_list.values()]

def save_data_to_file(contacts_list,file_name):
  with open(os.path.join(os.getcwd(),file_name), "w", encoding= 'utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)

def testing_data_for_correct(enter_list):
  header_len = len(enter_list[0])
  numb_of_err_strs = [] 
  for i in range(1, len(enter_list)):
    if len(enter_list[i]) != header_len:
       numb_of_err_strs += [i]
  try:
    if len(numb_of_err_strs) != 0:
      raise Exception(f"Ошибка! Несоответствие формата данных в строках: {numb_of_err_strs}")
  except Exception as e:
    print(str(e))
    exit()
  
    
if __name__ == "__main__":
  contacts_list = input_data("phonebook_raw.csv")
  # Добавлена процедура тестирования файла на соответствие заданному формату данных,
  # в случае обнаружения несоответствия - выводятся номера строк, которые оператор
  # должен самостоятельно проанализировать, т.к. нарушения могут быть различными
  testing_data_for_correct(contacts_list)
  print(pandas.read_csv(os.path.join(os.getcwd(),"phonebook_raw.csv")))
  save_data_to_file(parsing_data(contacts_list), "phonebook.csv")
  print('After program worked')
  print(pandas.read_csv(os.path.join(os.getcwd(),"phonebook.csv")))







  