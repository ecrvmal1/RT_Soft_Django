from django.views.generic import TemplateView
from mainapp.models import Record, Category

previous_record = ''


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        """
        The get_context_data function is a function that takes in the request object and returns a dictionary of context variables.
        The view will then use this dictionary to render the template with these variables.

        :param self: Represent the instance of the object itself
        :param **kwargs: Pass keyworded, variable-length argument list
        :return: A context dictionary
        """
        global previous_record

        all_categs = Category.objects.all()
        all_categs_dict = {}
        for el in all_categs:
            # print(el.id, el.name)
            all_categs_dict[el.name] = int(el.id)

        reqv_category_list_names = self.request.GET.getlist('category')
        reqv_category_list_id = []
        try:
            reqv_category_list_id = [all_categs_dict[item]
                                     for item in reqv_category_list_names]
        except KeyError as e:
            print(e)
        context = super().get_context_data(**kwargs)
        list1 = Record.objects.all().\
            filter(category__in=reqv_category_list_id).\
            order_by("num_of_show").reverse()
        # ---  Code below is for debug purposes :  -----
        # for el in list1:
        #     print(f'\n\n {el.file_url}  {el.num_of_show} ')
        #     for el1 in el.category.all():
        #         print(f' {el1} ', end='')
        # ---       End of debug code     -----
        context['item'] = ""
        if list1:
            for record in list1:
                if record.file_url != previous_record and record.num_of_show > 0:
                    context['item'] = record
                    previous_record = record.file_url
                    record.num_of_show -= 1
                    record.save(update_fields=["num_of_show",])
                    break
        return context
