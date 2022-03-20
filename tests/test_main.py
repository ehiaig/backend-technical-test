import json
import pytest


payload = {
    "patient_uuid": "8faafa6e-c19a-4dd1-b5b0-e1d55f9464d7",
    "value": 1.6,
    "unit": "mmol/L",
    "recorded_at": "2022-02-19T20:21:44.061000"
}
invalid_payload = {
    "patient_id": "8faafa6e-c19a-4dd1-b5b0-e1d55f9464d7",
    "value": 1.6,
    "unit": "mmol/L",
    "recorded_at": "2022-02-19T20:21:44.061000"
}
new_payload = {
    "patient_uuid": "6d42d8f7-81cb-43c9-a9f9-f6bfd7a11a49",
    "value": 4.5,
    "unit": "mg/dL",
    "recorded_at": "2022-05-19T20:21:44.061000"
}

def test_welcome(client):
    response = client.get("/v1")
    assert response.status_code == 200
    assert response.json() == {"msg": "The Blood Glucose Readings API."}
    

def test_create_reading(client):
    response = client.post("/v1/reading", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert payload["patient_uuid"] == data["patient_uuid"]
    assert payload["value"] == data["value"]
    assert payload["unit"] == data["unit"]
    assert payload["recorded_at"] == data["recorded_at"]
    

def test_create_reading_with_invalid_request(client):
    response = client.post("/v1/reading", json=invalid_payload)
    assert response.status_code == 400
    assert response.json() == "Invalid request"


def test_get_reading(client):
    response = client.post("/v1/reading", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    reading_id = data["reading_uuid"]
    response = client.get(f"/v1/reading/{reading_id}")
    assert response.status_code == 200


def test_get_reading_not_found(client):
    reading_id = "f62bbd3d-ebcb-458d-8c2f-5fc45c7a7d4c"
    response = client.get(f"/v1/reading/{reading_id}")
    assert response.status_code == 404
    assert response.json() == "Reading not found"


def test_get_all_readings(client):
    response_1 = client.post("/v1/reading", json=payload)
    assert response_1.status_code == 201

    payload_2 = {
        "patient_uuid": "9faafa6e-c19a-4dd1-b5b0-e1d55f9464d1",
        "value": 3.5,
        "unit": "mmol/L",
        "recorded_at": "2022-03-19T20:21:44.061000"
    }
    response_2 = client.post("/v1/reading", json=payload_2)
    assert response_2.status_code == 201

    response = client.get("/v1/reading")
    assert response.status_code == 200
    data  = response.json()
    assert len(data) == 2
    assert data[0]["patient_uuid"] == payload["patient_uuid"]
    assert data[1]["patient_uuid"] == payload_2["patient_uuid"]
    

def test_delete_reading(client):
    #Create reading
    response = client.post("/v1/reading", json=payload)
    assert response.status_code == 201
    
    #delete reading
    data = response.json()
    reading_id = data["reading_uuid"]
    deleted_response = client.delete(f"/v1/reading/{reading_id}")
    assert deleted_response.status_code == 204
    assert deleted_response.json() == "Reading deleted successfully"


def test_delete_reading_not_found(client):
    reading_id = "35530010-9bbc-49fc-add1-528afbb56830"
    deleted_response = client.delete(f"/v1/reading/{reading_id}")
    assert deleted_response.status_code == 404
    assert deleted_response.json() == "Reading not found"


def test_update_reading(client):
    response = client.post("/v1/reading", json=payload)
    assert response.status_code == 201
    
    data = response.json()

    reading_id = data["reading_uuid"]
    update_response = client.put(f"/v1/reading/{reading_id}", data=json.dumps(new_payload))
    assert update_response.status_code == 204
    assert update_response.json() == "Reading updated successfully"

@pytest.mark.parametrize(
    "update_payload", [
        {"patient_uuid": "31a8a2bc-a4f7-4c90-9a33-2cc64a9422a2"},
        {"value": 6.3},
        {"recorded_at": "2021-05-19T20:21:44.061000", "patient_uuid": "31a8a2bc-a4f7-4c90-9a33-2cc64a9422a2"},
        {"unit": "mmol/L"},
    ]
)
def test_update_reading_with_vary_parameters(client, update_payload):
    response = client.post("/v1/reading", json=payload)
    assert response.status_code == 201
    
    data = response.json()

    reading_id = data["reading_uuid"]
    update_response = client.put(
        f"/v1/reading/{reading_id}", 
        data=json.dumps(update_payload)
    )
    assert update_response.status_code == 204
    assert update_response.json() == "Reading updated successfully"


def test_update_reading_not_found(client):
    reading_id = "35530010-9bbc-49fc-add1-528afbb56830"
    response = client.put(f"/v1/reading/{reading_id}", data=json.dumps(new_payload))
    assert response.status_code == 404
    assert response.json() == "Reading not found"
