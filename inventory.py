import json

# Your other imports and code
inventory = []

inventory.append({
    'vin': '1G1ZD5ST6JF153496', 
    'make_model': 'Porsche 911', 
    'year': '2018', 
    'price': '110000', 
    'stock_number': '1'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153497', 
    'make_model': 'Porsche 911', 
    'year': '2019', 
    'price': '120000', 
    'stock_number': '2'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153498', 
    'make_model': 'Porsche Cayenne', 
    'year': '2020', 
    'price': '80000', 
    'stock_number': '3'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153499', 
    'make_model': 'Porsche Macan', 
    'year': '2021', 
    'price': '60000', 
    'stock_number': '4'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153500', 
    'make_model': 'Porsche Panamera', 
    'year': '2022', 
    'price': '90000', 
    'stock_number': '5'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153496', 
    'make_model': 'Porsche 911', 
    'year': '2018', 
    'price': '110000', 
    'stock_number': '6'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153497', 
    'make_model': 'Porsche 911', 
    'year': '2019', 
    'price': '120000', 
    'stock_number': '7'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153498', 
    'make_model': 'Porsche Cayenne', 
    'year': '2020', 
    'price': '80000', 
    'stock_number': '8'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153499', 
    'make_model': 'Porsche Macan', 
    'year': '2021', 
    'price': '60000', 
    'stock_number': '9'
})

inventory.append({
    'vin': '1G1ZD5ST6JF153500', 
    'make_model': 'Porsche Panamera', 
    'year': '2022', 
    'price': '90000', 
    'stock_number': '10'
})


# convert the inventory list to a json object
inventory_json = json.dumps(inventory, indent=4)

# write the json object to a file
with open('inventory.json', 'w') as f:
    f.write(inventory_json)