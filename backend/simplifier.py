def simplify_text(text):
    if not text:
        return ""

    replacements = {
        "approximately": "about",
        "individuals": "people",
        "assistance": "help",
        "utilize": "use",
        "demonstrate": "show",
        "purchase": "buy",
        "commence": "start",
        "terminate": "stop"
    }

    text = text.lower()

    for complex_word, simple_word in replacements.items():
        text = text.replace(complex_word, simple_word)

    return text
