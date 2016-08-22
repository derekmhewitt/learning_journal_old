from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.include('.views')
    #scan needs to be the last thing before we return config.wsgi_app()
    config.scan()
    return config.make_wsgi_app()
