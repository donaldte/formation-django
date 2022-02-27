from django.shortcuts import get_object_or_404, render
from .models import Articles
from .form import ArticleForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# CLASS BASE VIEW
"""
1-Creer une app 'blog'

2-Ajouter dans le settings

3-Creer un model 'Article'

4-Run migration

5-Creer un modelForm pour le Model 'Article'

6-Creer 'arcticle_list.html, article_detail.html, article_create.html, article_delete.html' template

7-Ajouter le Model 'Article dans le admin

8-Enregister un nouveau object article dans le admin

"""
class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'
    queryset = Articles.objects.all()
    success_url = '/blog'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'blog/article_create.html'
    queryset = Articles.objects.all()
    success_url = '/blog'

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Articles, pk=id_)

    

    


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Articles.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
   
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Articles, pk=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    queryset = Articles.objects.all()
    success_url = '/blog'

   
