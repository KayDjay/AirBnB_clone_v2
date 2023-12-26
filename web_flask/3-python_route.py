#!/usr/bin/python3
"""
A script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask


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
    return f"Python {text}".replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
