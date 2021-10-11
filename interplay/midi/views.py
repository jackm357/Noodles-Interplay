from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)

def continue_page(req):
    resp = loader.get_template('continue.html').render({}, req)
    return HttpResponse(resp)
