import openai

# COMMENTER ENTITY:
# inquiry: Why are we using the `gpt-4-0613` model?
# answer: The `gpt-4-0613` model is one of the latest and most efficient models from OpenAI for text generation tasks. It's designed to provide accurate predictions for tasks like ours.

openai.api_key = os.getenv("OPENAI_API_KEY")

def llm_agent(prev_play, opponent_history=[], model="gpt-4-0613", max_tokens=7, temperature=0.5):
    # COMMENTER ENTITY:
    # inquiry: Why are we maintaining a history of plays?
    # answer: Maintaining a history helps the model in recognizing patterns and making more accurate predictions based on past data.
    
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    rps_sequence = " ".join(opponent_history)
    
    # COMMENTER ENTITY:
    # inquiry: How do we derive the prediction from the OpenAI API?
    # answer: We pass the rps_sequence as a prompt to the model. The model then returns its prediction for the next move, which we extract and return.

    response = openai.Completion.create(
        model=model,
        prompt=f"RPS sequence: {rps_sequence}. What's the next move?",
        max_tokens=max_tokens,
        temperature=temperature
    )

    # Extracting the predicted move from the response
    next_move = response.choices[0].text.strip()

    return next_move
