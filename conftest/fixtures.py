from menu_app.models import IceCreamInfo
import pytest

@pytest.fixture
def ice_cream_data():
    IceCreamInfo.objects.create(
        ice_cream_flavour='Chocolate',
        ice_cream_name='Choco Blast',
        ice_cream_weight=100
    )