from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mobs')
def mobs():
    return render_template('mobs.html')

@app.route('/biomes')
def biomes():
    return render_template('biomes.html')

@app.route('/crafts')
def crafts():
    return render_template('crafts.html')

if __name__ == '__main__':
    app.run(debug=True, port=5003)