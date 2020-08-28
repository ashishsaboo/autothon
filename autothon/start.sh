#!/bin/sh
behave -f allure_behave.formatter:AllureFormatter -o ./output/allure-reports ./features

allure serve ./output/allure-reports --port 9090

PID=$!
echo PID is $PID

sleep 60

kill $(lsof -t -i:9090)


