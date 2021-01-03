from rich.console import Console
from rich.table import Table

class AoCDay:
    year = 0
    day = 0
    input = None
    part_one = 0
    part_two = 0
    start = None
    end = None

    def __init__(self, year, day):
        self.year = year
        self.day = day
        self.input = "data.txt"

    def lines(self):
        return open(self.input).readlines()

    def print(self):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Part 1", justify="center")
        table.add_column("Part 2", justify="center")
        table.add_column("Execution time", justify="center")
        table.add_row(str(self.part_one), str(self.part_two), str(round((self.end - self.start) * 1000, 3)) + "ms")
        console.print(table)
