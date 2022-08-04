from django.shortcuts import render,redirect

from django.views import View
from .models import Topic

class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        check = request.POST.getlist('chk_rikaido_kensaku')
        print('check =', check)

        return redirect("bbs:index")

index   = IndexView.as_view()
