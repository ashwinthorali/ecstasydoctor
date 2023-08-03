from home.models import Blog


def allpage(request):
    blogs = Blog.objects.all()[:4]
    context = {
        'blogs':blogs,
    }
    return context 