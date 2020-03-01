class ValidatorError(Exception):
    def __init__(self, message, errors):
        super()

        self.errors = errors


class ObjectDoesNotExistError(Exception):
    def __init__(self, object_name=None):
        super()

        self.object_name = object_name.lower()
