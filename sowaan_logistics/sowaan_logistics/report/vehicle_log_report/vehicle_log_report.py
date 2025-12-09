# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

# Copyright (c) 2025, and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):

    # Ensure filters dictionary exists
    filters = filters or {}

    values = {
        'from': filters.get("from"),
        'to': filters.get("to"),
        'driver': filters.get("driver"),
        'plate_number': filters.get("plate_number")
    }

    # Convert empty strings to None (fix optional filters)
    for key in values:
        if not values[key]:
            values[key] = None

    columns = [
        {"fieldname": "Company", "label": "Company", "fieldtype": "Data"},
        {"fieldname": "Work Shop", "label": "Work Shop", "fieldtype": "Data"},
        {"fieldname": "Vehicle Details", "label": "Vehicle Details", "fieldtype": "Data"},
        {"fieldname": "Plate No", "label": "Plate No", "fieldtype": "Data"},
        {"fieldname": "Job Card No", "label": "Job Card No", "fieldtype": "Data"},
        {"fieldname": "Date", "label": "Date", "fieldtype": "Date"},
        {"fieldname": "Job Item", "label": "Job Item", "fieldtype": "Data"},
        {"fieldname": "Job Type", "label": "Job Type", "fieldtype": "Data"},
        {"fieldname": "Expense Amount", "label": "Expense Amount", "fieldtype": "Currency"},
        {"fieldname": "Full Name", "label": "Full Name", "fieldtype": "Data"},
        {"fieldname": "Date of Parts Recieved", "label": "Date of Parts Recieved", "fieldtype": "Date"},
        {"fieldname": "Date of Receiving Back from Workshop", "label": "Date of Receiving Back from Workshop", "fieldtype": "Date"},
        {"fieldname": "Warranty", "label": "Warranty", "fieldtype": "Data"},
        {"fieldname": "Expiry Date", "label": "Expiry Date", "fieldtype": "Date"},
        {"fieldname": "Last Purchase Date", "label": "Last Purchase Date", "fieldtype": "Date"},
        {"fieldname": "Expected Date of Change", "label": "Expected Date of Change", "fieldtype": "Date"}
    ]

    results = frappe.db.sql("""
        SELECT 
            vl.custom_company AS 'Company',
            vl.custom_workshop AS 'Work Shop',
            CONCAT(vl.make, ' ', vl.model) AS 'Vehicle Details',
            vl.license_plate AS 'Plate No',
            vl.name AS 'Job Card No',
            vl.custom_posting_date AS 'Date',
            service_item.service_item AS 'Job Item',
            service_item.type AS 'Job Type',
            FORMAT(service_item.expense_amount, 2) AS 'Expense Amount',
            service_item.custom_full_name AS 'Full Name',
            vl.custom_date_of_parts_received AS 'Date of Parts Recieved',
            vl.custom_date_of_receiving_back_from_workshop AS 'Date of Receiving Back from Workshop',
            service_item.custom_warrantee AS 'Warranty',
            service_item.custom_expiry_date AS 'Expiry Date',
            service_item.custom_last_purchase_date AS 'Last Purchase Date',
            service_item.custom_expected_date_of_change AS 'Expected Date of Change'
        FROM 
            `tabVehicle Log` vl
        JOIN 
            `tabVehicle Service` service_item ON service_item.parent = vl.name
            AND service_item.parenttype = 'Vehicle Log'
        WHERE 
            vl.docstatus = 1
            AND (%(from)s IS NULL OR %(to)s IS NULL OR vl.custom_posting_date BETWEEN %(from)s AND %(to)s)
            AND (%(plate_number)s IS NULL OR vl.license_plate = %(plate_number)s)
            AND (%(driver)s IS NULL OR service_item.custom_technician_name = %(driver)s)
        ORDER BY 
            vl.name
        """, values, as_dict=True)

    return columns, results
