
def load_api(app):
    @app.route('/api')
    def hello_world():
        return 'Hello World!'
