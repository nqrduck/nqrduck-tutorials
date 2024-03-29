from nqrduck.module.module_controller import ModuleController

class TutorialsController(ModuleController):

    def __init__(self, module):
        """Initialize the controller."""
        super().__init__(module)

    def on_loading(self):
        """This method is called when the module is loaded."""
        pass