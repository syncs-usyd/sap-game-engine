#!/bin/bash
submission_file=tutorialsubmission.py
num_submission=2
test_env=testing_environment

echo "Deleting previous test environment"
rm -rf $test_env

echo "Creating fresh testing_environment"
mkdir $test_env

cd $test_env

echo "Creating folders for game engine\n"
mkdir output

echo "Copying game engine"
cp -r ../engine engine

submission_pids=()
for ((i = 0; i < num_submission; i++))
do
    echo "Creating folder for submission $i"
    folder=submission$i
    mkdir $folder

    cd $folder

    echo "Creating io folder, files and pipes"
    mkdir io
    touch io/submission.log
    touch io/submission.err
    from_engine=io/from_engine.pipe
    to_engine=io/to_engine.pipe
    mkfifo $from_engine
    mkfifo $to_engine
    chmod 0666 $from_engine
    chmod 0666 $to_engine

    echo "Copying submission $i into folder"
    cp ../../$submission_file submission.py

    echo "Copying submission helper into folder"
    cp -r ../../submissionhelper submissionhelper

    python3 submission.py > io/submission.log 2>io/submission.err &
    submission_pids+=($!)

    cd ..
done

python3 -m engine &
engine_pid=$!

sleep_time=300
echo "Game has started. Waiting $sleep_time seconds"
sleep $sleep_time

echo "Killing engine if it hasn't already finished"
kill $engine_pid

for pid in "${submission_pids[@]}"
do
    echo "Killing submission with PID: $pid"
    kill $pid
done

echo "Cleanup named pipes"
for ((i = 0; i < num_submission; i++))
do
    from_engine=submission$i/io/from_engine.pipe
    to_engine=submission$i/io/to_engine.pipe
    rm $from_engine
    rm $to_engine
done