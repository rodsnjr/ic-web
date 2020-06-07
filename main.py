import os
from quart import Quart
from quart import request

PATH = os.path.dirname(__file__)
app = Quart(__name__, static_folder=f'{PATH}/public')


@app.route('/')
async def root():
    try:
        print('Serving Static File')
        static = await app.send_static_file('index.html')
        return static
    except Exception as e:
        print(e)
        return 'Error'

if __name__ == '__main__':
    app.run()
