import pytest
from models.vehicle import VehicleData
from pydantic import ValidationError

def test_vehicle_data_valid():
    vehicle = VehicleData(make="VW", model="Golf", year="2020", current_mileage=15000)
    assert vehicle.make == "VW"
    assert vehicle.model == "Golf"
    assert vehicle.year == "2020"
    assert vehicle.current_mileage == 15000

def test_vehicle_data_invalid_mileage():
    with pytest.raises(ValidationError):
        VehicleData(make="VW", model="Golf", year="2020", current_mileage="invalid")
