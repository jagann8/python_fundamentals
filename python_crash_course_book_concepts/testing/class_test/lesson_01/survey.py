class AnonymousSurvey:
    """Collecting the anonymous answers from the survey form"""

    def __init__(self, question):
        """Store the question , prepare to store the response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show the survey question"""
        print(self.question)

    def store_response(self, response):
        """Storing the responses in the list"""
        self.responses.append(response)

    def show_results(self):
        """showing the answers"""
        print('Survey Results')
        for response in self.responses:
            print("  -", response.title())
