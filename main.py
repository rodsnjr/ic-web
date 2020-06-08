import os
from quart import Quart
from quart import request
from web.api import user_schema
from web.service import user as user_service


PATH = os.path.dirname(__file__)
app = Quart(__name__, static_folder=f'{PATH}/dist')


@app.route('/register', methods=['GET', 'POST'])
async def register():
    try:
        if request.method == 'POST':
            user_body = await request.get_form()
            user = user_schema.load(user_body)
            user_service.register(user)
            # TODO - Redirect to DONE page
            return 'Register POST'
        # TODO - Redirect to Register Page
        return 'Register Page'
    except Exception as e:
        print(e)
        return 'Error', 500


@app.route('/')
async def root():
    try:
        print('Serving Static File')
        static = await app.send_static_file('index.html')
        return static
    except Exception as e:
        print(e)
        return 'Error', 500

if __name__ == '__main__':
    app.run()
