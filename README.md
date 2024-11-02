<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proposición Lógica de Estudiantes y BBC</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #f4f4f9;
        }
        h1, h2 {
            color: #333;
        }
        p {
            color: #555;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 4px;
            color: #d14;
        }
    </style>
</head>
<body>

    <h1>Proposición Lógica de Estudiantes y BBC</h1>
    
    <p>Este archivo explora la relación entre el clima y las visitas de los estudiantes a distintas instituciones. Basándonos en lógica proposicional, formulamos ciertas reglas y verificamos su validez mediante inferencias.</p>

    <h2>Símbolos Definidos</h2>
    <p>En primer lugar, definimos tres símbolos lógicos que representan las variables de nuestro problema:</p>
    <ul>
        <li><code>lluvia</code>: Indica si está lloviendo.</li>
        <li><code>BBC</code>: Indica si los estudiantes visitan BBC.</li>
        <li><code>Unimayor</code>: Indica si los estudiantes visitan Unimayor.</li>
    </ul>

    <h2>Proposiciones y Reglas Lógicas</h2>
    <p>Con los símbolos anteriores, se construyen las siguientes proposiciones:</p>

    <h3>1. Regla Lluvia y Visita a BBC</h3>
    <p>La primera regla indica que si <code>no está lloviendo</code>, entonces los estudiantes visitan BBC.</p>
    <p>Esto se representa lógicamente como una implicación: <code>¬lluvia → BBC</code>.</p>

    <h3>2. Regla de Visita Exclusiva</h3>
    <p>La segunda regla establece que los estudiantes visitaron BBC o Unimayor, pero no ambos.</p>
    <p>Esta es una <em>disyunción exclusiva</em>, representada como: <code>(BBC ∨ Unimayor) ∧ ¬(BBC ∧ Unimayor)</code>.</p>

    <h3>3. Visita Confirmada a Unimayor</h3>
    <p>Se sabe que los estudiantes visitaron Unimayor. Esto se define simplemente como <code>Unimayor</code>.</p>

    <h2>Base de Conocimiento</h2>
    <p>Las reglas anteriores se combinan para formar una <em>base de conocimiento</em>. Con esta base de conocimiento, se realizan inferencias para responder preguntas específicas sobre el estado de BBC y el clima.</p>

    <h2>Inferencias</h2>
    <p>Finalmente, utilizamos la base de conocimiento para verificar las siguientes inferencias:</p>
    <ul>
        <li>¿Es posible deducir que los estudiantes visitaron BBC hoy?</li>
        <li>¿Podemos deducir que está lloviendo hoy?</li>
    </ul>

    <p>Estas inferencias permiten extraer conclusiones basadas en la lógica proposicional definida en el código.</p>

</body>
</html>
