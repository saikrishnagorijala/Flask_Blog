from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='bf35fd3b9f135cc2b11424831fdbbb1b'

posts = [
	{
		'author' : 'Sai Krishna Gorijala',
		'title' : 'Blog Post 1',
		'content' : 'POst Content',
		'date_posted' : 'July 29, 2019'
	},
	{
		'author' : 'Test',
		'title' : 'Blog Post 2',
		'content' : 'POst Content',
		'date_posted' : 'July 30, 2019'
	}

]

@app.route('/')
@app.route('/homepage')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Ctreated {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True) 