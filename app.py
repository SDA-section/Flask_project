from flask import Flask, render_template , redirect, url_for, flash
from forms import RegisterForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dwqdj 0q09qwd jq0wdj q09jw09j'

@app.route('/', methods=['POST', 'get'])
def home():
    return render_template('index.html', title="Home", style='home.css')

@app.route('/about')
def about():
   return render_template('about.html', title="About US")

@app.route('/login',  methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      if form.email.data == "abdo@gmail.com" and form.password.data == "123456":
         flash('Login Successfully', 'success')
         return redirect(url_for('home'))
      else:
         flash('Invalid Credential', 'danger')
   return render_template('login.html', title="Login", form=form)

@app.route('/register', methods=['GET','POST'])
def register():
   form = RegisterForm()
   if form.validate_on_submit():
      flash('Account Created', 'success')
      return redirect(url_for('home'))
   
   return render_template('register.html', title="Sign up",form=form)


if __name__ == "__main__":
    app.run(debug=True,port=3000)

