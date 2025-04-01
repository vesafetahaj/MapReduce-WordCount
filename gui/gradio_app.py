import gradio as gr
from src.mapper import WordCountMapper
from src.reducer import WordCountReducer

def word_count(text):
    lines = text.strip().split("\n")
    mapper = WordCountMapper()
    reducer = WordCountReducer()
    mapped = [pair for line in lines for pair in mapper.map(line)]
    grouped = reducer.shuffle_and_sort(mapped)
    reduced = reducer.reduce(grouped)
    return "\n".join(f"{word}: {count}" for word, count in sorted(reduced.items()))

iface = gr.Interface(fn=word_count,
                     inputs="textarea",
                     outputs="textbox",
                     title="MapReduce Word Counter")

iface.launch()
