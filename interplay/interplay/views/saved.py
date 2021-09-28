from django.http import HttpResponse
from django.template import loader


# example view
def main(req):
    resp = loader.get_template('saved.html').render({}, req)
    return HttpResponse(resp)