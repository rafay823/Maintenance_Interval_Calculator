from models.vehicle import MaintenanceInterval

MAINTENANCE_INTERVALS = {
    "VW Golf": MaintenanceInterval(intervals={"Oil Change": 15000, "Inspection": 30000,"Brake Fluid": 40000}),
    "Mercedes C-Class": MaintenanceInterval(intervals={"Oil Change": 20000, "Inspection": 40000, "Brake Fluid": 60000}),
    "BMW 3 Series": MaintenanceInterval(intervals={"Oil Change": 18000, "Inspection": 36000,"Brake Fluid": 20000}),
}
