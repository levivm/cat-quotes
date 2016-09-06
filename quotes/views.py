from django.views.generic import TemplateView


class CatQuotesView(TemplateView):
    template_name = "quotes.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CatQuotesView, self).get_context_data(**kwargs)

        cat_quote_one = "I'm bilingual cat and know how to meow in several languages: Meow."
        cat_quote_two = "I'm not angry, go to kill yourself."
        context.update({
            'cat_quote_one': cat_quote_one,
            'cat_quote_two': cat_quote_two
        })
        return context
