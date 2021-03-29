from PIL import Image
import json
import time

def rotate_atlas(json_file, rotate_amount):
    global data
    # global rotate_amount
    with open(json_file) as f:
        data = json.load(f)

    atlas = Image.open(data["meta"]["image"])
    atlas_rotated = atlas.copy()

    atlas_images = []
    atlas_names = []

    x_list = []
    y_list = []

    for i in data["frames"]:
        
        f = "frame"

        x = i[f]["x"]
        y = i[f]["y"]
        w = i[f]["w"]
        h = i[f]["h"]

        x_list.append(x)
        y_list.append(y)

        atlas_images.append(atlas.crop((x, 
                                        y, 
                                        x + w, 
                                        y + h
                                        )))
        atlas_names.append(i["filename"])

    atlas_rotated.putalpha(0)

    for i in range(len(atlas_images)):
        atlas_images[i] = atlas_images[i].rotate(float(rotate_amount))
        atlas_rotated.paste(atlas_images[i], 
                            (x_list[i], y_list[i]),
                            mask=atlas_images[i])

    atlas_rotated.save(f"{data['meta']['image'][:-4]}_rotated_{rotate_amount}.png", "PNG")

if __name__ == "__main__":
    json_file = input("Json file (SSP json array): ")
    rotate_amount = input("How many degrees to rotate: ")
    print("Rotating...")
    try:
        rotate_atlas(json_file, rotate_amount)
    except FileNotFoundError:
        print(f"No such file {json_file}") 
    except ValueError:
        print("How much to rotate has to be an integer or float") 
    else:
        time.sleep(1)
        print()
        print("Rotated")
        time.sleep(0.1)
        print(f"Output file at: /{data['meta']['image']}_rotated_{rotate_amount}.png")
        del data
        del rotate_amount
        del json_file
