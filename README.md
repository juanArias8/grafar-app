# Grafar
***
## Description
***
Grafar is an application whose main objective is to 
create augmented reality objects based on the graph 
of a mathematical function.
***
## Actual state
***
* Database on mongoDb created
* Pymongo connector added
* Api rest defined
* * http://127.0.0.1:5000/api (GET)return all graphs objects
* * http://127.0.0.1:5000/api/data (POST) params: {"function": "x^2+2"}
* Class Graph added
* * Graph class create the graph of a function and save it into the database
 
 