"""
Módulo para la recolección de datos de Fórmula 1 usando FastF1.

Este módulo contiene funciones para obtener datos de sesiones de Fórmula 1,
incluyendo datos de clasificación y otras sesiones como prácticas libres y carreras.
"""

import fastf1

def get_session_data(year, event_name, session_identifier):
    """
    Función interna que obtiene los datos de cualquier sesión de F1.
    
    Args:
        year (int): Año de la temporada
        event_name (str): Nombre del evento/gran premio
        session_identifier (str): Identificador de la sesión
                                 ('FP1', 'FP2', 'FP3', 'Sprint', 'Qualifying', 'Race')
    
    Returns:
        fastf1.core.Session: Objeto de sesión con todos los datos cargados
    """
    try:
        # Obtener la sesión específica
        session = fastf1.get_session(year, event_name, session_identifier)
        
        # Cargar los datos de la sesión
        session.load()
        
        print(f"✓ Datos cargados exitosamente para {session_identifier} - {event_name} {year}")
        print(f"  Fecha: {session.date}")
        print(f"  Circuito: {session.event['EventName']}")
        print(f"  Ubicación: {session.event['Location']}")
        
        return session
        
    except Exception as e:
        print(f"❌ Error al cargar los datos: {str(e)}")
        return None


def get_qualifying_data(year, event_name):
    """
    Función que obtiene los datos de clasificación de un Gran Premio específico.
    
    Args:
        year (int): Año de la temporada
        event_name (str): Nombre del evento/gran premio
    
    Returns:
        pandas.DataFrame: DataFrame con los resultados de clasificación
    """
    # Usar la función interna para obtener los datos de la sesión de clasificación
    qualifying_session = get_session_data(year, event_name, 'Qualifying')
    
    if qualifying_session is None:
        return None
    
    try:
        # Obtener los resultados de clasificación
        qualifying_results = qualifying_session.results
        
        # Seleccionar las columnas más relevantes para clasificación
        relevant_columns = [
            'Position', 'DriverNumber', 'BroadcastName', 'Abbreviation',
            'TeamName', 'Q1', 'Q2', 'Q3', 'BestTime'
        ]
        
        # Filtrar solo las columnas que existen en los datos
        existing_columns = [col for col in relevant_columns if col in qualifying_results.columns]
        qualifying_df = qualifying_results[existing_columns].copy()

        # Asigna la columna 'BestTime' como el mejor tiempo de clasificación
        if 'BestTime' not in qualifying_df.columns:
            qualifying_df['BestTime'] = qualifying_df[['Q1', 'Q2', 'Q3']].min(axis=1)
        
        # Ordenar por posición
        qualifying_df = qualifying_df.sort_values('Position').reset_index(drop=True)
        
        print(f"✓ Datos de clasificación procesados: {len(qualifying_df)} pilotos")
        
        return qualifying_df
        
    except Exception as e:
        print(f"❌ Error al procesar los datos de clasificación: {str(e)}")
        return None
