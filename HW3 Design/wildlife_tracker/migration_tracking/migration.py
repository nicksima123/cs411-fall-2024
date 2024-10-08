from typing import Any

class Migration:
    current_date: int
    migration_id: int
    migration_path: MigrationPath
    status: str = "Scheduled"
    start_date: str
    pass