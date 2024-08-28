def mostrar_ahorcado(intentos):
    """
    Muestra la etapa actual del ahorcado en función de los intentos restantes.

    Parámetros:
    intentos (int): El número de intentos restantes.

    Retorna:
    str: La representación visual del ahorcado.
    """
    etapas = [
        '''
         ------
         |    |
         |
         |
         |
         |
        -------
        ''',
        '''
         ------
         |    |
         |    O
         |
         |
         |
        -------
        ''',
        '''
         ------
         |    |
         |    O
         |    |
         |
         |
        -------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|
         |
         |
        -------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        -------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        -------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        -------
        '''
    ]
    return etapas[6 - intentos]