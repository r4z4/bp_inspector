from flask_reports.models.db import Color

def test_writer(client):
    # Have it send req to my index
    response = client.get("/gemma/writer")
    # b because response.data is a bytes type
    assert b"<title>Gemma - Flask Reports</title>" in response.data

def test_form_get(client):
    # Have it send req to my index
    response = client.get("/gemma/writer/form")
    # b because response.data is a bytes type
    assert b'<form id="writer_form" method="POST" action="/gemma/writer/submit">' in response.data

# def test_post(client, app):
#     # response = client.post("/gemma/writer/submit", data={"email": "test@test.com", "password": "test_pass"})
#     response = client.post("/gemma/writer/submit", data={"name": "PERIWINKLE", "rbg": "#CCCCFF"})
#     # Verify this gets added to DB
#     with app.app_context():
#         # We 
#         assert Color.query.last().name == "PERIWINKLE"