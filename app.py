from flask import Flask, render_template, request, url_for
from Equasion_solver import Equasion_solver
import os


def transpose(s):

    matrix = double_from_string_matrix(s)
    m = len(matrix)
    n = len(matrix[0])

    for j in range(n):
        inner = []
        for i in range(m):
            inner.append(matrix[i][j])
        matrix.append(s)

    return matrix

equation_solver = Equasion_solver()


def double_from_string_matrix(s):
    matrix = []
    lines = s.split('\n')
    for l in lines:
        matrix.append([float(i) for i in l.split(" ")])
    return matrix


def apply_func_to_output_matrix(matrix, solution, func):
    matrix = func(matrix, solution)

    new_matrix = "$\\left(\\begin{matrix}\n"

    if len(matrix) > 0 and not isinstance(matrix[0], list):
        matrix = [matrix]
    rows_quantity = len(matrix)
    cols_quantity = len(matrix[0])

    for row in range(rows_quantity):
        line = ""
        for col in range(cols_quantity):
            line += str(matrix[row][col])
            if col != cols_quantity - 1:
                line += '&'
            else:
                line += '\\\\\n'
        new_matrix += line
    new_matrix += "\\end{matrix}\\right)$\n"

    return new_matrix

"""
The first argument is the name of the application’s module or package.
If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as
application or imported as module the name will be different ('__main__' versus the actual import name).
This is needed so that Flask knows where to look for templates, static files, and so on.
"""
app = Flask(__name__)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# route() decorator is used to bind a function to a URL
# Bind home-page to home_page() function
@app.route("/")
@app.route("/home-page")
def home_page():
    """
    Renders home page.
    :return: Home page render.
    """
    return render_template("homepage.html", header="Home page")


# Bind matrix-computation to matrix_computation() function
@app.route("/matrix-computation", methods=["GET", "POST"])
@app.route("/matrix-computation/<string:username>", methods=["GET", "POST"])
def matrix_computation(username=None):
    """

    :return:
    """
    if request.method == "GET":
        if username:
            username = username[0].capitalize() + username[1:]
        return render_template("matrix_computation.html",
                               header="Linear Algebra",
                               username=username)
    elif request.method == "POST":
        matrix = request.form["Matrix text area"]
        new_matrix = apply_func_to_output_matrix(double_from_string_matrix(matrix), [1, 1, 1], equation_solver.LU_solve)
        return render_template("matrix_computation.html",
                               header="Linear Algebra",
                               username=username,
                               matrix=matrix,
                               new_matrix=new_matrix)
    else:
        return "EM what?"

if __name__ == '__main__':
    app.run(debug=True)
