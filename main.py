from sanic import Sanic
from sanic.response import json
from sanic import response
app = Sanic("hello_example")

@app.route("/")
async def test(request):
  # return json({"hello": "world"})
  return await response.file('GFG.pdf')
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)