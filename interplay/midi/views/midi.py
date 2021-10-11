from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)

