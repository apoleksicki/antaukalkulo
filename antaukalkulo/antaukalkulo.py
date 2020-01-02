import csv
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Expense:
    amount: float
    description: str
    created_at: datetime


class ExpenseStore:
    FIELDNAMES = ['Date', 'Description', 'Amount']
    
    def __init__(self, storage_file_name: str) -> None:
        self._storage_file_name = storage_file_name
        self._initialized = False

    def add(self, expense: Expense) -> None:
        if not self._initialized:
            self._initialize()

        with open(self._storage_file_name, 'a+',) as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=self.FIELDNAMES, lineterminator='\n',
            )
            writer.writerow(
                {
                    'Date': expense.created_at,
                    'Description': expense.description,
                    'Amount': expense.amount,
                },
            )

    def _initialize(self) -> None:
        with open(self._storage_file_name, 'r') as storage:
            header_line = storage.readline()

        if header_line != self._build_header_row():
            with open(self._storage_file_name, 'w') as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=self.FIELDNAMES, lineterminator='\n',
                )
                writer.writeheader()
        self._initialized = True

    @classmethod
    def _build_header_row(cls) -> str:
        return ','.join(cls.FIELDNAMES) + '\n'
