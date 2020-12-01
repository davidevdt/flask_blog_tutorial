from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)

# export FLASK_APP=run.py   // flask run