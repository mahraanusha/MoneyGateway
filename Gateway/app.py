from flask import Flask,render_template,request,url_for,redirect
import stripe

app=Flask(__name__)

public_key="pk_test_51BTUDGJAJfZb9HEBwDg86TN1KNprHjkfipXmEDMb0gSCassK5T3ZfxsAbcgKVmAIXF7oZ6ItlZZbXO6idTHE67IM007EwQ4uN3"

stripe.api_key="sk_test_tR3PYbcVNZZ796tH88S4VQ2u"

@app.route('/')
def index():
    return render_template('index.html',public_key=public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/payment',methods=['POST'])
def payment():

    customer=stripe.Customer.create(email=request.form['stripeEmail'],
                                    source=request.form['stripeToken'])

    charge=stripe.Charge.create(
           customer=customer.id,
           amount=1999,
           currency='usd',
           description='Donation'
    )

    return redirect(url_for('thankyou.html'))


if __name__=='__main__':
    app.run(debug=True)