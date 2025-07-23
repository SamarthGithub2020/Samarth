from app import app

def test_conn():
    response=app.test_client().get("/")
    
    assert response.status_code==200
    assert response.data=="WELCOME TO THE HOME PAGE!!"