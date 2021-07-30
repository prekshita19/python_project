import pandas as pd
import csv


def add_question():
    
    try:                                                                                                    # Creating a Function to add a Question                  
        
        enter_question=input("Enter a question...\n")                                                       # Entering a Question
        enter_option_1=input("Please Suggest the option-1 for the following question\n")                    # Entering Option-1
        enter_option_2=input("Please Suggest the option-2 for the following question\n")                    # Entering Option-2
        enter_option_3=input("Please Suggest the option-3 for the following question\n")                    # Entering Option-3
        enter_option_4=input("Please Suggest the option-4 for the following question\n")                    # Entering Option-4
        correct_option=int(input("Enter the Number of correct answer to store\n"))                          # Entering Correct Option as Answer        
        a=[[enter_question,enter_option_1,enter_option_2,enter_option_3,enter_option_4,correct_option]]     # Creating a list for entered data
        add_to_file=pd.DataFrame(a,columns=['Questions','OP1','OP2','OP3','OP4','CA'])                      # Creating a Data-Frame
        add_to_file.to_csv("KBC.csv",mode="a")                                                              # Adding data to file and opening in append mode
    
    except Exception as e:                                                                                  # Catching Exception and printing error
        print("There is an Error :- ",e)

def show_question():                                                                                        # Creating a Function for showing Questions
    
    try:                                                                                                    # Declaring a Try Block
        
        read_question=pd.read_csv("KBC.csv")                                                                # Creating a variable to read file
        read_question_DataFrame=pd.DataFrame(read_question["Questions"])                                    # Declaring a dataframe with a variable
        print(read_question_DataFrame)                                                                      # Printing DataFrame
    
    except Exception as e:                                                                                  # Catching Exception and printing Error
        print("There is an error in reading file",e)

show_question()
#def start_quiz()