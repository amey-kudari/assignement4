from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import json

global_score=5

app = Flask(__name__)
# name will be changed later, configs will be added later
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class QuizResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.score}"

class QuizQuestions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(350))
    Option1 = db.Column(db.String(350)) 
    Option2 = db.Column(db.String(350)) 
    Option3 = db.Column(db.String(350))
    Answer = db.Column(db.Integer)

def addUserScore(marks):
    new = QuizResults(score=marks)
    db.session.add(new)
    db.session.commit()

def getUserMarks():
    return QuizResults.query.all()

@app.route("/")
def IntroductionPage():
    return render_template('Introduction.html')

@app.route("/Theory")
def TheoryPage():
    return render_template('Theory.html')

@app.route("/Objective")
def ObjectivePage():
    return render_template('Objective.html')

@app.route("/Experiment")
def ExperimentPage():
    return render_template('Experiment.html')

@app.route("/Manual")
def ManualPage():
    return render_template('Manual.html')

@app.route("/Quizzes")
def QuizzesPage():
    Questions = QuizQuestions.query.all()
    answers = []
    for i in Questions:
        answers.append(i.Answer)
    return render_template('Quizzes.html',
        QuestionList = Questions,
        ListAnswers = answers)

@app.route("/Procedure")
def ProcedurePage():
    return render_template('Procedure.html')

@app.route("/Refrences")
def RefrencesPage():
    return render_template('Refrences.html')

@app.route("/Feedback")
def FeedbackPage():
    return render_template('Feedback.html')


@app.route("/Results")
def ResultPage():
    histodata=[0,0,0,0,0,0,0,0,0,0,0]
    for i in QuizResults.query.all():
        if int(str(i))>=0 and int(str(i))<=10:
            histodata[int(str(i))]+=1
        userMarksList = getUserMarks()
    return render_template('Results.html',
        tscore=userMarksList[-1],
        scores=userMarksList,
        histoData=histodata)

@app.route("/add_score/<marks>")
def addScrore(marks):
    addUserScore(marks)
    return redirect(url_for('ResultPage'))

# test to make sure the controller with database works perfectly
# get histodata
def histoDataTest():
    histodata=[0,0,0,0,0,0,0,0,0,0,0]
    for i in QuizResults.query.all():
        if int(str(i))>=0 and int(str(i))<=10:
            histodata[int(str(i))]+=1
    return histodata

# test questions
def QuestionTest():
    Questions = QuizQuestions.query.all()
    return Questions

# tests are written in test_app.py

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
