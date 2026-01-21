from sqlalchemy import String,Date,Boolean,DateTime
from sqlalchemy.orm import Mapped,mapped_column
from datetime import datetime,date
from app.db.base import Base

class Patient(Base):
    __tablename__ = "patients_data"


    ids:Mapped[int] = mapped_column(primary_key=True)
    first_name:Mapped[str] = mapped_column(String(100))
    last_name:Mapped[str] = mapped_column(String(100))
    dob:Mapped[date] = mapped_column(Date)
    gender: Mapped[str] = mapped_column(String(10))

