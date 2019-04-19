from app import db, feedbacks
print("\n--------------------------------------------------------\n")
print("Recieved feedback messages")
print("\n--------------------------------------------------------\n")
for i in feedbacks.query.all():
    print("Name : " + i.name)
    print("Feedback :")
    print(i.feedbackText)
    print("\n--------------------------------------------------------\n")
