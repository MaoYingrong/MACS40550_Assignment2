# Sugarscape Constant Growback model

This is Epstein & Axtell’s Sugarscape Constant Growback model. It’s based on the NetLogo Sugarscape 2 Constant Growback (Li and Wilensky, 2009), but the code is adapted from Mesa examples (https://github.com/projectmesa/mesa-examples/tree/main/examples/sugarscape_cg). This model aims to simulate that a population of agents gathers renewable, spatially unequally distributed resources from its environment. It shows agents' movement and survival patterns. 

Two types of agents:  
- Sugar: constantly grows until it reaches its capacity;  
- Ant: wanders around to collect and eat sugar.    


      
In a time step:  
Each sugar site  
- if it doesn’t reach its capacity, grows one unit of sugar;   
Each ant
- looks out as far as vision permits in the four directions and identifies the unoccupied sites with the most sugar;
  - If there are more than one sites having the most sugar, the ant will choose the nearest one and move to that site;  
  - Then, it collects all the sugar at that site and updates its sugar holding.
  - The sugar holding of each ant is updated (the original value + new collected - metabolism). If it’s negative, this ant starve and is moved out of the model.


## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

## Files

* ``sugarscape/agents.py``: Defines the SsAgent, and Sugar agent classes.
* ``sugarscape/schedule.py``: This is exactly based on wolf_sheep/schedule.py.
* ``sugarscape/model.py``: Defines the Sugarscape Constant Growback model itself
* ``sugarscape/server.py``: Sets up the interactive visualization server
* ``run.py``: Launches a model visualization server.
