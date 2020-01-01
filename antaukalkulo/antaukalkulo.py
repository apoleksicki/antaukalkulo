from dataclasses import dataclass
from datetime import datetime


@dataclass
class Expense:
    amount: float
    description: str
    created_at: datetime
