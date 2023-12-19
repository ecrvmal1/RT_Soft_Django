from django.views.generic import TemplateView

from mainapp.apps import MainappConfig
from mainapp.models import Record



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

        reqv_category_list_names = self.request.GET.getlist('category')
        reqv_category_list_id = []
        try:
            reqv_category_list_id = [MainappConfig.all_categs_dict[item]
                                     for item in reqv_category_list_names]
        except KeyError as e:
            print(f'key not found in dict {e}')

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
                if record.file_url != self.request.session.get('previous_record') and record.num_of_show > 0:
                    context['item'] = record
                    self.request.session['previous_record'] = record.file_url

                    record.num_of_show -= 1
                    record.save(update_fields=["num_of_show",])
                    break
        return context
