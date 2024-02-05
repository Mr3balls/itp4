from flask import Flask, render_template, request

app = Flask(__name__)

projects_data = [
    {'title': 'Project 1', 'description': 'Description 1'},
    {'title': 'Project 2', 'description': 'Description 2'},
    {'title': 'Project 3', 'description': 'Description 3'},
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        write_to_file(f'Name: {name}, Email: {email}')
        return f'Thank you, {name}, for contacting me!'
    return render_template('contact.html')


def write_to_file(data):
    with open('data.txt', 'a') as file:
        file.write(data + '\n')


if __name__ == '__main__':
    app.run(debug=True)
