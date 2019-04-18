import app

def test_histoDataTest():
    histoData = app.histoDataTest()
    assert len(histoData) == 11

def test_QuestionTest():
    QuestionList = app.QuestionTest()
    assert len(QuestionList) == 10

def test_Questions():
    QuestionList = app.QuestionTest()
    assert QuestionList[0].Answer == QuestionList[2].Answer

def test_add_score():
    oldLength = len(app.getUserMarks())
    app.addUserScore(4)
    newLength = len(app.getUserMarks())
    assert newLength - oldLength == 1