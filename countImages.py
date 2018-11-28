images = open('folder-hierarchy.txt', 'r+')
images_counter = {}

for name in images.read().split():
   
    if name not in images_counter:
        images_counter[name] = 1
    else:
        images_counter[name[:12]] += 1

print(images_counter)
images.close();
