from typing import Optional

class MigrationPath:
    path_id: int
    current_location: str
    destination: Habitat
    duration: Optional[int] = None
    species: str
    start_location: Habitat
    pass