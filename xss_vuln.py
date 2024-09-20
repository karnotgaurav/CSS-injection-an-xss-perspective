from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>XSS Vulnerable Template</title>
    </head>
    <body>
        <h1>Welcome to the XSS Demo</h1>
        <form method="GET" action="/greet">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" />
            <input type="submit" value="Submit" />
        </form>
    </body>
    </html>
    '''

@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    
    # Vulnerable template that directly inserts user input
    template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h2>Hello, {name}!</h2>
        <p>Your input was: {name}</p>
    </body>
    </html>
    '''
    
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
