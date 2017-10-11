# from django.http import Http404
from django.shortcuts import render


def view_static_template(request, path):
    path = 'tmp/' + path.strip('/') + '.html'
    # raise Http404('Template not found "{}"'.format(path))
    p = ''

    return render(request, path, {'poll': p})
