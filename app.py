from fastapi import status
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import Union
from typing import List
from db import  models, schemas
from db.db import SessionLocal, engine
from fastapi import File, UploadFile
from db import crud
import aiofiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(
    "/forms",
    status_code=status.HTTP_201_CREATED,
)
async def read_item(
    form: schemas.UserForm, 
    db: Session  = Depends(get_db),
):
    
    return await crud.create_user_form(db=db,form=form)
    
@app.get(
    "/forms",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.AllForm
)
async def read_item(
    db: Session  = Depends(get_db),
):
    
    result =  await crud.get_all_forms(db=db)

    return {
        "all_forms": result
    }

@app.post(
    "/items/uploadfile",
    status_code=status.HTTP_201_CREATED,
)
async def create_file(
    upfile:UploadFile = File(...) 
):
    async with aiofiles.open("uploaded_files/" + upfile.filename, 'wb') as out_file:
        content = await upfile.read()  # async read
        await out_file.write(content)  # async write
        return {"filename": upfile.filename}



if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
