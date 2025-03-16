#!/bin/bash

# Define input and output paths
INPUT_DIR="input_data"
OUTPUT_DIR="output"

# Remove previous output (HDFS) if exists
hadoop fs -rm -r $OUTPUT_DIR

# Run the Hadoop Streaming Job
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input $INPUT_DIR/sample.txt \
    -output $OUTPUT_DIR \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py

# Show the output
hadoop fs -cat $OUTPUT_DIR/part-*
