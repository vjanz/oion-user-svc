import os

environment = os.getenv("ENVIRONMENT", "dev")
prefix = "devapi" if environment == "dev" else "api"

EMPLOYEE_SERVICE_URL = f"http://{prefix}.xypsylon.xyz/employees-service/employees"
