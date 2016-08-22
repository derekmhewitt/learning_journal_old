# from pyramid.view import view_config
# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'learning_journal_basic'}

from pyramid.response import Response


def my_view(request):
    return Response("This is my first view!")


def includeme(config):
    config.add_view(my_view, route_name='home')
