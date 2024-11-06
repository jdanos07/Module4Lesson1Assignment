def mood_response(mood):
    if mood == 'happy':
        return 'Great to hear! Spread that feeling to those around you!'
    elif mood == 'sad':
        return 'Do you want tp talk about it?'
    elif mood == 'angry':
        return 'Get it off your chest. Let me hear it.'
    elif mood == 'hungry':
        return 'Let\'s go eat!'
    elif mood == 'tired':
        return 'Go relax and try to get some sleep.'
    else:
        return 'I don\'t quite understand.\nEither way, if it\'s a good mood -\n    Keep it up!\nIf it\'s a bad mood -\n    Hope you find a resolution!'