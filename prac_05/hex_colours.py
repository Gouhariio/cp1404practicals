COLORS = {"darksalmon": "#e9967a", "floralwhite": "#fffaf0", "goldenrod": "#daa520", "gray6": "#0f0f0f",
          "indianred1": "#ff6a6a", "mediumpurple2": "#9f79ee", "mistyrose4": "#8b7d7b", "orange3": "#cd8500",
          "paleturquoise2": "#aeeeee", "skyblue4": "#4a708b"}
for key, value in COLORS.items():
    print(key, end='  ')

color_name = input("\n Enter color name: ").lower()
while color_name != "":
    if color_name in COLORS:
        print(color_name, "is", COLORS[color_name])
    else:
        print("Invalid color")
    color_name = input("Enter color name: ").lower()
