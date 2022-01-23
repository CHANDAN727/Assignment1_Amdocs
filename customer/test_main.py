from fastapi.testclient import TestClient
import datetime
from main import app

client = TestClient(app)

data= {
        'created_on':"test",
        'customer_type': 'Test',
        'email': 'test@gmail.com',
        'first_name': 'Chandan',
        'id': 1,
        'last_name': 'Panda',
          }


def test_read_main():
    response = client.post("/customer/",json=data)
   
    assert response.status_code == 201
    assert response.json() == data
  

def test_get():
    response = client.get("/customer/",json=data)
   
    assert response.status_code == 200
   