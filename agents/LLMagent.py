import random
import os
import openai

# COMMENTER ENTITY:
# inquiry: How does the LLM agent operate?
# answer: The LLM agent interacts with the GPT-4 API, passing the history of moves as a context. It then predicts the next most probable move based on that context.

openai.api_key = os.getenv("OPENAI_API_KEY")

def llm_agent(prev_play, opponent_history=[]):
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    if len(opponent_history) == 0:
        return random.choice(["R", "P", "S"])

    rps_string = " ".join(opponent_history)
    response = openai.Completion.create(
        model="gpt-4-0613",
        prompt=f"RPS sequence: {rps_string}. What's the next move?",
        max_tokens=5,
        temperature=0.5
    )
    next_move = response.choices[0].text.strip()

    # PRINT CREATOR ENTITY:
    print(f"LLM Agent uses GPT-4 prediction and suggests the move: {next_move}")

    return next_move
