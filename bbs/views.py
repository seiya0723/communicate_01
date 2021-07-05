from django.shortcuts import render,redirect
from django.views import View

import datetime

from .models import Topic,TopicReply
from .forms import TopicForm,TopicReplyForm

import magic


ALLOWED_MIME    = [ "image/png","image/jpeg","video/mp4" ]

class BbsView(View):

    def get(self, request, *args, **kwargs):

        #DBへ全件取得
        topics  = Topic.objects.all()

        context = { "topics":topics }

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        mime    = ""

        if "attachment" in request.FILES:
            mime    = magic.from_buffer(request.FILES["attachment"].read(1024) , mime=True)
            print(mime)

            if mime not in ALLOWED_MIME:
                print("このファイルは許可されていません")
                return redirect("bbs:index")

        
        copied          = request.POST.copy()
        copied["mime"]  = mime

        form    = TopicForm(copied,request.FILES)

        if form.is_valid():
            print("OK")
            form.save()
        else:
            print("バリデーションNG")
        

        return redirect("bbs:index")

index   = BbsView.as_view()

class BbsReplyView(View):

    def get(self, request, pk, *args, **kwargs):

        topic       = Topic.objects.filter(id=pk).first()
        replies     = TopicReply.objects.filter(target=pk)

        context     = { "topic":topic,
                        "replies":replies,
                        }

        return render(request,"bbs/single.html",context)

    def post(self, request, pk, *args, **kwargs):

        mime    = ""

        if "attachment" in request.FILES:
            mime    = magic.from_buffer(request.FILES["attachment"].read(1024) , mime=True)
            print(mime)

            if mime not in ALLOWED_MIME:
                print("このファイルは許可されていません")
                return redirect("bbs:single",pk)


        copied              = request.POST.copy()
        copied["target"]    = pk
        copied["mime"]      = mime

        form    = TopicReplyForm(copied,request.FILES)

        if form.is_valid():
            print("OK")
            form.save()
        else:
            print("バリデーションNG")
        

        return redirect("bbs:single",pk)

single  = BbsReplyView.as_view()

