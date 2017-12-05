from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from photo import InstaApi

def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def getPhoto():
    insta = InstaApi(username="cleydsa", password="dsds")
    insta.getPhoto()
    return {'message': 'Welcome to API Star!'}


routes = [
    Route('/', 'GET', welcome),
    Route('/photo', 'GET', getPhoto),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]


app = App(routes=routes)


if __name__ == '__main__':
    app.main()
