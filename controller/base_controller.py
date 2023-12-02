class BaseController:
    def __init__(self, view, model, name=None):
        self.view = view
        self.model = model
        self.name = name

    def run(self):
        if self.view and not self.view.is_running():
            print("Starting", self.name)
            self.view.run()
    
    def stop(self):
        if self.view and self.view.is_running():
            self.view.stop()
            print("Stopping", self.name)

    def switch_window(self, controller_class):
        if controller_class:
            next_controller = controller_class()
            self.stop()
            next_controller.run()

