import frappe
from datetime import date, timedelta

def validate_sales_order(doc, method):
    for item in doc.items:
        if item.rate != item.custom_sales_price:
            frappe.throw("Rate must match Custom Sales Price")

def create_customer_plan(doc, method):
    for item in doc.items:
        frappe.get_doc({
            "doctype": "Customer Plan",
            "customer": doc.customer,
            "plan": item.item_code,
            "sales_order": doc.name,
            "start_date": item.start_date,
            "end_date": item.end_date,
            "status": "Active"
        }).insert(ignore_permissions=True)

def update_customer_plan_status():
    today = date.today()
    plans = frappe.get_all("Customer Plan", fields=["name","end_date"])
    for p in plans:
        if not p.end_date: continue
        if p.end_date < today:
            status = "Expired"
        elif p.end_date <= today + timedelta(days=30):
            status = "Expiring Soon"
        else:
            status = "Active"
        frappe.db.set_value("Customer Plan", p.name, "status", status)
