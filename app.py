from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result="")

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.form['expression']
        
        # Basic validation to ensure the input contains only valid characters
        if not all(c in "0123456789+-*/%.() " for c in expression):
            return render_template('index.html', result="Error: Invalid characters in input!")

        # Evaluate the mathematical expression
        result = eval(expression)

        # Display the result in the format: "expression = result"
        return render_template('index.html', result=f"{expression} = {result}")
    except ZeroDivisionError:
        return render_template('index.html', result="Error: Division by zero!")
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
