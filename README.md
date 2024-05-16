**UPDATE: I've developed a TEXT_TO_SQL repository (https://github.com/devang1218/TEXT_TO_SQL) that leverages natural language processing to translate human language into SQL queries. It utilizes llm (Gemini-pro) to generate these queries, which are then executed in the backend to deliver the intended results.**

<h1>Assignment</h1>

Scenario:

Company XYZ held a promo sale for their signature items named: x,y,z. Sales are at an
all-time high, but they want to create a marketing strategy to target age groups of people by
looking at total quantities purchased.

They then created a database with these business rules:

• A sales receipt can have multiple items in an order.

• For every order, the clerk records all quantities for all items, including items not
bought (which they denote with quantity=NULL).

• Each customer can do multiple sales transactions, and has his/her age stored in a
database.

Refer to the image below for the table structures and relationships.

![image](https://github.com/devang1218/Data_Engineer_Assignment-/assets/46046916/79a2fdfc-f8f0-49b6-baea-d1aefe3c2c9d)


**Objectives**

Create a Python script that can:

1. connect to the SQLite3 database provided

2. extract the total quantities of each item bought per customer aged 18-35.
- For each customer, get the sum of each item
- Items with no purchase (total quantity=0) should be omitted from the final
list
- No decimal points allowed (The company doesn’t sell half of an item ;) )
Challenge: Provide 2 solutions, one using purely SQL, the other using Pandas

3. store the query to a CSV file, delimiter should be the semicolon character (';')


**Test case:**

Customer 1 bought Item X on multiple occasions, totaling 10 for Item X only

Customer 2 bought one of each item only once, totaling 1 each Item

Customer 3 bought Item Z on two occasions, totaling 2 for Item Z only

Then the output file should look like the example below:

Customer;Age;Item;Quantity

1;21;x;10

2;23;x;1

2;23;y;1

2;23;z;1

3;35;z;2

**Soution:**

This repository gives you the solution of the above problem.

**Python version used 3.11**

To execute this on your local machine clone the repository and follow the mentioned below steps:
1. Create the virtual environment and download the dependent libraries given in requirements.txt file:

Create and activate the venv by (in Windows):

    python -m venv <virtual_environment_name>

    <virtual_environment_name>\Scripts\activate
  
  Download the libraries :
      
    pip install -r requirements.txt

2. Run main.py python file which is present inside app folder

Go to the terminal and to the app directory and the execute:
 
    python main.py

3. After the successful run, output files for both the cases (pandas and sql) will be created in the output folder.
