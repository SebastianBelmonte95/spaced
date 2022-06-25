class NoSlotsAvailableException(Exception):
    def __init__(self, entity) -> None:
        self.entity = entity
        super().__init__(
            f"{entity} has no available module slots. Uninstall a module or upgrade the entity's frame."
        )
