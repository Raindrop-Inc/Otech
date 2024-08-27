

def on_save(doc, method):
    for item in doc.items:
        for task in frappe.db.get_all("Task wise Budget", filters = {"parent":item.custom_task, "item_name":item.item_code}, fields=["*]):
            frappe.db.set_value("Task wise Budget", task.name, "consumed_qty", item.qty)
            frappe.db.commit()                                                                                             
