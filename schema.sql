CREATE TABLE personal
(
    personid INTEGER PRIMARY KEY AUTOINCREMENT,
    fk_test INTEGER NOT NULL,
    answers_id INTEGER NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INTEGER NOT NULL,
    residence VARCHAR(15) NOT NULL,
    education VARCHAR(15) NOT NULL,
    SIknowledge BOOLEAN NOT NULL,
    FOREIGN KEY(fk_test) REFERENCES test(result_id),
    FOREIGN KEY(answers_id) REFERENCES questionnaire(answers_id)
);

CREATE TABLE test
(
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
	quizSI1 BOOLEAN NOT NULL,
	quizSI2 BOOLEAN NOT NULL,
	quizSI3 BOOLEAN NOT NULL,
	quizSI4 BOOLEAN NOT NULL,
	quizSI5 BOOLEAN NOT NULL,
	quizSI6 BOOLEAN NOT NULL
);

CREATE TABLE questionnaire
(
    answers_id          INTEGER PRIMARY KEY AUTOINCREMENT,
	have_met BOOLEAN NOT NULL,
	SIvsSystemy BOOLEAN NOT NULL,
	feelings VARCHAR(10) NOT NULL,
	EasyToFind BOOLEAN NOT NULL,
	EasyToFindExample1 BOOLEAN NOT NULL,
	EasyToFindExample2 BOOLEAN NOT NULL,
	EasyToFindExample3 BOOLEAN NOT NULL,
	EasyToFindExample4 BOOLEAN NOT NULL,
	EasyToFindExample5 BOOLEAN NOT NULL,
	EasyToFindExample6 BOOLEAN NOT NULL,
	are_useful VARCHAR(10) NOT NULL,
	fear BOOLEAN NOT NULL,
	endangered BOOLEAN NOT NULL,
	linkMonitoring1 BOOLEAN NOT NULL,
	linkMonitoring2 BOOLEAN NOT NULL,
	linkMonitoring3 BOOLEAN NOT NULL,
	linkMonitoring4 BOOLEAN NOT NULL,
	linkMonitoring5 BOOLEAN NOT NULL,
	linkMonitoring6 BOOLEAN NOT NULL,
	is_good BOOLEAN NOT NULL,
	is_affecting BOOLEAN NOT NULL,
	would_you_accept BOOLEAN NOT NULL,
	is_helping VARCHAR(10) NOT NULL,
	emotional_disorders INTEGER NOT NULL
);