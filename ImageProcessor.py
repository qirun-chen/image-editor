# coding=utf-8
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class ImageProcessor:
    def __init__(self, output_path):
        self.image_path = os.getcwd() + os.sep + "img_template.jpg"
        self.font1_path = os.getcwd() + os.sep + "msyh.ttf"
        self.font2_path = os.getcwd() + os.sep + "Microsoft-Yahei-UI-Bold.ttc"
        self.output_path = output_path
        print self.image_path

    def add_name_and_id_on_img(self, name_id_dict):
        if not os.path.exists(self.image_path):
            return "image does not exist."

        if not os.path.exists(self.font1_path) or not os.path.exists(self.font2_path):
            return "font does not exist."

        self.edit_each_image(name_id_dict)

        return "Success"

    def edit_each_image(self, name_id_dict):
        for name, id in name_id_dict.iteritems():
            image = Image.open(self.image_path)
            if image.mode not in ('L', 'RGB'):
                image = image.convert('RGB')

            draw = ImageDraw.Draw(image)
            font1 = ImageFont.truetype(self.font1_path, 30)
            font2 = ImageFont.truetype(self.font2_path, 32)
            draw.text((301, 98), name, (0, 0, 0), font=font1)
            draw.text((300, 170), id, (0, 0, 0), font=font1)
            draw.text((301, 238), u"认证成功", (0, 0, 0), font=font2)
            draw = ImageDraw.Draw(image)

            save_path = '%s/%s' % (self.output_path, name + "_" + id + ".jpg")

            if not os.path.exists:
                os.makedirs(self.output_path)

            image.save(save_path)