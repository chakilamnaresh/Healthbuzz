mkdir healthbuzz


cd healthbuzz

python -m venv myvenv
source myvenv/scripts/activate.bat

pip install fastapi
pip install psycopg2-binary
pip install uvicorn
pip install alembic  


alembic init migrations


alembic revision --autogenerate -m "creating patients table"



