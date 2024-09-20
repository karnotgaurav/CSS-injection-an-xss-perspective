from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSS Injection and XSS Vulnerable Template</title>
    </head>
    <body>
        <h1>Welcome to the CSS Injection and XSS Demo</h1>
        <form method="GET" action="/greet">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" />
            <label for="color">Enter your favorite color:</label>
            <input type="text" id="color" name="color" />
            <input type="submit" value="Submit" />
        </form>
    </body>
    </html>
    '''

@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    color = request.args.get('color', '')

    # Vulnerable template that directly inserts user input into style and HTML
    template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello</title>
        <style>
            h2 {{
                color: {color}; /* CSS Injection vulnerability */
            }}
        </style>
    </head>
    <body>
        <h2>Hello, {name}!</h2> <!-- XSS vulnerability -->
        <p>Your favorite color is: {color}</p> <!-- XSS vulnerability -->
    </body>
    </html>
    '''

    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
