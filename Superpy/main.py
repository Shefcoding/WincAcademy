# Imports
import argparse
import csv
import json 
from datetime import date
from pathlib import Path
import os
from datetime import timedelta, datetime
from rich.console import Console
from rich.table import Table
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

 


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"



def buy_product(name, price, expiration_date):

    #get current buy date from textfile
    with open('date.txt') as f:
        line = f.readline()
        

    todays_date = datetime.strptime(line, '%Y-%m-%d').date()
   
    #check if files already exists, if so append a row with new data
        
    if os.path.exists('./bought.csv') and os.path.exists('./inventory.csv'):


        #read bought csv file first in order to get current id
        
        csv_file=open('bought.csv', 'r', newline = '')
        csv_reader = csv.reader(csv_file, delimiter=',')
        #Get current id from bought file.  
        id = int(list(csv_reader)[-1][-5])
      
        csv_file.close() 
        #increment id 
        id+=1   
        with open('bought.csv', 'a', newline = '') as buy_file:
           
            fieldnames = ['id','product_name','buy_date', 'buy_price', 'expiration_date']
            writer = csv.DictWriter(buy_file, fieldnames=fieldnames)
            writer.writerow({'id': id, 'product_name': name,'buy_date': todays_date, 'buy_price': price, 'expiration_date': expiration_date})
            buy_file.close() 

       
        
        # keep count of the product in inventory 
        inventory_file=open('inventory.csv', 'r', newline = '')
        inventory_reader = csv.reader(inventory_file, delimiter=',')
        inventory_list = list(inventory_reader)

        count = 1
        for item in inventory_list:
            if name in item:
                count +=1

             #add product to inventory   
        with open('inventory.csv', 'a', newline = '') as inventory_file:        
                fieldnames_inventory = ['product_name','count', 'buy_price', 'expiration_date', 'buy_date']
                writer_inventory = csv.DictWriter(inventory_file, fieldnames=fieldnames_inventory)
                writer_inventory.writerow({'product_name': name,'count': count,'buy_price': price, 'expiration_date': expiration_date, 'buy_date': todays_date})
                inventory_file.close()

        
    #if file doesnt exist create file with row 
    else:
        #Begin program from here
        #write todays date to file 
        todays_date = datetime.today().strftime('%Y-%m-%d')
        #Write new file with popped row to inventory csv file
        datetime_file = open('date.txt', 'w')
        datetime_file.write(todays_date)
        datetime_file.close() 

        #Start ID and count of product
        id = 1
        count = 1

        #create inventory file
        with open('inventory.csv', 'w', newline = '') as inventory_file:
            fieldnames_inventory = ['product_name','count', 'buy_price', 'expiration_date', 'buy_date']
            writer_inventory = csv.DictWriter(inventory_file, fieldnames=fieldnames_inventory)
            writer_inventory.writeheader()
            writer_inventory.writerow({'product_name': name,'count': count,'buy_price': price, 'expiration_date': expiration_date, 'buy_date': todays_date})
            inventory_file.close()


        #create bought file
        with open('bought.csv', 'w', newline = '') as buy_file:
            fieldnames = ['id','product_name','buy_date', 'buy_price', 'expiration_date']
            writer = csv.DictWriter(buy_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': id, 'product_name': name,'buy_date': todays_date, 'buy_price': price, 'expiration_date': expiration_date})
            buy_file.close()
            
    

def sell_product(name, price):
     #get current sell date
    with open('date.txt') as f:
        line = f.readline()
        print(str(line))

    todays_date = datetime.strptime(line, '%Y-%m-%d').date()

    #read inventory file and make a list with read file. Search for chosen product name and highest count. Remove that row from the list
    inventory_file=open('inventory.csv', 'r', newline = '')
    inventory_reader = csv.reader(inventory_file, delimiter=',')
    inventory_list = list(inventory_reader)
 
    #Get largest count of product 
    largest_count = 0
    for item in inventory_list[1:]:
        if name in item:
            if int(item[1])>largest_count:
                largest_count = int(item[1])


    # use the largest count to remove your sold product from the list
    for item in inventory_list[1:]:
        if name in item:
            if int(item[1]) == largest_count:
                inventory_list.remove(item);  
                print(item)

    inventory_file.close()       
    print(largest_count)

    #Write new file with popped row to inventory csv file
    inventory_file = open('inventory.csv', 'w', newline = '')
    writer = csv.writer(inventory_file, delimiter=',')
    writer.writerows(inventory_list)
    inventory_file.close()     

    if os.path.exists('./sold.csv'):
        #read csv file first in order to get id       
        csv_file=open('sold.csv', 'r', newline = '')
        csv_reader = csv.reader(csv_file, delimiter=',')
        sold_list = list(csv_reader)
        
        id = int(sold_list[-1][-4])
        #id = 1
        print(id)
        csv_file.close() 

        id+=1   

        with open('sold.csv', 'a', newline = '') as sell_file:
           
            fieldnames = ['id','product_name','sell_date', 'sell_price']
            writer = csv.DictWriter(sell_file, fieldnames=fieldnames)
            writer.writerow({'id': id, 'product_name': name,'sell_date': todays_date, 'sell_price': price})
            sell_file.close()       
        
        print(id)
    else:
        
        #If file doesn't exist create file and start the first item with id 1
        id = 1
        with open('sold.csv', 'w', newline = '') as sell_file:
            fieldnames = ['id','product_name','sell_date', 'sell_price']
            writer = csv.DictWriter(sell_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': id, 'product_name': name,'sell_date': todays_date, 'sell_price': price })
            sell_file.close()
            

def report_inventory(date, now, yesterday, all):

    # get current time from txt file
    with open('date.txt') as f:
        line = f.readline()

    #Get yesterdays date by getting current date from txt file and subtracting it with one day.
    todays_date = datetime.strptime(line, '%Y-%m-%d').date()
    yesterdays_date = todays_date - timedelta(1)
    yesterdays_date = yesterdays_date.strftime('%Y-%m-%d')

# report inventory to one of the three lists -- now, yesterdy or date. These are the options you have when reporting the inventory
    inventory_file=open('inventory.csv', 'r', newline = '')
    inventory_reader = csv.reader(inventory_file, delimiter=',')
    inventory_list = list(inventory_reader) 
    inventory_list = inventory_list[1:]
    nowlist=[]
    yesterdayslist=[]
    datelist=[]

    for row in inventory_list:
    #if argument now is used append the rows of today to the now list
        if now == 'now':
            if row[-1] == line:
                nowlist.append(row)
     #if argument yesterday is used append the rows of today to the yesterday list
        elif yesterday == 'yesterday':
            if row[-1] == yesterdays_date:
                yesterdayslist.append(row)
         #if the date argument  is used append the rows of today to the date list       
        elif date == row[-1]:
            datelist.append(row)
     
    print(datelist)
# create a table and use the following headers; Product_name || Count || Buy_price || Expiration_date || Buy_date
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")   
    table.add_column("Product_name", style="dim", width=12)
    table.add_column("Count")
    table.add_column("Buy_price", justify="right")
    table.add_column("Expiration_date", justify="right")
    table.add_column("Buy_date", justify="right")

    if now == 'now':
        for row in nowlist:
            table.add_row(*row)
    elif yesterday == 'yesterday':
        for row in yesterdayslist:
            table.add_row(*row)
    elif all =='all':
        for row in inventory_list:
            table.add_row(*row)
    else:
        for row in datelist:
            table.add_row(*row)
          
       
    console.print(table)

def report_revenue(date, now, yesterday):

        # get current time from txt file
        with open('date.txt') as f:
            line = f.readline()

        #Get yesterdays date by getting current date from txt file and subtracting it with one day.
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        yesterdays_date = todays_date - timedelta(1)
        yesterdays_date = yesterdays_date.strftime('%Y-%m-%d')

        #read sold file and the third row to get total revenue 
        csv_file=open('sold.csv', 'r', newline = '')
        csv_reader = csv.reader(csv_file, delimiter=',')
        sold_list = list(csv_reader)
        revenue_now = 0.0
        revenue_yesterday = 0.0
        revenue_date = 0.0
        for item in sold_list[1:]:
            if now == 'now':
                if item[2]==line:
                    revenue_now += float(item[3])
            elif yesterday == 'yesterday':
                if item[2] == yesterdays_date:
                     revenue_yesterday += float(item[3])            
            elif date == item[2]:
                 revenue_date += float(item[3])  

        if now == 'now':
            print(f'Total revenue now is : {round(revenue_now)}')
        elif yesterday == 'yesterday':
            print(f'Total revenue yesterday is : {round(revenue_yesterday)}')
        else:
            print(f'Total revenue on {date} is : {round(revenue_date)}')

        csv_file.close()

def report_profit(date, now, yesterday):
        # get current time from txt file
        with open('date.txt') as f:
            line = f.readline()
         #Get yesterdays date by getting current date from txt file and subtracting it with one day.
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        yesterdays_date = todays_date - timedelta(1)
        yesterdays_date = yesterdays_date.strftime('%Y-%m-%d')

        #read sold and bought file to get the total profit  

        # Get total revenue from sold file
        sold_file=open('sold.csv', 'r', newline = '')
        sold_reader = csv.reader(sold_file, delimiter=',')
        sold_list = list(sold_reader)
        revenue_now = 0.0
        revenue_yesterday = 0.0
        revenue_date = 0.0

        for item in sold_list[1:]:
            if now == 'now':
                if item[2]==line:
                    revenue_now += float(item[3])
            elif yesterday == 'yesterday':
                if item[2] == yesterdays_date:
                     revenue_yesterday += float(item[3])            
            elif date == item[2]:
                revenue_date += float(item[3])  

        sold_file.close()
        

        # Get total amount paid from bought file
        bought_file=open('bought.csv', 'r', newline = '')
        bought_reader = csv.reader(bought_file, delimiter=',')
        bought_list = list(bought_reader)
        costs_now = 0.0
        costs_yesterday = 0.0
        costs_date = 0.0

        for item in bought_list[1:]:
            if now == 'now':
                if item[2]==line:
                    costs_now += float(item[3])
            elif yesterday == 'yesterday':
                if item[2] == yesterdays_date:
                     costs_yesterday += float(item[3])            
            elif date == item[2]:
                costs_date += float(item[3])  

        bought_file.close()

        if now == 'now':
            total_profits_now = revenue_now - costs_now
            if total_profits_now < 0:
                total_profits_now = 0
            print(f'Total profit now is : {round(total_profits_now)}')
        elif yesterday == 'yesterday':
            total_profits_yesterday = revenue_yesterday - costs_yesterday
            if total_profits_yesterday < 0:
                total_profits_yesterday = 0
            print(f'Total profit yesterday is : {round(total_profits_yesterday)}')
        else:
            total_profits_date = revenue_date - costs_date
            if total_profits_date < 0:
                total_profits_date = 0
            print(f'Total profit on {date} is : {round(total_profits_date)}')

   
def advance_time(time):

    if os.path.exists('./date.txt'):
        # if date file already exists, read the date from file and advance the time 
        with open('date.txt') as f:
            line = f.readline()
    
        todays_date = datetime.strptime(line, '%Y-%m-%d').date()
        result = todays_date + timedelta(time) 
        result = result.strftime('%Y-%m-%d')
        print(f'The time is advanced from {todays_date} to {result} ')
    else:
        #if file doesn't exist use todays date to advance the time
        result = datetime.today() + timedelta(time) 
        result = result.strftime('%Y-%m-%d')
        print(f'The time is advanced from {datetime.today()} to {result} ')


    datetime_file = open('date.txt', 'w')
    datetime_file.write(result)
    datetime_file.close() 
          

def chart_products(product1, product2, product3, product4, product5):
#Chart up to five products independently. You can use this to compare 1,2,3,4 or 5 products in whichever order. 


    inventory_file=open('inventory.csv', 'r', newline = '')
    inventory_reader = csv.reader(inventory_file, delimiter=',')
    inventory_list = list(inventory_reader) 
    inventory_list = inventory_list[1:]

  #Get largest count of product1 
    largest_count_product1 = 0
    for item in inventory_list[1:]:
        if product1 in item:
            if int(item[1])>largest_count_product1:
                largest_count_product1 = int(item[1])
    inventory_file.close()  

      #Get largest count of product2
    largest_count_product2 = 0
    for item2 in inventory_list[1:]:
        if product2 in item2:
            if int(item2[1])>largest_count_product2:
                largest_count_product2 = int(item2[1])
    inventory_file.close()  

      #Get largest count of product3 
    largest_count_product3= 0
    for item in inventory_list[1:]:
        if product3 in item:
            if int(item[1])>largest_count_product3:
                largest_count_product3 = int(item[1])
    inventory_file.close() 

      #Get largest count of product4 
    largest_count_product4 = 0
    for item in inventory_list[1:]:
        if product4 in item:
            if int(item[1])>largest_count_product4:
                largest_count_product4 = int(item[1])
    inventory_file.close()   

      #Get largest count of product5
    largest_count_product5 = 0
    for item in inventory_list[1:]:
        if product5 in item:
            if int(item[1])>largest_count_product5:
                largest_count_product5 = int(item[1])
 

    inventory_file.close()  

    
    count_product1 = largest_count_product1
    count_product2 = largest_count_product2
    count_product3 = largest_count_product3
    count_product4 = largest_count_product4
    count_product5 = largest_count_product5

    if not args.product_name5 and args.product_name4:
        labels =[product1, product2, product3, product4]
        count_products=[count_product1, count_product2, count_product3, count_product4]
    elif not args.product_name5 and not args.product_name4 and args.product_name3:
        labels =[product1, product2, product3]
        count_products=[count_product1, count_product2, count_product3]
    elif not args.product_name5 and not args.product_name4 and not args.product_name3 and args.product_name2:
        labels =[product1, product2]
        count_products=[count_product1, count_product2]
    elif not args.product_name5 and not args.product_name4 and not args.product_name3 and not args.product_name2 and args.product_name1:
        labels =[product1]
        count_products=[count_product1]
    else:
        labels =[product1, product2, product3, product4, product5]
        count_products=[count_product1, count_product2, count_product3, count_product4, count_product5]

   
    x= np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, count_products, width, label='Count')

    ax.set_ylabel('Count')
    ax.set_title('Products in inventory')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()
    plt.show()

def chart_all():


    # load the data with pd.read_csv
    record = pd.read_csv('inventory.csv')
 
    #print(record.values)
   
    #labels = pd.unique(record['product_name'])
    # Get the highest counts of the different products. 
    highest_counts = record.groupby('product_name')['count'].max()
    next = highest_counts.to_dict()
    # Get key(unique) values 
    labels= list(next.keys())


    x= np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, highest_counts, width, label='Count')

    ax.set_ylabel('Count')
    ax.set_title('Products in inventory')
    ax.set_xticks(x, labels)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    fig.tight_layout()
    plt.show()   

def inventory_to_json():
    jsonArray = []
      
    #read csv file
    with open('inventory.csv', encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open('inventoryExport.json', 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)



def main():
    pass
    # Create the parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')


# parser for "buy" command
parser_buy = subparsers.add_parser('buy_product')
parser_buy.add_argument('--product_name',  type=str, help = 'Enter the name of the product you want to buy')
parser_buy.add_argument('--buy_price', type=str, help = 'Enter the price of the product you want to buy')
parser_buy.add_argument('--expiration_date', type=str, help = 'Enter the expiration date of the product you want to buy')
parser_buy.set_defaults(func=buy_product)

#parser for "sell" command
parser_sell = subparsers.add_parser('sell_product')
parser_sell.add_argument('--product_name',  type=str, help = 'Enter the name of the product you want to sell')
parser_sell.add_argument('--sell_price', type=str, help = 'Enter the price of the product you want to sell')
parser_sell.set_defaults(func=sell_product)

# parser for "report inventory" command
parser_buy = subparsers.add_parser('report_inventory', help= 'Report your inventory on any given timeframe. Use the available commands')
parser_buy.add_argument('--date', type=str, help = 'Enter on which date you would like a report of the inventory')
parser_buy.add_argument('--now', action='store_const', const='now', help = 'Report the inventory today')
parser_buy.add_argument('--yesterday', action='store_const', const='yesterday', help = 'Report the inventory yesterday')
parser_buy.add_argument('--all', action='store_const', const='all', help = 'Report the whole history of the inventory')
parser_buy.set_defaults(func=report_inventory)

# parser for "report revenue" command
parser_buy = subparsers.add_parser('report_revenue', help = 'Report revenue on any given timeframe.  Use the --now, --yesterday or --date commands')
parser_buy.add_argument('--date', type=str, help = 'Enter on which date you would like a report of the revenue')
parser_buy.add_argument('--now', action='store_const', const='now', help = 'Report the revenue today')
parser_buy.add_argument('--yesterday', action='store_const', const='yesterday', help = 'Report the revenue yesterday')
parser_buy.set_defaults(func=report_revenue)

# parser for "report profit" command
parser_buy = subparsers.add_parser('report_profit', help = 'Report profit on any given timeframe.  Use the --now, --yesterday or --date commands')
parser_buy.add_argument('--date', type=str, help = 'Enter on which date you would like a report of the profit')
parser_buy.add_argument('--now', action='store_const', const='now', help = 'Report the profit today')
parser_buy.add_argument('--yesterday', action='store_const', const='yesterday', help = 'Report the profit yesterday')
parser_buy.set_defaults(func=report_profit)
    


#parser for "chart product" command
parser_sell = subparsers.add_parser('chart_products', help='Chart up to five products. Handy for comparing products individually')
parser_sell.add_argument('--product_name1',  type=str, help= 'Enter the first product you want to chart')
parser_sell.add_argument('--product_name2',  type=str, help= 'Enter the second product you want to chart')
parser_sell.add_argument('--product_name3',  type=str, help= 'Enter the third product you want to chart')
parser_sell.add_argument('--product_name4',  type=str, help= 'Enter the fourth product you want to chart')
parser_sell.add_argument('--product_name5',  type=str, help= 'Enter the fifth product you want to chart')
parser_sell.set_defaults(func=chart_products)

#parser for "chart all" command
parser_sell = subparsers.add_parser('chart_all', help = "All the products in your inventory will get charted")
parser_sell.set_defaults(func=chart_all)

#parser for "inventory to json" command
parser_sell = subparsers.add_parser('inventory_to_json', help = "Convert your inventory file to json format")
parser_sell.set_defaults(func=inventory_to_json)

#parser for "advance time" command
parser_sell = subparsers.add_parser('advance_time', help = "Advance time in your text file")
parser_sell.add_argument('--time',  type=int, help = "Fill in how many days you would like to advance time. 1= one day, 2 = two days etc")
parser_sell.set_defaults(func=advance_time)

args = parser.parse_args()


if __name__ == "__main__":

    if args.command == "buy_product":
        print(buy_product( args.product_name, args.buy_price, args.expiration_date))
    elif args.command == "sell_product":
       print(sell_product(args.product_name, args.sell_price))
    elif args.command == "report_inventory":
        report_inventory(args.date, args.now, args.yesterday, args.all)
    elif args.command == "report_revenue":
        report_revenue(args.date, args.now, args.yesterday)
    elif args.command == "report_profit":
        report_profit(args.date, args.now, args.yesterday)
    elif args.command == "advance_time":
        advance_time(args.time)
    elif args.command == "chart_products":
        chart_products(args.product_name1, args.product_name2, args.product_name3, args.product_name4, args.product_name5)
    elif args.command == "chart_all":
        chart_all()
    elif args.command == "inventory_to_json":
        inventory_to_json()
     
    main()
   




