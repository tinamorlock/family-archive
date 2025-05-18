from app.db import Base
from app.db import engine
import app.models.persons

Base.metadata.drop_all(bind=engine)
print("✅ All tables dropped.")
