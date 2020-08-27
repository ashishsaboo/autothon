#!/bin/sh
behave -f allure_behave.formatter:AllureFormatter -o ./output/allure-reports ./features --tags=@webservice

allure serve ./output/allure-reports --port 9090