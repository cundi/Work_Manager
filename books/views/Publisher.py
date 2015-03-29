from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Work_Manager.books.models import Publisher, Book
from django.core.paginator import Paginator
from django.views.generic.list import MultipleObjectMixin
# Create your views here.


class PublisherList(ListView):
    model = Publisher
    allow_empty = True
    queryset = None
    paginate_by = 5
    paginate_orphans = 0
    context_object_name = None
    paginator_class = Paginator
    page_kwarg = 'page'


class PublisherDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context