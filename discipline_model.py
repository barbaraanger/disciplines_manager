from status import Status


class Discipline:
    def __init__(self, name, status=Status.PENDENTE):
        self.name = name
        self.status = status
