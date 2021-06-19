# Ortograpy

## Solución

Planteamos la solución del problema en varias fases:

### Primera aproximación

- Módulo simple: Módulo básico que integra la funcionalidad core, sin añadidos especiales.
Analizar un fichero pasado como argumento y sacar por linea de comandos los errores
ortográficos que pudieran existir. El módulo correrá como un servicio, analizando de forma
activa cada vez que haya una versión nueva del archivo. Las tecnologías usadas para esta
fase serán: `python3`, módulo `SpellChecker`, servicio de logging: módulo de `logging` de
python y gestión de dependencias y entornos mediante `venv`.

### Aproximaciones futuras

- Integración con IDEs: aproximar aún más la solución al usuario integrándola en su editor
de texto para aportar funcionalidades extra como resaltado de sintaxis, autocorrección,
sugerencias etc. Servir el módulo como un servicio en la nube podría ser una opción.

## Participantes

[@FranciscoJesusGata](https://github.com/FranciscoJesusGata)

[@SilverIcarus](https://github.com/silvericarus)

[@Vdedios](https://github.com/vdedios)
