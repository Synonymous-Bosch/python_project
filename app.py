from flask import Flask, render_template

from controllers.gym_class_controller import gym_class_blueprint
from controllers.member_controller import members_blueprint
from controllers.member_class_controller import member_class_blueprint

app = Flask(__name__)

app.register_blueprint(gym_class_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(member_class_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()