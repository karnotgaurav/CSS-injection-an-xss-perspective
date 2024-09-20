from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Safe XSS Demo</title>
    </head>
    <body>
        <h1>Welcome to the XSS Safe Demo</h1>
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

    # Safe template that escapes user input
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h2>Hello, {{ name|e }}!</h2>
        <p>Your input was: {{ name|e }}</p>
    </body>
    </html>
    '''
    
    return render_template_string(template, name=name)

if __name__ == '__main__':
    app.run(debug=True)