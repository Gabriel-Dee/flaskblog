from flaskblog import app, db  # Ensure flaskblog is your main application module

with app.app_context():
    db.create_all()
