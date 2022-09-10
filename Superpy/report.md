**Report**

Three technical elements in the code will be explained in this report.

**Technical element 1**

The first technical element in this report is can be found in the chart_products function. The chart_products function can chart up to five different products
that are filled in as arguments. This means the code needs to get find out how many products are in the inventory depending on which products are used as arguments. 
The chart should be dynamic to have a good user experience. An example of a dynamic chart is if the user fills in two products the chart should only chart two products, 
if the user fills in 4 products, only 4 products will be displayed in the chart etc.. 

The chart function uses two variables to make a chart, the label and number. The following code provides an example of 5 products charted.

```
        labels =[product1, product2, product3, product4, product5]
        count_products=[count_product1, count_product2, count_product3, count_product4, count_product5]
```

The two problems I solved to make this chart dynamic is first all, getting the different count numbers of all the 5 products. The second step was using 
an if-statement to display the products that were used as an argument. 

**Technical element 2 **

The following information is needed to chart all the different products and their count numbers.
- First of all I need to look through my inventory list and create "groups" of the different products. 
- The next piece of information is the count number of these different groups, ie 5 apples, 7 bananas etc

I used the panda framework for this problem. By using the record.groupby('product_name')['count'].max() I could get the highest counts of my different products.
The next variable to get are the names of the products. This was done by converting the dataframe to a dictionary, and extracting the key's in the key-value pair.

```
    # load the data with pd.read_csv
    record = pd.read_csv('inventory.csv')
 
  
    # Get the highest counts of the different products. 
    highest_counts = record.groupby('product_name')['count'].max()
    next = highest_counts.to_dict()
    print(next)
    # Get key(unique) values 
    labels= list(next.keys())
    
   ```
This code gets the following variables used in the chart-> Labels and highest_counts. 

**Technical element 3**

In the function def report_inventory(date, now, yesterday,all) , I used different lists to specify the timeframe that i wanted to report in a table. 
This lists were the now, yesterday and date list. In the nowlist I used the current date from the text file. In yesterdays date I subtracted one day from the current date.
By specifying my times I could compare my row in inventory with my timeframes and add them to the corresponding lists.

```
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
```
