costPerItem = 20.00
sellingPrice = 40.00
fixedCosts = 50000.00
profitsPerItem = sellingPrice - costPerItem
breakEven = int(fixedCosts/profitsPerItem)



print("Cost of production per Item = £"+ str(costPerItem))
print("Selling price of an item = £"+ str(sellingPrice))
print("Fixed costs in the business = £"+ str(fixedCosts))
print("Profits per item = £" + str(profitsPerItem))
print("Items needed to be sold to breakeven ="+ str(breakEven))

