from controller.base_controller import BaseController
from view.data_analyzer_view import DataAnalyzerView


class DataAnalyzerController(BaseController):
    def __init__(self):
        super().__init__(DataAnalyzerView(self, None), None, "Data Analyzer")
        
    def switch_to_main_window(self):
        from controller.main_controller import MainController
        self.switch_window(MainController)