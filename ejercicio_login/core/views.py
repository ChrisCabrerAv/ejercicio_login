from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "core/index.html"

@method_decorator(staff_member_required(),name='dispatch')
class ExerciseView(TemplateView):
    template_name = "core/exercise.html"