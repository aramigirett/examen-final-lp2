#importa app desde Flask para manejar errores y logs, e importa la 
# clase Conexion que se usa para conectarse a la base de datos.
from flask import current_app as app
from conexion.Conexion import Conexion

class NacionalidadDao:
    #este metodo obtiene todos los paises de la based de datos
    def getNacionalidades(self):

        nacionalidadSQL = """
        SELECT id, descripcion
        FROM nacionalidades
        """
        #objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
          cur.execute(nacionalidadSQL)
          #trae datos de db
          lista_nacionalidades = cur.fetchall()
          #retorno de datos
          lista_ordenada = []
          for item in lista_nacionalidades:
              lista_ordenada.append({
                  "id": item[0],
                  "descripcion": item[1]
                })
          return lista_ordenada
        except con.Error as e:
           app.logger.info(e)
        finally:
            cur.close()
            con.close()
    #este metodo obtiene todos los paises segun su id
    def getNacionalidadById(self, id):

        nacionalidadSQL = """
        SELECT id, descripcion
        FROM nacionalidades WHERE id=%s
        """
        #objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
          cur.execute(nacionalidadSQL, (id,))
          #trae datos de db
          nacionalidadEncontrada = cur.fetchone()
          #retorno de datos
          return {
                    "id": nacionalidadEncontrada[0],
                    "descripcion": nacionalidadEncontrada[1]
                }
        except con.Error as e:
             app.logger.info(e)
        finally:
            cur.close()
            con.close()
    #este metodo inserta un nuevo pais en la base de datos
    def guardarNacionalidad(self, descripcion):
        
        insertNacionalidadSQL = """
        INSERT INTO nacionalidades(descripcion) VALUES(%s)
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        #Ejecucion exitosa
        try:
            cur.execute(insertNacionalidadSQL, (descripcion,))
            #se confirma la isercion
            con.commit()

            return True

        #si algo falla aqui
        except con.Error as e:
            app.logger.info(e)
            
        #siempre se va a ejecutar
        finally:
            cur.close()
            con.close()

        return False    
    #este metodo actualiza la decripcion de un pais existente en la base de datos      
    def updateNacionalidad(self, id, descripcion):

        updateNacionalidadSQL = """
        UPDATE nacionalidades
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateNacionalidadSQL, (descripcion, id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False
    #este metodo elimina un pais de la base de datos segun su id
    def deleteNacionalidad(self, id):

        updateNacionalidadSQL = """
        DELETE FROM nacionalidades
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateNacionalidadSQL, (id,))
            # se confirma la insercion
            con.commit()

            return True

        # Si algo fallo entra aqui
        except con.Error as e:
            app.logger.info(e)

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

        return False    
