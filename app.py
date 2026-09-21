from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")


@app.route("/result", methods=["POST"])
def result():

    # Student answers
    coding = int(request.form["coding"])
    gaming = int(request.form["gaming"])
    electrical = int(request.form["electrical"])
    mechanical = int(request.form["mechanical"])
    design = int(request.form["design"])
    maths = int(request.form["maths"])
    business = int(request.form["business"])
    communication = int(request.form["communication"])


    # Career scores
    computer_score = coding + gaming + maths

    electrical_score = electrical + maths

    mechanical_score = mechanical + maths

    design_score = design + communication

    business_score = business + communication


    # Store scores
    scores = {
        "Computer Science": computer_score,
        "Electrical & Electronics": electrical_score,
        "Mechanical Engineering": mechanical_score,
        "Design & Creative": design_score,
        "Business & Management": business_score
    }


    # Find highest score
    top_career = max(scores, key=scores.get)

    top_score = scores[top_career]


    # Convert score into percentage
    percentage = round((top_score / 12) * 100)


    # Recommended courses
    recommendations = {

        "Computer Science": [
            "B.E Computer Science Engineering",
            "B.Tech Information Technology",
            "B.Tech Artificial Intelligence & Data Science",
            "B.Tech Cyber Security"
        ],

        "Electrical & Electronics": [
            "B.E Electrical & Electronics Engineering",
            "B.E Electronics & Communication Engineering",
            "B.Tech Electronics"
        ],

        "Mechanical Engineering": [
            "B.E Mechanical Engineering",
            "B.E Automobile Engineering",
            "B.E Mechatronics Engineering"
        ],

        "Design & Creative": [
            "B.Des",
            "B.Sc Visual Communication",
            "B.A Visual Communication"
        ],

        "Business & Management": [
            "BBA",
            "B.Com",
            "BMS",
            "BA Economics"
        ]
    }


    courses = recommendations[top_career]


    return render_template(
        "result.html",
        career=top_career,
        percentage=percentage,
        courses=courses
    )


if __name__ == "__main__":
    app.run(debug=True)