from PIL import Image
import win32api
import win32con
import win32gui

#hello it is huterox
StoreFolder = "D:\\time _ show\\picture\\download"

def setWallpaperFromBMP(imagepath):
        k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
        win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)

def setWallPaper(imagePath):
        """
        Given a path to an image, convert it to bmp and set it as wallpaper
        """
        bmpImage = Image.open(imagePath)
        newPath = StoreFolder + '\\mywallpaper.bmp'
        bmpImage.save(newPath, "BMP")
        setWallpaperFromBMP(newPath)
if __name__=='__main__':
        setWallPaper(r'D:\time _ show\picture\download\1.jpg')