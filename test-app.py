# test-app.http
POST http://localhost:5000/login # type: ignore
Content-Type: application/x-www-form-urlencoded

username=admin&password=password123

###
POST http://localhost:5000/login
Content-Type: application/x-www-form-urlencoded

username=admin&password=wrong

###
POST http://localhost:5000/login
Content-Type: application/x-www-form-urlencoded

username=test&password=test