import os

for filename in sorted(os.listdir("./img/thumbnails")):
		print(f'''<div class="image">\n\t<img src="./img/thumbnails/{filename}" alt="" />\n</div>''')
