from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


data_base_url="mysql+pymysql://root:Harsha%40345@localhost/task_manager"

engine=create_engine(data_base_url)

SessionLocal=sessionmaker(
    autocomit=True,
    autoflush=False,
    bind=engine
)

Base=declarative_base()