### To run the project:

```
pip install - r requirements.txt
python manage.py runserver
```

### API Endpoints:

#### Authentication:

```
api/token/ - Obtain JWT token.
api/token/refresh/ - Refresh JWT token.
```

#### For Admin:

```
1. Exams
   - GET /exams/ - List all exams.
   - POST /exams/ - Create a new exam.
   - GET /exams/{id}/ - Retrieve details of a specific exam.
   - PUT /exams/{id}/ - Update details of a specific exam.
   - DELETE /exams/{id}/ - Delete a specific exam.
   - GET /exams/{id}/questions/ - Retrieve all questions associated with a specific exam.

2. Questions
   - GET /questions/ - List all questions.
   - POST /questions/ - Create a new question.
   - GET /questions/{id}/ - Retrieve details of a specific question.
   - PUT /questions/{id}/ - Update details of a specific question.
   - DELETE /questions/{id}/ - Delete a specific question.

4. Options
   - GET /options/ - List all options.
   - POST /options/ - Create a new option.
   - GET /options/{id}/ - Retrieve details of a specific option.
   - PUT /options/{id}/ - Update details of a specific option.
   - DELETE /options/{id}/ - Delete a specific option.
   
5. Enrollments
   - GET /enrollments/ - List all enrollments.
   - POST /enrollments/ - Create a new enrollment.
   - GET /enrollments/{id}/ - Retrieve details of a specific enrollment.
   - PUT /enrollments/{id}/ - Update details of a specific enrollment.
   - DELETE /enrollments/{id}/ - Delete a specific enrollment.
```

#### For Students:

```
1. Question Set:
   - GET /get-question-set/<int:exam_id>/ - Get the question set for an exam.

2. Answer Submission:
   - GET /answerscripts/ - List all answer scripts.
   - POST /answerscripts/ - Create a new answer script.
   - GET /answerscripts/{id}/ - Retrieve details of a specific answer script.
   - PUT /answerscripts/{id}/ - Update details of a specific answer script.
   - DELETE /answerscripts/{id}/ - Delete a specific answer script.
```