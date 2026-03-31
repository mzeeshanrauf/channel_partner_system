import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def after_install():
    custom_fields = {
        "Item": [
            {
                "fieldname": "custom_sales_price",
                "label": "Sales Price",
                "fieldtype": "Currency",
                "insert_after": "standard_rate",
            },
            {
                "fieldname": "custom_actual_price",
                "label": "Actual Price",
                "fieldtype": "Currency",
                "insert_after": "custom_sales_price",
                "permlevel": 1,
            },
            {
                "fieldname": "validity_months",
                "label": "Validity Months",
                "fieldtype": "Int",
                "insert_after": "custom_actual_price",
            },
        ],
        "Sales Order Item": [
            {
                "fieldname": "custom_sales_price",
                "label": "Sales Price",
                "fieldtype": "Currency",
                "insert_after": "rate",
            },
            {
                "fieldname": "custom_actual_price",
                "label": "Actual Price",
                "fieldtype": "Currency",
                "insert_after": "custom_sales_price",
                "permlevel": 1,
            },
            {
                "fieldname": "validity_months",
                "label": "Validity Months",
                "fieldtype": "Int",
                "insert_after": "custom_actual_price",
            },
            {
                "fieldname": "start_date",
                "label": "Start Date",
                "fieldtype": "Date",
                "insert_after": "validity_months",
            },
            {
                "fieldname": "end_date",
                "label": "End Date",
                "fieldtype": "Date",
                "insert_after": "start_date",
            },
        ],
    }

    create_custom_fields(custom_fields, update=True)