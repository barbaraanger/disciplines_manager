from enum import Enum


class Status(Enum):
    PENDENTE = 'PENDENTE'
    APROVADO = 'APROVADO'

    @classmethod
    def from_string(cls, status_str):
        status_str_upper = status_str.upper()
        for status in cls:
            if status.value == status_str_upper:
                return status
        raise ValueError(f"No matching enum value for string: {status_str}")
