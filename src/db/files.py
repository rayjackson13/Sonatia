import sqlite3
import os
from datetime import datetime

from models.file import FileModel

DB_PATH = "db/files.db"


class FileDBController:
    _instance = None  # Singleton instance

    def __new__(cls):
        """Create or return the singleton instance."""
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Initialize the database connection and cursor."""
        try:
            os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
            self.connection = sqlite3.connect(DB_PATH)
            self.cursor = self.connection.cursor()
            self.create_table()
        except sqlite3.Error as e:
            print(f"Error initializing the database: {e}")
            self.connection = None
            self.cursor = None

    def create_table(self):
        """Create the files table."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS files (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    path TEXT NOT NULL UNIQUE,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_files(self, files: list[FileModel]):
        """Insert a file into the database."""
        try:
            print(files[0])
            sql = """
                INSERT OR IGNORE INTO files (name, path, updated_at)
                VALUES (?, ?, ?)
            """
            data = [(file.name, file.path, file.updated_at or datetime.now()) for file in files]
            self.cursor.executemany(sql, data)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error inserting file: {e}")

    def get_all_files(self) -> list[FileModel]:
        """Fetch all files from the database and return as a list of FileModels."""
        try:
            sql = "SELECT id, name, path, updated_at FROM files"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return [FileModel(file_id=row[0], name=row[1], path=row[2], updated_at=row[3]) for row in rows]
        except sqlite3.Error as e:
            print(f"Error fetching files: {e}")
            return []

    def update_file(self, file: FileModel):
        """Update file's information."""
        try:
            sql = """
                UPDATE files
                SET name = ?, path = ?, updated_at = ?
                WHERE id = ?
            """
            self.cursor.execute(sql, (file.name, file.path, file.updated_at or datetime.now(), file.id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error updating file: {e}")

    def delete_file(self, file_id):
        """Delete file from the database by ID."""
        try:
            sql = "DELETE FROM files WHERE id = ?"
            self.cursor.execute(sql, (file_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting file: {e}")

    def close_connection(self):
        """Close the database connection."""
        try:
            if self.connection:
                self.cursor.close()
                self.connection.close()
                self.connection = None
                self.cursor = None
                FileDBController._instance = None  # Reset the singleton instance
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")