#!/bin/sh
behave -f allure_behave.formatter:AllureFormatter -o ./output/allure-reports ./features

#allure serve --allure.serve.timeout=10 ./output/allure-reports --port 9090


