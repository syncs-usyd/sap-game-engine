#!/bin/bash

# Config
# The submission file to be used
submission_file=tutorialsubmission.py

# Number of submissions to play with
# (remember to update the corresponding config in the game engine)
num_submission=5

# The name of the testing environment
test_env=testing_environment

# Define the usage function
usage() {
    echo "Usage: $0 [-e] [-s submission_num]"
    echo "Options:"
    echo "  -e, --debug-engine       Enable debug mode for the engine"
    echo "  -s, --debug-submission   Enable debug mode for the submission with an integer value (0 <= submission_num < 5)"
    exit 1
}

# Initialize default values
debug_engine=false
debug_submission=false
debug_submission_value=""

# Parse the command-line options
while [[ $# -gt 0 ]]
do
    case "$1" in
        -e|--debug-engine)
            debug_engine=true
            shift
            ;;

        -s|--debug-submission)
            if [[ $# -lt 2 ]]
            then
                echo "Error: -s/--debug-submission requires an integer value (0 <= submission_num < 5)" >&2
                usage
            fi

            debug_submission=true
            debug_submission_value="$2"

            # Validate the integer value
            if [[ ! "$debug_submission_value" =~ ^[0-4]$ ]]
            then
                echo "Error: -s/--debug-submission submission_num must be an integer between 0 and 4 (inclusive)" >&2
                usage
            fi

            shift 2
            ;;

        *)
            echo "Invalid option: $1" >&2
            usage
            ;;
    esac
done

if [[ "$debug_engine" == true && "$debug_submission" == true ]]
then
    echo "Error: --debug-engine and --debug-submission flags cannot be used together" >&2
    usage
fi

if [[ "$debug_engine" == true ]]
then
    echo "Debug mode for the engine is enabled"
fi

if [[ "$debug_submission" == true ]]
then
    echo "Debug mode for the submission is enabled with a value of $debug_submission_value"
fi

echo "Deleting previous test environment"
rm -rf $test_env

echo "Creating fresh testing_environment"
mkdir $test_env

cd $test_env

mkdir output
cp -r ../engine engine
cp engine/__main__.py debug_engine.py

echo ""
submission_pids=()
for ((i = 0; i < num_submission; i++))
do
    folder=submission$i
    mkdir $folder

    cd $folder

    mkdir io
    touch io/submission.log
    touch io/submission.err

    from_engine=io/from_engine.pipe
    to_engine=io/to_engine.pipe
    mkfifo $from_engine
    mkfifo $to_engine
    chmod 0666 $from_engine
    chmod 0666 $to_engine

    cp ../../$submission_file submission.py
    cp -r ../../submissionhelper/submissionhelper/ submissionhelper

    if [[ "$debug_submission_value" != "$i" ]]
    then
        echo "Starting submission $i"
        python3 submission.py > io/submission.log 2>io/submission.err &
        submission_pids+=($!)
    fi

    cd ..
done
echo ""

if [[ "$debug_engine" == false ]]
then
    echo "Starting game engine"
    python3 -m engine &
    engine_pid=$!
fi

if [[ "$debug_engine" == false && "$debug_submission" == false ]]
then
    sleep_time=2
    echo "Game has started. Waiting $sleep_time seconds"
    echo ""
    sleep $sleep_time
else
    echo "Waiting for input before cleanup..."
    echo ""
    read
fi

if [[ "$debug_engine" == false ]]
then
    echo "Killing engine (note: this should fail)"
    kill $engine_pid
fi

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
