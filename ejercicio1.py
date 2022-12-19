class Nonogram:

    def __init__(self, clues):
        self.clues = clues
        self.rows = len(clues[0])
        self.cols = len(clues[1])
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def solve(self):
        self.eliminar_imposibles_soluciones()
        self.deduce_information()
        return self.grid
    
    def eliminar_imposibles_soluciones(self):
        # implementar lógica para eliminar soluciones imposibles 
        pass
    
    def deduce_information(self):
        # implementar lógica para deducir información 
        pass