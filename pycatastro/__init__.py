# coding=utf-8
import requests
import xmltodict


try:
    __version__ = __import__('pkg_resources') \
        .get_distribution(__name__).version
except Exception as e:
    __version__ = 'unknown'


class PyCatastro(object):
    base_url = "http://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC"

    @classmethod
    def ConsultaProvincia(cls):
        """Proporciona un listado de todas las provincias.

           Proporciona un listado de todas las provincias españolas en
           las que tiene competencia la Dirección general del Catastro.
           :return: Retorna un dicionario con los datos de la consulta
           :rtype: dict
        """

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaProvincia"
        response = requests.get(url)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)


    @classmethod
    def ConsultaMunicipio(cls, provincia, municipio=None):
        """Proporciona un listado de todos los municipios de una provincia.

            Proporciona un listado de todos los nombres de los municipios de una
            provincia (parámetro "Provincia"),así como sus códigos (de Hacienda
            y del INE), cuyo nombre Servicios web del Catastro 5 contiene la cadena
            del parámetro de entrada "Municipio". En caso de que este último
            parámetro no tenga ningún valor, el servicio devuelve todos los
            municipios de la  provincia.También proporciona información de si
            existe cartografía catastral (urbana o rústica) de cada municipio.

            :param str: Nombre de la provincia
            :param str: Opcional , nombre del municipio
            :return: Retorna un dicionario con los datos de la consulta
            :rtype: dict
        """

        params = {'Provincia': provincia}
        if municipio:
            params['Municipio'] = municipio
        else:
            params['Municipio'] = ''

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaMunicipio"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)


    @classmethod
    def ConsultaVia(cls, provincia, municipio, tipovia=None, nombrevia=None):
        """Proporciona un listado de todas las vías de un municipio.

            Proporciona un listado de todas las vías de un municipio (parámetros
            "Provincia" y "Municipio"), así como los códigos de las mismas según la
            Dirección General del Catastro (DGC) , cuyo nombre contiene la cadena
            del parámetro de entrada "NombreVia" y, en caso de que el parámetro
            "TipoVia" contenga información, existe coincidencia en el tipo de la
            vía. En caso de que el parámetro "NombreVia" no tenga ningún valor, el
            servicio devuelve todas las vías del municipio del "TipoVia" indicado.

            :param str: Nombre de la provincia
            :param str: Nombre de municipio
            :return: Retorna un dicionario con los datos de la consutla
            :rtype: dict
        """

        params = {'Provincia': provincia,
                  'Municipio': municipio}
        if tipovia:
            params['TipoVia'] = tipovia
        else:
            params['TipoVia'] = ''
        if nombrevia:
            params['NombreVia'] = nombrevia
        else:
            params['NombreVia'] = ''

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaVia"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def ConsultaNumero(cls, provincia, municipio, tipovia, nombrevia, numero):
        """Proporciona la referencia catastral de la finca correspondiente.

            Proporciona,o bien la referencia catastral de la finca correspondiente
            al contenido del parámetro "Número",en caso de que este exista,o bien se
            devuelve un error ("El número no existe") y se proporciona una lista
            de los números más aproximados al solicitado, en un rango de 5 por
            arriba y 5 por abajo. Por ejemplo, si se solicita el número 10, y en
            esa vía existen los números 2,3,6,7,9,11,15 y 17, se devuelve una lista
            con los números 6,7,9,11 y 15.Junto con la lista de números, se
            proporcionan las referencias catastrales de las fincas.

            :param str: Nombre de la provincia
            :param str: Nombre del municipio
            :param str: Tipo d ela via
            :param str: Nombre de la via
            :param str,int: Numero del que se desea conocer la referencia
            :return: Retorna un dicionario con los datos de la consutla
            :rtype: dict
        """

        params = {'Provincia': provincia,
                  'Municipio': municipio,
                  'TipoVia': tipovia,
                  'NomVia': nombrevia,
                  'Numero': str(numero)}

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaNumero"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_DNPLOC(cls, provincia, municipio, sigla, calle, numero, bloque=None, escalera=None, planta=None,puerta=None):
        """Proporciona la lista de todos los inmuebles coincidentes o sus datos.

            Este servicio puede devolver o bien la lista de todos los inmuebles que
            coinciden con los criterios de búsqueda, proporcionando para cada
            inmueble la referencia catastral y su localización
            (bloque/escalera/planta/puerta) o bien, en el caso de que solo exista
            un inmueble con los parámetros de entrada indicados, proporciona los
            datos de un inmueble.

            :param str: Nombre de la provincia
            :param str: Nombre del municipio
            :param str: Sigla
            :param str: Nombre de la calle
            :param str,int: Numero del que se quiere conocer los datos
            :param str,int: Opcional,numero de bloque
            :param str: Opcional, numero d'escala
            :param str,int: Opcional, numero de planta
            :param str,int: Opcional, numero de puerta
            :return: Retorna un dicionario con los datos de la consutla
            :rtype: dict
        """

        params = {'Provincia': provincia,
                  'Municipio': municipio,
                  'Sigla': sigla,
                  'Calle': calle,
                  'Numero': str(numero)}
        if bloque:
            params['Bloque'] = str(bloque)
        else:
            params['Bloque'] = ''
        if escalera:
            params['Escalera'] = escalera
        else:
            params['Escalera'] = ''
        if planta:
            params['Planta'] = str(planta)
        else:
            params['Planta'] = ''
        if puerta:
            params['Puerta'] = str(puerta)
        else:
            params['Puerta'] = ''

        url = cls.base_url + "/OVCCallejero.asmx/Consulta_DNPLOC"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_DNPRC(cls, provincia, municipio, rc):
        """Proporciona los datos catastrales no protegidos de un inmueble

           Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
           PROTEGIDOS de un inmueble identificado por su localización" en todo
           excepto en los parámetros de entrada.

           :param str: Nombre de la provincia
           :param str: Nombre del municipio
           :param str: Referencia catastral
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {"Provincia": provincia,
                  "Municipio": municipio,
                  "RC": rc}

        url = cls.base_url + "/OVCCallejero.asmx/Consulta_DNPRC"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_DNPPP(cls, provincia, municipio, poligono, parcela):
        """Proporciona los datos catastrales no protegidos de un inmueble

           Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
           PROTEGIDOS de un inmueble identificado por su localización" en todo
           excepto en los parámetros de entrada.

           :param str: Nombre de la provincia
           :param str: Nombre del municipio
           :param str: Codigo del poligono
           :param str: Codigo de la parcela
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {'Provincia': provincia,
                  'Municipio': municipio,
                  'Poligono': poligono,
                  'Parcela': parcela}

        url = cls.base_url + "/OVCCallejero.asmx/Consulta_DNPPP"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def ConsultaProvincia(cls):
        """Proporciona un listado de las provincias.

           Proporciona un listado de todas las provincias españolas en las que
           tiene competencia la Dirección general del Catastro.

           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaProvincia"
        response = requests.get(url)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def ConsultaMunicipioCodigos(cls, provincia, municipio):
        """Proporciona un listado de todos los nombres de los municipios de una provincia.

           Proporciona un listado de todos los nombres de los municipios de una
           provincia (parámetro "Provincia"),así como sus códigos (de Hacienda y
           del INE), cuyo nombre Servicios web del Catastro 5 contiene la cadena
           del parámetro de entrada "Municipio".En caso de que este último
           parámetro no tenga ningún valor, el servicio devuelve todos los
           municipios de la provincia.También proporciona información de si existe
           cartografía catastral (urbana o rústica) de cada municipio.

           :param str: Nombre de la provincia
           :param str: Nombre del municipio

           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {"Provincia": provincia,
                  "Municipio": municipio}

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaMunicipio"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def ConsultaViaCodigos(cls, provincia, municipio, tipovia=None, nombrevia=None):
        """Proporciona un listado de las vías de un municipio

           Proporciona un listado de todas las vías de un municipio
           (parámetros "Provincia" y "Municipio"), así como los códigos de las
           mismas según la Dirección General del Catastro (DGC), cuyo nombre
           contiene la cadena del parámetro de entrada "NombreVia" y, en caso
           de que el parámetro "TipoVia" contenga información, existe
           coincidencia en el tipo de la vía. En caso de que el parámetro
           "NombreVia" no tenga ningún valor, el servicio devuelve todas
           las vías del municipio del "TipoVia" indicado.

           :param str: Nombre de provincia
           :param str: Nombre del municipio
           :param str: Opcional,Tipo de via
           :param str: Nombre de via

           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {'Provincia': provincia,
                  'Municipio': municipio}
        if nombrevia:
            params['NombreVia'] = nombrevia
        else:
            params['NombreVia'] = ''
        if tipovia:
            params['TipoVia'] = tipovia
        else:
            params['TipoVia'] = ''

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaVia"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def ConsultaNumeroCodigos(cls, provincia, municipio, tipovia, nombrevia,numero):
        """Proporciona la referencia catastral de la finca correspondiente.

           Proporciona, o bien la referencia catastral de la finca correspondiente
           al contenido del parámetro "Número", en caso de que este exista, o bien
           se devuelve un error ("El número no existe") y se proporciona una lista
           de los números más aproximados al solicitado, en un rango de 5 por arriba
           y 5 por abajo. Por ejemplo, si se solicita el número 10, y en esa vía
           existen los números 2,3,6,7,9,11,15 y 17, se devuelve una lista con los
           números 6,7,9,11 y 15. Junto con la lista de números, se proporcionan
           las referencias catastrales de las fincas.

           :param str: Nombre de la provincia
           :param str: Nombre del municipio
           :param str: Tipo de la via
           :param str: Nombre de la via
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {'Provincia': provincia,
                  'Municipio': municipio,
                  'TipoVia': tipovia,
                  'NomVia': nombrevia,
                  'Numero': numero}

        url = cls.base_url + "/OVCCallejero.asmx/ConsultaVia"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_DNPLOC_Codigos(cls, provincia, municipio, sigla, nombrevia, numero, bloque=None, escalera=None, planta=None, puerta=None):
        """Proporciona la lista de todos los inmuebles que coinciden.

           Este servicio puede devolver o bien la lista de todos los inmuebles que
           coinciden con los criterios de búsqueda, proporcionando para cada
           inmueble la referencia catastral y su localización
           (bloque/escalera/planta/puerta) o bien,en el caso de que solo exista un
           inmueble con los parámetros de entrada indicados, proporciona los datos
           de un inmueble.

           :param str: Nombre de la provincia
           :param str: Nombre del municipio
           :param str: Sigla
           :param str: Nombre de la via
           :param str,int: Numero de inmueble
           :param str,int: Numero de bloque
           :param str: Escalera
           :param str,int: Numero de planta
           :param str,int: Numero de puerta
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {
            'Provincia': provincia,
            'Municipio': municipio,
            'Sigla': sigla,
            'Calle': nombrevia,
            'Numero': str(numero)}
        if bloque:
            params['Bloque'] = bloque
        else:
            params['Bloque'] = ''
        if planta:
            params['Escalera'] = escalera
        else:
            params['Escalera'] = ''
        if puerta:
            params['Puerta'] = str(puerta)
        else:
            params['Puerta'] = ''
        if escalera:
            params['Escalera'] = str(escalera)
        else:
            params['Escalera'] = ''

        url = cls.base_url + "/OVCCallejero.asmx/Consulta_DNPLOC"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_DNPRC_Codigos(cls, provincia, municipio, rc):
        """Proporciona los datos catastrales de un inmueble,

           Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
           PROTEGIDOS de un inmueble identificado por su localización"
           en todo excepto en los parámetros de entrada.

           :param str: Nombre de la provincia
           :param str: Nombre del municipio
           :param str: Referencia catastral
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {
            'Provincia': provincia,
            'Municipio': municipio,
            'RC': rc}

        url = cls.base_url + "/OVCCallejero.asmx/Consulta_DNPRC"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_DNPPP_Codigos(cls, provincia, municipio, poligono, parcela):
        """Proporciona los datos catastrales de un inmueble.

           Este servicio es idéntico al de "Consulta de DATOS CATASTRALES NO
           PROTEGIDOS de un inmueble identificado por su localización" en todo
           excepto en los parámetros de entrada.

           :param str: Nombre de la provincia
           :param str: Nombre del municipio
           :param str: Codigo del poligono
           :param str: Codigo de la parcela
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {
            "Provincia": provincia,
            "Municipio": municipio,
            "Poligono": poligono,
            "Parcela": parcela}

        url = cls.base_url + "/OVCCallejero.asmx/Consulta_DNPPP"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_RCCOOR(cls, srs, x, y):
        """A partir de unas coordenadas se obtiene la referencia catastral.

           A partir de unas coordenadas (X e Y) y su sistema de referencia se
           obtiene la referencia catastral de la parcela localizada en ese punto
           así como el domicilio (municipio, calle y número o polígono, parcela y
           municipio).

           :param str,int: Sistema de coordenadas
           :param str,int,float: Coordanda x
           :param str,int,float: Coordenada Y
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {
            "Coordenada_X": str(x),
            "Coordenada_Y": str(y)}
        if type(srs) == str:
            params["SRS"] = srs
        else:
            params["SRS"] = "EPSG:"+str(srs)

        url = cls.base_url + "/OVCCoordenadas.asmx?op=Consulta_RCCOOR"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_RCCOOR_Distancia(cls, srs, x, y):
        """Proporciona la referencia catastral a partir de unas coordenadas.

           A partir de unas coordenadas (X e Y) y su sistema de referencia se
           obtiene la referencia catastral de la parcela localizada en ese
           punto así como el domicilio (municipio, calle y número o polígono,
           parcela y municipio). En caso de no encontrar ninguna referencia
           catastral en dicho punto, se buscará en un área cuadrada de 50
           metros de lado, centrada en dichas coordenadas, y se devolverá
           la lista de referencias catastrales encontradas en dicha área.

           :param str,int: Sistema de coordenadas
           :param str,int,float: Coordanda X
           :param str,int,float: Coordanda Y
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {'Coordenada_X': x,
                  'Coordenada_Y': y}
        if type(srs) == str:
            params['SRS'] = srs
        else:
            params['SRS'] = "EPSG:"+str(srs)

        url = cls.base_url + "/OVCCoordenadas.asmx/Consulta_RCCOOR_Distancia"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)

    @classmethod
    def Consulta_CPMRC(cls, provicia, municipio, srs, rc):
        """Proporciona la localizacion de una parcela.

           A partir de la RC de una parcela se obtienen las coordenadas X, Y en el
           sistema de referencia en el que está almacenado el dato en la D.G. del
           Catastro, a menos que se especifique lo contrario en el parámetro
           opcional SRS que se indica en la respuesta, así como el domicilio
           (municipio, calle y número o polígono, parcela y unicipio).

           :param str: Nombre de la provincia
           :param str: Nombre del municipio
           :param str,int: Sistema de coordenadas
           :param str: Referencia catastral
           :return: Retorna un dicionario con los datos de la consutla
           :rtype: dict
        """

        params = {'SRS': srs,
                  'Provincia': provicia,
                  'Municipio': municipio,
                  'RC': rc}

        url = cls.base_url + "/OVCCoordenadas.asmx/Consulta_CPMRC"
        response = requests.get(url, params=params)
        return xmltodict.parse(response.content, process_namespaces=False, xml_attribs=False)
