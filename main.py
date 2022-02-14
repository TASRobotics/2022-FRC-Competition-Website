from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    
    # for replit hosting
    # from replit import web
    # web.run(app, debug=True)