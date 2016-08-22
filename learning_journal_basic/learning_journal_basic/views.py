# from pyramid.view import view_config
# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'learning_journal_basic'}

from pyramid.response import Response
import os

HERE = os.path.dirname(__file__)


def my_view(request):
    imported_text = open(os.path.join(HERE, 'sample.html')).read()
    return Response(imported_text)


def includeme(config):
    config.add_view(my_view, route_name='home')
