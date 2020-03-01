from catalog.command.configs.database import DATABASE


class BaseRepository:
    _entity = None

    def __init__(self):
        self.session = DATABASE.session

    def get(self, id):
        try:
            return self.session.query(self._entity).get(id)
        except Exception as e:
            self.session.rollback()

            raise e

    def create(self, entity):
        return self.__save(entity)

    def update(self, entity):
        return self.__save(entity)

    def __save(self, entity):
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.flush()

            return entity
        except Exception as e:
            self.session.rollback()

            raise e
