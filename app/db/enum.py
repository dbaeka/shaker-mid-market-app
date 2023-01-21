from enum import Enum


class Flavors(str, Enum):
    postgres = "postgresql"
    mysql = "mysql"
    sqlite = "sqlite"
