from flask import Flask, render_template, flash, redirect, url_for
from forms import TicketForm
import random
import string

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def generate_ticket_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

@app.route('/', methods=['GET', 'POST'])
def ticket():
    form = TicketForm()
    if form.validate_on_submit():
        ticket_id = generate_ticket_id()
        flash(f'Ticket submitted successfully! Your Ticket ID is: {ticket_id}', 'success')
        return redirect(url_for('ticket'))
    return render_template('ticket.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
