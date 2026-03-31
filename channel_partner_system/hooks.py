app_name = "channel_partner_system"
app_title = "Channel Partner System"
app_publisher = "Your Company"
app_description = "Sales & Plan Management"
app_email = "you@email.com"
app_license = "MIT"

app_include_js = "/assets/channel_partner_system/js/sales_order.js"

fixtures = ["Custom Field", "DocType"]

scheduler_events = {
    "daily": [
        "channel_partner_system.api.update_customer_plan_status"
    ]
}

doc_events = {
    "Sales Order": {
        "before_save": "channel_partner_system.api.validate_sales_order",
        "on_submit": "channel_partner_system.api.create_customer_plan"
    }
}
