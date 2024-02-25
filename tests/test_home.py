def test_index(client):
    # Have it send req to my index
    response = client.get("/")
    # b because response.data is a bytes type
    assert b"<title>Home - Flask Reports</title>" in response.data