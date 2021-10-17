from app import app_context, create_app
app = create_app()

app.app_context().push()