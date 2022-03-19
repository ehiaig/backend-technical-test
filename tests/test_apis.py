def test_welcome(client):
    response = client.get("/v1")
    assert response.status_code == 200
    assert response.json() == {"msg": "The Blood Glucose Readings API."}


def test_create_reading(client):
    payload = {
        "patient_uuid": "8faafa6e-c19a-4dd1-b5b0-e1d55f9464d7",
        "value": 1.6,
        "unit": "mmol/L",
        "recorded_at": "2022-02-19T20:21:44.061000"
    }
    response = client.post("/v1/reading", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert payload["patient_uuid"] == data["patient_uuid"]
    assert payload["value"] == data["value"]
    assert payload["unit"] == data["unit"]
    assert payload["recorded_at"] == data["recorded_at"]
