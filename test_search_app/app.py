import os
from flask import Flask, render_template, request, jsonify
from searcher.searchers.base_searcher import Searcher


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(os.environ['APP_SETTINGS'])
    return app


app = create_app()


@app.errorhandler(Exception)
def handle_invalid_usage(error_instance):
    message = "{} / {}".format(error_instance.__class__.__name__, str(error_instance))
    result = jsonify(dict(exception=message, success=False))
    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/')
def search():
    query = request.args.get('query').strip("'")
    result = Searcher.search(query)
    obj_books = result['results']
    books = [dict(id=book.id, title=book.title, score=book.rank, words=book.words) for book in obj_books]
    result['data'] = dict(results=books)
    result['success'] = True
    return jsonify(result)
