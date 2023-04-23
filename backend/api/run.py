from config.config import app
from config.config import config

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.get('App', 'server.port'))