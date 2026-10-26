from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import ProductForm
from .models import Product

class OwnedProductMixin(LoginRequiredMixin):
    """Every query is scoped to the logged-in user. Someone else's product 404s."""
    model = Product

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user)

class ProductListView(OwnedProductMixin, ListView):
    paginate_by = 10

class ProductDetailView(OwnedProductMixin, DetailView):
    pass

class ProductCreateView(OwnedProductMixin, SuccessMessageMixin, CreateView):
    form_class = ProductForm
    success_message = "Product created."

    def form_valid(self, form):
        form.instance.owner = self.request.user   # never trust the client for ownership
        return super().form_valid(form)

class ProductUpdateView(OwnedProductMixin, SuccessMessageMixin, UpdateView):
    form_class = ProductForm
    success_message = "Product updated."

class ProductDeleteView(OwnedProductMixin, SuccessMessageMixin, DeleteView):
    success_url = reverse_lazy("product-list")
    success_message = "Product deleted."