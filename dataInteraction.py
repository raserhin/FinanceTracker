import numpy as np 
import pandas as pd


class FinanceTrackerIO:
    path = ".\\"
    table=""
    extension = ".csv"

    categories = "categories"
    tags = "tags"
    

    @classmethod
    def init_table(cls, data):
        # print(">>>>    Initialize "+ cls.table + cls.extension)
        data.to_csv(cls.path 
                    + cls.table 
                    + cls.extension ,sep=";" )

    @classmethod
    def save_table(cls, data):
        # print(">>>>    Save " + cls.table + cls.extension)
        
        pd.DataFrame(data).to_csv(cls.path 
                    + cls.table 
                    + cls.extension ,sep=";")

    @classmethod
    def load_table(cls):
        # print(">>>>    Load " + cls.table + cls.extension)
        return pd.read_csv(cls.path 
                    + cls.table 
                    + cls.extension ,sep=";", index_col=0)

    @classmethod
    def add_record(cls, record):
        # print(">>>>    Adding record to " + cls.table + cls.extension)
        data = cls.load_table().append(record.data, sort = False)
        cls.save_table(data)

#############################
#                           #
#  T R A N S A C T I O N S  #
#                           #
#############################
class TransactionIO(FinanceTrackerIO):
    table = "transactions"


#############################
#                           #
#      A C C O U N T S      #
#                           #
#############################
class AccountIO(FinanceTrackerIO):
    table = "accounts"
    

#############################
#                           #
#      C A T E G O R Y      #
#                           #
#############################
class CategoryIO(FinanceTrackerIO):
    table = "categories"


#############################
#                           #
#          T A G            #
#                           #
#############################
class TagIO(FinanceTrackerIO):
    table = "tags"



if __name__ == '__main__':
    
    pass

        
        
        
    
    