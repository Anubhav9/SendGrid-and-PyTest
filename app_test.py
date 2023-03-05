from app import create_email

def test_positive_scenario():
    response=create_email("Hello","hello@gmail.com")
    assert response==202,"Status Code not matching"

def test_negative_scenario_empty_receipent_email():
    response=create_email("Hello","")
    assert response==400,"Status Code not matching"

def test_negative_scenario_empty_body():
    response=create_email("","hello@gmail.com")
    assert response==400,"Status Code not matching"


def test_negative_scenario_empty_all():
    response=create_email("","")
    assert response==400,"Status Code not matching"
