
frappe.ui.form.on('Sales Order Item', {
    item_code(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (!row.item_code) return;

        frappe.db.get_doc('Item', row.item_code).then(doc => {
            row.custom_sales_price = doc.custom_sales_price || 0;
            row.custom_actual_price = doc.custom_actual_price || 0;
            row.rate = doc.custom_sales_price || 0;
            row.validity_months = doc.validity_months || 0;

            if (!row.start_date) {
                row.start_date = frappe.datetime.get_today();
            }

            if (row.start_date && row.validity_months) {
                row.end_date = frappe.datetime.add_months(
                    row.start_date,
                    cint(row.validity_months)
                );
            }

            frm.refresh_field("items");
        });
    },

    start_date(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (row.start_date && row.validity_months) {
            row.end_date = frappe.datetime.add_months(
                row.start_date,
                cint(row.validity_months)
            );
            frm.refresh_field("items");
        }
    },

    validity_months(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (row.start_date && row.validity_months) {
            row.end_date = frappe.datetime.add_months(
                row.start_date,
                cint(row.validity_months)
            );
            frm.refresh_field("items");
        }
    }
});

frappe.ui.form.on('Sales Order', {
    refresh(frm) {
        if (!frappe.user.has_role("Sales Manager")) {
            frm.fields_dict.items.grid.update_docfield_property(
                "rate",
                "read_only",
                1
            );
        }
    }
});