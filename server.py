from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'One 4 all, all for 1'

@app.route('/')
def index():
    if 'view_count' in session:
        session['view_count'] += 1
    else:
        session['view_count'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_3')
def add_3():
    if 'increment_count' in session:
        session['increment_count'] += 3
    else:
        session['increment_count'] = 3
    session['view_count'] += 2
    return redirect('/')

@app.route('/add_x', methods=['POST'])
def add_x():
    x = int(request.form['how_many'])
    if 'increment_count' in session:
        session['increment_count'] += x
    else:
        session['increment_count'] = x
    session['view_count'] += x - 1
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
