from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="frontend/build/static",
    template_folder="frontend/build")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello {u}'.format(u=username)


if __name__ == '__main__':
    app.config.from_object('configurations.DevelopmentConfig')
    app.run()
