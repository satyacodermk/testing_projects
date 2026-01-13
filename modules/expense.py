class Expense:
    """Represents a single expense entry."""

    def __init__(self, amount: float, category: str, date: str):
        self.amount = amount
        self.category = category
        self.date = date

    def to_file_string(self) -> str:
        """Convert expense to string for file storage."""
        return f"{self.amount},{self.category},{self.date}\n"

    @staticmethod
    def from_file_string(line: str):
        """Create Expense object from file line."""
        amount, category, date = line.strip().split(',')
        return Expense(float(amount), category, date)

    def __str__(self):
        return f"{self.amount:<10.2f} {self.category:<15} {self.date}"