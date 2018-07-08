from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms
#from reviews.forms import RatingForm, ChapterReviewForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormMixin
from django.urls import reverse_lazy

from . import models
from .models import Chapter, Rating, Book
from .forms import RatingForm
from django.db.models import Count, Q
import json
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext



class BookListView(ListView):
    model = models.Book
    template_name = 'book_list.html'


    def get_data(self,request):
            book_id = None
            engaging_list = []
            boring_list = []
            series = []
            if request.method == 'GET':
                book_id = request.GET['book_id']
                if book_id:
                    book = Book.objects.get(id=int(book_id)).prefetch_related('chapter_set').all()
                    for chapter in book:
                        boring_list.append(chapter.rating_set.filter(review='Boring').count())
                        engaging_list.append(chapter.rating_set.filter(review='Engaging').count())

            series = [boring_list, engaging_list]
            return HttpResponse(series)



    def get_engaging_set(self, request):
        engaging_set = []
        for chapter in self.objects.all():
            engaging_set.append(chapter.rating_set.filter(review='Engaging').count())
        return HttpResponse(engaging_set)

    def get_boring_set(self, request):
        boring_set = []
        for chapter in self.objects.all():
            boring_set.append(chapter.rating_set.filter(review='Boring').count())
        return HttpResponse(boring_set)

    def get_chapter_list(self, request):
        chapter_list = []
        for chapter in self.objects.all():
            chapter_list.append(chapter.chapter_number)
        return HttpResponse(chapter_list)



    


    """
    def get_data(self):

        def get_engaging_set(self):
            engaging_set = []
            for chapter in self.chapter_set.all:
                engaging_set.append(chapter.rating_set.filter(review='Engaging').count())
            return engaging_set

        def get_boring_set(self):
            boring_set = []
            for chapter in self.chapter_set.all:
                boring_set.append(chapter.rating_set.filter(review='Boring').count())
            return boring_set

        engaging_dict = {}
        engaging_dict['name'] = 'Engaging'
        engaging_dict['data'] = get_engaging_set(self)

        boring_dict = {}
        boring_dict['name'] = 'Boring'
        boring_dict['data'] = get_boring_set(self)

        return render([engaging_dict, boring_dict])
    """

   


    """
    def get_series(self,request):
        book_title = Book.title
        dataset = self.objects.values('chapter_number').annotate(bored_count=Count('chapter', filter=Q(review='Boring')),
                                                        engaged_count=Count('chapter', filter=Q(review='Engaging')))

        categories = list()
        bored_series_data = list()
        engaged_series_data = list()


        for entry in dataset:
            categories.append(entry['chapter'].chapter_number)
            bored_series_data.append(entry['bored_count'])
            engaged_series_data.append(entry['engaged_count'])


        bored_series = {
            'name': "Bored",
            'data': bored_series_data
        }

        engaged_series = {
            'name': "Engaged",
            'data': engaged_series_data
        }

        chart = {
            'chart': {'type': 'area'},
            'title': book_title,
            'xAxis': {'categories': categories},
            'series': [bored_series, engaged_series]
        }

        dump = json.dumps(chart)
    
        return render(request, 'book_list.html', {
            'categories': json.dumps(categories),
            'bored_series': json.dumps(bored_series),
            'engaged_series': json.dumps(engaged_series)
        })
    """


        

class BookDetailView(DetailView, FormMixin):
    model = models.Book
    template_name = 'book_detail.html'
    form_class = RatingForm


    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        context['form'] = RatingForm(initial={'chapter': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BookDetailView, self).form_valid(form)

success_url = reverse_lazy('book_list')

