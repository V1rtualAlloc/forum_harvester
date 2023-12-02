from controller.base_controller import BaseController
from view.harvester_view import HarvesterView


class HarvesterController(BaseController):
    def __init__(self):
        super().__init__(HarvesterView(self, None), None, "Harvester")
        
    def switch_to_main_window(self):
        from controller.main_controller import MainController
        self.switch_window(MainController)