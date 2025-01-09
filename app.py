from buzz_bite import create_app


from   buzz_bite import db, create_app

app = create_app()
with app.app_context():
    db.create_all()


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
