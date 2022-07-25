from website import create_app

app = create_app()

if __name__ == '__main__':
    #automatically updates code before public release
    app.run(debug=True)
    