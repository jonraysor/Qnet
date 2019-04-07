from flask import Flask, jsonify, request
import pandas

app = Flask(__name__)

__schools = None
__courses = None

@app.route('/')
def hello_world():
    return 'hi2'

def __readInFile(path, list):
    list = []
    data = pandas.read_csv(path)
    for i, row in data.iterrows():
        for school in row:
            list.append(school)

    return jsonify(list)

@app.route('/readInSchools')
def readInSchools():
    return __readInFile("schools.csv", __schools)

@app.route('/readInCourses')
def readInCourses():
    return __readInFile("Courses - Sheet1.csv", __courses)

@app.route('/ ')
def getAllSchools():
    return jsonify([])


@app.route('/getSchools')
def getSchools():
    return __schools

@app.route('/getCourses')
def getCourses():
    return __courses

__editDistanceMemo = {}


def editDistance(str1, str2):
    return editDistance(str1, str2, len(str1), len(str2))

def editDistance(str1, str2, i, j):

    if (str1, str2, i, j) in __editDistanceMemo:
        return __editDistanceMemo[(str1, str2, i, j)]
    if i==0:
        ans = j
    if j==0:
        ans = i

    if str1[i]==str2[j]:
        ans = editDistance(str1, str2, i-1, j-1)
    else:
        ans = 1 + min(editDistance(str1, str2, i-1, j), editDistance(str1, str2, i, j-1), editDistance(str1, str2, i-1, j-1))

    __editDistanceMemo[(str1, str2, i, j)] = ans

    return ans

@app.route('/writeToSchools')
def writeToSchools():
    name = request.args.get('name')
    if __schools is None:
        return "-1"
    if name not in __schools:
        return "1"
    #     with open('readInSchools.json') as outfile:
    #         json.dump(name, outfile)
    #     return name
    return name

app.run()
