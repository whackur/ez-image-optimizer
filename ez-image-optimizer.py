import os
import sys
from PIL import Image
from conf import image_config
import ntpath
import argparse

def save_optimized_img(img_path, picture, ratio):
    width, height = (picture.size)
    picture.thumbnail((width*ratio,height*ratio), Image.ANTIALIAS)

    # following only_jpg option! => force convert to jpg
    if image_config["only_jpg"] == True:
        picture = picture.convert('RGB')
        file_name = ntpath.basename(img_path)
        new_name = os.path.splitext(file_name)[0]+'.jpg'
        picture.save('./img-optimized/'+new_name,"JPEG",optimize=True,quality=quality)
    else:
        picture.save('./img-optimized/'+ntpath.basename(img_path),optimize=True,quality=quality)

def resize_img(img_path, max_dimension):
    picture = Image.open(img_path)
    width, height = (picture.size)
    if width > height :
        longger_size = width
    else:
        longger_size = height
    ratio = max_dimension / longger_size
    
    print('Compress Ratio => ', ratio)
    save_optimized_img(img_path, picture, ratio)

def init_conf():
    cwd = os.path.dirname(os.path.realpath(__file__))
    quality = image_config["quality"]
    max_dimension = image_config["max_dimension"]
    return cwd, quality, max_dimension

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def init_parser():
    parser = MyParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', required=False, help='Specific Image file path to convert.\nIf do not use it,\n[./img/*] images will be optimized in [./img-optimized]')
    
    if len(sys.argv) == 1:
        return None
    elif len(sys.argv) != 3 :
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
    img_path = args.f
    return img_path
    

if __name__ == "__main__":
    img_path = init_parser()
    cwd, quality, max_dimension = init_conf()
    print(cwd, quality, max_dimension)
    

    if img_path == None:
        pass
    else:
        specific_path = cwd + '/' + img_path
        resize_img(specific_path, image_config["max_dimension"])