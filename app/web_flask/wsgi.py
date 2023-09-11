#!/usr/bin/env python3
from flask import Flask, flash, render_template, request, redirect, session, url_for
import requests  # Add this import at the top of your Flask app

app = Flask(__name__)


# set global variables
API_BASE_URL = 'http://localhost:8001/api'
app.secret_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im9vdGFvcm9qdSIsImV4cCI6MTcxNDUyMzIyOH0.Lm916VGAQkunkbK9XkuKJ_qgcx3WQyKXFzWcJ6l7axA"
base_url = 'http://localhost:5000/'


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template("landingpage.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    global session
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Make an HTTP POST request to your FastAPI login endpoint
        response = requests.post(
            'http://localhost:8001/login/', data={'username': username, 'password': password})
        print(response)
        if response.status_code == 200:
            # Authentication succeeded, store the access token in the session or a cookie
            access_token = response.json()['access_token']
            print(access_token)
            # For example, store it in the session
            session['access_token'] = access_token
            session['username'] = username.split('@')[0]
            print(session)

            # Flash login successful message
            flash('User Login Successful', 'success')

            # Redirect to accounts page on successful login
            return redirect(url_for('accounts_page'))

        # Authentication failed, show an error message
        flash('Invalid credentials', 'danger')

    return render_template('login.html', session=session)

# logout route


@app.route('/logout')
def logout():
    # Clear the user's session (remove the access_token)
    session.pop('access_token', None)
    session.pop('username', None)

    flash("You're now logged out!", category='danger')
    # Redirect to the login page or any other desired page
    return redirect(url_for('login'))


@app.route('/accounts', methods=['GET'])
def accounts_page():
    # Fetch the list of accounts from your API endpoint
    response = requests.get(f'{API_BASE_URL}/accounts')

    if response.status_code == 200:
        accounts_data = response.json()
        return render_template('accounts.html', accounts=accounts_data)
    else:
        flash('Failed to fetch account data from the API.', 'danger')
        return render_template('accounts.html', accounts=[])


@app.route('/cases', methods=['GET'])
def cases_page():
    # Fetch the list of accounts from your API endpoint
    response = requests.get(f'{API_BASE_URL}/cases')
    print(response.text)

    if response.status_code == 200:
        cases_data = response.json()
        return render_template('cases.html', cases=cases_data)
    else:
        flash('Failed to fetch cases data from the API.', 'danger')
        return render_template('cases.html', cases=[])


@app.route('/accounts/<int:account_id>')
@app.route('/accounts/<int:account_id>/cases')
def account_cases_page(account_id):
    access_token = session.get('access_token')
    if not access_token:
        flash('Login Required to perform action, Please Login', 'danger')
        return redirect(url_for('login'))

    # Fetch the list of accounts from your API endpoint
    headers = {'Authorization': f'Bearer {access_token}'}
    account_response = requests.get(f"{API_BASE_URL}/accounts/{account_id}")
    print(f'account response: ****', account_response.status_code)
    cases_response = requests.get(
        f'{API_BASE_URL}/accounts/{account_id}/cases')
    print(f'case response: ****', cases_response.status_code)
    account_data = account_response.json()

    if cases_response.status_code == 200:
        cases_data = cases_response.json()
        return render_template('account_cases.html', cases=cases_data, account=account_data, headers=headers)
    else:
        flash('Failed to fetch cases data from the API.', 'danger')
        return render_template('account_cases.html', cases=[])


@app.route('/<int:account_id>/cases', methods=['GET', 'POST'])
def create_case_page(account_id):
    if request.method == 'POST':
        # Handle the case creation form submission
        form_data = {
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "email": request.form.get('email'),
            "address": request.form.get('address')
        }

        # Send a POST request to create the case using the captured account_id
        response = requests.post(
            f'{API_BASE_URL}/{account_id}/cases', json=form_data)

        if response.status_code in (200, 201):
            case_created = response.json()
            flash('Case created successfully with the following details:', 'success')
            flash(case_created, 'success')
            render_template('createcase.html')
        else:
            flash('Failed to create the case. Please check the input data.', 'danger')

    return render_template('createcase.html')


@app.route('/createaccount', methods=['GET', 'POST'])
def create_account_page():
    """The account creation route"""
    print(session)
    # Get the access token from the session or cookie
    access_token = session.get('access_token')
    print("access_token:", access_token)  # to be deleted

    if not access_token:
        flash('Login Required to perform action', 'danger')
        print('session_flash', session)
        return redirect(url_for('login'))
    else:
        # Make an authenticated request to your FastAPI API with the access token
        headers = {'Authorization': f'Bearer {access_token}'}
        print("headers", headers)
        if request.method == 'POST':
            # Handle the account creation form submission
            form_data = {
                "first_name": request.form.get('first_name'),
                "last_name": request.form.get('last_name'),
                "email": request.form.get('email'),
                "address": request.form.get('address')
            }
            # Send a POST request to create the account
            response = requests.post(
                f'{API_BASE_URL}/accounts', json=form_data, headers=headers)
            if response.status_code in (200, 201):
                account_created = response.json()
                flash(
                    'Account created successfully with the following details:', 'success')
                flash(account_created, 'success')
                # check for checkbox
                checkbox = request.form.get('createmorecheck')
                if checkbox == 'on':
                    return render_template('createaccount.html')
                else:
                    return redirect(url_for('accounts_page'))
            elif response.status_code == 401:
                flash('Session Expired: Please login again.', 'danger')
                return redirect(url_for('login'))
            else:
                flash(
                    'Failed to create the account. Please check the input data.', 'danger')

        return render_template('createaccount.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """The User Signup route"""
    if request.method == 'POST':
        register_data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'password': request.form.get('password'),
            'password2': request.form.get('password2')
        }
        if register_data['password'] != register_data['password2']:
            flash(
                'Password and Confirmation not the same, please check and try again', 'danger')
            return render_template('signup.html')
        register_data.pop('password2')
        print(f'register_data: ', register_data)
        try:
            response = requests.post(f'{API_BASE_URL}/users',
                                     json=register_data)
            if response.status_code in (201, 200):
                user_created = response.json().get('username')
                flash(
                    f'User: {user_created} Registered Successfully! Please Login', 'success')
                return redirect(url_for('login'))
            elif response.status_code == 409:
                flash(
                    'User Already Exists, please try a different Username or Email', 'danger')
            else:
                flash(
                    f'Unable to create user {register_data["username"]}', 'danger')
        except Exception as err:
            flash(err, 'danger')
    return render_template('signup.html')


@app.route('/cases/<int:id>', methods=['GET'])
@app.route('/cases/<int:id>/updates', methods=['GET'])
def cases_updates_page(id):
    # Fetch the list of accounts from your API endpoint
    access_token = session.get('access_token')
    if not access_token:
        flash('Login Required to access this page! Please Login')
        return redirect(url_for('login'))
    case_response = requests.get(f"{API_BASE_URL}/cases/{id}")
    # headers
    headers = {'Authorization': f'Bearer {access_token}'}
    updates_response = requests.get(
        f'{API_BASE_URL}/cases/{id}/updates')
    case_data = case_response.json()
    if updates_response.status_code == 200:
        updates_data = updates_response.json()
        print(updates_data)
        return render_template('casedetails.html', case=case_data, updates=updates_data, headers=headers)
    else:
        flash('Failed to fetch cases data from the API.', 'danger')
        return render_template('casedetails.html', cases=[])


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
