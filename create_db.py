from flaskblog import app, db, User, Post

with app.app_context():
    # Create the database
    db.create_all()

    # Create new users
    user1 = User(username='caren', email='cm@demo.com', password='password')
    user2 = User(username='johndoe', email='jd@demo.com', password='password')
    user3 = User(username='gladys', email='g@demo.com', password='password')

    # Add the users to the session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # Commit the session to save the users to the database
    db.session.commit()

    # List of users
    users = [user1, user2, user3]

    # Create posts for each user
    for user in users:
        post1 = Post(title=f"Post 1 by {user.username}", content="Content of post 1", author=user)
        post2 = Post(title=f"Post 2 by {user.username}", content="Content of post 2", author=user)
        post3 = Post(title=f"Post 3 by {user.username}", content="Content of post 3", author=user)

        # Add the posts to the session
        db.session.add(post1)
        db.session.add(post2)
        db.session.add(post3)

    # Commit the session to save the posts to the database
    db.session.commit()

    # Query and print all posts to confirm
    all_posts = Post.query.all()
    for post in all_posts:
        print(post)
