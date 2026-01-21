from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://test:test123@localhost/healthbuzz"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine,autoflush=False)