from fastapi import APIRouter

# --------- Setup data ---------
# load_dotenv(".env")
# db_url = os.environ["DB_URL"]
# engine = create_engine(db_url, echo=True)
# connection = engine.connect()


router = APIRouter(prefix="/crud", tags=["crud"])


@router.get("/restaurants")
def get_all():
    pass


@router.get("/restaurants/{id_}")
def get_by_id():
    pass


@router.post("/restaurants")
def create():
    pass


@router.patch("/restaurants/{id_}")
def update():
    pass


@router.delete("/restaurants/{id_}")
def delete():
    pass