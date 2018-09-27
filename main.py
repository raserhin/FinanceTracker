# coding=utf8
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from financeconsole import TransactionUI, AccountUI, CategoryUI, TagUI, init_data
from tabulate import tabulate


def table_print(data):
    return tabulate(data, headers='keys', tablefmt='psql', floatfmt=".2f")



def menu():
    
    print("-"*30, "  F I N A N C E   T R A C K E R  ", "-"*30, sep="\n")
    while True:
        print("Choose your option: \n", "A -> Account", "T -> Transaction", "F -> Tags", "C -> Category", "I -> Initialize", "Q -> Quit", sep="\n" )
        option = input(">>> ").upper()
        if(option == "A"):
            AccountUI.menu()
        elif(option == "T"):
            TransactionUI.menu()
        elif(option == "F"):
            TagUI.menu()
        elif(option == "C"):
            CategoryUI.menu()
        elif(option == "I"):
            init_data()
        elif(option == "Q"):
            break
        




    
def main():
    pass
    

if __name__ == '__main__':
   menu()
    
    
    












