from app import create_app, db
from app.models import User
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)


app.run(host="0.0.0.0",port=5000)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
