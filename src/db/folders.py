import sqlite3
import os

from models.folder import FolderModel

DB_PATH = "db/folders.db"


class FolderDBController:
    def __init__(self):
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
        """Create the folders table."""
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS folders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    path TEXT NOT NULL UNIQUE
                )
            """
            )
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_folders(self, folders: list[FolderModel]):
        """Insert a folder into the database."""
        try:
            sql = """
                INSERT OR IGNORE INTO folders (path)
                VALUES (?)
            """
            data = [(folder.path,) for folder in folders]
            self.cursor.executemany(sql, data)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error inserting folder: {e}")

    def get_all_folders(self) -> list[FolderModel]:
        """Fetch all folders from the database and return as a list of FolderModel."""
        try:
            sql = "SELECT id, path FROM folders"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return [FolderModel(folder_id=row[0], path=row[1]) for row in rows]
        except sqlite3.Error as e:
            print(f"Error fetching folders: {e}")
            return []

    def delete_folder(self, folder_id):
        """Delete folder from the database by ID."""
        try:
            sql = "DELETE FROM folders WHERE id = ?"
            self.cursor.execute(sql, (folder_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting folder: {e}")

    def close_connection(self):
        """Close the database connection."""
        try:
            if self.connection:
                self.cursor.close()
                self.connection.close()
                self.connection = None
                self.cursor = None
        except sqlite3.Error as e:
            print(f"Error closing the database connection: {e}")
