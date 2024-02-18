
#   project name        : credit card analysis
#   made by             : Vinayak Tiwari
#   session             : 2021-22

import pandas as pd
import time
import matplotlib.pyplot as plt

df = pd.DataFrame()
csv_file = "C:\\Final.csv"


def introduction():
    msg = '''
          Hellow
          My name is Vinayak Tiwari
          I would Like to Present You My Project On Topic CREDIT CARD ANALYSIS .

          
. Now, this dataset consists of 20 customers mentioning their age, salary, marital_status, 
     credit card limit, credit card category, etc. There are nearly 15 features.
          

. In this project we are going to analyse the same dataset using Python Pandas
  on windows machine but the project can be run on any machine support:
                                                             .python5
                                                             .pandas
                                                             .matplotlib
                         '''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')


def made_by():
    msg = ''' 
            Credit Card Analysis made by    : Vinayak Tiwari
            Roll No                         : 50
            session                         : 2021-22
            
            Thanks for evaluating my Project.
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')


def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen


def clear():
    for x in range(65):
               print()


def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nD A T A   A N A L Y S I S   M E N U  ')
            print('_'*100,'\n')
            print('1.   Show Whole DataFrame')
            print('2.   Show Columns')
            print('3.   how Top Rows')
            print('4.   Row Bottom Rows')
            print('5.   Show Specific Column')
            print('6.   Add a New Record')
            print('7.   Add a New Column')
            print('8.   Delete a Column')
            print('9.   Delete a Record')
            print('10.  Card Type User')
            print('11.  Gender wise User')
            print('12.  Data Summery')
            print('13.  Exit (Move to main menu)')
            ch = int(input('\n\nEnter your choice:'))
            if ch == 1:
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 2:
                print(df.columns)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 6:
                a = input('Enter Customer ID :')
                b = input('Enter Customer Type :')
                c = input(' Enter Customer Age:')
                d = input('Enter Customer Gender :')
                e = input('Enter Customer Dependent Count :')
                f = input('Enter Education Level :')
                g = input('Enter Marital Status :')
                h = input('Enter Income Category :')
                i = input('Enter Card Category :')
                j = input('Enter Credit Limit :')
                k = input('Enter Revolving Balance :')
                l = input('Enter Average Open to Buy Card :')
                m = input('Enter Total Transaction amount :')
                n = input('Enter Total Transaction Credit:')
                o = input('Enter Average Utilization Ratio  :')
               
                data = {'clientID': a, 'Type': b, 'age': c,
                        'gender': d, 'Dependent_count': e, 'Educational_Level': f, 'Marital_Status': g,
                        'Income_Category':h,'Card_Category':i,'Credit_Limit':j,
                        'Total_Revolving_Bal':k,'Avg_Open_To_Buy':l,'Total_Trans_Amt':m,
                        'Total_Trans_Ct':n,'Average_Utilization_Ration':o
                        }
                df = df.append(data, ignore_index=True)
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 7:
                col_name = input('Enter new column name :')
                col_value = int(input('Enter default column value :'))
                df[col_name] = col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 8:
                col_name = input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 9:
                index_no = int(
                    input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 10:
                print(df.columns)
                print(df['Type'].unique())
                tipe = input('Enter Card Type ')
                g = df.groupby('Type')
                print('Card Type : ', tipe)
                print(g['Type'].count())
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 11:
                df1 = df.Gender.unique()
                print('Available Gender :', df1)
                print('\n\n')
                schName = input('Enter Gender Type :')
                df1 = df[df.Gender == schName]
                print(df1)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 12:
                print(df.describe())
                print("\n\n\nPress any key to continue....")
                wait = input()
            if ch == 13:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('1.  Whole Data LINE Graph\n')
        print('2.  Whole Data Bar Graph\n')
        print('3.  Whole Data Scatter Graph\n')
        print('4.  Whole Data Pie Chart\n')
        print('5.  Bar Graph By Education Level\n')
        print('6.  Bar Graph By Income Level\n')
        print('7.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()

        if ch == 2:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.bar(x, y)  #bar graph
            plt.grid(True)
            plt.show()
            wait = input()

        if ch == 3:
            g = df.groupby('Gender')
            x = df['Gender'].unique()
            y = g['Gender'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Gender')
            plt.ylabel('Total Credit Card Users')
            plt.title('Credit Card User- Gender wise')
            plt.grid(True)
            plt.scatter(x, y)
            plt.show()
            wait = input()

        if ch == 4:
            g = df.groupby("Card_Category")
            x = df['Card_Category'].unique()
            y = g['Card_Category'].count()
            plt.pie(y, labels=x, autopct='% .2f', startangle=90)  #pie graph
            plt.xticks(rotation='vertical')
            plt.title('Credit Card User- Card Type')
            plt.show()

        if ch == 5:
            g = df.groupby("Education_Level")
            x = df['Education_Level'].unique()
            y = g['Education_Level'].count()
            plt.bar(x, y)
            #plt.xticks(rotation='vertical')
            plt.grid(True)
            plt.title('Education Level wise Card User')
            plt.xlabel('Education Level')
            plt.show()
            wait = input()

        if ch == 6:
            g = df.groupby("Income_Category")
            x = df['Income_Category'].unique()
            y = g['Income_Category'].count()
            plt.grid(True)
            plt.title('Credit Card User- Income Group')
            plt.xlabel('Income Group')
            plt.ylabel('Card Users')
            plt.bar(x,y)
            plt.show()

        if ch == 7:
            break



def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('5.  Exit\n')
                      choice = int(input('Enter your choice :'))

                      if choice == 1:
                                read_csv_file()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 2:
                                data_analysis_menu()
                                wait = input('\n\n Press any key to continue....')

                      if choice == 3:
                                graph()
                                wait = input('\n\n Press any key to continue....')
                      if choice == 4:
                                export_menu()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 5:
                                 break
           clear()
           made_by()


# call your main menu
main_menu()
