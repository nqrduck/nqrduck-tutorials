from nqrduck.module.module_view import ModuleView
from .widget import Ui_Form
from  PyQt6.QtWidgets import QWidget


class TutorialsView(ModuleView):

    def __init__(self, module):
        super().__init__(module)

        widget = QWidget()
        self._ui_form = Ui_Form()
        self._ui_form.setupUi(self)
        self.widget = widget