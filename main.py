import canvasapi
import dotenv
import os

# loads env file into environment as a variable
dotenv.load_dotenv('token.env')

# gets the token from the variable loaded into the os as a variable 
TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://calstatela.instructure.com'

canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

result = canvas_api.get_user('self')


print(result)

