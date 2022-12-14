from survey import AnonymousSurvey

# defining the question makes the survey
question = "What language did you first learn to speak"
my_survey = AnonymousSurvey(question)

# show the question and store responses to the question
my_survey.show_question()
print(f"Enter 'q' any time to exit \n")
while True:
    response = input('Language : ')
    if response == 'q':
        break
    my_survey.store_response(response)
# show the survey results
print(f"Thank you to everyone who participated in the survey")
my_survey.show_results()
