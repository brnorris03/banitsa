def read_fortunes(filename):
    lines = open("%s" % filename).readlines()
    fortunes = []
    for line in lines:
        if line.startswith("Б:"):
            bg_text = line.strip()
        elif line.startswith("E:"):
            en_text = line.strip()
            fortunes.append((bg_text,en_text))
    return fortunes
