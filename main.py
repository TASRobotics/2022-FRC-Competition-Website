from website import create_app
from replit import web

app = create_app()

if __name__ == '__main__':
<<<<<<< HEAD
    # app.run(debug=True)
    
    # for replit hosting
    web.run(app, debug=True)
=======
    app.run(debug=True)
>>>>>>> origin/master
