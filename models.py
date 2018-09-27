import numpy as np
import pandas as pd
from dataInteraction import TransactionIO, AccountIO, CategoryIO, TagIO, FinanceTrackerIO
from tabulate import tabulate



class BaseModel():
    """
    Clase de la cual se derivan todas las demás con información de las columnas y la data I/O
    """
    dataIO = FinanceTrackerIO
    COLUMNS = []
    data = None

    
    @classmethod
    def init_table(cls): 
        cls.dataIO.init_table(pd.DataFrame(columns= cls.COLUMNS))
    
    @classmethod
    def load_table(cls):
        return cls.dataIO.load_table()

    
    def add_record(self):
        table_data = self.dataIO.load_table().append(self.data, sort = False, ignore_index=True)
        self.dataIO.save_table(table_data)
        return table_data

    def set_record(self, index):
        table_data = self.dataIO.load_table()
        table_data.loc[[index], :] = self.data.iloc[0, :].tolist()
        self.dataIO.save_table(table_data)

    @classmethod
    def delete_record(cls, index):   
        cls.dataIO.save_table(cls.dataIO.load_table().drop(index=index))

    

#############################
#                           #
#  T R A N S A C T I O N S  #
#                           #
#############################
class Transaction(BaseModel):
    dataIO = TransactionIO
    COLUMNS= [ "category_ID", "tag_list_ID", "name", "description ", "date", "date_inserted", "amount", "coin", "account_ID"]
    

    category_ID = 0
    tag_list_ID = 0
    name = ""
    description = ""
    date = pd.Timestamp.now() #PlaceHolder, no tiene porque ser la fecha actual 
    date_inserted = pd.Timestamp.now()
    amount = 0
    coin = ""
    account_ID = 0


    def __init__(self, category_ID, tag_list_ID, name, description, date, amount, coin, account_ID):
        self.category_ID = category_ID
        self.tag_list_ID = tag_list_ID
        self.name = name
        self.description = description
        self.date = date
        self.date_inserted = pd.Timestamp.now()
        self.amount = amount
        self.coin = coin
        self.account_ID = account_ID

        self.data = pd.DataFrame([[self.category_ID, self.tag_list_ID, self.name, self.description, self.date, self.date_inserted, self.amount, self.coin, self.account_ID]],
                                columns=self.COLUMNS
                                )

    
    
#############################
#                           #
#      A C C O U N T S      #
#                           #
#############################   
class Account(BaseModel):
    dataIO = AccountIO
    COLUMNS = ["name", "description", "initial_cash", "defaultCoin"]

    name = ""
    description = ""
    initial_cash = 0
    default_coin = ""

    def __init__(self, name, description, initial_cash, default_coin):
        self.name = name
        self.description = description
        self.initial_cash = initial_cash
        self.default_coin = default_coin

        self.data = pd.DataFrame([[self.name, self.description, self.initial_cash, self.default_coin]], columns= self.COLUMNS)

    




#############################
#                           #
#      C A T E G O R Y      #
#                           #
#############################
class Category(BaseModel):
    dataIO = CategoryIO
    COLUMNS = ["name", "description"]
   
    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.data = pd.DataFrame([[name, description]], columns=self.COLUMNS)

   
    

#############################
#                           #
#          T A G            #
#                           #
#############################
class Tag(BaseModel):
    dataIO = TagIO
    COLUMNS = ["name", "description"]

    name = ""
    description = ""

    def __init__(self, name, description):
        self.name = name
        self.description = description

        self.data = pd.DataFrame([[name, description]], columns=self.COLUMNS)


def main():
    pass

if __name__ == '__main__':
    main()