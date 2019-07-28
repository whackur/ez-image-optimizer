import os
import sys
from PIL import Image
from conf import image_config
import ntpath
import argparse


def optimize_in_dir(file_names, img_dir_path):
    for i in range(len(file_names)):
        print('{0}.{1}'.format(i+1, file_names[i]))
        try:
            resize_img(img_dir_path+file_names[i], image_config["max_dimension"])
        except Exception as e:
            print('Error => ', e)


def get_all_file_path(cwd):
    img_dir_path = cwd + '/' + image_config["origin_img_dir_path"]
    print('img_dir_path => ', img_dir_path)
    file_names = []

    # check extension
    for file_name in os.listdir(img_dir_path):
        ext = os.path.splitext(file_name)[1].lower()
        support_exts = ['.bmp','.gif','.png','.tiff','.jpeg','.jpg']
        if ext in support_exts:
            file_names.append(file_name)

    print('Bellow images will be optimize!!!')
    print(file_names)
    optimize_in_dir(file_names, img_dir_path)

    

def save_optimized_img(img_path, picture, ratio):
    width, height = (picture.size)
    picture.thumbnail((width*ratio,height*ratio), Image.ANTIALIAS)

    # following optimize_into_jpg option! => force convert to jpg
    if image_config["optimize_into_jpg"] == True:
        picture = picture.convert('RGB')
        file_name = ntpath.basename(img_path)
        new_name = os.path.splitext(file_name)[0]+'.jpg'
        print('optimizing...', img_path)
        try:
            picture.save(image_config["optimized_img_dir_path"] + new_name,"JPEG", optimize=True, quality=quality)
            print('Success !!!')
        except Exception as e:
            print('error => ', e)
    else:
        print('optimizing...', img_path)
        try:
            picture.save(image_config["optimized_img_dir_path"] + ntpath.basename(img_path), optimize=True, quality=quality)
        except Exception as e:
            print('error => ', e)


def resize_img(img_path, max_dimension):
    picture = Image.open(img_path)
    width, height = (picture.size)
    if width > height :
        longger_size = width
    else:
        longger_size = height
    ratio = max_dimension / longger_size
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
    help = '''Specific Image file path to convert. \nBasically, If do not use it, \n[./img/*] images will be optimized in [./img-optimized]\nor change conf.py
    '''
    parser = MyParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', required=False, help=help)
    
    if len(sys.argv) == 1:
        return None
    elif len(sys.argv) > 3 :
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
    img_path = args.f
    return img_path
    

if __name__ == "__main__":
    img_path = init_parser()
    cwd, quality, max_dimension = init_conf()
    print(cwd, quality, max_dimension)
    
    # convert all images in img directory
    if img_path == None:
        get_all_file_path(cwd)

    # convert specific image
    else:
        print('Target => ', img_path)
        try:
            resize_img(img_path, image_config["max_dimension"])
        except Exception as e:
            print('Error => ', e)
    input('Press any key...')