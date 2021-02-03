from django.shortcuts import render
import request

def post_list(request):
    return render(request, 'blog/post_list.html', {})
