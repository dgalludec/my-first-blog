# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:38:45 2021

@author: Multiple Monitors
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)