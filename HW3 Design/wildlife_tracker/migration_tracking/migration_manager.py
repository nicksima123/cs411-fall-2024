from typing import Optional


class MigrationManager:
    migrations: dict[int, Migration] = {}
    paths: dict[int, MigrationPath] = {}
    pass
