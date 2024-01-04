import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template
import predict_authorGender

app = Flask(__name__)

def generate_graph():
    graph = predict_authorGender.predictShowGraph()
    graph.savefig('static/plot.png')
    graph.clf()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    generate_graph()
    return render_template('graph.html')

if __name__ == '__main__':
    app.run()