# buscador_pdfs.py
import PyPDF2

class BuscadorPDFs:
    @staticmethod
    def buscar_palabra(archivo_pdf, palabra):
        coincidencias = []

        with open(archivo_pdf, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_paginas = len(pdf_reader.pages)

            for pagina_num in range(num_paginas):
                pagina = pdf_reader.pages[pagina_num]
                texto_pagina = pagina.extract_text()

                if palabra.lower() in texto_pagina.lower():
                    coincidencias.append(f"Coincidencia en la página {pagina_num + 1}")

        return coincidencias
