#!/usr/bin/pytho3
"""
A script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space)
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Renders "Hello HBNB!" when the root URL is visited.

    Returns:
    - str: Greeting message "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Renders "HBNB" when '/hbnb' route is visited.

    Returns:
    - str: "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    Renders the modified input text for the '/c/<text>' route.

    Args:
    - text (str): The text provided in the URL

    Returns:
    - str: Modified text with spaces replacing underscores
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_text(text="is cool"):
    """
    Renders the modified input text for the '/python/<text>' route.
    """
    return f"python {text}".replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Renders the modified input number """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Number_Template Function"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
