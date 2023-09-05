from flask import Flask, flash, render_template, request, redirect, session, url_for
import requests  # Add this import at the top of your Flask app
import secrets

# Configure the base URL for your API
API_BASE_URL = 'http://localhost:8001/api'

app = Flask(__name__)
app.secret_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im9vdGFvcm9qdSIsImV4cCI6MTcxNDUyMzIyOH0.Lm916VGAQkunkbK9XkuKJ_qgcx3WQyKXFzWcJ6l7axA"

# Dummy user credentials for testing (replace with your actual authentication logic)
dummy_user = {'username': 'user', 'password': 'password'}
base_url = 'http://localhost:5000/'


@app.route('/')
def home():
    return "Welcome to the CRM Web App"


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
            print(session)

            # Redirect to accounts page on successful login
            return redirect(url_for('accounts_page'))

        # Authentication failed, show an error message
        flash('Invalid credentials', 'danger')

    return render_template('login.html')


""" @app.route('/accounts')
def accounts():
    # Get the access token from the session or cookie
    access_token = session.get('access_token')

    if access_token:
        # Make an authenticated request to your FastAPI API with the access token
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get('http://localhost:8001/api/accounts', headers=headers)

        if response.status_code == 200:
            accounts = response.json()
            return render_template('accounts.html', accounts=accounts)

    return redirect(url_for('login'))  # Redirect to login page if not authenticated """




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


@app.route('/accounts/<int:account_id>/cases', methods=['GET'])
def account_cases_page(account_id):
    # Fetch the list of accounts from your API endpoint
    account_response = requests.get(f"{API_BASE_URL}/accounts/{account_id}")
    cases_response = requests.get(
        f'{API_BASE_URL}/accounts/{account_id}/cases')
    account_data = account_response.json()
    if cases_response.status_code == 200:
        cases_data = cases_response.json()
        return render_template('account_cases.html', cases=cases_data, account=account_data)
    else:
        flash('Failed to fetch cases data from the API.', 'danger')
        return render_template('account_cases.html', cases=[])


@app.route('/createcase', methods=['GET', 'POST'])
def create_case_page():
    if request.method == 'POST':
        # Handle the account creation form submission
        form_data = {
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "email": request.form.get('email'),
            "address": request.form.get('address')
        }

        # Send a POST request to create the account
        response = requests.post(f'{API_BASE_URL}/cases', json=form_data)
        print(response.status_code)
        if response.status_code in (200, 201):
            case_created = response.json()
            flash('Case created successfully with the following details:', 'success')
            flash(case_created, 'success')
            return redirect(url_for('create_account_page'))
        else:
            flash('Failed to create the case. Please check the input data.', 'danger')
            return redirect(url_for('create_account_page'))

    return render_template('createcase.html')


@app.route('/createaccount', methods=['GET', 'POST'])
def create_account_page():
    """The account creation route"""
    print(session)
    # Get the access token from the session or cookie
    access_token = session.get(
        'access_token')
    print("access_token:", access_token)

    if access_token:
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
            print("form data:", form_data)
            # Send a POST request to create the account
            response = requests.post(
                f'{API_BASE_URL}/accounts', json=form_data, headers=headers)
            print("status_code:", response.status_code)
            if response.status_code in (200, 201):
                account_created = response.json()
                flash(
                    'Account created successfully with the following details:', 'success')
                flash(account_created, 'success')
                return redirect(url_for('accounts_page'))
            else:
                flash(
                    'Failed to create the account. Please check the input data.', 'danger')

        return render_template('createaccount.html')


@app.route('/cases/<int:id>', methods=['GET'])
@app.route('/cases/<int:id>/updates', methods=['GET'])
def cases_updates_page(id):
    # Fetch the list of accounts from your API endpoint
    case_response = requests.get(f"{API_BASE_URL}/cases/{id}")
    updates_response = requests.get(
        f'{API_BASE_URL}/cases/{id}/updates')
    case_data = case_response.json()
    if updates_response.status_code == 200:
        updates_data = updates_response.json()
        print(updates_data)
        return render_template('casedetails.html', case=case_data, updates=updates_data)
    else:
        flash('Failed to fetch cases data from the API.', 'danger')
        return render_template('casedetails.html', cases=[])


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
