Superpy

**Description**

Superpy is a command-line tool that keeps track of inventory. It's core functionality is keeping track and producing reports on various data. CSV files get created during this process. 

**Usage**

The program can be used by using the following commands:
- Buy command
- Sell command
- Report inventory/revenue/profit command
- Chart command
- Advance time command
- Inventory to JSON

***Buy command***

In order to buy a product. The following arguments are needed: product_name, price and expiration date. This is how the command line looks like
> python main.py buy_product --product_name banana --buy_price 0.8 --expiration_date 2022-09-09

***Sell command***

In order to sell a product. The following arguments are needed: product_name and price. This is how the command line looks like
> python main.py sell_product --product_name banana --sell_price 0.8 


***Report inventory***

In order to report the inventory. The following can be used: now, yesterday, date or all. The arguments correspond to what time frame you would like to report the inventory. Using the all argument displays the inventory on all time frames. These are examples of how the command line can be used. 
> python main.py report_inventory --now
> python main.py report_inventory --yesterday
> python main.py report_inventory --date 2022-09-08
> python main.py report_inventory --all 


***Report revenue***

In order to report the revenue. The following can be used: now, yesterday or date. The arguments correspond to what time frame you would like to report the revenue. . These are examples of how the command line can be used. 
> python main.py report_revenue --now
> python main.py report_revenue --yesterday
> python main.py report_revenue --date 2022-09-08


***Report profit***

In order to report the profit. The following can be used: now, yesterday or date. The arguments correspond to what time frame you would like to report the profit. . These are examples of how the command line can be used. 
> python main.py report_profit --now
> python main.py report_profit --yesterday
> python main.py report_profit --date 2022-09-08

***Chart products***

It is possible to chart up to five products in your inventory. This is an example how this command can be used. 
> python main.py chart_products --product_name1 apple --product_name2 banana
> python main.py chart_products --product_name1 orange --product_name2 mandarin --product_name3 kiwi --product_name4 banana
> python main.py chart_products --product_name1 kiwi --product_name2 banana --product_name3 orange
> 
***Chart all***

Using this command charts all the different types of products in  your inventory. This is an example of how this command can be used. 
> python main.py chart_all

***Advance time***

Using this command advances the time in the program. This is an example of how this command can be used. 
>  python main.py advance_time --time 1 

***CSV to JSON***

Using this command transforms the inventory CSV file to JSON format. This is an example of how this command can be used. 
>  python main.py inventory_to_json



**Example outputs**

In the following example we will buy the following items: 4 bananas, 3 apples, 2 oranges, 1 kiwi and 3 mandarins with the current date 2022-09-08
This is an example of the inventory now.

<img src="https://user-images.githubusercontent.com/103627787/189226816-6aa268a4-1d95-4b90-9221-11c408717af1.png" width="400" height="250">

This is an example of a chart with the following items -- kiwi, banana and orange

<img src="https://user-images.githubusercontent.com/103627787/189228156-9b13daf0-111e-4b8d-847b-7e7bccc797c8.png" width="400" height="400">

This is an example of a chart with all the items

<img src="https://user-images.githubusercontent.com/103627787/189227069-9abccc57-1a63-4d91-a27a-e6f012963370.png" width="400" height="400">


In the following example the time will be advanced by one day and we will buy a few other items
> PS C:\Users\Gebruiker\Documents\wincademy\superpy> python main.py advance_time --time 1 
> The time is advanced from 2022-09-08 to 2022-09-09 


Buy another banana on new date. 

Report inventory today

![image](https://user-images.githubusercontent.com/103627787/189229118-4e24883e-6610-4891-a204-442cfafaa5d9.png)

Report inventory yesterday

![image](https://user-images.githubusercontent.com/103627787/189229298-a7afe3d5-3d71-4315-900d-8f1ff09f124e.png)









