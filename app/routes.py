from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import ContactForm
from app.models import Contact


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    title = 'Home'
    form = ContactForm()

    if form.validate_on_submit():
        try:
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data
            )

            db.session.add(contact)
            db.session.commit()

            flash(f'Thanks for your submission, we will contact you shortly. A copy has been sent to {form.email.data}')
            return redirect(url_for('index'))
        except:
            flash('Sorry your submission did not go through. Try again')
            return redirect(url_for('index'))
    return render_template('index.html', title=title, form=form)
