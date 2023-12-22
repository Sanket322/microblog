from app import app,db
from app.models import User,Post
import sqlalchemy as sa
import sqlalchemy.orm as so

# The app.shell_context_processor decorator registers the function
# as a shell context function
@app.shell_context_processor
def make_shell_context():
    return {'sa':sa,'so':so,'db':db,'User':User,'Post':Post}

# from app import app, db
# from app.models import User, Post
# import sqlalchemy as sa
# app.app_context().push()