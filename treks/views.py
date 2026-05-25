from django.views.generic import ListView, DetailView
from django.db.models import Q, Avg
from .models import Trek

class TrekListView(ListView):
    model               = Trek
    template_name       = 'treks/trek_list.html'
    context_object_name = 'treks'
    paginate_by         = 9

    def get_queryset(self):
        qs         = Trek.objects.filter(is_active=True)
        q          = self.request.GET.get('q', '')
        region     = self.request.GET.get('region', '')
        difficulty = self.request.GET.get('difficulty', '')
        max_price  = self.request.GET.get('max_price', '')

        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
        if region:
            qs = qs.filter(region=region)
        if difficulty:
            qs = qs.filter(difficulty=difficulty)
        if max_price:
            qs = qs.filter(price__lte=max_price)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['regions']     = Trek.REGION_CHOICES
        ctx['difficulties'] = Trek.DIFFICULTY_CHOICES
        return ctx

class TrekDetailView(DetailView):
    model               = Trek
    template_name       = 'treks/trek_detail.html'
    context_object_name = 'trek'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['reviews']    = self.object.reviews.all().order_by('-created_at')
        ctx['avg_rating'] = self.object.reviews.aggregate(Avg('rating'))['rating__avg']
        return ctx