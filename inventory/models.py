from django.conf import settings
from django.db import models


class Inventory(models.Model): # schema for the Inventory Table
    item_ID = models.IntegerField(primary_key=True)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_type = models.CharField(max_length=30)
    product_size = models.CharField(max_length=15)
    product_color = models.CharField(max_length=15)
    product_description = models.TextField()

    # Class functions go here, the ones below are from our proposal.
    # I merged the inventory and product tables from our class list because they don't make sense independently
    #get/set/edit ID: int
    #get/set/edit name: str
    #get/set/edit quantity: int
    #get/set/edit item_cost: float
    #get/set/edit product_type: str
    #get/set/edit product_size: str
    #get/set/edit product_color: str
    #get/set/edit product_description: str
    #remove()

    def __str__(self): # print output format
        inventory_string1 = f"Item ID: {item_ID} Item Name: {item_name} Quantity: {quantity} Cost: {item_cost}"
        inventory_string2 = f"Type: {product_type} Size: {product_size} Color: {product_color} Description: {product_description}"
        return inventory_string1, inventory_string2

class Sales(models.Model): # schema for the Sales Table
    salesID = models.IntegerField(primary_key=True)
    productID = models.ForeignKey(Inventory, on_delete=models.DO_NOTHING) # this attributes the productID as foreign key and indicates what to do if the product is deleted, in this case nothing
    salesDate = models.DateField()
    salesQuantity = models.IntegerField()
    salesTotal = models.DecimalField(max_digits=10, decimal_places=2)

    #Class functions go here (ones below are from our proposal):
    #get_saleID: int
    #get_sale: str
    #remove_sale: str
    #get_date: str
    #calc_revenue: float
    #get_total_price: int

    def __str__(self): # print output format
        sales_string = f"Sale ID: {salesID} Product ID: {productID} Date: {salesDate} Quantity: {saleQuantity} Sales Total: {salesTotal}"
        return sales_string