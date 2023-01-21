from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils import get_root_dir
from .enum import Flavors
from ..core.config import settings

options = {
    "pool_pre_ping": False,
    "connect_args": {
        "check_same_thread": False
    }
}

db_flavor = settings.DATABASE_FLAVOR

if db_flavor is Flavors.postgres:
    options["pool_pre_ping"] = True

sql_uri = settings.SQLALCHEMY_DATABASE_URI
if sql_uri is None:
    project_dir = get_root_dir()
    db_dir = project_dir.joinpath('storage/db/sql_app.db')
    sql_uri = ''.join(['sqlite:///', db_dir])

engine = create_engine(sql_uri, **options)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
