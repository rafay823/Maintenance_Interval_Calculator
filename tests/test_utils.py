from scheduler.utils import get_maintenance_intervals, calculate_next_maintenance
from models.vehicle import MaintenanceInterval
from unittest.mock import patch


def test_get_maintenance_intervals_with_predefined():
    # Assuming you have a predefined interval for VW Golf
    intervals = get_maintenance_intervals("VW", "Golf")
    assert intervals.intervals == {"Oil Change": 15000, "Inspection": 30000,"Brake Fluid": 40000}
def test_get_maintenance_intervals_with_custom():
    # Mock input to simulate user input for custom intervals

    with patch('builtins.input', side_effect=["30000", "40000", "50000"]):
        intervals = get_maintenance_intervals("VW", "Polo")
        assert intervals.intervals == {
            "Oil Change": 30000,
            "Inspection": 40000,
            "Brake Fluid": 50000
        }
def test_calculate_next_maintenance():
    intervals = MaintenanceInterval(intervals={"Oil Change": 15000, "Inspection": 30000})
    upcoming_maintenance = calculate_next_maintenance(10000, intervals)

    assert upcoming_maintenance["Oil Change"] == 5000
    assert upcoming_maintenance["Inspection"] == 20000
