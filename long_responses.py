import random

R_EATING = "I don't like eating anything because I'm a bot. Obviously!"


def unknown():
    response = ['Could you please re-phase that?',
                '...',
                "Sounds about right",
                "What does that mean?"][random.randint(4)]
    return response