from controller.base_controller import BaseController
from view.main_view import MainView


class MainController(BaseController):
    def __init__(self):
        super().__init__(MainView(self, None), None, name="Main")

    def switch_to_harvester_window(self):
        from controller.harvester_controller import HarvesterController
        self.switch_window(HarvesterController)

    def switch_to_data_analyzer_window(self):
        from controller.data_analyzer_controller import DataAnalyzerController
        self.switch_window(DataAnalyzerController)

