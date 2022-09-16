from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})   #templateフォルダの中のblog/post_list.htmlをさす
