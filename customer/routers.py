from fastapi import FastAPI,APIRouter,Depends,status,Response,HTTPException
import schemas,database,models
from sqlalchemy.orm import Session
from database import SessionLocal, engine,get_database
from customers import get_all,create_customers,get_customer_by_id,delete_customer,update_customer_by_id

router=APIRouter(
        prefix="/customer"

)

#to get all customer details
@router.get('/')
def get_customers(db: Session= Depends(get_database)):
    return get_all(db)
    

#to insert customer
@router.post('/',status_code=status.HTTP_201_CREATED)
def post_customer(request: schemas.Customer,db: Session= Depends(get_database)):
    return create_customers(request, db)




#to get customer by id
@router.get('/{id}',status_code=200)
def get_by_id(id:int,db: Session= Depends(get_database)):
    return get_customer_by_id(id,db)

#to delete a customer
@router.delete('/customer/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int,db: Session= Depends(get_database)):
     delete_customer(id,db)
     return Response(status_code=status.HTTP_204_NO_CONTENT)

# update customer      
@router.put('/customer/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Customer,db: Session= Depends(get_database)):
    return update_customer_by_id(id,request,db)


        
       
    



