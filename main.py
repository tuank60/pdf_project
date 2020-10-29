from sanic import Sanic
from sanic.response import json
from sanic import response
app = Sanic("hello_example")

@app.route("/")
async def test(request):
  return json({"hello": "world solution github1"})
  # return await response.file('GFG.pdf')
  # return response.empty()

@app.route('/file')
async def handle_request11(request):
    return await response.file('GFG.pdf')

@app.route('/file')
async def handle_request(request):
    return await response.file('GFG.pdf')

@app.route('/raw')
def handle_request(request):
    return response.raw(b'raw data')

@app.route("/streaming")
async def index(request):
    async def streaming_fn(response):
        await response.write('foo')
        await response.write('bar')
    return response.stream(streaming_fn, content_type='text/plain')

@app.route('/big_file.png')
async def handle_request(request):
    return await response.file_stream('logo.png')

@app.route('/redirect')
def handle_request(request):
    return response.redirect('/streaming')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)