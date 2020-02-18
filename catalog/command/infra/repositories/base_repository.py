from catalog.command.configs.database import DATABASE


class BaseRepository:
    _entity = None

    def __init__(self):
        self.session = DATABASE.session

    def create(self, entity):
        return self.__save(entity)

    def update(self, entity):
        return self.__save(entity)

    def __save(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.flush()

        return entity
