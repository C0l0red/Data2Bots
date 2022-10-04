import enum


class ElementType(enum.Enum):
    STRING = 'string'
    INTEGER = 'integer'
    BOOLEAN = 'boolean'
    ENUM = 'enum'
    ARRAY = 'array'
    OBJECT = 'object'
