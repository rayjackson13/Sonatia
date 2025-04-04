from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

from PySide6.QtCore import QObject, Signal

# Define a generic type variable T
T = TypeVar("T")


class AbstractDBController(QObject, Generic[T]):
    @property
    @abstractmethod
    def data_updated(self) -> Signal:
        """Abstract property for database update signal."""
        pass

    @abstractmethod
    def create_table(self) -> None:
        """Abstract method to create a table."""
        pass

    @abstractmethod
    def insert_records(self, records: List[T]) -> None:
        """Abstract method to insert multiple records."""
        pass

    @abstractmethod
    def fetch_all(self, condition: str | None) -> List[T]:
        """Abstract method to fetch all records."""
        pass

    @abstractmethod
    def fetch_by_id(self, record_id: int) -> T:
        """Abstract method to fetch a record by its ID."""
        pass

    @abstractmethod
    def update_record(self, record: T) -> None:
        """Abstract method to update an existing record."""
        pass
    
    @abstractmethod
    def update_records(self, records: List[T]) -> None:
        """Abstract method to update multiple records."""
        pass

    @abstractmethod
    def delete_record(self, record_id: int) -> None:
        """Abstract method to delete a record by its ID."""
        pass

    @abstractmethod
    def close_connection(self) -> None:
        """Abstract method to close the database connection."""
        pass
