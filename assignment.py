# file_path = 'gedcom.ged'
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from gedcom.element.individual import IndividualElement
from gedcom.element.family import FamilyElement
from gedcom.parser import Parser
from prettytable import PrettyTable
from prettytable import MSWORD_FRIENDLY
from prettytable import DOUBLE_BORDER
x = PrettyTable()
y = PrettyTable()
filep = input("enter gedcom file path: ")
# filep = "gedcom.ged"
gedcom_parser = Parser()
gedcom_parser.parse_file(filep)
root_child_elements = gedcom_parser.get_root_child_elements()
x.field_names = ["ID","Name", "Gender", "Birth date", "Alive", "Death", "Child", "Spouse"]
mapall = {}
for element in root_child_elements:
    
    if isinstance(element, IndividualElement):
        # print(element.get_individual())
        # spouses = 
        Children = ""
        spouseid = ""
        family = str(element.get_individual()).split("\n")
        for i in family:
            familyparts = i.split(" ")
            # print(familyparts)
            if("FAMS" in familyparts):
                spouseid = familyparts[2].strip('\r') if familyparts[2] != " " else ""
            elif("FAMC" in familyparts):
                Children = familyparts[2].strip('\r') if familyparts[2] != " " else ""
        death = "NA" if element.get_death_data()[0]=="" else element.get_death_data()[0]
        Alive = True if death == "NA" else False
        chi = Children if Children!="" else "NA"
        sp = spouseid if spouseid != "" else "NA"
        mapall[element.get_pointer()] = element.get_name()[0]+" "+element.get_name()[1]
        x.add_row([element.get_pointer(), element.get_name()[0]+" "+element.get_name()[1], element.get_gender(), element.get_birth_data()[0],Alive, death,chi, spouseid])
# print(mapall['@I6000000187342139825@'])
x.set_style(DOUBLE_BORDER)
print(x.get_string())
y.field_names = ["FAM ID","Married","Divorced","Husband ID","Husband Name", "Wife ID",  "Wife Name","Children",]
for element in root_child_elements:
    if isinstance(element, FamilyElement):
        Husbandid = ""      
        Wifeid = "" 
        Children = []
        point = element.get_pointer() 
        family = str(element.get_individual()).split("\n")
        for i in family:
            familyparts = i.split(" ")
            # print(familyparts)
            if("HUSB" in familyparts):
                Husbandid = familyparts[2].strip('\r')
            elif("WIFE" in familyparts):
                Wifeid = familyparts[2].strip('\r')
            elif("CHIL" in familyparts):
                Children.append(familyparts[2].strip('\r'))
        # print(mapall[Husbandid.strip('\r')])
        y.add_row([point," "," ",Husbandid,mapall[Husbandid.strip('\r')],Wifeid, mapall[Wifeid.strip('\r')], Children])
print(y)