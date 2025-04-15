import sqlite3
import os
from datetime import datetime
from PySide6.QtCore import Signal

from models.project import ProjectModel

from .controller import AbstractDBController

DB_PATH = "db/main.db"


class ProjectDBController(AbstractDBController[ProjectModel]):
    data_updated = Signal()

    def __init__(self):
        """Initialize the database connection and cursor."""
        super().__init__()
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
        """Create the projects table."""
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    filename TEXT NOT NULL,
                    path TEXT NOT NULL UNIQUE,
                    folder_path TEXT NOT NULL,
                    title TEXT,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            )
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_records(self, projects: list[ProjectModel], no_commit=False):
        """Insert a project into the database."""
        try:
            sql = """
                INSERT OR IGNORE INTO projects (filename, path, folder_path, title, updated_at)
                VALUES (?, ?, ?, ?, ?)
            """
            data = [
                (
                    project.filename,
                    project.path,
                    project.folder_path,
                    project.title,
                    project.updated_at or datetime.now(),
                )
                for project in projects
            ]
            self.cursor.executemany(sql, data)
            if no_commit == False:
                self.connection.commit()
                self.data_updated.emit()
        except sqlite3.Error as e:
            print(f"Error inserting project: {e}")

    def fetch_all(self, condition: str | None) -> list[ProjectModel]:
        """Fetch all projects from the database and return as a list of FileModels."""
        try:
            sql = "SELECT id, filename, path, folder_path, title, `updated_at` FROM projects"
            if condition:
                sql += f" WHERE {condition}"
            sql += " ORDER BY updated_at DESC"

            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return [
                ProjectModel(
                    file_id=row[0],
                    filename=row[1],
                    path=row[2],
                    folder_path=row[3],
                    title=row[4],
                    updated_at=row[5],
                )
                for row in rows
            ]
        except sqlite3.Error as e:
            print(f"Error fetching projects: {e}")
            return []

    def fetch_by_id(self, id: int) -> ProjectModel:
        """Fetch all projects from the database and return as a list of FileModels."""
        try:
            sql = """
                SELECT id, filename, path, folder_path, title, updated_at 
                FROM projects
                WHERE id = ?
                ORDER BY updated_at DESC
            """
            self.cursor.execute(sql, (id,))
            row = self.cursor.fetchone()
            return ProjectModel(
                file_id=row[0],
                filename=row[1],
                path=row[2],
                folder_path=row[3],
                title=row[4],
                updated_at=row[5],
            )
        except sqlite3.Error as e:
            print(f"Error fetching projects: {e}")
            return []

    def update_record(self, file: ProjectModel):
        """Update project's information."""
        try:
            sql = """
                UPDATE projects
                SET title = ?, updated_at = ?
                WHERE id = ?
            """
            self.cursor.execute(
                sql, (file.title, datetime.now(), file.id)
            )
            self.connection.commit()
            self.data_updated.emit()
        except sqlite3.Error as e:
            print(f"Error updating project: {e}")
            
    def update_records(self, records: list[ProjectModel], no_commit=False):
        """Update project's information."""
        try:
            sql = """
                UPDATE projects
                SET filename = ?, updated_at = ?
                WHERE path = ?
            """
            self.cursor.executemany(
                sql, [(file.filename, file.updated_at or datetime.now(), file.path) for file in records]
            )
            if no_commit == False:
                self.connection.commit()
                self.data_updated.emit()
        except sqlite3.Error as e:
            print(f"Error updating project: {e}")

    def delete_record(self, project_id):
        """Delete project from the database by ID."""
        try:
            sql = "DELETE FROM projects WHERE id = ?"
            self.cursor.execute(sql, (project_id,))
            self.connection.commit()
            self.data_updated.emit()
        except sqlite3.Error as e:
            print(f"Error deleting project: {e}")
            
    def commit(self):
        self.connection.commit()
        self.data_updated.emit()

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
