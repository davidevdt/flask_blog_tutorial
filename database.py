from flaskblog.models import db
from flaskblog.models import User, Post

#db.create_all()

# user_1 = User(username='Corey', email='c@demo.com', password='password')
# db.session.add(user_1)
# user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
# db.session.add(user_2)
# db.session.commit()

# print(User.query.all())
# print(User.query.first())
# print(User.query.filter_by(username='Corey').all())
# user = User.query.first()
# print(user.id)
# user = User.query.get(1) # same user
# print(user.posts)

# post_1 = Post(title='Blog 1', content='First Post Content', user_id=user.id)
# post_2 = Post(title='Blog 2', content='Second Post Content', user_id=user.id)
# db.session.add(post_1)
# db.session.add(post_2)
# db.session.commit()
# for post in user.posts:
#     print(post.title)

# post = Post.query.first()
# print(post)
# print(post.user_id)
# print(post.author)

#db.drop_all()
#db.create_all()

user = User.query.first()
print(user)
print(user.password)