from django.shortcuts import render


def main_index(request):
    return render(request, 'layouts/base.html')
