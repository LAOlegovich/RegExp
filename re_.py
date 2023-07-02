from pprint import pprint

import csv,os, pandas,re

with open(os.getcwd()+"\phonebook_raw.csv", encoding= 'utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
print(pandas.read_csv(os.getcwd()+"\phonebook_raw.csv"))
pattern_fio = re.compile("[а-яёА-ЯЁ]+")
pattern_phone = r"(\+7|8)?[\s-]*[\(]*(\d{3})[\)]*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*[(]?(доб\.)*\s*(\d*)[)]?"
pattern_sub_phone = r"+7(\2)\3-\4-\5 \6\7"
no_conflict_list = {}
for id,val in enumerate(contacts_list):
  if id == 0 : continue
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

return_list = [val for val in no_conflict_list.values()]
with open("phonebook.csv", "w", encoding= 'utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  
  datawriter.writerows(return_list)








  