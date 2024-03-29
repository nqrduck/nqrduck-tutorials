from nqrduck.module.module import Module
from .model import TutorialsModel
from .view import TutorialsView
from .controller import TutorialsController

Tutorials = Module(TutorialsModel, TutorialsView, TutorialsController)