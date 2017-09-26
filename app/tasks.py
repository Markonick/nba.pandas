from celery import Celery
from parser import Parser


celery = Celery()
celery.config_from_object('celeryconfig')


@app.task
def read_csv_chunks(path):
    parser = Parser(app.csv_path, app.chunk_size)
    stats = parser.get_stats()
    return stats


if __name__ == '__main__':
    app.run(port=8889, debug=True)
