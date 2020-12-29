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


## To use above: In the django console:
# from django.utils import timezone
# from import_fortunes import read_fortunes
# from banitsa.models import Fortune
# fortunes = read_fortunes('/home/norris/Downloads/късмети.txt')
# for (b, e) in fortunes:
#     f = Fortune(fortune_text=b, english_text=e, pub_date=timezone.now())
#     f.save()

