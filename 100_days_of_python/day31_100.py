import emoji

    # Define a dictionary mapping colors to ANSI color codes
color_mapping = {
        "red": "\033[31m",
        "white": "\033[0m",
        "blue": "\033[34m",
        "yellow": "\033[33m",
        "green": "\033[32m",
        "purple": "\033[35m",
        "cyan": "\033[36m",
        "pink": "\033[95m"
    }

    # Updated colorChanger function using the color_mapping dictionary
def colorChanger(color):
    return color_mapping.get(color, "")

title = f"{colorChanger('red')}=\
{colorChanger('white')}= \
{colorChanger('blue')}= \
{colorChanger('yellow')}Music App \
{colorChanger('blue')}= \
{colorChanger('white')}= \
{colorChanger('red')}="

print( f"{title: >62}")
print(f"🔥▶️{colorChanger('white')}\t Radio Gaga")
print(f"\t{colorChanger('yellow')} Queen")

print()
print(f"{colorChanger('white')}PREV\n\
\t{colorChanger('green')}NEXT\n\
\t\t{colorChanger('purple')}PAUSE")
print()
print("*********************************")
print("*********************************")
print()

welcome = f"{colorChanger('white')}WELCOME TO"
text = "--  ARMBOOK  --"

phrase_1 = f"{colorChanger('yellow')}Definitely not a rip off of"
phrase_2 = f"{colorChanger('yellow')}a certain other social"
phrase_3 = f"{colorChanger('yellow')}networking site."
honest = f"{colorChanger('red')}Honest."
print(f"{welcome: >42}")
print(f"{colorChanger('blue')}{text:^65}")
print()
print(f" {phrase_1: >58}")
print(f"{phrase_2: >59}")
print(f"{phrase_3: >60}")
print()
print(f"{honest: >42}")
print(f"""
\t\t\t\t\t\t\t{colorChanger('white')}Username: \n\
\t\t\t\t\t\t\t{colorChanger('white')}Password:""")