from flask import Flask, render_template, request, redirect, url_for
from ride_tracking import Ride
from payment import Payment

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track_ride', methods=['GET', 'POST'])
def track_ride():
    if request.method == 'POST':
        # Get ride data from the form
        ride_id = request.form['ride_id']
        driver_id = request.form['driver_id']
        passenger_id = request.form['passenger_id']
        pickup_location = request.form['pickup_location']
        dropoff_location = request.form['dropoff_location']
        # Create a new ride instance
        track_ride_ride = Ride(ride_id, driver_id, passenger_id, pickup_location, dropoff_location)
        # Here you can save the ride to the database or perform any other actions
        return redirect(url_for('index'))
    return render_template('track_ride.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # Get payment data from the form
        ride_id = request.form['ride_id']
        amount = request.form['amount']
        payment_method = request.form['payment_method']
        # Create a new payment instance
        payment = Payment(ride_id, amount, payment_method)
        # Here you can save the payment to the database or perform any other actions
        return redirect(url_for('index'))
    return render_template('payment.html')

if __name__ == '__main__':
    app.run(debug=True)
