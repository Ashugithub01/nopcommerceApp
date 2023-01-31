
pytest -s -v -m "sanity" --html=./Reports/sanity_Regression.html TestCases/ --browser chrome

rem pytest -s -v -m "sanity" --html=./Reports/sanity_Regression.html TestCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/sanity_Regression.html TestCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/sanity_Regression.html TestCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/sanity_Regression.html TestCases/ --browser chrome

pytest -s -v -m "sanity" --html=./Reports/sanity_Regression.html TestCases/ --browser firefox

rem pytest -s -v -m "regression" --html=./Reports/sanity_Regression.html TestCases/ --browser firefox
rem pytest -s -v -m "sanity or regression" --html=./Reports/sanity_Regression.html TestCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./Reports/sanity_Regression.html TestCases/ --browser firefox

pytest -s -v -m "sanity" --html=./Reports/sanity_Regression.html TestCases/ --browser edge

rem pytest -s -v -m "regression" --html=./Reports/sanity_Regression.html TestCases/ --browser edge
rem pytest -s -v -m "sanity or regression" --html=./Reports/sanity_Regression.html TestCases/ --browser edge
rem pytest -s -v -m "sanity and regression" --html=./Reports/sanity_Regression.html TestCases/ --browser edge