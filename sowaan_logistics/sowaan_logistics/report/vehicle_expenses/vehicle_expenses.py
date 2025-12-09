# Copyright (c) 2025
# Script Report: Logistics Fuel & Distance Report

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

    # Convert empty values to None so optional filters work
    for key in values:
        if not values[key]:
            values[key] = None

    # Define report columns
    columns = [
        {"fieldname": "Vehicle", "label": "Vehicle", "fieldtype": "Link", "options": "Vehicle", "width": 140},
        {"fieldname": "Driver", "label": "Driver", "fieldtype": "Link", "options": "Driver", "width": 140},
        {"fieldname": "Trip Date", "label": "Trip Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "Distance Covered", "label": "Distance Covered (KM)", "fieldtype": "Float", "width": 150},
        {"fieldname": "Fuel Consumption Qty", "label": "Fuel (Liters)", "fieldtype": "Float", "width": 150}
    ]

    # SQL Query to fetch data
    results = frappe.db.sql("""
        SELECT 
            lt.vehicle AS 'Vehicle',
            lt.driver AS 'Driver',
            DATE(lt.time_in) AS 'Trip Date',
            FORMAT(lt.distance_covered, 2) AS 'Distance Covered',
            FORMAT(lt.fuel_consumption, 2) AS 'Fuel Consumption Qty'
        FROM 
            `tabLogistics Table` lt
        INNER JOIN 
            `tabLogistic Car` lb ON lb.name = lt.parent
        WHERE 
            lb.docstatus = 1
            AND (%(from)s IS NULL OR %(to)s IS NULL OR DATE(lt.time_in) BETWEEN %(from)s AND %(to)s)
            AND (%(company)s IS NULL OR lb.company = %(company)s)
            AND (%(vehicle)s IS NULL OR lt.vehicle = %(vehicle)s)
            AND (%(driver)s IS NULL OR lt.driver = %(driver)s)
        ORDER BY 
            lt.time_in DESC
    """, values, as_dict=True)

    return columns, results
