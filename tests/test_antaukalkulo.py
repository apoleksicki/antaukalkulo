from datetime import datetime
from unittest import TestCase

from antaukalkulo.antaukalkulo import Expense


class TestExpense(TestCase):
    def test_takes_init_parameters(self) -> None:
        Expense(amount=10, description='foo bar', created_at=datetime.now())
