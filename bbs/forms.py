from django import forms

from .models import Topic,TopicReply


class TopicForm(forms.ModelForm):
    class Meta:
        model   = Topic
        fields  = ["comment","attachment","mime"]

class TopicReplyForm(forms.ModelForm):
    class Meta:
        model   = TopicReply
        fields  = ["comment","attachment","mime","target"]

