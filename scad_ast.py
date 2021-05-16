from enum import Enum

class ScadAstTypes(Enum):
    GLOBAL_VAR = 0
    MODULE = 1
    FUNCTION = 2
    USE = 3
    INCLUDE = 4
    PARAMETER = 5

class ScadAstObject:
    def __init__(self, scadType):
        self.scadType = scadType

    def getType(self):
        return self.scadType

class ScadUse(ScadAstObject):
    def __init__(self, filename):
        super().__init__(ScadAstTypes.USE)
        self.filename = filename

class ScadInclude(ScadAstObject):
    def __init__(self, filename):
        super().__init__(ScadAstTypes.INCLUDE)
        self.filename = filename

class ScadGlobalVar(ScadAstObject):
    def __init__(self, name):
        super().__init__(ScadAstTypes.GLOBAL_VAR)
        self.name = name

class ScadCallable(ScadAstObject):
    def __init__(self, name, parameters, scadType):
        super().__init__(scadType)
        self.name = name
        self.parameters = parameters

    def __repr__(self):
        return f'{self.name} ({self.parameters})'

class ScadModule(ScadCallable):
    def __init__(self, name, parameters):
        super().__init__(name, parameters, ScadAstTypes.MODULE)

class ScadFunction(ScadCallable):
    def __init__(self, name, parameters):
        super().__init__(name, parameters, ScadAstTypes.FUNCTION)

class ScadParameter(ScadAstObject):
    def __init__(self, name, optional=False):
        super().__init__(ScadAstTypes.PARAMETER)
        self.name = name
        self.optional = optional

    def __repr__(self):
        return self.name + "=..." if self.optional else  self.name
