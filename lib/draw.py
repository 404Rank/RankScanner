import os;
from PIL import Image
class functions:
    # 将一个灰度值转换成对应的字符
    def GraytoChar(self,gray):
        allChar = """@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'"""
        char = allChar[int(len(allChar)*gray/256)]
        return char


    # 将真彩色图像转换成字符画，真彩色图像文件路径为path
    def toCharImage(self,path):
        if(os.path.exists(path)):
            img = Image.open(path)
            ow, oh = img.size  # 原始图像的宽和高
            w = 80  # 调整后的宽度（即字符画每行有w个字符）
            h = w * oh // ow  # 高度也按比例调整（即字符画总共有h行）
            h = h // 2  # 在文本中，行与行之间有间隔，要进一步缩小高度才能得到较好效果
            img = img.resize((w, h))  # 调整图片大小
            img = img.convert('L')  # 将真彩色图像转换为灰度图
            charImg = ''  # 用于存储字符画

            for y in range(h):
                s = ''
                for x in range(w):
                    gray = img.getpixel((x, y))  # 取出灰度值
                    char = self.GraytoChar(gray)
                    s = s + char
                charImg = charImg + s + '\n'
            return charImg
        else:
            return "";

class Draw:
    def toCharImage(path) -> str:
        change = functions();
        return change.toCharImage(path);
