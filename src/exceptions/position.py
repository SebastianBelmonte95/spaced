class NoPositionException(Exception):
    def __init__(self, entity) -> None:
        self.entity = entity
        super().__init__(f"{entity} has no position. Use {entity}.set_position()")
