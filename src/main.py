# import os
# import subprocess
#
# # Define input and output directories in HDFS
# INPUT_DIR = "input_data"
# OUTPUT_DIR = "output"
#
#
# def run_hadoop_job():
#     """Run the Hadoop Streaming job for word count."""
#
#     # Remove previous output directory if it exists
#     subprocess.run(f"hadoop fs -rm -r {OUTPUT_DIR}", shell=True, check=False)
#
#     # Run the Hadoop Streaming Job
#     hadoop_cmd = f"""
#     hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
#         -input {INPUT_DIR}/sample.txt \
#         -output {OUTPUT_DIR} \
#         -mapper mapper.py \
#         -reducer reducer.py \
#         -file mapper.py \
#         -file reducer.py
#     """
#
#     process = subprocess.run(hadoop_cmd, shell=True)
#     if process.returncode == 0:
#         print("\n✅ Hadoop Streaming job completed successfully!\n")
#     else:
#         print("\n❌ Hadoop Streaming job failed.\n")
#
#     # Display the output
#     print("📜 Word Count Results:\n")
#     subprocess.run(f"hadoop fs -cat {OUTPUT_DIR}/part-*", shell=True)
#
#
# if __name__ == "__main__":
#     run_hadoop_job()
