frappe.ui.form.on('Sales Order Item', {
    item_code: function(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (!row.item_code) return;

        frappe.db.get_doc('Item', row.item_code).then(doc => {
            row.custom_sales_price = doc.custom_sales_price;
            row.custom_actual_price = doc.custom_actual_price;
            row.rate = doc.custom_sales_price;
            row.validity_months = doc.validity_months;

            if (!row.start_date) {
                row.start_date = frappe.datetime.get_today();
            }

            if (row.start_date && row.validity_months) {
                row.end_date = frappe.datetime.add_months(
                    row.start_date,
                    row.validity_months
                );
            }

            frm.refresh_field('items');
        });
    }
});
