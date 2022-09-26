# file_path = 'gedcom.ged'
from gedcom.element.individual import IndividualElement
from gedcom.element.family import FamilyElement
from gedcom.parser import Parser
from prettytable import PrettyTable
x = PrettyTable()
y = PrettyTable()
# filep = input("enter gedcom file path: ")
filep = "gedcom.ged"
gedcom_parser = Parser()
gedcom_parser.parse_file(filep)
root_child_elements = gedcom_parser.get_root_child_elements()
x.field_names = ["ID","Name", "Gender", "Birth date", "Alive", "Death", "Child", "Spouse"]
for element in root_child_elements:
    if isinstance(element, IndividualElement):
        print(element.get_individual())
        death = "NA" if element.get_death_data()[0]=="" else element.get_death_data()[0]
        Alive = True if death == False else False
        x.add_row([element.get_pointer(), element.get_name(), element.get_gender(), element.get_birth_data()[0],Alive, death, element.get_child_elements(), "ahh"])
print(x)
y.field_names = ["ID","Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
for element in root_child_elements:
    if isinstance(element, FamilyElement):
            print(element.get_individual())
# print(y)

# filecontent = []
# taglist = [
#     "INDI",
#     "NAME",# 1 name is supported 
#     "SEX",
#     "BIRT",
#     "DEAT",
#     "FAMC",
#     "FAMS",
#     "FAM",
#     "MARR",
#     "HUSB",
#     "WIFE",
#     "CHILL",
#     "DIV",
#     "DATE",# 2 date is supported
#     "NOTE"
# ]
# famlist = []
# indilist = []
# with open(filep, "r") as geddy: 
#     line = geddy.readline()
#     while(line!=""):
#         filecontent.append(line)
#         line = geddy.readline()
# for i in filecontent:
#     valid = "N"
#     level = ""
#     tag = ""
#     arg = ""
#     print("--> "+i)
#     parts = i.split(" ")
#     if(parts[1]=="HEAD\n"):
#         # parts[1]==parts[:len(parts[1])-2]
    
#         valid = "Y"
#         level = parts[0]
#         tag = parts[1].strip('\n')
#         print("<-- "+level+"|"+tag+"|"+valid +"\n")
#     else:
#         if(parts[1] in taglist):
#             if((parts[1]=="DATE" and parts[0]=="1") or (parts[1]=="NAME" and parts[0]=="2")):
#                 print("invalid, we dont support #2 NAME or #1 DATE\n")
#             else:
#                 valid = "Y"
#                 level = parts[0]
#                 tag = parts[1]
#                 arg =" ".join(parts[2:])
#                 #parts[-1] = parts[1:-1]
#                 print("<-- "+level+"|"+tag+"|"+valid+"|"+arg)

#             # cdoe 
#         elif(len(parts) > 2):
#             if(parts[2]=="INDI" or parts[2]=="FAM"):
#                 valid = "Y"
#                 level = parts[0]
#                 tag = parts[2]
#                 arg = parts[1]
#                 #parts[-1] = parts[1:-1]
#                 # print("<--"+" ".join(parts[2:]))
#                 print("<-- "+level+"|"+tag+"|"+valid+"|"+arg)
#                 #code
            
#             else: 
#                 valid = "N"
#                 level = parts[0]
#                 tag = parts[1]
#                 arg = " ".join(parts[2:])
#                 #parts[-1] = parts[1:-1]
#                 print("<-- "+level+"|"+tag+"|"+valid+"|"+arg)
#         else:
#             valid = "N"
            
#             # parts[1]==parts[:len(parts[1])-2]
#             # print(parts[1])
#             level = parts[0]
#             tag = parts[1].strip('\n')
#             print("<-- "+level+"|"+tag+"|"+valid+"\n")

# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
