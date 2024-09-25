from . models import categories, company_details, more_items 
def global_data_send(request):
    data = {
        'category' : categories.objects.all(),
        'company' : company_details.objects.first(),
        'items' : more_items.objects.all(),
        # 'Category' : Category_1.objects.all(),
    }
    return data