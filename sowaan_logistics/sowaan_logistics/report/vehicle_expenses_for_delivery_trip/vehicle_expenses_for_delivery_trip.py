import frappe

def execute(filters=None):
    filters = filters or {}

    # Filter values from the report parameters
    values = {
        "from": filters.get("from"),
        "to": filters.get("to"),
        "company": filters.get("company"),
        "vehicle": filters.get("vehicle"),
        "driver": filters.get("driver")
    }

    # Convert empty strings to None so optional filters work
    for key in values:
        if not values[key]:
            values[key] = None

    # Define report columns
    columns = [
        {"fieldname": "Vehicle", "label": "Vehicle", "fieldtype": "Link", "options": "Vehicle", "width": 140},
        {"fieldname": "Driver", "label": "Driver", "fieldtype": "Link", "options": "Driver", "width": 140},
        {"fieldname": "Trip Date", "label": "Trip Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "Distance Covered", "label": "Distance Covered (KM)", "fieldtype": "Float", "width": 150},
        {"fieldname": "Fuel Consumption Qty", "label": "Fuel Consumption (Liters)", "fieldtype": "Float", "width": 180}
    ]

    # SQL Query to fetch data
    results = frappe.db.sql(""" 
        SELECT 
            dt.vehicle AS 'Vehicle',
            dt.driver AS 'Driver',
            DATE(dt.departure_time) AS 'Trip Date',
            FORMAT(ds.distance, 2) AS 'Distance Covered',
            FORMAT(ds.custom_total_value, 2) AS 'Fuel Consumption Qty'
        FROM 
            `tabDelivery Stop` ds
        INNER JOIN 
            `tabDelivery Trip` dt ON dt.name = ds.parent
        WHERE 
            ds.docstatus = 1
            AND (%(from)s IS NULL OR %(to)s IS NULL OR DATE(dt.departure_time) BETWEEN %(from)s AND %(to)s)
            AND (%(company)s IS NULL OR dt.company = %(company)s)
            AND (%(vehicle)s IS NULL OR dt.vehicle = %(vehicle)s)
            AND (%(driver)s IS NULL OR dt.driver = %(driver)s)
        ORDER BY dt.departure_time DESC
    """, values, as_dict=True)

    return columns, results
