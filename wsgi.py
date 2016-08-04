from app import app as application


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 80, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
