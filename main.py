import sqlite3

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
app.secret_key = "zuhdgf6RH@#DVSD"


def get_db_connection():
    conn = sqlite3.connect('mysite/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def general():
    if request.method == 'POST':
        gender = request.form.get('gender')
        age = request.form.get('age')
        residence = request.form.get('residence')
        education = request.form.get('education')
        do_know = request.form.get('SIknowledge')
        if do_know == "FALSE":
            return redirect(url_for('.definition', gender=gender, age=age, residence=residence, education=education,
                                    do_know=do_know))
        else:
            return redirect(
                url_for('.test', gender=gender, age=age, residence=residence, education=education, do_know=do_know))

        # instrukcja dla GET
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    gender = request.args['gender']
    age = request.args['age']
    residence = request.args['residence']
    education = request.args['education']
    do_know = request.args['do_know']
    if request.method == 'POST':
        quiz_si1 = request.form.get('quizSI1')
        quiz_si2 = request.form.get('quizSI2')
        quiz_si3 = request.form.get('quizSI3')
        quiz_si4 = request.form.get('quizSI4')
        quiz_si5 = request.form.get('quizSI5')
        quiz_si6 = request.form.get('quizSI6')
        return redirect(
            url_for('.questionnaire', gender=gender, age=age, residence=residence, education=education, do_know=do_know,
                    quiz_si1=quiz_si1, quiz_si2=quiz_si2, quiz_si3=quiz_si3, quiz_si4=quiz_si4, quiz_si5=quiz_si5,
                    quiz_si6=quiz_si6))

        # instrukcja dla GET
    return render_template('test.html')


@app.route('/definition', methods=['GET', 'POST'])
def definition():
    gender = request.args['gender']
    age = request.args['age']
    residence = request.args['residence']
    education = request.args['education']
    do_know = request.args['do_know']
    if request.method == 'POST':
        quiz_si1 = "FALSE"
        quiz_si2 = "FALSE"
        quiz_si3 = "FALSE"
        quiz_si4 = "FALSE"
        quiz_si5 = "FALSE"
        quiz_si6 = "FALSE"
        return redirect(
            url_for('.questionnaire', gender=gender, age=age, residence=residence, education=education, do_know=do_know,
                    quiz_si1=quiz_si1, quiz_si2=quiz_si2, quiz_si3=quiz_si3, quiz_si4=quiz_si4, quiz_si5=quiz_si5,
                    quiz_si6=quiz_si6))

        # instrukcja dla GET
    return render_template('definition.html')


@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    gender = request.args['gender']
    age = request.args['age']
    residence = request.args['residence']
    education = request.args['education']
    do_know = request.args['do_know']
    quiz_si1 = request.args['quiz_si1']
    quiz_si2 = request.args['quiz_si2']
    quiz_si3 = request.args['quiz_si3']
    quiz_si4 = request.args['quiz_si4']
    quiz_si5 = request.args['quiz_si5']
    quiz_si6 = request.args['quiz_si6']

    if request.method == 'POST':
        have_met = request.form.get('haveMet')
        SIvsSystemy = request.form.get('SIvsSystemy')
        feelings = request.form.get('feelings')
        EasyToFind = request.form.get('EasyToFind')
        EasyToFindExample1 = request.form.get('EasyToFindExample1')
        EasyToFindExample2 = request.form.get('EasyToFindExample2')
        EasyToFindExample3 = request.form.get('EasyToFindExample3')
        EasyToFindExample4 = request.form.get('EasyToFindExample4')
        EasyToFindExample5 = request.form.get('EasyToFindExample5')
        EasyToFindExample6 = request.form.get('EasyToFindExample6')
        are_useful = request.form.get('areUseful')
        fear = request.form.get('fear')
        endangered = request.form.get('endangered')
        linkMonitoring1 = request.form.get('linkMonitoring1')
        linkMonitoring2 = request.form.get('linkMonitoring2')
        linkMonitoring3 = request.form.get('linkMonitoring3')
        linkMonitoring4 = request.form.get('linkMonitoring4')
        linkMonitoring5 = request.form.get('linkMonitoring5')
        linkMonitoring6 = request.form.get('linkMonitoring6')
        is_good = request.form.get('isGood')
        is_affecting = request.form.get('isAffecting')
        would_you_accept = request.form.get('wouldAccept')
        is_helping = request.form.get('isHelping')
        emotional_disorders = request.form.get('emotionalDisorders')

        conn = get_db_connection()
        conn.execute("INSERT INTO test(quizSI1, quizSI2, quizSI3, quizSI4, quizSI5, quizSI6) "
                     "VALUES (?, ?, ?, ?, ?, ?);", (quiz_si1, quiz_si2, quiz_si3, quiz_si4, quiz_si5, quiz_si6,))
        conn.execute("INSERT INTO questionnaire(have_met, SIvsSystemy, feelings, EasyToFind, EasyToFindExample1, "
                     "EasyToFindExample2, EasyToFindExample3, EasyToFindExample4, EasyToFindExample5, "
                     "EasyToFindExample6, are_useful, fear, endangered, linkMonitoring1, linkMonitoring2, "
                     "linkMonitoring3, linkMonitoring4, linkMonitoring5, linkMonitoring6, is_good, is_affecting, "
                     "would_you_accept, is_helping, emotional_disorders) "
                     "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (have_met, SIvsSystemy, feelings, EasyToFind, EasyToFindExample1, EasyToFindExample2,
                                                                                                           EasyToFindExample3, EasyToFindExample4, EasyToFindExample5, EasyToFindExample6, are_useful, fear,
                                                                                                           endangered, linkMonitoring1, linkMonitoring2, linkMonitoring3, linkMonitoring4, linkMonitoring5,
                                                                                                           linkMonitoring6, is_good, is_affecting, would_you_accept, is_helping, emotional_disorders,))
        conn.commit()
        cur = conn.cursor()
        cur.execute('select count(*) from test;')
        testid = cur.fetchone()[0]
        cur.execute('select count(*) from questionnaire;')
        questid = cur.fetchone()[0]
        conn.execute('INSERT INTO personal (fk_test, answers_id, gender, age, residence, education, SIknowledge) '
                     'VALUES (?, ?, ?, ?, ?, ?, ?); ', (testid, questid, gender, age, residence, education, do_know,))
        conn.commit()
        conn.close()
        return render_template('thanks.html')
        # instrukcja dla GET
    return render_template('questionnaire.html')


if __name__ == '__main__':
    app.run()
