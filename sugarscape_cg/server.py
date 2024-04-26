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
    "initial_population": 100,
    "stay": mesa.visualization.Choice(
        name="Can an ant stay in place",
        value="Yes",
        choices=["Yes", "No"], 
    )

}


server = mesa.visualization.ModularServer(
    model_cls=SugarscapeCg, 
    visualization_elements=[canvas_element, chart_element], 
    name="Sugarscape 2 Constant Growback",
    model_params=model_params,
)
# server.launch()
