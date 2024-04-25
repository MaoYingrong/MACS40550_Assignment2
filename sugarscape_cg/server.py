import mesa

from .agents import SsAgent, Sugar
from .model import SugarscapeCg

color_dic = {4: "#005C00", 3: "#008300", 2: "#00AA00", 1: "#00F800"}


def SsAgent_portrayal(agent):
    if agent is None:
        return

    if type(agent) is SsAgent:
        return {"Shape": "sugarscape_cg/resources/ant.png", "scale": 0.9, "Layer": 1}

    elif type(agent) is Sugar:
        color = color_dic[agent.amount] if agent.amount != 0 else "#D6F5D6"
        return {
            "Color": color,
            "Shape": "rect",
            "Filled": "true",
            "Layer": 0,
            "w": 1,
            "h": 1,
        }

    return {}


canvas_element = mesa.visualization.CanvasGrid(SsAgent_portrayal, 50, 50, 500, 500)
chart_element = mesa.visualization.ChartModule(
    [{"Label": "SsAgent", "Color": "#AA0000"}]
)

model_params = {
    "width": 50,
    "height": 50,
    "initial_population": mesa.visualization.Slider(
        name="Population",
        value = 100,
        min_value=50,
        max_value=200,
        step=10,
        description="Choose the population",
    ),
    "min_sugar": mesa.visualization.Slider(
        name="Minimum Sugar",
        value=6,
        min_value=0,
        max_value=10,
        step=1,
        description="Choose the minimum sugar",
    ),
    "max_sugar": mesa.visualization.Slider(
        name="Maximum Sugar",
        value=25,
        min_value=10,
        max_value=50,
        step=1,
        description="Choose the maximum sugar",
    ),
    "min_metabolism": mesa.visualization.Slider(
        name="Minimum Metabolism",
        value=2,
        min_value=0,
        max_value=5,
        step=1,
        description="Choose the minimum metabolism",
    ),
    "max_metabolism": mesa.visualization.Slider(
        name="Maximum Metabolism",
        value=4,
        min_value=2,
        max_value=10,
        step=1,
        description="Choose the maximum metabolism",
    ),
    "min_vision": mesa.visualization.Slider(
        name="Minimum Vision",
        value=1,
        min_value=0,
        max_value=5,
        step=1,
        description="Choose the minimum vision",
    ),
    "max_vision": mesa.visualization.Slider(
        name="Maximum Vision",
        value=6,
        min_value=5,
        max_value=10,
        step=1,
        description="Choose the maximum vision",
    ),
}


server = mesa.visualization.ModularServer(
    model_cls=SugarscapeCg, 
    visualization_elements=[canvas_element, chart_element], 
    name="Sugarscape 2 Constant Growback",
    model_params=model_params,
)
# server.launch()
