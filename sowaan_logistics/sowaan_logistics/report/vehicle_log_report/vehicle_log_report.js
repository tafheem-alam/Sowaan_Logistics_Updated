// Copyright (c) 2025, Sowaan and contributors
// For license information, please see license.txt

frappe.query_reports["Vehicle Log Report"] = {
	"filters": [
{
   "fieldname": "from",
   "fieldtype": "Date",
   "label": "From",
   "mandatory": 0,
   "wildcard_filter": 0
  },
  {
   "fieldname": "to",
   "fieldtype": "Date",
   "label": "To",
   "mandatory": 0,
   "wildcard_filter": 0
  },
  {
   "fieldname": "driver",
   "fieldtype": "Link",
   "label": "Driver",
   "mandatory": 0,
   "options": "Employee",
   "wildcard_filter": 0
  },
  {
   "fieldname": "plate_number",
   "fieldtype": "Link",
   "label": "License Plate Number",
   "mandatory": 0,
   "options": "Vehicle",
   "wildcard_filter": 0
  }
	]
};
