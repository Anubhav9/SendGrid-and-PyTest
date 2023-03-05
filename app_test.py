from app import createEmail

def test_positive_scenario():
    response=createEmail("Hello","hello@gmail.com")
    assert response==202,"Status Code not matching"

def test_negative_scenario_empty_receipent_email():
    response=createEmail("Hello","")
    assert response==400,"Status Code not matching"

def test_negative_scenario_empty_body():
    response=createEmail("","hello@gmail.com")
    assert response==400,"Status Code not matching"


def test_negative_scenario_empty_all():
    response=createEmail("","")
    assert response==400,"Status Code not matching"