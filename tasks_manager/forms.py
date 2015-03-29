# -*- coding: utf-8 -*-
from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(label=u'项目名称')
    description = forms.CharField(widget=forms.Textarea, )
    client_name = forms.CharField()

    def send_mail(self):
        pass
