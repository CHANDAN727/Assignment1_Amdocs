from sqlalchemy.orm import Session
import models,schemas
from fastapi import status,HTTPException


def get_all(db:Session):
    all_customers=db.query(models.Customer).all()
    return all_customers

def create_customers(request: schemas.Customer,db: Session):
    new_customer = models.Customer(
                                first_name=request.first_name,
                                last_name=request.last_name,
                                email=request.email,
                                customer_type=request.customer_type,
                                # created_on=request.created_on,
                               )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def get_customer_by_id(id:int,db: Session):
    customer=db.query(models.Customer).get(id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Customer with id {id} is not found')
       
    return customer

def delete_customer(id:int,db: Session):
    customer=db.query(models.Customer).get(id)
    if not customer:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Customer with id {id} is not availble ')
    
    db.delete(customer)
    db.commit()  
    
  
            
   
def update_customer_by_id(id:int,request: schemas.Customer,db: Session):

    customer=db.query(models.Customer).filter(models.Customer.id == id)
    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(request, key, value)

    if not customer.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Customer with id {id} is not availble ')

    customer.update(update_data)
    db.commit()

    return f'Customer With Id {id} Details Updated Succesfully'

