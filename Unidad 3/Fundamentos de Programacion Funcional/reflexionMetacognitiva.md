# Reflexion Metacognitiva
## Joham Barberena Machorro #22010166

1. ¿Qué significa que una función sea "pura"?

 Una función pura es aquella que siempre produce el mismo resultado cuando recibe las mismas entradas, sin importar cuántas veces se ejecute ni en qué contexto. Además, de que no depende de factores externos y no modifica nada fuera de sí misma, por lo tanto, no provoca efectos secundarios.
 
 Un ejemplo de la vida real sería armar un set de LEGO siguiendo las instrucciones: si siempre usas las mismas piezas y sigues los mismos pasos, obtendrás exactamente el mismo modelo final. Nada fuera del manual afecta el resultado, y tampoco alteras algo externo al proceso de ensamblado.

2. En la Parte 3, ¿por qué `crear_transformador` retorna una función en lugar de aplicar directamente la transformación? ¿Qué ventaja ofrece este diseño?

crear_transformador devuelve una función porque su objetivo no es transformar directamente, sino crear una herramienta que pueda ser utilizada posteriormente. Esto permite que las transformaciones se definan primero y se apliquen después, lo que facilita integrarlas en sistemas más complejos, como se vio en la Parte 3 con un pipeline de funciones.

3. ¿Qué dificultades encontraste al convertir el código imperativo a funcional en la Parte 2? ¿Qué parte fue más difícil y cómo la resolviste? 

Encontré mucha dificultad a nivel conceptual. Personalmente batallé bastante para entender por qué alguien querría transformar un código tan simple en algo más segmentado y abstracto. No me resultaba intuitivo ver la utilidad práctica del enfoque funcional. Sin embargo, después de dedicar tiempo al análisis, revisar explicaciones en video y apoyarme en chatbots para obtener respuestas más personalizadas, comencé a comprender los conceptos y pude aplicarlos correctamente.

4. Si tuvieras que explicar la diferencia entre programación imperativa y funcional a alguien que no programa, ¿qué analogía usarías?

La programación imperativa es como seguir una receta de cocina usando todo lo que tienes en la alacena: vas tomando ingredientes, cambiando cosas de lugar y manipulando directamente lo que ya existe, paso a paso.

En cambio, la programación funcional sería como usar un kit de “cocina tu propia pizza”, donde no solo te dan la receta, sino también todos los ingredientes exactos y separados. No tomas nada de la alacena ni modificas nada fuera del kit: simplemente usas lo que viene dentro y obtienes siempre el mismo resultado si sigues las instrucciones.