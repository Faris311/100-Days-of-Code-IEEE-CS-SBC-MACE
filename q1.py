def words(text):
    let = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(let.find(c) + 1) for c in text.lower() if c in let])
