from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from mainapp.models import Record, Category

all_categs = Category.objects.all()
all_categs_dict = {}
for el in all_categs:
    print(el.id, el.name)
    all_categs_dict[el.name] = int(el.id)

previous_record = ''


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        global previous_record
        reqv_category_list_names = self.request.GET.getlist('category')
        print(f'reqv_category_list_names : {reqv_category_list_names}')
        reqv_category_list_id = [all_categs_dict[item] for item in reqv_category_list_names]
        print(f'reqv_category_list_id : {reqv_category_list_id}')
        context = super().get_context_data(**kwargs)
        list1 = Record.objects.all().\
            filter(category__in=reqv_category_list_id).\
            order_by("num_of_show").reverse()
        # Code below is for testing purposes :
        for el in list1:
            print(f'\n\n {el.file_url}  {el.num_of_show} ')
            for el1 in el.category.all():
                print(f' {el1} ', end='')
        context['item'] = ""
        if list1:
            record = list1[0]
            if record.file_url == previous_record:
                for el in list1[1:]:
                    if el != previous_record:
                        record = el
                        print(f'prev: {previous_record.file_url}')
                        break
            context['item'] = record
            previous_record = record.file_url
            record.num_of_show -= 1
            record.save(update_fields=["num_of_show",])
        return context

