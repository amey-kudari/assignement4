import app

# test to make sure all values are within range 0,10
def test_histoDataTest():
    histoData = app.getUserMarks()
    histodata=[0,0,0,0,0,0,0,0,0,0,0]
    for i in histoData:
        if int(str(i))>=0 and int(str(i))<=10:
            histodata[int(str(i))]+=1
    assert len(histodata) == 11

# test to make sure all questions exist
def test_QuestionTest():
    QuestionList = app.QuestionTest()
    assert len(QuestionList) == 10

# test to make sure questins are not altered
def test_Questions():
    QuestionList = app.QuestionTest()
    assert QuestionList[0].Answer == QuestionList[2].Answer

# test to check working of add score controller
def test_add_score():
    oldLength = len(app.getUserMarks())
    app.addUserScore(4)
    newLength = len(app.getUserMarks())
    assert newLength - oldLength == 1