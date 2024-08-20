from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .models import projeto as Projeto
from django.shortcuts import get_object_or_404, redirect

class ProjetoListView(ListView):
    model = Projeto  #list


class ProjetoCreateView(CreateView):
    model = Projeto  #form
    fields = ["titlle", "deadline"]
    success_url = reverse_lazy("projeto_list")


class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = ["titlle", "deadline"]
    success_url = reverse_lazy("projeto_list")
    
class ProjetoDeleteView(DeleteView):
    model = Projeto
    success_url = reverse_lazy("projeto_list")
    
class ProjetoCompleteView(View):
    def get(self, request, pk):
        projeto = get_object_or_404(Projeto, pk=pk)
        projeto.mark_has_complete()
        return redirect("projeto_list")