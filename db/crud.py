from sqlalchemy.orm import Session

from db import models, schemas


async def create_user_form(db: Session, form: schemas.UserForm):
    db_user = models.UserForm(form=form.form)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

async def get_all_forms(db: Session):
    return  db.query(
        models.UserForm
    ).all()
    