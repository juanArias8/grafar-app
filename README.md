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
* * http://127.0.0.1:5000/api/data (POST) params: {"function": "x^2+2", "a": 1, "b": 20}
* Controllers added 
* * controller_graph crate a graph image from a function and save it 
* * controller_database define all necessary operations whit mongodb database
 
 