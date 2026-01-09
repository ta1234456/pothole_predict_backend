from app import app

if __name__ == '__main__':
    print(f'Server running on http://{app.config["HOST"]}:{app.config["PORT"]}/')
    print('Press Ctrl+C to stop the server')
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
