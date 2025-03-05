import pytest


@pytest.mark.django_db
def test_add_item_with_valid_data(client):
    dict_data ={
        "ice_cream_flavour":"Chocolate",
        "ice_cream_name":"ChocoBlast",
        "ice_cream_weight":100
    }
    response = client.post('/menu-app/add-item/',data = dict_data)
    expected_data = {
        "ice_cream_flavour": "Chocolate",
        "ice_cream_name": "Choco Blast",
        "ice_cream_weight": 100.0
    }
