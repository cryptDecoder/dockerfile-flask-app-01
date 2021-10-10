"""
This is a entry point of flask application
"""
from app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
