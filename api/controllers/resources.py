from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create_recipes(db: Session, resouces, db_recipes=None):
    # Create a new instance of the Resouces model with the provided data
    db_names = models.Resouces(
        ingredients_name =resouces.name,
        description =resouces.description
    )
    # Add the newly created Recipes object to the database session
    db.add(db_recipes)
    # Commit the changes to the database
    db.commit()
    # Refresh the Recipes object to ensure it reflects the current state in the database
    db.refresh(db_recipes)
    # Return the newly created Recipes object
    return db_recipes


def read_all(db: Session):
    return db.query(models.Recipes).all()


def read_one(db: Session, recipes_id):
    return db.query(models.Recipes).filter(models.Recipes.id ==recipes_id).first()


def update(db: Session, recipes_id, recipes):
    # Query the database for the specific recipes to update
    db_recipes = db.query(models.Recipes).filter(models.Recipes.id == recipes_id)
    # Extract the update data from the provided 'recipes' object
    update_data = recipes.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_recipes.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated recipes record
    return db_recipes.first()


def delete(db: Session, recipes_id):
    # Query the database for the specific recipes to delete
    db_recipes = db.query(models.Recipes).filter(models.Recipes.id == recipes_id)
    # Delete the database record without synchronizing the session
    db_recipes.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
