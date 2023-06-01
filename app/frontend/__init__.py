import pathlib
from app import app

current_folder = str(pathlib.Path(__file__).parent)

app.template_folder = current_folder+"/templates" #TODO: can dont work on windows
app.static_folder = current_folder+"/static"

from app.frontend import routes