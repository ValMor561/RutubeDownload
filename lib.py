from rutube import Rutube

def main():
    #Здесь можно указать свою ссылку или вынести её в параметр
    rt = Rutube('https://rutube.ru/video/46683613f856788afb068bd4e7ddf5b7/')
    print(rt.playlist[-1]._get_segment_urls())
    rt.playlist[-1].download()

if __name__ == "__main__":
    main()