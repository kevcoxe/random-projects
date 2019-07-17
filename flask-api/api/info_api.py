
def load_api(app):
    @app.route('/api/hello', methods=["GET"])
    def hello_world():
        return 'Hello World!'
