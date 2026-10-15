# Animatronic AI

A tiny, local, rule-based chatbot exploring the metaphor:

> “AI is no different than animatronics at Chuck E. Cheese.”

Showbot matches message text against a handful of patterns and chooses a
prepared response. It demonstrates how simple cues and scripted behavior can
create an impression of interaction.

The analogy is intentionally provocative, not a technical claim that all AI
systems work like this. Modern AI systems vary widely in their design and
capabilities. This project is a small teaching demo, not an AI model.

## Requirements

- Python 3.10 or newer
- No third-party packages
- No API keys or network connection

## Run

```bash
python3 showbot.py

Show the selected rule for each response:

bash


python3 showbot.py --explain
Use a fixed random seed to make the demo repeatable:

bash


python3 showbot.py --seed 7
Test
bash


python3 -m unittest -v
How it works
The program checks the message against ordered keyword-pattern cues.
The first matching cue selects a response category.
Showbot chooses a prepared line from that category.
If nothing matches, it uses a fallback response.
The rules and response lines are in showbot.py. Add a Cue to expand the
demo.

License
MIT