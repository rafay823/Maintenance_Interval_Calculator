from models.vehicle import MaintenanceInterval

MAINTENANCE_INTERVALS = {
    "VW Golf": {"2019": MaintenanceInterval(intervals={"Oil Change": 15000, "Inspection": 30000, "Brake Fluid": 40000}),
                "2020": MaintenanceInterval(
                    intervals={"Oil Change": 15000, "Inspection": 30000, "Brake Fluid": 40000})},
    "Mercedes C-Class": {
        "2019": MaintenanceInterval(intervals={"Oil Change": 20000, "Inspection": 40000, "Brake Fluid": 60000}),
        "2020": MaintenanceInterval(intervals={"Oil Change": 20000, "Inspection": 40000, "Brake Fluid": 60000})}
}
