from django.shortcuts import render


def index(request):
    attributes = [
        (k, getattr(request, k)) for k in dir(request)
        if isinstance(getattr(request, k), basestring)
        and not k.startswith('_')
    ]
    request_vars = [
        ('request.attributes', sorted(attributes)),
        ('request.COOKIES', sorted(request.COOKIES.iteritems())),
        ('request.GET', sorted(request.GET.iteritems())),
        ('request.POST', sorted(request.POST.iteritems())),
        ('request.META', sorted(request.META.iteritems())),
    ]
    return render(request, 'requestdump/index.html', {
        'request_vars': request_vars,
    })
