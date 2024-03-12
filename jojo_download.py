from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import img2pdf
import glob
import shutil
import os


def downloader():

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(20)

    for index in range(95):

        driver.get(f"https://lermanga.org/capitulos/jojo-no-kimyou-na-bouken-part-7-steel-ball-run-colorida-capitulo-{index+1:02}/")

        page_number = driver.find_element(By.XPATH, "//select[@class='select_paged']/option[2]").text

        page_number = int(page_number.split("/")[-1].strip())

        os.makedirs(f"imagens/capitulo-{index+1:02}", exist_ok=True)

        for pages_index in range(page_number):

            url_img = f"https://img.lermanga.org/J/jojo-no-kimyou-na-bouken-part-7-steel-ball-run-colorida/capitulo-{index+1}/{pages_index+1}.jpg"

            r = requests.get(url_img)

            with open(f"imagens/capitulo-{index+1:02}/capitulo-{index+1:02}_pagina_{pages_index+1:02}.jpg", 'wb') as outfile:
                outfile.write(r.content)

            print(f"Baixei a página {pages_index+1}")

        print(f"terminei o capitulo {index+1}")

def img_2_pdf():

    for folder in os.listdir("imagens/"):

        with open(f"pdfs/jojo-{folder}.pdf","wb") as f:
            f.write(img2pdf.convert(glob.glob(f"imagens/{folder}/*.jpg")))

if __name__ == "__main__":

    '''if os.path.exists('imagens/'):

        shutil.rmtree('imagens/')

    os.makedirs("imagens/", exist_ok=True)'''

    if os.path.exists('pdfs/'):

        shutil.rmtree('pdfs/')

    os.makedirs("pdfs/", exist_ok=True)
    
    #downloader()
    
    img_2_pdf()