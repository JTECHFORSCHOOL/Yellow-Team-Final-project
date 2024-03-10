from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Booking, Driver, Feedback, Payment, User
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configure the database connection
engine = create_engine('sqlite:///zTrip.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the database
def insert_data():
    # Example: Insert a new user
    new_user = User(username='John', email='john@example.com')
    session.add(new_user)

    # Example: Insert a new booking
    new_booking = Booking(user_id=new_user.id, pickup_location='Location A', dropoff_location='Location B')
    session.add(new_booking)

    # Example: Insert a new driver
    new_driver = Driver(name='Alice', vehicle='Toyota Camry')
    session.add(new_driver)

    # Example: Insert a new payment
    new_payment = Payment(user_id=new_user.id, amount=50.0, status='Completed')
    session.add(new_payment)

    # Example: Insert a new feedback
    new_feedback = Feedback(user_id=new_user.id, rating=4, comment='Great service!')
    session.add(new_feedback)

    # Commit the session to persist changes to the database
    session.commit()
# Define your user authentication logic here
def authenticate(username, password):
    # Example: Check if username and password match in database
    if username == 'admin' and password == 'yellow':
        return True
    else:
        return False

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if authenticate(username, password):
        # Redirect to dashboard or any other page upon successful login
        return redirect(url_for('dashboard'))
    else:
        # Redirect back to login page with an error message
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    # Render the dashboard template
    return render_template('dashboard.html')

# Define routes and application logic...
@app.route('/')
def index():
    # Call insert_data function to insert data into the database
    insert_data()
    return render_template('index.html')

@app.route('/users')
def get_users():
    users = session.query(User).all()
    return render_template('users.html', users=users)

@app.route('/bookings')
def get_bookings():
    bookings = session.query(Booking).all()
    return render_template('bookings.html', bookings=bookings)

@app.route('/drivers')
def get_drivers():
    drivers = session.query(Driver).all()
    return render_template('drivers.html', drivers=drivers)

@app.route('/payments')
def get_payments():
    payments = session.query(Payment).all()
    return render_template('payments.html', payments=payments)

@app.route('/feedbacks')
def get_feedbacks():
    feedbacks = session.query(Feedback).all()
    return render_template('feedbacks.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
