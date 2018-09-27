
import numpy as np
import pandas as pd
from models import Transaction, Account, Category, Tag
from tabulate import tabulate

def table_print(data):
    return tabulate(data, headers='keys', tablefmt='psql', floatfmt=".2f")

def request_index(cls):
    """
    Function to request a index

    Arguments:
        cls -- Class to check a existing index
    """
    data= cls.model.load_table()
    index_list= data.iloc[:, 0]
    while True:
        
        print(table_print(data))
        index = request_int()
        if index in index_list:
            print("\n>>>> The selected record is: ", table_print(data.loc[[index], :]), sep="\n")
            return index
        else:
            print(">>>> ERROR: The selected index does not correspond to the table", sep="\n")
            

def request_int(message= "Select a correct index (Integer):", min_value = 0, max_value= + np.inf):
    while True:
        try:
            print(message)
            integer= int(input("\t>>> "))
            if(integer >= min_value and integer <= max_value):
                break
            else:
                print(">>>> ERROR: Insert a month between 1 and 12 (included)")
            
        except Exception:
            print(">>>> ERROR: Insert a valid Integer")

    return integer


def request_confirm(message = "Are you sure to continue the present action [Y/N]? "):
    print(message)
    count = 0
    while count < 3:
        selected_option = input("\t>>> ").upper().strip()
        
        if(selected_option == "Y"):
            return True
        elif(selected_option == "N"):
            return False
        else:
            print("You have to select a correct input ( Y | N ) ")
            count+=1

    return False

def request_string(field_name, allow_blank = False):
    print("Enter a correct value for {}".format(field_name))
    resultado = input("\t>>> ").strip()
    while(len(resultado) == 0 and not allow_blank):
        print("Enter the correct value for {}".format(field_name))
        resultado = input("\t>>> ").strip()
    return resultado

def request_float(field_name):
    print("Enter a correct amount (i.e. 516.21):")
    while True:
        try:
            initial_cash = float(input("\t>>> "))
            break
        except Exception:
            print("Enter a correct amount (i.e. 516.21):")
    return initial_cash

def request_coin(field_name):
    print("Default coin (will be used for initial Cash): ")
    default_coin = input("\t>>> ").upper().strip()
    while(not len(default_coin) == 3 and not default_coin.isalpha() ):
        print("Choose a coin in its ISO format (i.e EUR): ")
        default_coin = input("\t>>> ").upper()
    return default_coin

def request_date(field_name):
    year = request_int("Select a year of the transactions (Integer)")
    month = request_int("Select a month of the transactions (Integer)", min_value= 1, max_value=12)
    day = request_int("Select a day of the transactions (Integer)", min_value= 1, max_value=31)
    hour = request_int("Select a hour of the transactions (Integer)", min_value= 0, max_value=23)
    minute = request_int("Select a minute of the transactions (Integer)", min_value= 1, max_value=60)
        
    return pd.Timestamp(year=year, month=month, day=day, hour=hour, minute=minute)

def request_account(mesage= ""):
    UI = AccountUI
    return request_index(UI)

def request_category(mesage= ""):
    UI = CategoryUI
    return request_index(UI)

def request_tag_list(mesage= ""):
    UI = TagUI
    data= UI.model.load_table()
    data_index_list= data.iloc[:, 0]
    while True:
        print(table_print(data))
        try:

            index_list = request_string("Tag List (1,23,5)", allow_blank=True).split(",")
            if(request_confirm("Are you sure that you want to record this transaction without Tags [Y/N]?")):
                return ""

        except Exception:
            print(">>>> ERROR: The indexes must be in format 4,65,4,41,1 ", sep="\n")
            continue
        
        for index in index_list:
            index_in=True
            try:
                if(int(index) not in data_index_list):
                    index_in = False   
                    break         
            except Exception:
                print(">>>> ERROR: Indexes could not be converted to Integer ", sep="\n")
                break
        if(index_in):
            return ",".join(index_list)
        
            
                
            
                

def init_data():
    """
    Método para iniciar/resetear todos los ficheros
    """
    if(request_confirm(message = "Do you want to reset all the tables to the inital state [Y/N]?")):
        Account.init_table()
        Transaction.init_table()
        Category.init_table()
        Tag.init_table()
        print("-"*20,">>>  Todas las tablas han sido inicializadas", "-"*20, sep="\n")
    else:
        print("The tables initialization has been canceld")




console_requesters = {"string": request_string, 
                      "coin": request_coin, 
                      "float": request_float, 
                      "int": request_int, 
                      "date" : request_date,
                      "account": request_account,
                      "category": request_category,
                      "tag list": request_tag_list
                    }


class ConsoleUI():

    model= Tag
    fields = {"name": "string", "description": "string" }



    @classmethod
    def menu(cls):
        bucle = True
        while bucle:
            print(table_print(cls.model.load_table()))
            print("Choose your option: \n")
            for key in cls.options.keys():
                print(key.upper(), " -> ", cls.options[key.upper()][1], sep="", end="\n")
            option = input(">>> ").upper()
            
            try:
                if (len(option.strip()) != 0):    
                    bucle = cls.options[option][0](cls)
            except Exception as e:
                print(">>> ERROR: Error a la hora de coger el input del usuario")
                print(e)



    
    def new_object(cls):
        print("\n"*2, "-"*25, "Category creation has started", "-"*25, sep="\n", end="\n")
        lista_retorno = []
        for field in cls.fields.keys():
            lista_retorno.append(console_requesters[cls.fields[field]](field))

        new_object = cls.model(*lista_retorno)
        new_object.add_record()
        return True
        
    
    def modify_object(cls):
        index = request_index(cls)
        print("\n"*2, "-"*25, "Category modification has started", "-"*25, sep="\n", end="\n")
        lista_retorno = []
        for field in cls.fields.keys():
            lista_retorno.append(console_requesters[cls.fields[field]](field))

        new_object = cls.model(*lista_retorno)
        new_object.set_record(index)

        return True
    
    
    def delete_object(cls):
        index = request_index(cls)
        if(request_confirm("Are you sure that you want to delete the selected record [Y/N]?")):
            cls.model.delete_record(index)

        return True

    
    def goback(cls):
        return False
    
    new_object = new_object
    modify_object = modify_object 
    delete_object = delete_object
    goback = goback

    options = {"N" : [new_object, "Creation of a new  object"], 
               "M": [modify_object, "Modification of a existing object"], 
               "D":[delete_object, "Delte a existing object"], 
               "Q": [goback, "Exit"]
              }

#############################
#                           #
#  T R A N S A C T I O N S  #
#                           #
#############################
class TransactionUI(ConsoleUI):
    model = Transaction
    fields = {"category": "category", "tag list": "tag list", "name": "string", "description": "string", "date":"date", "amount":"float", "coin": "coin", "account": "account" }
    options = {"N" : [ConsoleUI.new_object, "Creation of a new  object"], 
               "M": [ConsoleUI.modify_object, "Modification of a existing object"], 
               "D":[ConsoleUI.delete_object, "Delte a existing object"], 
               "Q": [ConsoleUI.goback, "Exit"]
              }

#############################
#                           #
#      A C C O U N T S      #
#                           #
#############################   
class AccountUI(ConsoleUI):
    model = Account
    fields = {"name": "string", "description": "string", "default coin": "coin", "initial cash": "float" }
    options = {"N" : [ConsoleUI.new_object, "Creation of a new  object"], 
               "M": [ConsoleUI.modify_object, "Modification of a existing object"], 
               "D":[ConsoleUI.delete_object, "Delte a existing object"], 
               "Q": [ConsoleUI.goback, "Exit"]
              }

#############################
#                           #
#      C A T E G O R Y      #
#                           #
#############################
class CategoryUI(ConsoleUI):
    model = Category
    fields = {"name": "string", "description": "string" }
    options = {"N" : [ConsoleUI.new_object, "Creation of a new  object"], 
               "M": [ConsoleUI.modify_object, "Modification of a existing object"], 
               "D":[ConsoleUI.delete_object, "Delte a existing object"], 
               "Q": [ConsoleUI.goback, "Exit"]
              }

#############################
#                           #
#          T A G            #
#                           #
#############################
class TagUI(ConsoleUI):
    model = Tag
    fields = {"name": "string", "description": "string" }

    options = {"N" : [ConsoleUI.new_object, "Creation of a new  object"], 
            "M": [ConsoleUI.modify_object, "Modification of a existing object"], 
            "D":[ConsoleUI.delete_object, "Delte a existing object"], 
            "Q": [ConsoleUI.goback, "Exit"]
            }






def main():
    pass

if __name__ == '__main__':
    CategoryUI.menu()
    