from fixtures import ice_cream_data
import pytest
from menu_app.models import IceCreamInfo

@pytest.mark.django_db
def test_list_items_with_data(client,ice_cream_data):
    response = client.get('/menu-app/menu-data/')
    response_data = response.json()
    print(8,response_data)
    ice_cream_item = response_data["ice cream details"][0]
    expected_output = {
        "ice_cream_flavour": "Chocolate",
        "ice_cream_name": "Choco Blast",
        "ice_cream_weight": 100
    }
    assert expected_output["ice_cream_flavour"] == ice_cream_item["ice_cream_flavour"]
    assert expected_output["ice_cream_name"] == ice_cream_item["ice_cream_name"]
    assert expected_output["ice_cream_weight"] == ice_cream_item["ice_cream_weight"]

@pytest.mark.django_db
def test_list_items_with_empty_data(client,ice_cream_data):
    IceCreamInfo.objects.all().delete()
    response = client.get('/menu-app/menu-data/')
    response_data = response.json()
    assert len(response_data['ice_cream_details']) == 0