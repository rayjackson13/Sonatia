from db.projects import ProjectModel


def get_project_title(project: ProjectModel) -> str:
    return project.title if project.title else project.filename
