from datetime import datetime
from tempfile import NamedTemporaryFile
from unittest import TestCase

from antaukalkulo.antaukalkulo import Expense, ExpenseStore


class TestExpenseStore(TestCase):
    def setUp(self) -> None:
        self.storage_file = NamedTemporaryFile()
        self.expenses = [
            Expense(
                amount=10, description='foo bar', created_at=datetime.now(),
            ),
            Expense(
                amount=15, description='baz', created_at=datetime.now(),
            ),
        ]

    def test_writes_one_row_to_storage_file(self):
        store = ExpenseStore(self.storage_file.name)
        expense = self.expenses[0]
        store.add(expense)
        expected_content = (
            'Date,Description,Amount\n'
            f'{expense.created_at},{expense.description},{expense.amount}\n'
        )
        self.assertEqual(self.storage_file.read().decode(), expected_content,)

    def test_writes_multiple_rows_to_storage_file(self):
        store = ExpenseStore(self.storage_file.name)
        for e in self.expenses:
            store.add(e)
        self.assertEqual(
            self.storage_file.read().decode(), self.expected_content(),
        )

    def expected_content(self) -> str:
        lines = [
            'Date,Description,Amount',
            *((
                f'{e.created_at},'
                f'{e.description},'
                f'{e.amount}'
            ) for e in self.expenses)
        ]
        return '\n'.join(lines) + '\n'
