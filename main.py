import Browser.open
import Browser.close
import Registro.registro
import BookAPI.books_client



def main(name):
    Browser.close.close()
    driver = Browser.open.open()
    Registro.registro.registro(driver)
    BookAPI.books_client.obterLivros()
    BookAPI.books_client.obterLivroPorId('9781449325862')


    print(name)









if __name__ == '__main__':
    main('Registro-RPA')
