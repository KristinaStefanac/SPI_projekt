DROP DATABASE IF EXISTS Sales;
CREATE DATABASE IF NOT EXISTS Sales;
USE Sales;

CREATE TABLE IF NOT EXISTS Country (
	id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE (name)
);

CREATE TABLE IF NOT EXISTS State (
    id INTEGER NOT NULL AUTO_INCREMENT,
    state_name VARCHAR(40) DEFAULT NULL,
    country_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (state_name),
    FOREIGN KEY (country_id) REFERENCES Country(id)
);

 CREATE TABLE IF NOT EXISTS Product_Category (
	id INTEGER NOT NULL AUTO_INCREMENT,
	category VARCHAR(40) NOT NULL,
	UNIQUE(category),
	PRIMARY KEY (id)
 );
 
 CREATE TABLE IF NOT EXISTS Product_Subcategory (
	id INTEGER NOT NULL AUTO_INCREMENT,
    sub_category_name VARCHAR(40) NOT NULL,
    category_id INT,
    FOREIGN KEY(category_id) REFERENCES Product_Category(id),
    PRIMARY KEY (id)
 );
 
CREATE TABLE IF NOT EXISTS Product (
	id INTEGER NOT NULL AUTO_INCREMENT,
	product VARCHAR(40) NOT NULL,
	unit_price INTEGER NOT NULL,
    PRIMARY KEY (id),
	UNIQUE (product,unit_price),
	id_Product_Subcategory INTEGER NOT NULL,
	FOREIGN KEY(id_product_subcategory) REFERENCES Product_Subcategory (id)
 );

CREATE TABLE IF NOT EXISTS Costumer (
	id INTEGER NOT NULL AUTO_INCREMENT,
    age CHAR(3) NOT NULL,
    age_group VARCHAR (20) NOT NULL,
    gender CHAR(2) NOT NULL,
    UNIQUE (age_group, gender),
    PRIMARY KEY (id),
    id_country INTEGER NOT NULL,
    FOREIGN KEY (id_country) REFERENCES Country(id)
);

CREATE TABLE IF NOT EXISTS Orders (
	id INTEGER NOT NULL AUTO_INCREMENT,
    cost DOUBLE NOT NULL,
    ravenue DOUBLE NOT NULL,
    date DATETIME NOT NULL,
    order_quantity INTEGER NOT NULL,
    id_product INTEGER NOT NULL,
    id_costumer INTEGER NOT NULL,
    id_country INTEGER NOT NULL,
    profit DOUBLE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_product) REFERENCES Product(id),
	FOREIGN KEY (id_costumer) REFERENCES Costumer(id)
);



select * from Country;
select * from State;
select *from Product_Category;
select * from Product_Subcategory;
select *from Product;
select *from Costumer;
select *from Orders;
