import csv
import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='Sales'
)


################################################################################33
# Definirajte SQL upit za unos podataka u tablicu "Product_Category"
query = """
    INSERT IGNORE INTO Product_Category (category)
    VALUES (%s)
"""

# Otvorite CSV datoteku i pročitajte redove
with open('C:\\Users\\Kristina\\Desktop\\SPI\\product_subcategory.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Preskoči zaglavlje (header)

    # Kreirajte kursor za izvršavanje SQL upita
    cursor = conn.cursor()

    # Iterirajte kroz redove i izvršite SQL upit za svaki red
    for row in csv_reader:
        category = row[0]
        
        # Izvrši SQL upit za unos kategorije
        cursor.execute(query, (category,))
        
        # Potvrdite promjene u bazi podataka
        conn.commit()

############################################################################################33333
#Definirajte SQL upit za unos podataka u tablicu "Product_Subcategory"
query = """
    INSERT INTO Product_Subcategory (sub_category_name, category_id)
    VALUES (%s, %s)
"""


with open('C:\\Users\\Kristina\\Desktop\\SPI\\product_subcategory.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    cursor = conn.cursor()

    for row in csv_reader:
        sub_category_name = row[1]
        category = row[0]
        select_query = """
            SELECT id
            FROM Product_Category
            WHERE category = %s
        """
        cursor.execute(select_query, (category,))
        result = cursor.fetchone()
        if result:
            category_id = result[0]
            cursor.execute(query, (sub_category_name, category_id))
            conn.commit()
##################################################################################################3
# Definirajte SQL upit za unos podataka u tablicu "Product"
product_query = """
    INSERT IGNORE INTO Product (product, unit_price, id_Product_Subcategory)
    VALUES (%s, %s, %s)
"""

# Otvorite CSV datoteku i pročitajte redove
with open('C:\\Users\\Kristina\\Desktop\\SPI\\product.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Preskoči zaglavlje (header)

    # Kreirajte kursor za izvršavanje SQL upita
    cursor = conn.cursor()

    # Iterirajte kroz redove i izvršite SQL upit za svaki red
    for row in csv_reader:
        product = row[0]
        unit_price = int(row[1])
        subcategory_id = row[2]

        # Provjerite postojanje vrijednosti stranog ključa
        if subcategory_id:
            # Izvrši SQL upit za unos podataka s vrijednosti stranog ključa
            cursor.execute(product_query, (product, unit_price, subcategory_id))
        else:
            # Izvrši SQL upit za unos podataka bez vrijednosti stranog ključa
            cursor.execute(product_query, (product, unit_price, None))

        # Potvrdite promjene u bazi podataka
        conn.commit()

##################################################################################################
# Definirajte SQL upit za unos podataka u tablicu "Costumer"
customer_query = """
    INSERT IGNORE INTO Costumer (age, age_group, gender, id_country)
    VALUES (%s, %s, %s, %s)
"""

# Otvorite CSV datoteku i pročitajte redove
with open('C:\\Users\\Kristina\\Desktop\\SPI\\customer.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Preskoči zaglavlje (header)

    # Kreirajte kursor za izvršavanje SQL upita
    cursor = conn.cursor()

    # Iterirajte kroz redove i izvršite SQL upit za svaki red
    for row in csv_reader:
        age = row[0]
        age_group = row[1]
        gender = row[2]
        country_id = row[3]

        # Izvrši SQL upit za unos podataka
        cursor.execute(customer_query, (age, age_group, gender, country_id))

    # Potvrdite promjene u bazi podataka
    conn.commit()

##############################################################################################3

country_query = """
    INSERT IGNORE INTO Country (name, state_name)
    VALUES (%s, %s)
"""

with open('C:\\Users\\Kristina\\Desktop\\SPI\\country.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    cursor = conn.cursor()
    for row in csv_reader:
        country_name = row[0]
        state_name = row[1]

        cursor.execute(country_query, (country_name, state_name))

# Zatvorite kursor i prekinite vezu s bazom podataka
cursor.close()
conn.close()


country_query = """
    INSERT IGNORE INTO Country (name, state_name)
    VALUES (%s, %s)
"""

with open('C:\\Users\\Kristina\\Desktop\\SPI\\country.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    cursor = conn.cursor()
    for row in csv_reader:
        country_name = row[0]
        state_name = row[1]

        cursor.execute(country_query, (country_name, state_name))

  

  