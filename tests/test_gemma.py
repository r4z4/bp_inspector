def test_writer(client):
    # Have it send req to my index
    response = client.get("/gemma/writer")
    # b because response.data is a bytes type
    assert b"<title>Gemma - Flask Reports</title>" in response.data