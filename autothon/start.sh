#!/bin/sh
behave -f allure_behave.formatter:AllureFormatter -o ./output/allure-reports ./features --tags=@example