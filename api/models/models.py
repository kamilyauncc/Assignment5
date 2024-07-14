from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="sandwich")
    sandwich_details= relationship("SandwitchDetail", back_populates="sandwich")


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="resource")


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")


class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, index=True, nullable=False)

    sandwich = relationship("Sandwich", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")

    class IngredientsDetail(Base):
        __tablename__ = "ingredients_details"

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        ingredients_id = Column(Integer, ForeignKey("ingredients.id"))
        sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
        amount = Column(Integer, index=True, nullable=False)

        sandwich = relationship("Sandwich", back_populates="ingredients_details")
        ingredients = relationship("Ingredients", back_populates="ingredients_details")

    class Resouces(Base):
        __tablename__ = "resouces_details"

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        resouces_id = Column(Integer, ForeignKey("resouces.id"))
        sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
        amount = Column(Integer, index=True, nullable=False)

        sandwich = relationship("Sandwich", back_populates="resouces_details")
        ingredients = relationship("Ingredients", back_populates="resouces_details")


class Recipes:(Base):
    __tablename__ = "recipes_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    recipes_id = Column(Integer, ForeignKey("recipes.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, index=True, nullable=False)

    sandwich = relationship("Sandwich", back_populates="recipes_details")
    ingredients = relationship("Ingredients", back_populates="recipes_details")


class Order_details:
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("order_details.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, index=True, nullable=False)

    sandwich = relationship("Sandwich", back_populates="order_details")
    ingredients = relationship("Ingredients", back_populates="order_details")