def extract_features(span):
    text = span['text']
    return {
        "font_size": span["size"],
        "is_bold": span["flags"] & 2 > 0,
        "char_count": len(text),
        "is_upper": text.isupper(),
        "starts_with_number": text.strip()[0].isdigit() if text.strip() else False,
        "page": span["page"],
        "y_pos": span["y"],
    }