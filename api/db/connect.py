from sqlalchemy.orm import create_session, sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine



DB_URL="sqlite:///weather.db"
Base = declarative_base()

db_engine = create_engine(url=DB_URL)
SessionLocal = sessionmaker(bind=db_engine, autoflush=False, autocommit=False)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:    
        db.close()
    
        