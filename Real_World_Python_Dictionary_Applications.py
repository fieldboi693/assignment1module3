# Initial menu
restaurant_menu = { 
    "Starters" : { 
        "Soup" : 5.99, 
        "Bruschetta" : 6.50
    }, 
    "Main Course" : {
        "Steak" : 15.99, 
        "Salmon" : 13.99
    },
    "Desserts" : {
        "Cake" : 4.99, 
        "Ice cream" : 3.99
    }
}

# 1. Add a new category "Beverages" with at least two items
restaurant_menu["Beverages"] = {
    "Coffee" : 2.99,
    "Tea" : 1.99
}

# 2. Update the price of "Steak" to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# 3. Remove "Bruschetta" from "Starters"
restaurant_menu["Starters"].pop("Bruschetta", None)

# Print updated menu
print(restaurant_menu)