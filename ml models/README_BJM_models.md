# Project-3_BJM_models
23 November 2020

DATA

All models so far have been run using the "training" datafile, split into test and training sets. NaN values were removed, and columns with categorical values (e.g. Male/Female) transformed to dummy variables. The number of dependents was categorized in the original file as 0, 1, 2, 3+; for simplicity, the 3+ was changed to 3, and the column treated as numerical. The target column is Loan_Status_Y, where "0" indicates loan denied and "1" indicates loan accepted. The models run so far do not investigate the amount of the loan.

Because the question to date is simply whether a loan was approved or not, the loan amount and loan term seem logically in a gray area between factors contributing to a decision and the result of the decision - we do not know what people asked for vs. what they received. Most models were run both with and without those columns. While removing them may increase accuracy, it may also more closely match the user's situation. Of course letting them pick an amount could be interesting...

Maximum accuracy so far has been in the 70 - 80% range in all cases. The hunt continues.

File names will be edited at some point, but the ones considered here are labeled "fewer_dummies" because of the way the data was preprocessed.

----------------------------------------------------------------------------------------------------
GRID SEARCH (Project_3_BJM_grid_fewer_dummies)

Still running variations, so far accuracy is in the same range as all the others.

----------------------------------------------------------------------------------------------------
KNEIGHBORS CLASSIFIER (Project_3_BJM_KNN_fewer_dummies)

The same random state (57) was used throughout. There are graphs available showing the test/train convergence for each one. Did a little playing with other parameters, but nothing convincing to report yet.

KNN 1 : All factors included - this had the highest score

	data: drop["Loan_Status_Y", "Loan_ID"])
	for k in range(1, 40, 2):
   		 knn = KNeighborsClassifier(n_neighbors=k)
	k = 5 seemed best

	>> k=3 Test Acc: 0.800

KNN 2 : Took out Loan_Amount_Term - slight decrease in score

	data: drop(["Loan_Status_Y", "Loan_ID", 'Loan_Amount_Term'])
	for k in range(1, 40, 2):
   		 knn = KNeighborsClassifier(n_neighbors=k)
	k = 5 seemed best

	>> k=5 Test Acc: 0.792

KNN 3: Also removed LoanAmount - no further change in score

	data: drop(["Loan_Status_Y", "Loan_ID", 'LoanAmount', 'Loan_Amount_Term'])
	for k in range(1, 40, 2):
   		 knn = KNeighborsClassifier(n_neighbors=k)
	k = 7 seemed best

	>> k=7 Test Acc: 0.792

KNN 4: Also removed factors scored as less important in random forests - further decrease in score

	data: drop(["Loan_Status_Y", "Loan_ID", 'Property_Area_Urban', 'Self_Employed_Yes', 	'LoanAmount', 'Education_Graduate', 'Gender_Female', 'Loan_Amount_Term', 	'Property_Area_Semiurban', 'Property_Area_Rural'])
	for k in range(1, 40, 2):
   		 knn = KNeighborsClassifier(n_neighbors=k)
	k = 15 seemed best

	>> k=15 Test Acc: 0.758

----------------------------------------------------------------------------------------------------
DECISION TREES AND RANDOM FOREST (Project_3_BJM_Random_forest_fewer_dummies)

The same random state (57) was used throughout. For decision trees, there are graphs that can be printed out showing the decision path. For random forests, each was run with two sets of parameters, the second incorporating some ideas from the scikit documentation (which didn't help the scores, as far as tested). oob (out of bucket) scores for random forests are based on training data that wasn't used in a particular training run.

Decision Tree 1: Run to completion, big complicated tree.

	data: drop(["Loan_Status_Y", "Loan_ID"])

	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X_train, y_train)

	>>clf.score(X_test, y_test) = 0.675

Decision Tree 2: max_depth 3, actually improved score (again, have tree picture).

	data: drop(["Loan_Status_Y", "Loan_ID"])

	clf = tree.DecisionTreeClassifier(max_depth = 3)
	clf = clf.fit(X_train, y_train)

	>>clf.score(X_test, y_test) = 0.775

Decision Tree 3: max_depth 3, removed Loan_Amount_Term - some further score improvement.

	data:drop(["Loan_Status_Y", "Loan_ID", 'Loan_Amount_Term'])

	clf = tree.DecisionTreeClassifier(max_depth = 3)
	clf = clf.fit(X_train, y_train)

	>>clf.score(X_test, y_test) = 0.792

Decision Tree 4: max_depth 3, also removed LoanAmount - small drop in score.

	data: drop(["Loan_Status_Y", "Loan_ID", 'LoanAmount', 'Loan_Amount_Term'])

	clf = tree.DecisionTreeClassifier(max_depth = 3)
	clf = clf.fit(X_train, y_train)
	
	>>clf.score(X_test, y_test) = 0.742

Decision Tree 5: Run to completion; also removed factors scored as less important in random forests (below) - decreases score noticeably (compare Decision Tree 1)

	data: drop(["Loan_Status_Y", "Loan_ID", 'Property_Area_Urban', 'Self_Employed_Yes', 	'LoanAmount', 'Education_Graduate', 'Gender_Female', 'Loan_Amount_Term', 	'Property_Area_Semiurban', 'Property_Area_Rural'])

	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X_train, y_train)

	>>clf.score(X_test, y_test) = 0.625

Decision Tree 6: max_depth 3; also removed factors scored as less important in random forests (below) - no additional effect beyond removing LoanAmount (compare Decision Tree 4)

	data: drop(["Loan_Status_Y", "Loan_ID", 'Property_Area_Urban', 'Self_Employed_Yes', 	'LoanAmount', 'Education_Graduate', 'Gender_Female', 'Loan_Amount_Term', 	'Property_Area_Semiurban', 'Property_Area_Rural'])

	clf = tree.DecisionTreeClassifier(max_depth = 3)
	clf = clf.fit(X_train, y_train)

	>>clf.score(X_test, y_test) = 0.742


Random Forest 1
	"Normal" parameters
	data: drop(["Loan_Status_Y", "Loan_ID"])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True)

	Training score:  1.0
	Training score with oob sampling:  0.805

	>>Test score:  0.775

	Feature importance:
	[(0.2545660303780528, 'Credit_History_1.0'),
 	(0.1934237713276679, 'LoanAmount'),
 	(0.1925115642079434, 'ApplicantIncome'),
 	(0.10214297697022091, 'CoapplicantIncome'),
 	(0.05228753831715169, 'Dependents'),
 	(0.04905234431003756, 'Loan_Amount_Term'),
 	(0.030745078975053207, 'Married_Yes'),
 	(0.023163989851700637, 'Gender_Female'),
 	(0.023125590124404315, 'Education_Graduate'),
 	(0.021760074073080175, 'Property_Area_Semiurban'),
 	(0.021060343470290174, 'Self_Employed_Yes'),
 	(0.02024239830778944, 'Property_Area_Rural'),
 	(0.015918299686607774, 'Property_Area_Urban')]

	"Additional" parameters
	data: drop(["Loan_Status_Y", "Loan_ID"])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True, max_features=None, 		max_depth=None, min_samples_split=2)

	Training score, parameters added:  1.0
	Training score with oob sampling, parameters added:  0.797

	>>Test score, parameters added:  0.733

Random Forest 2: took out Loan_Amount_Term
	"Normal" parameters
	data: drop(["Loan_Status_Y", "Loan_ID", 'Loan_Amount_Term'])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True)

	Training score:  1.0
	Training score with oob sampling:  0.814

	>>Test score:  0.75

	Feature importance:
	[(0.2585073880773157, 'Credit_History_1.0'),
 	(0.20723756310634098, 'LoanAmount'),
 	(0.20507419599952217, 'ApplicantIncome'),
 	(0.1115836984945613, 'CoapplicantIncome'),
 	(0.05691140520356927, 'Dependents'),
 	(0.030776358517664772, 'Married_Yes'),
 	(0.02501354642025796, 'Education_Graduate'),
 	(0.0239079641390355, 'Gender_Female'),
 	(0.02357204560324534, 'Property_Area_Semiurban'),
 	(0.020625578884348694, 'Self_Employed_Yes'),
 	(0.02051294579450853, 'Property_Area_Rural'),
 	(0.01627730975962991, 'Property_Area_Urban')]

	"Additional" parameters
	data: drop(["Loan_Status_Y", "Loan_ID", 'Loan_Amount_Term'])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True, max_features=None, 		max_depth=None, min_samples_split=2)

	Training score, parameters added:  1.0
	Training score with oob sampling, parameters added:  0.780

	>>Test score, parameters added:  0.742

	Feature importance:
	[(0.30968518815756113, 'Credit_History_1.0'),
 	(0.22447121639012907, 'ApplicantIncome'),
 	(0.20697720407255865, 'LoanAmount'),
 	(0.08885423684819797, 'CoapplicantIncome'),
 	(0.0359861590988197, 'Dependents'),
 	(0.03114274180286901, 'Married_Yes'),
 	(0.020242435968616742, 'Property_Area_Semiurban'),
 	(0.019286348100211986, 'Education_Graduate'),
 	(0.018300204011104115, 'Gender_Female'),
 	(0.016716000498628977, 'Property_Area_Rural'),
 	(0.016037447202552832, 'Self_Employed_Yes'),
 	(0.012300817848749807, 'Property_Area_Urban')]

Random Forest 3: took out Loan_Amount_Term and LoanAmount
	"Normal" parameters
	data: drop(["Loan_Status_Y", "Loan_ID", 'LoanAmount', 'Loan_Amount_Term'])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True)

	Training score:  0.997
	Training score with oob sampling:  0.769

	>>Test score:  0.733

	Feature importance:
	[(0.3434784087065228, 'ApplicantIncome'),
 	(0.26244966884958665, 'Credit_History_1.0'),
 	(0.1496593738086105, 'CoapplicantIncome'),
 	(0.06413649565269215, 'Dependents'),
 	(0.03667586875843572, 'Married_Yes'),
 	(0.0286296568702607, 'Education_Graduate'),
 	(0.026739268581055128, 'Gender_Female'),
 	(0.02604427941624157, 'Property_Area_Semiurban'),
 	(0.023835171914341643, 'Self_Employed_Yes'),
 	(0.021666929089986395, 'Property_Area_Rural'),
 	(0.01668487835226702, 'Property_Area_Urban')]

	"Additional" parameters
	data: drop(["Loan_Status_Y", "Loan_ID", 'LoanAmount', 'Loan_Amount_Term'])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True, max_features=None, 		max_depth=None, min_samples_split=2)

	Training score, parameters added:  0.997
	Training score with oob sampling, parameters added:  0.783

	>>Test score, parameters added:  0.717

	Feature importance:
	[(0.3627153405553092, 'ApplicantIncome'),
 	(0.30183030830376517, 'Credit_History_1.0'),
 	(0.13044572910921842, 'CoapplicantIncome'),
 	(0.04916314242174194, 'Dependents'),
 	(0.03199027563367385, 'Married_Yes'),
 	(0.02350953017694175, 'Property_Area_Semiurban'),
 	(0.02185090009441822, 'Property_Area_Rural'),
 	(0.021146259935696934, 'Gender_Female'),
 	(0.02110932400501742, 'Education_Graduate'),
 	(0.019226359455124867, 'Self_Employed_Yes'),
 	(0.017012830309092185, 'Property_Area_Urban')]

Random Forest 4: took out Loan_Amount_Term and LoanAmount, as well as factors with importance <0.3 in both versions of previous run (this decreased the score)

	"Normal" parameters
	data: drop(["Loan_Status_Y", "Loan_ID", 'Property_Area_Urban', 'Self_Employed_Yes', 	'LoanAmount', 'Education_Graduate', 'Gender_Female', 'Loan_Amount_Term', 	'Property_Area_Semiurban', 'Property_Area_Rural'])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True)

	Training score:  0.997
	Training score with oob sampling:  0.780

	>>Test score:  0.667

	Feature importance:
	[(0.44992514095261715, 'ApplicantIncome'),
 	(0.29593743817229856, 'Credit_History_1.0'),
 	(0.1640639983749913, 'CoapplicantIncome'),
 	(0.05763910097322732, 'Dependents'),
 	(0.032434321526865664, 'Married_Yes')]

	"Additional" parameters
	data: drop(["Loan_Status_Y", "Loan_ID", 'Property_Area_Urban', 'Self_Employed_Yes', 	'LoanAmount', 'Education_Graduate', 'Gender_Female', 'Loan_Amount_Term', 	'Property_Area_Semiurban', 'Property_Area_Rural'])
	rf = RandomForestClassifier(n_estimators=200, oob_score = True, max_features=None, 		max_depth=None, min_samples_split=2)

	Training score, parameters added:  0.9972
	Training score with oob sampling, parameters added:  0.769

	>>Test score, parameters added:  0.675

	Feature importance:
	[(0.44707434742857804, 'ApplicantIncome'),
 	(0.31228351185569725, 'Credit_History_1.0'),
 	(0.14718939403224882, 'CoapplicantIncome'),
 	(0.05537754526522716, 'Dependents'),
 	(0.03807520141824874, 'Married_Yes')]

----------------------------------------------------------------------------------------------------
NEURAL NETWORKS (Project_3_BJM_deep_fewer_dummies)
The same random seed (1) was used throughout and the same random state (1) for test/train splits. 

Network 1: All columns used
	model = Sequential()
	model.add(Dense(units=100, activation='relu', input_dim=13))
	model.add(Dense(units=100, activation='relu'))
	model.add(Dense(units=2, activation='softmax'))
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	model.fit(X_train_scaled, y_train_categorical, epochs=60, shuffle=True, verbose=2)

	120/1 - 3s - loss: 0.6665 - accuracy: 0.7500

	>> Normal Neural Network 1 - Loss: 0.700603723526001, Accuracy: 0.75

Network 2: Took out Loan_Amount_Term - small decrease in accuracy
	model = Sequential()
	model.add(Dense(units=100, activation='relu', input_dim=12))
	model.add(Dense(units=100, activation='relu'))
	model.add(Dense(units=2, activation='softmax'))
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	model.fit(X_train_scaled, y_train_categorical, epochs=60, shuffle=True, verbose=2)

	120/1 - 3s - loss: 0.7005 - accuracy: 0.7333
	>> Normal Neural Network 1 - Loss: 0.7009, Accuracy: 0.7333

Network 3: Took out Loan_Amount_Term and LoanAmount - back to original accuracy
	model = Sequential()
	model.add(Dense(units=100, activation='relu', input_dim=11))
	model.add(Dense(units=100, activation='relu'))
	model.add(Dense(units=2, activation='softmax'))
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	model.fit(X_train_scaled, y_train_categorical, epochs=60, shuffle=True, verbose=2)

	120/1 - 3s - loss: 0.6535 - accuracy: 0.7500
	>> Normal Neural Network 1 - Loss: 0.6735, Accuracy: 0.75

Network 4: Took out Loan_Amount_Term and LoanAmount, added a layer - no change in accuracy
	model = Sequential()
	model.add(Dense(units=100, activation='relu', input_dim=11))
	model.add(Dense(units=100, activation='relu'))
	model.add(Dense(units=100, activation='relu'))
	model.add(Dense(units=2, activation='softmax'))
	model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
	model.fit(X_train_scaled, y_train_categorical, epochs=60, shuffle=True, verbose=2)

	120/1 - 2s - loss: 0.8270 - accuracy: 0.7500
	>> Normal Neural Network 1 - Loss: 0.8330, Accuracy: 0.75
----------------------------------------------------------------------------------------------------

